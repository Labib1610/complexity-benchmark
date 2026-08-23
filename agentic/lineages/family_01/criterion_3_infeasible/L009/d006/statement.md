# Problem C — Linguistic Panels

Time limit: 2 s   Memory limit: 256 MB

You are organizing an international linguistic conference featuring $n$ distinct languages, numbered 1 through $n$. To facilitate communication, you have hired $m$ bilingual interpreters. Each interpreter is certified to translate between a specific combination of two languages. 

The conference organizers want to host a special "closed discussion panel." A valid panel requires selecting exactly three interpreters from your roster. For the panel to function cohesively, the combined set of languages that these three interpreters are certified to translate must consist of exactly three distinct languages.

Given the roster of hired interpreters, your task is to identify the three languages involved in such a panel.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of languages and the number of hired interpreters, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that you have an interpreter who translates between language $u$ and language $v$.
You have at most one interpreter for any specific pair of languages.
It is guaranteed that the roster contains at least one valid panel.

## Output
Print three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing the three languages involved in the panel. If there are multiple valid sets of three languages, print the lexicographically smallest one (the one with the smallest $a$; in case of a tie, the smallest $b$; and finally the smallest $c$).

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