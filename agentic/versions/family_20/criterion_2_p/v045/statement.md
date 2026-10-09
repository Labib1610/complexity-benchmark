# Problem B — Certification Drives for the Delivery Fleet

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics organisation needs to evaluate its delivery personnel. To do this, it maintains two distinct rosters: delivery drivers and safety inspectors. A certification drive always involves exactly one driver and exactly one inspector. No drive ever pairs two drivers or two inspectors together.

Each person (whether driver or inspector) is required to participate in some specific count of drives. Let $D$ be the maximum number of drives assigned to any single individual across the entire program.

Drives are scheduled on specific days, numbered sequentially starting from 1. A drive takes an entire day. Because no person can be in two places at once, any two drives sharing a participant (either the driver or the inspector) must be assigned to different days.

Since the busiest individual has $D$ drives, the schedule must span at least $D$ days. The operational goal is to compress the schedule as much as possible, completing all drives in exactly $D$ days. Your task is to assign each drive a day from $1$ to $D$ such that no person ever has multiple drives on the same day. (The strict two-sided nature of the pairings guarantees it is always possible to fit all drives into exactly $D$ days without conflicts.)

## Input
The first line contains three integers: the driver headcount $n_L$, the inspector headcount $n_R$, and the total number of drives $m$.
The next $m$ lines each contain two integers $u$ and $v$, representing a drive between driver $u$ and inspector $v$.

Facility limits dictate that the driver roster and the inspector roster each contain at least one person, and neither roster can exceed a maximum capacity of one hundred thousand people.
The total number of required drives can be as low as zero, up to a maximum of four times a single roster's maximum capacity.
Driver IDs range from 1 to the driver headcount, and inspector IDs range from 1 to the inspector headcount.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $i$-th integer represents the day assigned to the $i$-th drive in the input order. Each day must be an integer between $1$ and $D$ inclusive, and drives sharing any person must differ in their assigned day.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
