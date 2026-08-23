# Problem B — Factory Protocol

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant is rolling out a new shift system for its $n$ personnel, who are identified by sequential ID numbers starting from 1 up to $n$. Under the new system, each person must be assigned a shift type, which is either $1$ or $2$.

To comply with strict safety mandates regarding shared equipment, personnel who operate the same machinery cannot be on the identical shift type. Specifically, if two people are recorded as sharing equipment, their assigned shift types must add up to exactly 3. You are provided with a log detailing $m$ instances of equipment sharing between pairs of personnel.

Your task is to determine whether it is possible to assign a shift type to all $n$ individuals without violating the safety mandates. If the mandates cannot be met, you must report this. If there are multiple valid ways to assign the shifts, you must provide the sequence of shift types that is lexicographically smallest.

## Input
The first line of the input contains the integers $n$ and $m$. The plant employs at least one person and has a maximum headcount of $200,000$. The log of shared equipment may be empty, but will contain no more than $200,000$ records. 
Each of the following $m$ lines contains two integers $u$ and $v$ representing a logged pair. Both values are valid personnel ID numbers, indicating that person $u$ and person $v$ share equipment.

## Output
If no valid shift assignment can be made, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers (each either $1$ or $2$), representing the lexicographically smallest valid sequence of shift types, where the $i$-th integer corresponds to person $i$.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
