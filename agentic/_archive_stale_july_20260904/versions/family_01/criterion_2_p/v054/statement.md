# Synchronized Transmission

Time limit: 1 s   Memory limit: 256 MB

You are designing a synchronized transmission with $n$ interlocking gears, labeled 1 to $n$. When the machine is turned on, every gear rotates steadily in one of two states: state 1 (clockwise) or state 2 (counter-clockwise).

The transmission framework specifies $m$ contact points between specific gears. Because the teeth of contacting gears mesh, any two gears that share a contact point are physically forced to rotate in opposite states; otherwise, the entire transmission locks up.

Your task is to determine whether it is physically possible to assign an initial rotation state to every gear in the transmission such that no two meshing gears share the same rotation state. If a jam is unavoidable, state so. If a valid configuration exists, you might find several ways to set up the gears. In that case, you must choose the one that yields the lexicographically smallest sequence of states when you list the gears' states in order from gear 1 to gear $n$.

## Input
The first line contains two integers $n$ and $m$. The number of gears $n$ is at least 1. It is limited by the maximum capacity of the transmission housing, which is constructed from exactly 400 identical modules, each capable of holding exactly 500 gears. The number of contact points $m$ is a non-negative integer that will not exceed the total gear capacity of the housing.

Each of the next $m$ lines contains two integers $u$ and $v$. These mean the gear labeled $u$ and the gear labeled $v$ share a contact point, and are guaranteed to be valid gear labels from 1 to $n$.

## Output
If no valid assignment of rotation states exists without causing a lock-up, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers, each being either 1 or 2. These integers must represent the rotation states of gears 1 through $n$, respectively, forming the lexicographically smallest sequence among all valid assignments.

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
