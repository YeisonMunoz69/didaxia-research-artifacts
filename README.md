# Differential calculus tutor study artifacts

Version 0.2.0 accompanies a four-week formative university evaluation of a Spanish-language conversational tutor for differential calculus. Student activities ran from 16 September to 9 October 2026; the cumulative student extraction closed on 10 October. Two teachers subsequently reviewed selected mathematical content and demonstrated functions. This release preserves the seven aggregate CSVs from [v0.1.0](https://github.com/YeisonMunoz69/didaxia-research-artifacts/tree/v0.1.0) and adds documentation for inspecting the analysis and the tutor's turn contract.

## Review the study materials

Clone or download the tagged version and run `python verify.py` with Python 3.10 or later. The script uses the standard library and makes no network requests. It checks selected aggregate results, including the inclusion arithmetic, complete-pair totals by analysis window and class, questionnaire distributions, self-perception transitions, paired teacher-rating patterns, and selected technical counts. It also checks the consistency of the released scripted trace. `SHA256SUMS` records the file digests.

| Material | What it supports |
| --- | --- |
| [Analysis and data guide](analysis-guide.md) | Definitions, denominators, rules used in the analysis, and links from manuscript tables and figures to released inputs |
| [Aggregate tables](data/) | Review of released counts and distributions without participant records |
| [Instrument documentation](instruments/README.md) | Spanish wording and response options for recovered student closing items, plus the rated criteria from both teacher instruments |
| [Turn contract and development case](technical/README.md) | An inspection of task continuity, scoped checking, and closure in one preserved scripted case |
| [Citation metadata](CITATION.cff) | Identification of this version as a citable dataset and documentation package |

The release contains derived tables rather than an anonymized copy of the production database. The aggregate tables contain no participant rows or conversations, individual survey responses, consent records, evaluator forms, or precise individual timestamps. The Spanish dialogue in the technical file consists of scripted development inputs. Class-level survey outcomes, copyrighted source passages, and the tutor implementation remain outside this release. The package allows readers to check the released aggregate arithmetic and inspect the recorded case. It does not allow independent reconstruction of participant selection, record linkage, individual judgments, or re-execution of the service.

Cite this tagged version and the accompanying article when available. No new licensing terms are assigned by this release.
