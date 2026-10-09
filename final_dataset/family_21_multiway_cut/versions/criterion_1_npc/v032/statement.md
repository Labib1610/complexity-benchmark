# Problem A — Grid Synchronization Zoning

Time limit: 5 s
Memory limit: 256 MB

## Description
A regional power grid consists of $n$ substations linked by $m$ bidirectional transmission lines. Each line has a hardware cost to install a phase-decoupler. Among the substations, $k$ are designated as phase-reference generators. 

To ensure grid stability during an upcoming transition, the network must be decomposed into safe operating zones. Because the transmission network is highly redundant and standard substations seamlessly adopt any local phase, the zoning process is structurally straightforward: we simply drop certain connections so that independent synchronization regions form organically. 

Specifically, a line that is decoupled no longer transmits phase synchronization signals in either direction. Your task is to select a set of lines to decouple such that no two phase-reference generators remain connected through any sequence of coupled lines. Substations that are not reference generators are highly flexible; they will automatically synchronize to whichever generator they remain connected to, or operate safely in a standby state if connected to none. Their final zone assignment is unconstrained and irrelevant to the grid's acceptance criteria. What is measured is solely the total hardware cost of the decoupled lines.

There is a fixed hardware budget $B$. Choose a set of lines to decouple whose total cost does not exceed $B$ and whose removal leaves every pair of phase-reference generators disconnected, or report that no valid decoupling within budget can zone the grid.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers, the identifiers of the phase-reference generators (substations are numbered $1$ to $n$).
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a transmission line between substation $u$ and substation $v$ with decoupling cost $w$.

## Output
If a valid set of lines can be decoupled within the budget, output `YES` on the first line. On the second line, output an integer $c$, the number of decoupled lines. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a decoupled line.
If it is impossible to achieve this within the budget, output `NO`.

## Example

**Input:**
```
5 6 3 11
1 3 5
1 2 4
2 3 5
2 4 3
3 5 4
4 5 2
1 4 6
```

**Output:**
```
YES
3
2 3
3 5
4 5
```
