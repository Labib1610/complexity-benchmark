# Swarm Synchronization Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A swarm of $2q$ autonomous drones is preparing for a coordinated flight. The drones are assigned unique IDs from $1$ to $2q$. The swarm's hardware is heterogeneous: drones $1$ through $q$ possess navigation lasers, whereas drones $q+1$ through $2q$ are fitted with retroreflectors.

To establish a stable flight formation, the swarm must be entirely partitioned into independent two-drone squads. A squad is only operational if it contains exactly one laser and exactly one retroreflector. Additionally, interference and obstacles mean that squads can only be formed between specific pairs of drones that have verified line-of-sight. You are provided with a complete list of these verified channels.

Your task is to determine whether it is possible to activate a subset of these channels such that every single drone in the swarm is assigned to exactly one squad. If such a complete partitioning exists, you must output the channels to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a verified channel between drone $a$ and drone $b$.

## Output
If the swarm can be completely partitioned into operational squads, print `YES` on the first line, followed by $q$ lines each containing the two integers of an activated channel. If it is impossible, print `NO`.

## Example 1
### Input
```
3 4
1 4
2 5
3 5
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
