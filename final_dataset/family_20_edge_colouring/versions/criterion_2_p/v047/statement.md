# Problem B — Service Windows on a Two-Sided Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
A communication facility contains two distinct groups of terminals: the Alpha bank and the Beta bank. Data links are installed such that each link bridges exactly one Alpha terminal to exactly one Beta terminal. Links never connect two terminals within the same bank.

To maintain the system, each data link must be taken offline during a specific maintenance phase. The phases are sequentially numbered 1, 2, 3, and so on. A critical hardware limitation dictates that if two or more data links terminate at the exact same terminal (whether in the Alpha or Beta bank), they must be assigned to strictly different maintenance phases. This is because a terminal cannot safely have multiple of its connections offline simultaneously.

By design, the facility's topology adheres to two strict operational invariants:
1. The total number of link terminations on the Alpha bank is always identical to the total number of link terminations on the Beta bank.
2. The maximum number of links connected to any single terminal never exceeds the total number of links in the system.

Let $K$ be the highest number of data links connected to any single terminal in the facility. Because all $K$ links at that busiest terminal must be assigned different phases, the facility requires at least $K$ maintenance phases. Due to the strict Alpha-to-Beta wiring, it is a proven property of the facility that exactly $K$ phases are always sufficient to schedule all links safely.

Your task is to assign a maintenance phase to each data link using at most $K$ distinct phases. The phases must be chosen from the range 1 to $K$, ensuring no terminal has multiple links scheduled in the same phase.

## Input
The first line contains three integers $A$, $B$, and $L$ ($1 \le A, B \le 100000$, $0 \le L \le 400000$), representing the number of Alpha terminals, Beta terminals, and data links, respectively.
The next $L$ lines each contain two integers $u$ and $v$ ($1 \le u \le A$, $1 \le v \le B$), indicating a data link between Alpha terminal $u$ and Beta terminal $v$.

## Output
Print `YES` on the first line.
On the second line, print $L$ integers. The $i$-th integer (corresponding to the $i$-th link in the input) must be the phase assigned to that link. The assigned phases must be between 1 and $K$, inclusive, and must satisfy the safety limitations.

## Example

**Input**
```text
3 3 4
1 1
1 2
2 2
3 2
```

**Output**
```text
YES
1 2 1 3
```
