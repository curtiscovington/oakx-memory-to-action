# Frozen scaled OAKX study

Status: frozen before model execution on 2026-08-30.

## Question

Does a concise matching OAKX entry improve strict diagnosis and remediation on
new repository incidents compared with no exchange and with an equally sized
but unrelated exchange?

## Design

- Twelve new synthetic incident families, none used in the excluded pilot.
- Three within-task conditions: baseline, unrelated-placebo, and matching OAKX.
- Thirty-six fresh, sequential episodes using one exact local model and digest.
- Fixed temperature, seed, context, prompt, tool schema, and eight-call budget.
- Condition order is deterministically shuffled within task.
- Operational policy filenames are opaque. Baseline remains solvable by local
  search over incident field names.
- OAKX agents may make exactly one literal knowledge search. They cannot list
  the knowledge directory. A miss must return immediately to operational
  investigation. This is the bounded no-match lesson from the excluded pilot.
- A knowledge entry contains a reusable rule and authoritative pointer, never
  the live incident values or computed answer.

## Outcomes

Primary: strict success, requiring the exact root-cause identifier, exact
recommended value, citation of the authoritative operational policy, and proof
that the policy was actually read.

Secondary: root-cause accuracy, value accuracy, verification rate, submission
rate, tool calls, latency, and token use.

## Analysis

Report paired task-level differences with a deterministic paired-bootstrap
interval. Because there is one model and one deterministic run per cell, results
generalize only to this task distribution and locked model. No task, answer,
budget, or prompt changes are allowed after the first scaled model call.
