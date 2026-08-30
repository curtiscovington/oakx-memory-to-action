# OAKX × deterministic-calculator audit

Run: `20260830-123547`

## Factorial result

| OAKX | Calculator | Strict success | Root cause | Value | Source read |
|---:|---:|---:|---:|---:|---:|
| no | no | 0/12 | 0/12 | 0/12 | 3/12 |
| no | yes | 2/12 | 2/12 | 2/12 | 6/12 |
| yes | no | 6/12 | 12/12 | 6/12 | 12/12 |
| yes | yes | **11/12** | **12/12** | **11/12** | **12/12** |

The calculator improved strict success by 41.7 points when OAKX was present,
versus 16.7 points without OAKX. The estimated positive factorial interaction
is +25 points, but its paired-bootstrap interval (-8.3 to +58.3 points) crosses
zero. The synergy is therefore promising rather than conclusive at twelve
tasks.

OAKX+calculator beat calculator-only on nine tasks and lost none (two-sided
exact paired sign test p=0.0039). Calculator addition improved five OAKX tasks
and harmed none (two-sided exact sign test p=0.0625). These exact tests and the
bootstrap intervals should be interpreted within this synthetic task bank.

## Mechanism

OAKX supplied navigation and the reusable rule: both OAKX cells achieved 12/12
root-cause accuracy and 12/12 authoritative verification. The deterministic
calculator then removed all five numeric errors observed in OAKX-only.

The combined cell used the calculator exactly nine times—once for every numeric
task—and every returned value matched the deterministic ground truth. It did
not invoke the calculator for the three categorical tasks.

The only combined-cell failure was `umber`, where the model returned `forge ->
seal>index>publish` rather than the requested value `seal>index>publish`. This
was the same normalization error in OAKX-only and is outside a numeric
calculator's scope.

Calculator-only succeeded on `nectar` and categorical `tulip`. On other tasks it
either failed to reach the authoritative capsule or lacked enough calls to
submit. A calculator cannot execute a rule that the agent has not found.

## Integrity

- 24/24 new episodes completed with no infrastructure exclusions.
- The 24 no-calculator cells are linked to the immutable scaled source run by
  a source-manifest SHA-256 recorded before new execution.
- Combined analysis contains exactly 48 cells: twelve tasks by four conditions.
- Exact locked local model and digest; fixed temperature, seed, context, and
  eight-call budget; sequential fresh sessions.
- No fallback model, router, subagent, remote endpoint, shell, or write tool.
- The calculator uses a restricted Python AST evaluator and has no access to
  task IDs, files, expected values, OAKX, or the grader.
- All nine expected numeric expressions have independent unit tests. Code-like
  expressions, names, file access, exponentiation, excessive results, and
  division by zero are rejected.
- OAKX remained clean at the pinned source-run commit.

## Implication for OAKX

The evidence supports a layered architecture:

1. OAKX retrieves a concise, accepted rule and its authoritative pointer.
2. The agent verifies the current operational source.
3. A constrained deterministic substrate executes calculations or validation.
4. The language model explains and submits the result.

Knowledge exchange and deterministic execution solve different failure modes.
Neither should be treated as a substitute for the other.
