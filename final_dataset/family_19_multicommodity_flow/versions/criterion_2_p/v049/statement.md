# Phase II: Corridor Volume Allocation

Time limit: 2 s
Memory limit: 256 MB

## Description
Our physical distribution network consists of several distribution centers connected by unidirectional freight routes. Every freight route possesses a strict hard limit on the quantity of freight units it can process during a single operational shift.

To maintain network stability, any operational plan must adhere to the following rules:
- Every freight route must be allocated a non-negative integer number of freight units.
- The allocation for any given freight route cannot exceed its strict hard limit.
- At every distribution center—with the exception of two special centers—the sum of freight units arriving via incoming routes must exactly equal the sum of freight units departing via outgoing routes.

The predictive models in Phase I have finalized the network topology and the hard limits for all routes. Additionally, Phase III operations demand a specific, fixed quota of freight units to be successfully moved between the two special centers. 

Your task is to implement Phase II: design an operational plan that satisfies all the rules above, while ensuring that the net departure (total departing minus total arriving) from the dispatch center equals the required fixed quota, and the net arrival (total arriving minus total departing) at the receiving center equals the required fixed quota. If the hard limits make it impossible to achieve this exact quota, the plan must be rejected.

## Input
The first line contains three integers: $n$ (the number of distribution centers), $m$ (the number of freight routes), and the number $1$ (representing the single freight category).
The second line contains three integers: $s$ (the dispatch center), $t$ (the receiving center), and $d$ (the required fixed quota).
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a unidirectional freight route from center $u$ to center $v$ with a hard limit of $cap$ freight units.

## Output
If an operational plan can meet the quota, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of freight units allocated to each route (in the exact order the routes were provided in the input).
If the quota cannot be met under the given hard limits, print `NO`.

## Example

### Input
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```
YES
5 5 0 5 5
```
