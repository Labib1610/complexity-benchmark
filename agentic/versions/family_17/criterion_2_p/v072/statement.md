# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for the drill. The inventory of assets consists of controllers (assigned IDs from $1$ to $q$) and platforms (assigned IDs from $q+1$ to $2q$). Command insists that all $2q$ assets must be active simultaneously in a single, unified plan.

A controller can only be synced with a platform if that specific grouping is present in the certification log. Uncertified syncs are strictly prohibited, regardless of operational convenience. The log may contain many overlapping options, with some controllers certified for multiple platforms and vice versa. This redundancy does not matter; only the explicit presence of a specific sync in the log makes it available for use.

A compliant roster selects a subset of the pre-certified syncs such that each controller is synced with exactly one platform, and each platform is synced with exactly one controller. No asset may participate in more than one sync, and no asset may be left idle. Because there are exactly $q$ controllers and $q$ platforms, a compliant roster will form exactly $q$ syncs, covering the entire inventory.

Your task is to determine whether the certification log allows for a roster that commits all assets under these rules. If it does, provide one such roster; otherwise, state that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (which also equals the number of platforms) and the number of pre-certified syncs, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ are pre-certified to sync.

## Output
If a compliant roster can be formed, output `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated sync. If no such roster is possible, output `NO`.

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
