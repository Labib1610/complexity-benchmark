# Problem A — Manuscript Restoration

Time limit: 5 s   Memory limit: 256 MB

## Description

An ancient library is restoring $s$ fragile scrolls. The restoration facility contains $c$ specialized atmospheric chambers.

Each scroll requires a strict sequence of restoration phases. A phase consists of placing the scroll into a specific chamber for a precise number of time units. The physical constraints of the restoration process are:

- A scroll's phases must be conducted in the exact order they are prescribed. A new phase for a scroll cannot begin until its preceding phase has fully concluded.
- A chamber is a sealed environment and can hold only a single scroll at a time.
- Once a scroll is sealed inside a chamber for a phase, it cannot be removed or interrupted until the full duration of that phase has elapsed.

Your task is to coordinate the use of the chambers to minimize the time at which all scrolls are completely restored. Report this earliest possible completion time.

## Input

The first line contains two integers $s$ and $c$, representing the number of scrolls and chambers. The batch being processed contains a minimum of one scroll and a maximum of 10, dictated by the carrying case's 10 slots. The facility operates with a minimum of one chamber and a maximum of 10, corresponding to the 10 available rooms.

Each of the next $s$ lines details the requirements for one scroll. A line begins with an integer $p$, representing the number of phases for that scroll, followed by $p$ pairs of integers `chamber duration`, detailing the phases in their required order. A `chamber` is identified by an integer from 1 up to $c$. A phase's `duration` requires a minimum of one time unit, and its maximum is strictly capped at 1000 time units by the sand in the monitoring hourglass. The cumulative number of phases across all scrolls is capped at 50 by the daily ledger's maximum entry count.

## Output

Print a single integer: the earliest possible time at which all scrolls are completely restored.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical scrolls each pass through chambers 1, 2, and 3 (taking 2 time units in each); the second scroll trails the first through the sequence and concludes at time 8. In Example 3, the two scrolls use different chambers and are restored in parallel, concluding at time 4.
