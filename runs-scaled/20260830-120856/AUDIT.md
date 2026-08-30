# Scaled OAKX run audit

Run: `20260830-120856`

## Main result

| Condition | Submitted | Strict success | Root cause | Value | Source read | Mean calls |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 0/12 | 0/12 | 0/12 | 0/12 | 3/12 | 8.00 |
| unrelated placebo | 0/12 | 0/12 | 0/12 | 0/12 | 0/12 | 8.00 |
| matching OAKX | 12/12 | 6/12 | 12/12 | 6/12 | 12/12 | 6.58 |

Under the frozen eight-call budget, OAKX improved strict success by 50
percentage points over both comparators. The paired bootstrap interval is +25
to +75 points. There were six paired OAKX wins and no paired losses; a
two-sided exact sign/McNemar test on the discordant pairs gives p=0.03125.

The scope matters: this supports a causal claim about these synthetic tasks,
this model, and this investigation budget. It does not establish that OAKX
improves every task or model.

## Mechanism

Every matching-OAKX agent:

1. read the repository-hosted OAKX skill;
2. made exactly one search for the live opaque incident code;
3. read the matching accepted entry;
4. followed its pointer to the authoritative operational capsule;
5. submitted a diagnosis.

Every OAKX agent identified the exact root-cause label and actually read the
authoritative source. Baseline agents instead began serially inspecting opaque
capsules; only three reached the authoritative capsule and none retained a call
for submission. Placebo agents made one bounded knowledge search, got no match,
and then investigated operational files without enumerating knowledge.

OAKX therefore demonstrated a navigation and reusable-diagnosis benefit. It
did not solve downstream reasoning: only six of twelve recommended values were
exact. Five failures were arithmetic errors despite the model quoting the
correct rule and source. One was an output-normalization error (`forge ->
seal>index>publish` instead of the requested sequence `seal>index>publish`).

## Integrity checks

- 36/36 episodes completed; no infrastructure exclusions.
- The manifest was written before the first model call and records task-bank,
  protocol, config, model, and repository hashes.
- Exact model: `qwen3.8:27b-q4_K_M`, digest beginning `25b843619e94`.
- Loopback Ollama only, temperature zero, fixed seed, sequential fresh sessions.
- No fallback model, model router, subagent, shell, network tool, or write tool.
- Treatment and placebo repositories remained clean at their pinned commits.
- No OAKX-directory enumeration occurred.
- All treatment and placebo episodes made exactly one OAKX search; baseline
  episodes made none.

## Next ablation

The clean next test is a 2x2 design: OAKX present/absent crossed with a small
deterministic calculator or validator present/absent. That would test whether
OAKX reliably supplies the right rule while a separate execution substrate
removes arithmetic as the bottleneck. A second useful axis is a larger tool
budget, which would estimate whether OAKX changes ultimate solvability or mainly
reduces search cost.
