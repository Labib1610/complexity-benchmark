# Problem B — Grid Phase Configuration

Time limit: 1 s   Memory limit: 256 MB

You are configuring the properties of an $n \times n$ grid. To do this, you must assign a single phase array $p$ of length $n$, where each element $p_i \in \{1, 2\}$ for $1 \le i \le n$.
This array simultaneously dictates the phases of the grid's rows and columns: the phase of row $i$ is defined as $p_i$, and the phase of column $i$ is also defined as $p_i$.

You are given a list of $m$ conflict cells within the grid. The $k$-th conflict cell is located at row $u_k$ and column $v_k$.
A phase configuration is valid if, for every conflict cell, the phase of its row is different from the phase of its column.

Your objective is to determine if there exists a valid phase configuration. If there are multiple valid configurations, you must output the one whose sequence $p_1, p_2, \dots, p_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the size of the phase array and the number of conflict cells.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying the 1-based row and column indices of a conflict cell.

## Output
If no valid phase configuration is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2\}$) denoting the phase array. Among all valid assignments, you must output the lexicographically smallest sequence.

## Example 1
Input:
4 4
1 2
2 3
3 4
1 4
Output:
YES
1 2 1 2

## Example 2
Input:
3 3
1 2
1 3
2 3
Output:
NO