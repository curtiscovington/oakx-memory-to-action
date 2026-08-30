# OAKX × deterministic-calculator ablation

**FROZEN 2x2 ABLATION — TWO CELLS REUSED, TWO CELLS NEW**

| Cell | Submit | Strict | Root | Value | Source | Calculator uses | Mean calls | Mean wall (s) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| no_oakx_no_calculator | 0/12 | 0/12 (0.0%) | 0.0% | 0.0% | 25.0% | 0 | 8.00 | 34.26 |
| no_oakx_calculator | 2/12 | 2/12 (16.7%) | 16.7% | 16.7% | 50.0% | 4 | 8.00 | 39.86 |
| oakx_no_calculator | 12/12 | 6/12 (50.0%) | 100.0% | 50.0% | 100.0% | 0 | 6.58 | 39.11 |
| oakx_calculator | 12/12 | 11/12 (91.7%) | 100.0% | 91.7% | 100.0% | 9 | 6.75 | 39.70 |

## Paired effects on strict success

- oakx_without_calculator: +0.500 (paired-bootstrap 95% interval +0.250 to +0.750)
- oakx_with_calculator: +0.750 (paired-bootstrap 95% interval +0.500 to +1.000)
- calculator_without_oakx: +0.167 (paired-bootstrap 95% interval +0.000 to +0.417)
- calculator_with_oakx: +0.417 (paired-bootstrap 95% interval +0.167 to +0.667)
- factorial_interaction: +0.250 (paired-bootstrap 95% interval -0.083 to +0.583)

Interpret within the frozen synthetic task bank, exact local model, and eight-call budget.
