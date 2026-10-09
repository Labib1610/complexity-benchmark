# Character State Migration

Time limit: 2 s   Memory limit: 256 MB

## Description
During a massive in-game event, an MMO server must migrate player characters through a series of internal data states. The server architecture defines various character states and specific transition microservices that convert a character from one state to another.

Because of database locks, each transition microservice has a hard concurrency ceiling, representing the maximum number of characters it can process per server tick. You must configure the load on each microservice to migrate exactly a target quantity of characters per tick from a single initial state to a single finalized state.

The number of characters assigned to each microservice must be a non-negative integer that does not exceed its concurrency ceiling. When characters are assigned to transition through these states, they must not become stuck or materialize out of nothing. For every state other than the initial and finalized states, the total number of characters arriving into the state per tick must exactly equal the total number of characters transitioning out of it. At the initial state, the total number of characters transitioning out minus the total arriving must exactly equal the target quantity. At the finalized state, the total number arriving minus the total transitioning out must exactly equal the target quantity.

All characters are identical for the purposes of this migration. You must determine a valid load assignment for every microservice such that exactly the target quantity of characters reaches the finalized state per tick without exceeding any microservice's concurrency ceiling. If it is impossible to migrate exactly this quantity, you must report that the migration cannot be configured. If multiple valid configurations exist, any one of them will be accepted.

## Input
The first line contains three integers: `n` (the number of character states), `m` (the number of transition microservices), and `1` (representing a single event type).
The second line contains three integers: `s` (the initial state), `t` (the finalized state), and `d` (the target quantity of characters to migrate per tick).
The next `m` lines each contain three integers: `u`, `v`, and `cap`. This indicates a transition microservice that converts characters from state `u` to state `v`, with a concurrency ceiling of `cap` characters per tick.

## Output
If the migration can be configured, output `YES` on the first line. On the second line, output `m` integers representing the number of characters per tick assigned to each transition microservice, in the exact order the microservices were listed in the input.
If it is impossible to migrate exactly `d` characters per tick, output `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 10
1 3 10
2 3 5
2 4 5
3 4 5
```

### Output
```text
YES
5 5 0 5 5
```
