# Problem C — Linguistic Panels

Time limit: 2 s   Memory limit: 256 MB

You are organizing an international linguistic conference featuring $n$ distinct languages, numbered 1 through $n$. To facilitate communication, you have hired $m$ bilingual interpreters. Each interpreter is certified to translate between a specific combination of two languages. 

The conference organizers want to host a special "closed discussion panel." A valid panel requires selecting exactly three different languages, and dedicating exactly three interpreters from your roster to serve this panel. For the panel to function, each of the three dedicated interpreters must handle a different pair of the three selected languages.

Given the roster of hired interpreters, your task is to identify three languages that can form such a panel.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ — representing an interpreter in your roster who translates between language $u$ and language $v$.
There is at most one interpreter for any given combination of two languages.
It is guaranteed that at least one valid closed discussion panel can be formed.

## Output
Output three integers $a$ $b$ $c$ on a single line, ordered such that $a < b < c$, representing the languages in the panel. If multiple such panels exist, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and finally the smallest $c$).

## Example 1
Input:
4 5
1 2
1 3
2 3
2 4
3 4

Output:
1 2 3

## Example 2
Input:
5 6
1 2
1 4
2 4
3 4
3 5
4 5

Output:
1 2 4