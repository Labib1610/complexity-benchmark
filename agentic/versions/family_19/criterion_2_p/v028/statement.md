# Problem B — Single-Asset Settlement over a Clearing System

Time limit: 2 s   Memory limit: 256 MB

## Description
A central clearing authority must process a specific volume of a digital token from a primary holding account to a final settlement account during a single batch window. The tokens move through a system of registered intermediary accounts, connected by one-way clearing channels. Each channel carries a strict regulatory ceiling on the number of tokens it can process per window, reflecting risk limits that cannot be augmented mid-batch. A fixed quantity of the tokens, counted in whole units, must travel from the primary account to the settlement account during this one window.

On every channel the number of tokens assigned is a non-negative whole number that must not exceed that channel's ceiling. At every account other than the primary and the settlement accounts the tokens are conserved: the tokens arriving equal the tokens departing, so nothing accumulates or vanishes in transit. At the primary account the net departure equals the required quantity, and at the settlement account the net arrival equals it. Liquidity repositioning, processing times, channel distances, and the exact order in which tokens are cleared are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate accounts, and the required end-to-end quantity bind the answer.

Produce an allocation that delivers the full quantity from the primary account to the settlement account within every channel's ceiling, or report that this quantity cannot be delivered in a single window. (Regulators sometimes reach for elaborate multi-asset machinery here; with only one token type to move, the shared-limit contention that makes the general problem hard simply does not arise.)

## Input
Line 1: `n m 1` (where `n` is the number of accounts and `m` is the number of channels). 
Next line: `s t d` (where `s` is the primary account, `t` is the settlement account, and `d` is the required quantity). 
Next `m` lines: `u v cap` (representing a one-way channel from account `u` to account `v` with a ceiling of `cap`).

## Output
`YES` then one line with `m` integers — the allocated tokens on channel `j` (in input order); or `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```text
YES
5 5 0 5 5
```
