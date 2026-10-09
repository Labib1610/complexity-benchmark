# Problem A — Gourmet Exhibition Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description
You are organizing a gourmet exhibition featuring $n$ distinct signature dishes, numbered 1 to $n$. The event is structured as a sequence of tasting rounds, starting from round 1. Each dish must be featured in exactly one round.

The service mechanics and venue rules impose strict physical limits on the event:
* **Equipment limit:** Each round is delivered to the dining room using a specialized trolley system. The trolley system has exactly $M$ plate slots in total. Since each dish requires one slot and no alternative transport is allowed, the number of dishes in a single round is physically limited by this count.
* **Time limit:** The dining room's lighting system is programmed to automatically shut down at the exact conclusion of the $T$-th tasting round. All dishes must be served before this shutdown.

Additionally, the head chef has specified $m$ flavor progression requirements. Each requirement dictates that a specific dish $a$ must be served in a round that takes place strictly before the round containing dish $b$. Serving them in the same round is forbidden, as guests must cleanse their palates between these specific dishes.

Determine if it is possible to assign each of the $n$ dishes to a round such that all equipment, venue, and chef requirements are satisfied. If it is possible, provide a valid schedule.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the following $m$ lines contains two integers $a$ and $b$, representing a flavor progression requirement where dish $a$ must be served in an earlier round than dish $b$.

## Output
If a valid schedule can be formed, print `YES` on the first line, followed by a second line containing $n$ integers. The $i$-th integer must be the round number during which dish $i$ is served. If no such schedule is possible, print `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
