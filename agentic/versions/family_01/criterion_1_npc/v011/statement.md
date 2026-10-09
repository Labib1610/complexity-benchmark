# Problem A — Deep-Sea Containment

Time limit: 2 s   Memory limit: 256 MB

A deep-sea research station operates three reinforced containment modules, designated as 1, 2, and 3. The station has recently recovered $n$ anomalous artifacts from the ocean floor. Every artifact must be secured within exactly one of these three modules.

However, the artifacts emit interfering energy fields. Testing has identified specific pairs of artifacts that will critically overload a module's shielding if they are confined in the same space. 

You must formulate a storage plan that assigns every artifact to a module such that no two interfering artifacts are placed together. If it is impossible to secure all artifacts under these conditions, you must report this failure.

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
