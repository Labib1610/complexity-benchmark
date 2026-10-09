# Problem B — Phase II: Containment Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
The decommissioning of a subterranean research facility is divided into three distinct operational phases. 

During Phase I (Survey and Assessment), automated drones mapped the entire network of chambers and connecting passages. For each passage, they determined the precise material cost required to install a permanent bulkhead. A passage with a bulkhead installed becomes completely impassable.

You are responsible for Phase II (Isolation Planning). The facility contains two specific chambers holding reactive legacy materials. These two chambers must be completely isolated from each other so that no sequence of open passages allows transit between them. You have been allocated a strict material budget for this phase. You must select a set of passages to receive bulkheads such that the total cost of the installations is no more than the allocated budget, and the two critical chambers are disconnected. The status of all other chambers is irrelevant to the success of this phase; they may remain accessible from either of the two critical chambers, as long as the critical chambers cannot reach each other. 

Once your plan is approved, Phase III (Execution) will commence, during which engineering teams will deploy the bulkheads exactly as you specified and begin chemical scrubbing of the separated zones. Your task right now is solely to produce the approved Phase II isolation plan.

## Input
Line 1: five integers $n$ (the number of chambers), $m$ (the number of passages), $s$ and $t$ (the identifiers of the two critical chambers), and $B$ (the maximum material budget).
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a bidirectional passage between chamber $u$ and chamber $v$ that requires $w$ units of material to install a bulkhead. 
Chambers are numbered from $1$ to $n$. 

## Output
If a valid isolation plan exists that does not exceed the budget $B$, print `YES`. On the next line, print the number of bulkheads to install, $c$. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a passage to receive a bulkhead. If there are multiple valid plans within the budget, any valid set of passages is acceptable.
If it is impossible to isolate the two critical chambers without exceeding the budget, print `NO`.

## Example
### Input
```text
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 4
3 4 5
```

### Output
```text
YES
2
1 2
1 3
```
