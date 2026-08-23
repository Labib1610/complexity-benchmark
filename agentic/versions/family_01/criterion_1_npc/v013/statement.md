# Problem A — Shift Allocation Protocol

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant operates three daily shifts: Shift 1, Shift 2, and Shift 3. There are $n$ personnel available. To ensure smooth operations, certain pairs of personnel have documented incompatibilities and cannot be scheduled on the same shift.

If the plant only had two shifts, assigning personnel would be a straightforward alternating process. The addition of a third shift provides more flexibility to resolve incompatibilities. The plant uses a sequential protocol to assign each person to exactly one of the three shifts. Because early shifts are preferred, the protocol dictates that the final assignment must be the lexicographically smallest valid sequence. This means the system heavily prioritizes assigning person 1 to Shift 1. If that choice inevitably forces a scheduling failure later in the process, person 1 is evaluated for Shift 2, and so on. The same strict sequential preference applies to person 2, person 3, and all others up to person $n$.

Your task is to determine the final schedule produced by this protocol, ensuring no two incompatible personnel share a shift, or to detect if no such schedule can be formed.

## Input
The first line provides two integers $n$ and $m$ — the total number of personnel and the number of documented incompatibilities ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, indicating that person $u$ and person $v$ cannot be assigned to the same shift.

## Output
If there is no way to assign all personnel without violating the incompatibility rules, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ represents the shift assigned to person $i$. The sequence must be the lexicographically smallest valid assignment.

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
