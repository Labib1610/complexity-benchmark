# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The assets are divided into two equal groups of size $q$: a set of controllers (assigned consecutive IDs from $1$ to $q$) and a set of platforms (assigned consecutive IDs from $q+1$ to $2q$). Each controller and platform is a distinct asset.

A controller can only be teamed with a platform if their specific pairing appears on the approved certification list. Uncertified combinations are strictly forbidden. The certification list may be large and densely overlapping. 

To comply with hardware tiering protocols, the certification list is guaranteed to only contain pairings that satisfy two conditions:
1. The numerical gap between the platform's ID and the controller's ID is at least 1 and at most $2q - 1$.
2. The sum of their IDs does not exceed $3q$.

The directorate's remote segment requires a roster for the upcoming drill. An acceptable roster activates a subset of the certified combinations such that **every** controller and **every** platform is committed in **exactly one** activated combination. No asset can be omitted, and no asset can be shared between two combinations. Because both groups are exactly the same size, an acceptable roster fully commits every asset with nothing left over.

Determine whether the certification list admits such a complete one-to-one commitment of all assets. If it does, output one valid roster; otherwise, report that the certified combinations cannot simultaneously commit every asset.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (and platforms) and the number of certified combinations, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified pair consisting of controller $a$ and platform $b$.

## Output
If a complete roster is possible, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated pair. If no such roster exists, print `NO`.

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
