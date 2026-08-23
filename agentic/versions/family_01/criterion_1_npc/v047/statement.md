# Secure Facility Deployment

Time limit: 2 s   Memory limit: 256 MB

You are managing the deployment of $n$ security personnel across three distinct zones (labeled 1, 2, and 3) in a secure facility. The personnel are numbered 1 to $n$. 

During the initial screening, the intelligence unit produced a list of $m$ incompatibility reports. Each report identifies two personnel who cannot be deployed to the same zone due to operational risks. 

To comply with facility regulations, the deployment must satisfy the following organizational conditions:
- The total number of incompatibility reports processed, $m$, is guaranteed to never exceed 780.
- Exactly $n$ personnel must be assigned across the zones, meaning no personnel can be left unassigned or assigned to multiple zones.
- The sum of the zone labels assigned to all $n$ personnel must be less than or equal to $3n$.

Your objective is to assign each of the $n$ personnel to a zone such that no two personnel in the same zone share an incompatibility report. 

If multiple valid deployment configurations exist, you must select the one that is lexicographically smallest. A configuration $A$ is lexicographically smaller than $B$ if, for the lowest-numbered personnel where their zone assignments differ, configuration $A$ assigns them to a lower-numbered zone than $B$.

If it is impossible to satisfy all conditions, you must report this so the deployment can be aborted.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ n ≤ 40, 0 ≤ m ≤ n(n-1)/2).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of personnel who are incompatible.

## Output
If no valid deployment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $z_1, z_2, \dots, z_n$ (each in {1, 2, 3}), where $z_i$ is the zone assigned to personnel $i$. Among all valid configurations, output the lexicographically smallest sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
