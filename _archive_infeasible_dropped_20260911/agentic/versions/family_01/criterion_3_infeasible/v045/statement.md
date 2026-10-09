# Problem C — Communication Blockages

Time limit: 2 s   Memory limit: 256 MB

A corporation is auditing its internal communication network. The system administrators have implemented a series of bilateral communication blocks between certain pairs of staff members. 

Your objective is to identify a strict triad of restricted communication. Specifically, you must locate exactly three staff members such that every individual in this triad is blocked from communicating with both of the other two individuals. 

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of staff members and the number of bilateral communication blocks, respectively.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating a communication block between staff member $u$ and staff member $v$. 

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identified staff members. These must be printed in ascending order ($a < b < c$). 
If multiple such triads exist, output the one that appears first lexicographically (minimize $a$; in case of a tie, minimize $b$; in case of a further tie, minimize $c$).

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
