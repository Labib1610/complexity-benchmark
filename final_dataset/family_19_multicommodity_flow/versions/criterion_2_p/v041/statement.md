# Problem B — Cargo Transfer Quota

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics coordinator is scheduling the movement of shipping crates across a system of facilities connected by one-way transit corridors. Each corridor has a strict maximum limit on the number of crates it can transport during a single shift.

A fixed quota of crates must be transferred from a designated initial facility to a final facility. For every facility aside from the initial and final ones, the total number of crates arriving via incoming corridors must exactly equal the total number of crates departing via outgoing corridors; nothing can be stored or created in transit. At the initial facility, the total departing crates minus any arriving crates must exactly equal the required quota. Conversely, at the final facility, the total arriving crates minus any departing crates must equal the required quota.

You must assign a non-negative whole number of crates to each corridor such that no corridor's limit is exceeded, and the exact quota is successfully transferred. If no such assignment exists, you must indicate this.

## Input
Line 1: `n m 1` (where `n` is the number of facilities, `m` is the number of corridors, and `1` is a constant integer). Facilities are numbered from 1 to `n`.
Line 2: `s t d` (`s` is the initial facility, `t` is the final facility, and `d` is the required quota).
Next `m` lines: `u v cap` (representing a one-way corridor from facility `u` to facility `v` with a maximum limit of `cap` crates).

## Output
If the quota can be met, print `YES` on the first line. On the second line, print `m` integers separated by spaces — the number of crates assigned to each corridor, in the exact order the corridors were provided in the input. If there are multiple valid assignments, any of them is acceptable.
If it is impossible to meet the quota, print `NO`.

## Example
### Input
```
4 5 1
1 4 10
1 2 10
2 3 5
1 3 5
3 4 10
2 4 5
```

### Output
```
YES
5 0 5 5 5
```
