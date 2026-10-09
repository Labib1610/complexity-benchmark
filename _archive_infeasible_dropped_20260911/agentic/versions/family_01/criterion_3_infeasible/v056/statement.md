# Problem C — The Tripartite Coalition

Time limit: 2 s   Memory limit: 256 MB

You are studying the economic ledgers of an ancient empire divided into $n$ provinces, identified by integers from $1$ to $n$. The ledgers document $m$ bilateral trade agreements, with each agreement established between two different provinces.

The empire's Great Council chamber contained exactly 2000 seats, ensuring that the number of provinces $n$ never exceeded this capacity. The number of recorded trade agreements $m$ was limited by the imperial library's storage limit of exactly 200,000 scrolls, as well as the natural restriction that any two provinces can share at most one bilateral agreement. You may assume there are always at least 3 provinces and at least 3 agreements.

Researchers are trying to locate a "Tripartite Coalition" within these ledgers. Such a coalition is formed when three distinct provinces are completely economically integrated—meaning a trade agreement exists between the first and second province, between the first and third, and between the second and third. Historical evidence confirms that at least one Tripartite Coalition is documented in these ledgers. Your objective is to determine which provinces form this coalition.

## Input
The first line provides the two integers $n$ and $m$. The possible ranges for these values are dictated by the physical constraints of the council chamber and the library mentioned above.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ — specifying a pair of provinces that have a bilateral trade agreement.
It is guaranteed that the provided ledgers contain at least one Tripartite Coalition.

## Output
Output three integers $a$, $b$, and $c$, separated by spaces, with $a < b < c$, representing the identifiers of the provinces in the Tripartite Coalition. If multiple such coalitions exist, provide the one that is lexicographically earliest (prioritize the smallest value for $a$; if tied, the smallest for $b$; and finally the smallest for $c$).

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
