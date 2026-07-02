# Fixed Model Prompt Template

ONE template, identical for every model and every problem in the main study.
The harness slots the statement into `{STATEMENT}`. Do not vary wording per
model — comparability depends on this being fixed.

## System message
```
You are an expert competitive programmer. You write correct, efficient Python 3
solutions. Your program reads all input from standard input and writes only the
required answer to standard output. Output only a single Python 3 code block and
nothing else — no explanation before or after.
```

## User message
```
Solve the following problem in Python 3.

{STATEMENT}

Requirements:
- Read from standard input, write to standard output.
- Output only the answer in the exact format specified.
- Return only one Python 3 code block.
```

## Extraction rule
From the model response, extract the first fenced ```python ... ``` block. If no
fenced block exists, treat the entire response as code. Store raw response AND
extracted code (see generation driver).

## Variants (defined later, do NOT add here)
- Time-budget study appends a grading-policy block — see `studies/`.
- Token-budget study caps `max_tokens` at generation — see `studies/`.
- Multi-turn study sends a turn sequence — see `studies/`.
The BASE template above never changes.
