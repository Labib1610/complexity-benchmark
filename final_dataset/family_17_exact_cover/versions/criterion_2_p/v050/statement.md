# Full-Capacity Command/Response Synchronization

Time limit: 2 s
Memory limit: 256 MB

## Description
The remote sector's hardware array must be fully engaged for the upcoming drill. The array consists of $2q$ hardware units. Units assigned identifiers from $1$ up to $q$ are initialized in command mode, while units with identifiers from $q+1$ up to $2q$ are initialized in response mode.

During the drill, units communicate via telemetry links. The engineering logs provide a catalog of pre-verified links, each specifying a command unit and a response unit that can successfully synchronize. Unlisted combinations are strictly forbidden due to hardware mismatches. The logs may contain densely overlapping options, with many more verified combinations than will ultimately be activated.

Each unit is equipped with a single transceiver. Activating a link consumes the transceiver of both the specific command unit and the specific response unit it connects. To achieve full capacity, you must activate a collection of the pre-verified links such that every transceiver in the entire array (all $2q$ of them) is consumed. A transceiver cannot support multiple links, and no transceiver may be left idle.

Determine if it is possible to activate a set of links that engages all units simultaneously in this manner. If such a configuration exists, you must also provide the list of links to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of units and the number of pre-verified links, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a pre-verified link capable of synchronizing command unit $a$ and response unit $b$.

## Output
If a valid configuration exists, print `YES` on the first line, followed by $q$ lines each containing the two unit identifiers for an active link in your selection. If no such configuration is possible, print `NO`.

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
