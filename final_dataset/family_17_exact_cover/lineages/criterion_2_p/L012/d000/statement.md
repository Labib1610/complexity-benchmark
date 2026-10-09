# Problem B — Full-Capacity Controller/Platform Synchronization

Time limit: 2 s
Memory limit: 256 MB

## Description
The directorate's remote segment must be fully engaged for the upcoming drill. The segment consists of $2q$ hardware modules. Modules assigned identifiers from $1$ up to $q$ are configured as controllers, while modules with identifiers from $q+1$ up to $2q$ are configured as platforms.

During the drill, modules must communicate via dedicated telemetry channels. A valid channel strictly bridges one controller to one platform. The engineering logs provide a catalog of pre-verified channels, each specifying a controller and a platform that can successfully synchronize. Unlisted combinations are strictly forbidden due to hardware mismatches. The catalog may contain densely overlapping options, with many more verified combinations than will ultimately be used. 

To achieve full capacity, you must select a subset of these pre-verified channels such that every single module in the segment (all $2q$ of them) is assigned to exactly one active channel. A module cannot be assigned to multiple active channels, and no module can be left idle.

Determine if it is possible to activate a set of channels that engages all modules simultaneously in this manner. If such a configuration exists, you must also provide the list of channels to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of modules and the number of pre-verified channels, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a pre-verified channel between controller $a$ and platform $b$.

## Output
If a valid configuration exists, print `YES` on the first line, followed by $q$ lines each containing the two module identifiers for an active channel in your selection. If no such configuration is possible, print `NO`.

## Example
### Input
```text
3 4
1 4
2 5
3 5
2 6
```

### Output
```text
YES
1 4
3 5
2 6
```
