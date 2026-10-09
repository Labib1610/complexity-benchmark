# Shift Separation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility maintains a roster of $n$ operators. The facility's operations center is equipped with exactly 40 control consoles, meaning the roster size $n$ is at least one and will never exceed the number of available consoles. Over time, management has recorded $m$ specific pairs of operators who exhibit detrimental friction when working together. The number of such records $m$ can range from none at all up to the theoretical maximum where every operator has friction with every other operator. Company policy strictly dictates that any two operators in a recorded pair cannot be assigned to the same shift. 

The facility operates continuously, utilizing exactly three distinct shifts: shift 1, shift 2, and shift 3. 

Your task is to determine if it is possible to assign every single operator to exactly one of these three shifts such that the separation policy is never violated. If such an arrangement exists, you must also provide it.

## Input
The first line contains two integers $n$ and $m$ — the number of operators and the number of friction pairs.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that operator $u$ and operator $v$ cannot share a shift.

## Output
If there is no way to assign all operators without violating the policy, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ represents the shift assigned to operator $i$. If multiple valid assignments exist, any of them will be accepted.

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
