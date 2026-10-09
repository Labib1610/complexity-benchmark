# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate oversees a collection of operational assets, which are assigned numerical identifiers based on their role. Controllers are assigned consecutive integers from $1$ to $q$, while platforms receive consecutive integers from $q+1$ to $2q$. 

During operations, a controller may be teamed with a platform. However, this is only permitted when that exact combination appears on a pre-approved certification list. A controller is typically certified with several platforms, and a platform with several controllers. The certification list can be large and densely overlapping, containing many more certified combinations than will ultimately be used. Any combination not explicitly on this list is strictly forbidden, no matter how convenient it might be.

When an operational roster is formed, it consists of a selection of these certified combinations. A strict safety regulation dictates that no asset—neither controller nor platform—may be shared between two active combinations. That is, each asset can participate in at most one team on the roster.

Command is planning a drill for the remote segment. For this specific drill, the directorate demands full commitment of the assets. You must determine whether it is possible to form a roster from the certification list such that every single controller and every single platform is committed exactly once. If such a complete one-to-one commitment is possible, you must provide one valid configuration; otherwise, you must report that the requirements cannot be met.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ form a certified combination.

## Output
If a fully committed roster is possible, print `YES` on the first line, followed by $q$ lines each containing the two items of one chosen combination. If it is not possible, print `NO`.

## Example

### Input
```
2 3
1 3
1 4
2 3
```

### Output
```
YES
1 4
2 3
```
