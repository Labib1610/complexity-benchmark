# Problem B — Pneumatic Tube Logistics

Time limit: 2 s   Memory limit: 256 MB

## Description
A large institution operates across $n$ distinct rooms. To move physical documents securely, they have installed $m$ one-way pneumatic tubes between certain pairs of rooms. Each tube has a strict limit on how many document capsules it can safely transport in a single afternoon. The number of capsules assigned to each tube must be a non-negative integer that does not exceed this limit.

At room $s$, the total number of departing capsules minus the total number of arriving capsules must equal exactly $d$. At room $t$, the total number of arriving capsules minus the total number of departing capsules must equal exactly $d$. For all other rooms, the total arrivals must exactly equal the total departures. Capsules cannot be stored, created, or destroyed in transit.

Your task is to determine the exact number of capsules to send through each individual tube so that all conditions are met without exceeding any tube's maximum limit.

## Input
The first line contains three integers $n$, $m$, and $k$ (where $k = 1$, indicating a single batch of documents).
The second line contains three integers $s$, $t$, and $d$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, detailing a one-way tube from room $u$ to room $v$ with a maximum limit of $cap$ capsules.

## Output
If there is a valid arrangement, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of capsules sent through each tube, in the exact order the tubes were listed in the input. If no such arrangement exists, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 5
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
