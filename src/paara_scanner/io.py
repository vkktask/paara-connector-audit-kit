"""Input loading: coding-sheet CSV, JSON connector specs, doc folders."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import Connector, Factor, FactorCode

_CSV_COLUMNS = {
    "connector": "name",
    "F1": Factor.F1,
    "F2": Factor.F2,
    "F3": Factor.F3,
    "F4": Factor.F4,
    "F5": Factor.F5,
    "F6": Factor.F6,
    "F7": Factor.F7,
}


def _score_pair(row: dict, prefix: str) -> tuple[str, str]:
    lower = (row.get(f"{prefix}_lower") or "").strip()
    upper = (row.get(f"{prefix}_upper") or "").strip()
    return (lower, upper)


def load_coding_sheet(path: str | Path) -> list[Connector]:
    """Load connectors from a coding-sheet CSV (audit/coding-sheet.csv format)."""
    path = Path(path)
    connectors: list[Connector] = []
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            name = (row.get("connector") or "").strip()
            if not name:
                continue
            codes = {
                factor: FactorCode.parse(row[factor.value])
                for factor in Factor
            }
            default = _score_pair(row, "default")
            restricted = _score_pair(row, "restricted")
            connectors.append(
                Connector(
                    name=name,
                    codes=codes,
                    documentation_retrieved=(
                        row.get("documentation_retrieved") or ""
                    ).strip(),
                    has_write_limiting_control=bool(restricted[0]),
                    expected_default=default,
                    expected_restricted=restricted,
                )
            )
    return connectors


def load_json_spec(path: str | Path) -> Connector:
    """Load one connector from a JSON spec.

    Accepted shapes:
      {"name": ..., "factors": "UNUUYNY", ...}
      {"name": ..., "codes": {"F1": "Y", "F2": "N", ...}, ...}
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    name = data["name"]
    if "factors" in data:
        connector = Connector.from_code_string(name, data["factors"])
    else:
        codes = {
            Factor(key): FactorCode.parse(value)
            for key, value in data["codes"].items()
        }
        connector = Connector(name=name, codes=codes)
    connector.connector_type = data.get("type", "")
    connector.documentation_retrieved = data.get("documentation_retrieved", "")
    connector.has_write_limiting_control = bool(
        data.get("has_write_limiting_control", False)
    )
    return connector


def load_docs(paths: list[str | Path]) -> str:
    """Concatenate text from files / directories (md, txt, json, yaml, csv)."""
    texts: list[str] = []
    for raw in paths:
        path = Path(raw)
        files = (
            sorted(p for p in path.rglob("*") if p.is_file())
            if path.is_dir()
            else [path]
        )
        for file in files:
            if file.suffix.lower() not in {
                ".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".rst",
            }:
                continue
            try:
                texts.append(file.read_text(encoding="utf-8", errors="ignore"))
            except OSError:
                continue
    return "\n\n".join(texts)
