# Turn contract and scripted calculus case

The tutor retains the active exercise separately from the history of messages. The exercise specifies the mathematical operation and its referent, such as a function, variable, point, or assumptions. A new message supplies the current proposal, if any; an objective identifies what is being asked or checked. This distinction lets a question about a rule change the focus of assistance while the exercise remains open.

## Decision and response boundaries

The consolidated design resolves authorization and retrieves the current task state before interpreting the message. It clears the prior proposal, then interprets the request and aligns it with the active exercise or another identifiable task. If a candidate expression and a supported objective are available, attempt checking can produce a local or final verdict before assistance is composed. A checked partial step can receive confirmation while the final exercise remains open. A checked final result can take a direct confirmation route; an unresolved referent or unsupported expression can instead require clarification or yield no verdict.

Assistance strategy, presentation modifiers, and permitted disclosure serve separate purposes. Strategy selects the teaching move, while modifiers adjust how it is presented and disclosure bounds how much of the solution may be shown. Retrieved passages provide contextual material with provenance. The response contract separates narrative, asserted mathematical relations, cited material, and disclosure level. Validation examines supported claims and their assumptions before the delivered response and updated state are recorded. This document describes the interfaces between decisions; it does not supply deployment code or assert that every historical turn ran the consolidated design.

The strategy policy evaluates its ordered rules and selects the first applicable one, while retaining other applicable rules as discarded alternatives. The modifiers are resolved after strategy selection, and the announcement field is populated only when an established strategy changes. Disclosure is determined separately. This order lets the recorded choice be inspected without treating a prompt instruction or announcement as proof that it was enacted in the response.

For the consolidated design described in the article, the generator requests structured JSON, temperature 0, and at most 4,096 output units; semantic interpretation uses temperature 0, at most 1,800 output units, and an initial timeout of 12 seconds. Retrieval uses multilingual E5 base with normalized 768-dimensional embeddings and an initial cosine threshold of 0.70. These values describe the consolidated configuration; a service alias and temperature do not fix the provider snapshot or make outputs repeatable.

## Preserved development example

[scripted-calculus-case.csv](scripted-calculus-case.csv) records ten ordered inputs written for development and selected fields from the preserved trace. The task is to differentiate `x^x * exp(2x) / sqrt(x^2 + 1)` for `x > 0`. The recorded provider alias for generated turns was `deepseek-flash`; retrieval and database persistence were disabled for the bank. The public file includes the scripted inputs and trace fields. It does not include generated reply text, pilot messages, or a replay of the live service.

| Check point | Reading of the trace |
| --- | --- |
| Turn 4, conceptual question | The active exercise remains the same, with no candidate or closure recorded. |
| Turns 5, 8, and 9, valid intermediate proposals | The local verdict is favorable (`valida`), the overall attempt field remains `no_verificable`, and the exercise remains open. |
| Turn 10, final derivative proposal | The overall verdict is `valida` and the exercise closes. |

In the CSV, empty fields mean that no value was recorded in the extracted field. `closed`, `contract_fallback`, and `same_task` are recorded Boolean flags. `no_verificable` in the overall field does not override a verdict explicitly scoped to a local step. The case makes that distinction inspectable; its selection and use during development do not provide an independent accuracy estimate. The package verification checks the recorded sequence and its scope and closure fields, without calling the provider or checking responses afresh.
