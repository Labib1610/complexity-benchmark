# Symbiotic Colony

Time limit: 1 s
Memory limit: 256 MB

A research team is studying a colony of $n$ symbiotic organisms. In a controlled environment, each organism must be induced into one of two metabolic states, denoted as state 1 and state 2.

The colony relies on $m$ nutrient exchange channels. Each channel directly connects a specific pair of organisms, allowing them to continuously share nutrients. However, the channels contain a biological filter that alters the nutrients passing through them. 
Specifically, nutrients secreted by an organism in state 1 undergo a chemical shift in the channel and arrive requiring the receiver to be in state 2 to absorb them. Conversely, nutrients secreted by an organism in state 2 undergo a shift and arrive requiring the receiver to be in state 1.

For the colony to survive, every exchange channel must be viable in both directions. This means each organism's single assigned metabolic state must allow it to successfully absorb the nutrients arriving from all of its connected partners. If any organism cannot absorb the incoming nutrients from a channel, the entire colony will collapse.

You must determine a valid metabolic state assignment for all $n$ organisms that ensures survival. When multiple valid assignments exist, the laboratory's induction protocol dictates using the lexicographically smallest sequence (meaning the sequence of states $s_1, s_2, \dots, s_n$ should be as small as possible when evaluated element by element from the first organism to the last).

## Input
The first line provides the number of organisms $n$ and the number of exchange channels $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing an exchange channel connecting organism $u$ and organism $v$.

## Output
If it is impossible to assign the metabolic states without the colony collapsing, output a single line with `NO`.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, \dots, s_n$ (where each is 1 or 2), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```