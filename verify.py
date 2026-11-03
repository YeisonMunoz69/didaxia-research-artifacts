"""Recalculate and verify published counts using only the released CSV tables."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


def rows(table):
    with (DATA / f"{table}.csv").open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def totals(table, key, value):
    return {row[key]: int(row[value]) for row in rows(table)}


s = totals("study_counts", "measure", "count")
excluded = sum(s[k] for k in ("test_class_exclusions", "professional_exclusions", "nonresearch_exclusions"))
assert s["raw_turns"] - excluded == s["eligible_turns"] == 1474
assert s["eligible_turns"] - s["complete_pairs"] == 1
for table in ("weekly_activity", "class_activity"):
    assert sum(int(r["complete_pairs"]) for r in rows(table)) == s["complete_pairs"] == 1473
for key in ("pre_forms", "post_forms"):
    assert sum(int(r[key]) for r in rows("class_activity")) == s[key]
assert [s[k] for k in ("threads", "chat_people", "chat_or_survey_people")] == [251, 113, 117]
assert [s[k] for k in ("pre_forms", "post_forms", "linked_form_pairs", "chronological_form_pairs")] == [92, 83, 83, 80]
for i in range(1, 6):
    item = {r["category"]: int(r["count"]) for r in rows("post_experience") if r["item"] == f"F03.{i}"}
    numeric = sum(item[str(j)] for j in range(1, 6))
    favorable = item["4"] + item["5"]
    assert sum(item.values()) == s["post_forms"]
    if i == 5:
        assert (favorable, numeric) == (62, 82)
    print(f"F03.{i}: {favorable}/{numeric} ({100 * favorable / numeric:.2f}%)")
changes = {"increased": 0, "unchanged": 0, "decreased": 0}
for r in rows("self_perception"):
    a, b = int(r["pre_category"]), int(r["post_category"])
    changes["increased" if b > a else "decreased" if b < a else "unchanged"] += int(r["count"])
assert tuple(changes.values()) == (32, 20, 5)
assert sum(changes.values()) == s["comparable_numeric_pairs"] == 57
ratings = totals("teacher_content", "rating_pattern", "criteria")
assert ratings == {"both_favorable": 13, "neutral_and_favorable": 9, "insufficient_and_favorable": 2, "both_neutral": 2}
assert s["teachers"] * s["functional_criteria"] == s["functional_maximum_ratings"] == 8
tech = totals("technical_counts", "measure", "count")
assert (tech["frase_visible_literal_en_historial"], tech["frase_visible_no_vacia"]) == (298, 391)
assert tech["banco_proveedor_pasan"] == tech["banco_proveedor_casos"] == 62
assert tech["repeticion_completos"] == tech["repeticion_pares"] == 224
print("Self-perception:", changes)
print("Teacher criteria:", ratings)
print("All released consistency checks passed.")
