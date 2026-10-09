# Problem A — Corporate Restructuring

Time limit: 5 s
Memory limit: 256 MB

## Description
A corporation is reorganizing its management structure. There are $n$ department heads who must each be assigned a unique clearance tier from $1$ to $n$. Every tier from $1$ to $n$ will be occupied by exactly one department head.

The corporation has identified $m$ critical collaboration channels. Each channel requires two specific department heads to regularly exchange classified reports. When two department heads exchange reports, the security protocol requires encrypting the data. The processing time required for this encryption is determined by the gap between their clearance tiers. Specifically, if one head is at tier $x$ and the other is at tier $y$, the processing time for their channel is exactly $|x - y|$ milliseconds.

The board of directors demands that the total processing time across all $m$ collaboration channels must not exceed $B$ milliseconds. The channels are independent; their processing times are simply added together to find the total.

Determine if there is a way to assign the clearance tiers to the department heads such that the total processing time is at most $B$. If it is possible, provide a valid tier assignment. Otherwise, state that it is impossible.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that there is a collaboration channel between department head $u$ and department head $v$. The department heads are numbered $1$ to $n$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the clearance tier assigned to department head $i$. If there are multiple valid assignments, any of them will be accepted.
If no such assignment exists, print `NO`.

## Example 1
### Input
```
3 2 3
1 2
2 3
```
### Output
```
YES
1 2 3
```

## Example 2
### Input
```
3 3 3
1 2
2 3
3 1
```
### Output
```
NO
```
