# Reactive Compound Storage

Time limit: 1 s   Memory limit: 256 MB

A pharmaceutical company is managing $n$ newly synthesized chemical compounds, numbered 1 to $n$. To ensure safety, each compound must be securely stored in one of two climate-controlled facilities: Facility 1 or Facility 2.

Through preliminary testing, the safety team has identified $m$ pairs of compounds that are highly reactive with each other. If both compounds in a reactive pair are placed in the same facility, the shared ventilation system will cause a dangerous reaction. Therefore, they must be assigned to different facilities.

Your task is to determine whether it is possible to assign every compound to a facility without placing any reactive pair in the same facility.

If a safe storage plan exists, you must provide it. Because there are multiple ways to distribute the compounds safely, the logistics department prefers the plan that assigns as many low-numbered compounds to Facility 1 as possible. Formally, you must output the lexicographically smallest sequence of facility assignments. A sequence of assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first compound index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of compounds and the number of reactive pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of compounds that will react if stored in the same facility.

## Output
If there is no way to safely assign all compounds to Facility 1 and Facility 2, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid storage plan.

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