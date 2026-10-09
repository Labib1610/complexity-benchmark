# Problem B — Quality Assurance on the Assembly Line

Time limit: 2 s   Memory limit: 256 MB

## Description
A security factory manufactures locks and keys. Before shipping, specific lock-and-key pairs must be tested together to verify they interact correctly. Each planned test involves exactly one lock and exactly one key, and no test ever involves two locks or two keys — the pairs are strictly mixed. Different items are required for different numbers of tests, and the busiest item in the whole factory sets the scale of the schedule.

Testing is organised into numbered rounds 1, 2, 3, …, and performing a verification test consumes one whole round. The single binding physical rule is that two tests sharing a common item (either a lock or a key) may never be run in the same round, because an item cannot be physically engaged in two tests at once. Key profiles, lock mechanisms, security tiers, and whether an item is a lock or a key are all irrelevant beyond this physical rule; only which tests share an item matters.

Because the busiest item is involved in some number of tests and none of them can share a round, at least that many rounds are unavoidable. The operations goal is to schedule using **no more** rounds than that unavoidable minimum — exactly the busiest-item count. Assign every test a round drawn from that many rounds so that no item ever has two of its tests scheduled in the same round. (The strict separation of locks and keys guarantees the unavoidable minimum is always achievable; despite appearances, no round beyond the busiest-item count is ever needed.)

## Input
First line: three integers `nL`, `nR`, `m` (1 ≤ `nL`, `nR` ≤ 100000, 0 ≤ `m` ≤ 400000).
Next `m` lines: two integers `u` `v` (1 ≤ `u` ≤ `nL`, 1 ≤ `v` ≤ `nR`): a planned test between lock `u` and key `v`.

## Output
Print `YES`, then a line with `m` integers in 1..Δ — the round assigned to test `i` in input order (tests sharing any lock or key must differ).

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
