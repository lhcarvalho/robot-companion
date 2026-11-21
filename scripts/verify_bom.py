#!/usr/bin/env python3
"""Static BOM schema checks. This does not validate component compatibility."""
from pathlib import Path
import csv
import sys
p=Path(__file__).resolve().parents[1]/"bom"/"BOM.csv"
required=("id","subsystem","component","model_or_sku","qty","selection_status",
          "procurement_status","verification","known_dimensions_mm","source","notes")
with p.open(newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    assert tuple(reader.fieldnames or ())==required, "unexpected BOM column list"
    rows=list(reader)
assert rows, "empty BOM"
ids=set()
for row in rows:
    assert row["id"] not in ids, f"duplicate BOM id {row['id']}"
    ids.add(row["id"])
    assert all(x is not None for x in row.values()), f"invalid CSV cells in {row['id']}"
    assert row["component"] and row["model_or_sku"],f"missing component in {row['id']}"
    assert row["qty"].isdigit() and int(row["qty"])>0, f"invalid quantity in {row['id']}"
print(f"BOM static structure PASS: {len(rows)} rows. Compatibility NOT TESTED.")
