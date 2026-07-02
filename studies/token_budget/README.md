# Token Budget Study

Same prompts as the main study. The only change is max generation tokens, swept
across levels. We measure how pass@1-by-class degrades as the budget shrinks —
in particular whether NPC and infeasible problems (which may need more reasoning)
degrade faster than P problems.

## Run config additions
```yaml
study: token_budget
token_budget:
  levels: [512, 1024, 2048, 4096]   # one run per level, or sweep in one driver pass
```

## Output layout
Generations are written per level:
  `generations/<model>/__tok<level>/family_XX/criterion_n/solution.py`

The aggregator adds a `token_level` column when a level subfolder is detected.

## Note on thinking models
For thinking models (deepseek-r1, qwen3, gpt-oss), the chain-of-thought competes
with the code for token budget. The driver warns if a level is below 1024 tokens
for any thinking model, as the output is likely to be truncated mid-code.
