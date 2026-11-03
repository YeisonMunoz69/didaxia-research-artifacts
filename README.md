# Differential calculus tutor study artifacts

Version 0.1.0. Aggregate evidence for the formative university evaluation of a Spanish-language conversational differential calculus tutor. Student activities ran from 16 September to 9 October 2026. The cumulative extraction was closed on 10 October 2026. Teacher review was subsequent and involved two teachers.

Run `python verify.py` using Python 3.10 or later. The script needs only the standard library and makes no network requests. The CSV files are the canonical release. The checks cover the inclusion flow arithmetic, weekly and class totals, survey response distributions, ordinal transitions, teacher rating patterns, and selected technical counts.

| File | Unit and source |
| --- | --- |
| study_counts.csv | One count per measure. Derived from the reconciled OE4 pilot report and aggregated teacher review. A complete pair is a student message and its stored tutor response. |
| weekly_activity.csv | Counts by analysis window S1 (16–22 Sep), S2 (23–29 Sep), S3 (30 Sep–4 Oct), S4 (5–10 Oct). People may appear in multiple windows. |
| class_activity.csv | Counts by platform class, with class labels as reported in the paper. People may appear in multiple classes. Survey distributions are pooled across classes. |
| post_experience.csv | One count per item and category. F03.1 writing, F03.2 explanation, F03.3 procedure, F03.4 source, F03.5 satisfaction. Categories 1–5 are ordinal. NA means not applicable or nonuse and PNR means prefer not to answer. Favorability is categories 4 and 5 divided by numeric answers. |
| self_perception.csv | Counts per pre/post category pair for the item on perceived ability to explain the derivative at a point, using chronological pairs with numeric answers to the same item. |
| teacher_content.csv | Number of selected criteria by paired rating pattern. No evaluator-level rows. Favorable means 4 or 5. |
| technical_counts.csv | Aggregate development and trace counts from editorial reconciliation. Literal announcements measure the occurrence of wording. Designed bank and replay counts describe execution under their recorded conditions. |

The export uses a field allowlist from existing aggregate sources. It contains no participant rows, identifiers, conversation text, precise individual timestamps, consent records, evaluator forms, copyrighted source passages, or backend code. Class-level survey outcome breakdowns are excluded to reduce disclosure in small groups. Totals for distinct people and threads were derived upstream. These tables support checking reported arithmetic and reconstructing aggregate distributions. They cannot independently repeat participant selection, record linkage, individual judgments, or service execution.

Source instruments and implementation materials remain under project custody. No public data license is asserted for third-party or restricted materials. Cite this version and the linked study when available.
