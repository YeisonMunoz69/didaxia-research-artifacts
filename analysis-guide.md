# Analysis guide and data dictionary

The evaluation used descriptive counts and ordinal responses to characterize use and reported experience during an iterative university deployment. The released inputs begin at the aggregate stage. The processing rules below explain how those units were formed; they do not provide access to the source records.

## From recorded activity to analysis units

The cumulative inventory contained 1,602 turn records. The analysis excluded 122 professional consultations, three academic-tutoring records outside the research purpose, and three records from a test class. The remaining 1,474 traces included one without a student message, leaving 1,473 complete pairs. A pair consists of a student message and the stored tutor response. There were 251 conversations from 113 people with complete pairs; the union of people with an eligible conversation or form was 117. Earlier extracts overlap this cumulative inventory and are not added to it.

Eligibility was determined using the research purpose and historical consent record, including the applicable version and withdrawal status. Records classified as involving minors additionally required valid assent and evidence of representative authorization that had passed the platform's operational review by the relevant time. These conditions describe the record-selection procedure. The released tables allow its arithmetic to be checked after aggregation; they do not permit a new eligibility review.

## Questionnaires and teacher ratings

There were 92 pre-activity and 83 post-activity forms. Linking the records by participant and historical class yielded 83 matched sets, of which 80 were in chronological order. “Pre” and “post” refer to form order; some participants had used the tutor before submitting their first form. The self-perception analysis retained the 57 chronological sets with numeric answers to both P07 and F08. It compares the order of the two categories without assuming equal distances between them. A higher category indicates higher reported self-perception on that item rather than demonstrated learning.

For each F03 item, categories 4 and 5 were divided by the sum of categories 1–5. The denominator therefore varies by item. In F03.5 it is 82, yielding 62/82 favorable numeric responses (75.61%). The remaining post form did not contribute a numeric rating to that item. The teacher content table groups criteria by their two ratings. Categories 4 and 5 are favorable, category 3 is neutral, and insufficient information remains separate. The two teachers each completed both instruments. In the functionality review, eight maximum ratings are four criteria rated by two people.

## Inputs and manuscript outputs

The table links the released files to the numbered elements in the study manuscript. An entry described as partial identifies the portion that can be checked from this release.

| File | Row unit and fields | Manuscript coverage |
| --- | --- | --- |
| `study_counts.csv` | One measure and integer count per row; units are records, pairs, conversations, people, forms, form sets, ratings, or criteria as named | Figure 7; selected counts in §§4–5 |
| `weekly_activity.csv` | Analysis window, complete-pair count, and people with activity within the window | Table 5, activity columns; the same person may appear in several windows |
| `class_activity.csv` | Platform class, people with complete pairs, pairs, and form counts | Table 6, activity and form columns; distinct people may appear in more than one class; satisfaction by class is outside this release |
| `post_experience.csv` | Item, category, and count; `NA` and `PNR` are nonnumeric | Table 7 and Table B2 |
| `self_perception.csv` | Pre category, post category, and count; categories 1–5 | Figure 8 and Table B1 |
| `teacher_content.csv` | Unordered rating pattern and number of criteria with that pattern | Overall distribution in §5.3; this file does not reproduce the criterion rows of Table 8 |
| `technical_counts.csv` | Named aggregate measure and integer count | Selected counts in §§5.4–5.5 and Table 10; does not reproduce the full monitoring table |
| `technical/scripted-calculus-case.csv` | One recorded turn in a scripted development case | Table A1; records the technical fields behind the example rather than production conversations |

Run `python verify.py` to check the main calculations against the CSV inputs. The script does not recreate the manuscript figures. In the technical tables, a selected modifier, a modifier sent to the prompt, and a literal announcement in the stored response describe different events. A literal announcement is a wording match, while a development-bank pass or an operationally complete replay records satisfaction of the checks used under those conditions. None of these counts is a measure of learning, independent accuracy, or the quality of delivered help.
