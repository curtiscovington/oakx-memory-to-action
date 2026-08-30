# Frozen OAKX × deterministic-calculator ablation

Status: frozen before any new ablation model call on 2026-08-30.

## Design

The experiment crosses OAKX absent/present with a deterministic calculator
absent/present on the same twelve scaled-study tasks:

| Cell | OAKX | Calculator |
|---|---:|---:|
| A | no | no |
| B | no | yes |
| C | yes | no |
| D | yes | yes |

Cells A and C are reused byte-for-byte from frozen run `20260830-120856`.
Their task bank, model digest, seed, decoding settings, tool budget, and fixtures
are immutable. Only the 24 missing B/D episodes are newly executed.

The calculator is answer-blind. It evaluates an agent-supplied arithmetic
expression using numeric literals, parentheses, `+ - * / // %`, and
`ceil/floor/min/max`. It has no task identifiers, expected answers, files,
knowledge corpus, or grading data. Numeric tasks in calculator-present cells are
instructed to use it. Categorical tasks remain unaffected.

All cells retain the eight-call budget and authoritative-source requirement.
The primary outcome remains strict success. Secondary outcomes include root,
value, source-read and submission rates, calculator use, calls, and latency.

The factorial interaction is:

`(OAKX+calculator - OAKX-only) - (calculator-only - neither)`.

No prompt, answer, budget, task, or calculator change is permitted after the
first new model call.
