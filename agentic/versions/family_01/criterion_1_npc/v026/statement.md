# Problem A — Spectrum Division Protocol

Time limit: 2 s   Memory limit: 256 MB

As part of an automated signal pipeline, the control system executes three consecutive procedures: Signal Extraction, Spectrum Division, and Packet Encoding.

In the completed Signal Extraction phase, the system registered $n$ active broadcast units, numbered $1$ through $n$, and identified $m$ interfering pairs of units.

In the current **Spectrum Division** phase, every unit must be assigned to exactly one of three available operational frequencies, represented by the integers $1$, $2$, and $3$. If two units form an interfering pair, they cannot be assigned to the same frequency.

Once this phase succeeds, the chosen frequency assignment sequence $s_1, s_2, \dots, s_n$ will be passed directly to the Packet Encoding phase. If multiple valid frequency assignments exist, you must select the one that is lexicographically smallest (comparing $s_1$ first, then $s_2$, and so on) to ensure downstream deterministic initialization. If no valid assignment can satisfy all interference constraints, the processing pipeline aborts.

Determine whether a valid assignment exists, and if so, produce the lexicographically smallest frequency allocation sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of broadcast units and the number of interfering pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that unit $u$ and unit $v$ form an interfering pair.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the frequency assigned to unit $i$. Among all valid assignments, output the lexicographically smallest sequence.

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
