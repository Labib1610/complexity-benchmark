# Problem A — System State Configuration

Time limit: 2 s   Memory limit: 256 MB

You are configuring a system with $n$ components, indexed from $1$ to $n$. Each component must be set to exactly one of three operational modes: mode 1, mode 2, or mode 3. It is permissible for a mode to have zero components assigned to it.

The system is subject to $m$ interference constraints. Each constraint specifies a pair of components $u$ and $v$ that interfere with each other. To ensure system stability, any two components that interfere must be set to different operational modes.

The complete configuration of the system is represented by a sequence of $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ denotes the mode of component $i$. If there are multiple stable configurations, you must select the one whose configuration sequence is lexicographically smallest. That is, when comparing two valid sequences, the one with the smaller value at the first index where they differ is strictly preferred.

Determine if a stable configuration exists, and if so, output the optimal one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of components and the number of interference constraints.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that component $u$ and component $v$ interfere with each other.

## Output
If no stable configuration is possible, print a single line containing `NO`.
If a stable configuration is possible, print `YES` on the first line. On the second line, print exactly $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the mode assigned to component $i$. Among all stable configurations, you must output the lexicographically smallest sequence $c_1, c_2, \ldots, c_n$ (compare $c_1$ first, then $c_2$, etc.).

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