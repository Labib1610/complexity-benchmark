# Problem B — Single-Product Dispatch over a Corridor Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics grid is composed of several hubs linked by one-way haulage lanes. Every lane possesses a strict upper limit on the number of shipping containers it can transport during a single operational cycle. For any given lane, the assigned number of containers must be a non-negative whole number that does not exceed this limit.

Furthermore, containers cannot be stored or dismantled mid-journey. At any hub other than the origin and destination, the total number of containers arriving via incoming lanes must perfectly equal the total number departing via outgoing lanes.

Within this rigid framework, a specific operational mandate must be fulfilled. A single designated origin hub must dispatch a net amount (total departing minus total arriving) exactly equal to a precise target quantity of containers. Simultaneously, a single designated destination hub must receive a net amount (total arriving minus total departing) equal to that exact same quantity. Transit times, empty container repositioning, and the chronological sequence of movements are strictly outside the scope of this plan and must be ignored.

Determine a valid assignment of containers to each lane that satisfies all capacity limits and hub balances while successfully moving the target quantity from the origin to the destination in a single cycle. If no such assignment exists, report that the mandate is impossible.

## Input
The first line contains three integers: $n$ (the number of hubs), $m$ (the number of haulage lanes), and the number 1 (indicating a single product type).
The second line contains three integers: $s$ (the origin hub), $t$ (the destination hub), and $d$ (the required target quantity).
The next $m$ lines each contain three integers $u$, $v$, and $c$, representing a one-way haulage lane from hub $u$ to hub $v$ with a maximum capacity of $c$ containers. Hubs are numbered from 1 to $n$.

## Output
If the mandate can be fulfilled, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of containers assigned to each lane in the exact order they appeared in the input. If multiple valid assignments exist, any assignment satisfying all conditions is accepted.
If the mandate cannot be fulfilled, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output:**
```
YES
5 5 0 5 5
```
