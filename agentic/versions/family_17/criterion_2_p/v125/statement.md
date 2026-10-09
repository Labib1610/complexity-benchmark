# Phase-Locked Loop Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
An array of $2q$ oscillators is deployed within a testing facility. These components are strictly partitioned into two operational groups based on their IDs. Oscillators identified by integers from $1$ up to $q$ serve as frequency references. Oscillators identified from $q+1$ up to $2q$ operate as phase trackers.

The system relies on establishing synchronization locks between components. However, a lock can only be physically formed between specific, hardware-compatible pairs, which always consist of one frequency reference and one phase tracker. The system is supplied with the complete set of these compatible pairs.

During any operation, strict safety protocols apply. First, if a lock is established between a compatible pair, neither of those two oscillators may be involved in any other lock. Second, any oscillator—whether a reference or a tracker—that remains completely unlinked will trigger a system fault.

To proceed with the calibration test, the facility must be brought into a configuration where no safety protocols are violated and absolutely no system faults are triggered. Determine whether such an arrangement of locks can be selected from the available compatible pairs. If it is achievable, output the exact pairs that should be locked; otherwise, indicate that the test must be aborted.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The integer $q$ defines the size of each operational group, resulting in $2q$ total oscillators, while $t$ represents the total number of hardware-compatible pairs.
The subsequent $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that frequency reference $a$ and phase tracker $b$ are hardware-compatible and capable of forming a lock.

## Output
If the required arrangement is possible, print `YES` on the first line, followed by $q$ lines each containing the two oscillator identifiers of an activated lock. Any valid arrangement may be printed if multiple exist. If no such arrangement can be formed, print `NO`.

## Example
**Input**
```
3 4
1 4
2 5
3 6
2 6
```

**Output**
```
YES
1 4
2 5
3 6
```
