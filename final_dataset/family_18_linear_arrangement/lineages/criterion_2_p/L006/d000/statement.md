# Assembly Aisle Layout

Time limit: 5 s   Memory limit: 256 MB

## Description
A facility is installing $n$ workstations along a single straight assembly aisle. The aisle has exactly $n$ mounting slots numbered consecutively from 1 to $n$. Each workstation must be assigned to exactly one slot, and no two workstations can share a slot.

The workstations exchange components through $m$ dedicated transfer channels, each linking a specific pair of workstations. The channel network ensures components can travel between any two workstations via some sequence of channels. Additionally, the total number of channels $m$ is exactly one less than the number of workstations.

The operational overhead of a transfer channel connecting a workstation placed at slot $x$ and another at slot $y$ is the physical distance between them, measured as $|x - y|$. The facility has a total overhead budget $B$ for the sum of the overheads of all $m$ channels.

You must find an assignment of workstations to slots such that the total operational overhead is at most $B$, or report that no such assignment exists.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a transfer channel between workstation $u$ and workstation $v$. (The network structure guarantees that all workstations are reachable from each other, and $m = n - 1$).

## Output
If the budget can be met, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the slot number (from 1 to $n$) assigned to workstation $i$. If multiple assignments meet the budget, you may output any of them.
If the budget cannot be met, print `NO`.

## Example

### Input
```text
5 4 6
1 2
1 3
1 4
1 5
```

### Output
```text
YES
3 1 2 4 5
```
