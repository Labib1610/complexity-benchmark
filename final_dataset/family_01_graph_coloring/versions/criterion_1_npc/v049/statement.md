# Problem A — Deep-Sea Containment

Time limit: 2 s   Memory limit: 256 MB

Deep-sea research operations have recovered $n$ anomalous artifacts from the ocean floor. Extensive testing on these objects has identified $m$ specific pairs that emit interfering energy fields. The primary safety protocol dictates that if two artifacts are known to interfere with each other, they cannot be confined within the same physical space, as their combined resonance will critically overload any shielding.

The facility is equipped with exactly three reinforced containment modules, which are designated by the numbers 1, 2, and 3. 

Subject to the safety protocol, your task is to formulate a storage plan that assigns every single artifact to exactly one of the three available modules. If no such arrangement can be made without causing an overload, you must report this failure.

## Input
The first line provides two integers $n$ and $m$ — the total number of artifacts and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of interfering artifacts. Artifacts are numbered from 1 to $n$.

## Output
If no safe storage plan exists, print a single line with the word NO.
If a valid plan is possible, print YES on the first line. On the second line, print $n$ integers $m_1, m_2, \dots, m_n$ (each in \{1, 2, 3\}), where $m_i$ is the module chosen for artifact $i$. Any configuration that satisfies all safety conditions is acceptable.

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
