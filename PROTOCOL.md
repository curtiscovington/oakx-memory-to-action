# Protocol: Local OAKX Knowledge-Reuse Pilot

## Question

For fresh instances of one locked local language model, does a matching,
accepted, locally searchable OAKX corpus improve held-out repository incident
diagnosis relative to no shared corpus?

## Design

- Within-task comparison across baseline, unmatched-placebo, and OAKX arms.
- Six synthetic micro-repositories with opaque identifiers and newly generated
  incident values to reduce training-data contamination.
- The model, decoding parameters, tool schema, tool-call budget, task prompt,
  and grading rule are fixed across conditions.
- Every episode has a fresh conversation and runs sequentially.
- OAKX is a local Git repository pinned to a recorded commit. Agent tools are
  read-only. Network use is limited to a fixed loopback Ollama endpoint.
- Condition order is deterministically shuffled per task to reduce order and
  warm-cache bias.

## Outcomes

Primary outcome: strict task success. A response must contain the exact root
cause, exact recommended value, and the expected authoritative path from the
operational repository. A knowledge entry alone is not evidence.

Secondary outcomes: correct-field fraction, tool calls, latency, prompt tokens,
completion tokens, OAKX searches, and authoritative-source reads.

## Exclusions

Only infrastructure/model failures are excluded, with the reason retained.
Wrong answers, early stopping, budget exhaustion, and failure to verify are
scored as failures.

## Research lock

The run aborts before an episode if research mode is disabled, the endpoint is
not loopback, concurrency is not one, the configured model or digest is absent,
or Ollama reports any other loaded model. There is no fallback model, remote
API, subagent, shell tool, file-write tool, or concurrent episode execution.

## Interpretation

This run is explicitly an excluded pilot. It can demonstrate end-to-end
feasibility and reveal obvious effects, but it cannot support a publishable
claim. A confirmatory run should freeze new tasks before execution, include
multiple independent seeds/runs, and report paired uncertainty intervals.
