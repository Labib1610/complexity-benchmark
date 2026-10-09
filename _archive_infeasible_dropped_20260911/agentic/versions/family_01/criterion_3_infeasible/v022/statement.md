# Problem C — The Triple Alliance

Time limit: 2 s   Memory limit: 256 MB

You are analyzing the diplomatic archives of an ancient civilization comprising $n$ city-states, numbered $1$ through $n$. The records detail $m$ mutual defense pacts, each formed between a pair of city-states.

Historians are searching the archives for a "Triple Alliance." A Triple Alliance consists of three distinct city-states where every possible pair within the trio has established a mutual defense pact (i.e., a pact exists between the first and second, the first and third, and the second and third). It is a verified historical fact that at least one such alliance exists in the provided records. Your task is to identify its members.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of city-states that share a mutual defense pact.
It is guaranteed that at least one Triple Alliance exists.

## Output
Print three integers $a$ $b$ $c$ on a single line with $a < b < c$, representing the city-states in the Triple Alliance. Output the lexicographically smallest such trio (smallest $a$; ties by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
