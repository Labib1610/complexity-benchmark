# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate is preparing a deployment roster for the remote segment. The inventory consists of $q$ controllers, assigned identifiers $1$ through $q$, and $q$ platforms, assigned identifiers $q+1$ through $2q$.

Due to strict hardware compatibility protocols, a controller cannot interface with just any platform. You are provided with a comprehensive list of certified controller-platform data links. An active deployment team consists of a single controller and a single platform whose data link appears on this certified list.

To prevent signal interference during operations, a controller can be assigned to at most one team, and a platform can be assigned to at most one team. 

The upcoming drill mandates a maximum utilization protocol. The directorate requires a deployment roster where every single controller in the inventory is assigned to a platform, and every single platform is assigned to a controller. You must determine if it is possible to satisfy this maximum utilization protocol. If it is possible, you must output a valid set of teams; otherwise, you must report that the roster cannot be formed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (which also equals the number of platforms) and the number of certified data links.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ share a certified data link.

## Output
If a deployment roster satisfying the maximum utilization protocol is possible, print `YES` on the first line, followed by $q$ lines each containing the two identifiers of one chosen team. If it is not possible, print `NO`.

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
