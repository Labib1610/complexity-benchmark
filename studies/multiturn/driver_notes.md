# Multi-Turn Driver Notes

## Implementation: harness/multiturn.py

The multiturn driver extends generate.py logic without duplicating it.

### Message history
A running list of dicts `[{"role": "user"|"assistant", "content": "..."}]` is
maintained across turns for each (sequence, family, model) triple. Each new turn
appends a user message and the model's response as an assistant message.

### Per-turn loop
```
for turn_index, class_label in enumerate(sequence):
    criterion = lookup_criterion(family, class_label)
    user_content = build_turn_content(turn_index, criterion, condition, meta)
    history = build_turn_messages(history, user_content)
    raw = backends.generate(..., messages=history)
    history.append({"role": "assistant", "content": raw})
    code = extract_code(strip_thinking(raw))
    verdict = checker.judge_problem(criterion, write_temp_solution(code), ...)
    record_trajectory_row(turn_index, class_label, condition, verdict)
```

### Backends note
The Ollama backend already accepts a `messages` list. The Anthropic API uses
`system` + `messages`; pass the multi-turn history into `messages`.
backends.py will need a `generate_multiturn(messages_list, ...)` variant that
accepts a full history rather than a separate system/user pair.

### Output layout
```
runs/<date>_<name>/multiturn/
  <model>/<family>/<sequence_id>/<condition>/
    turn_01_solution.py
    turn_01_verdict.json
    turn_02_solution.py
    turn_02_verdict.json
    trajectory.json     <- full per-turn summary
```

### Aggregation metrics
- Direction-of-transition effects: NPC->P improvement rate, P->NPC degradation rate.
- Infeasibility detection: accuracy when a turn introduces INFEASIBLE.
- Revisit failures: e.g. does NPC->P->NPC succeed at turn 3 given turn 1 succeeded?
- Condition comparison: explicit vs implicit shift detection rate.

Implement as harness/multiturn.py reusing backends + checker; do not duplicate logic.
