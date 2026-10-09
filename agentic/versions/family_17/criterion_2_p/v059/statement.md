# Datacenter Transition Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A datacenter is moving its operations from $q$ old units (numbered $1$ through $q$) to $q$ new units (numbered $q+1$ through $2q$).

The transition requires selecting a set of transition pathways. You are given $t$ potential pathways. Each pathway links one old unit to one new unit, indicating that the old unit's configuration is supported by that specific new unit.

To execute a full transition, you must choose a subset of these pathways to activate. A successful full transition must incorporate all $2q$ units. However, each unit (whether old or new) has the capacity to be involved in only a single activated pathway. You must find a collection of activated pathways that includes all units without exceeding this capacity limit.

Determine if it is possible to achieve a full transition. If it is, output the specific pathways to use. Otherwise, report that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of old units (which also equals the number of new units) and the number of potential pathways.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a potential pathway between old unit $a$ and new unit $b$.

## Output
If a full transition is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two identifiers of a pathway chosen for your transition.
If it is impossible, print `NO`.

## Example 1

### Input
```
3 4
1 4
2 4
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

## Example 2

### Input
```
2 2
1 3
2 3
```

### Output
```
NO
```
