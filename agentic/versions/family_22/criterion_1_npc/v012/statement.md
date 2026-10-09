# Problem A — Winter Excavation Campaign

Time limit: 5 s   Memory limit: 256 MB

## Description
An archaeological expedition has identified $n$ distinct sectors of an ancient ruin that must be fully excavated before winter arrives in exactly $T$ weeks.

The expedition has $M$ identical excavation crews. Each sector requires exactly one week of work to excavate, and a single crew can only handle one sector per week. Consequently, the maximum number of sectors that can be actively excavated during any single week is limited to $M$.

The ruin is structurally complex, meaning the sectors cannot be excavated in an arbitrary order. Certain sectors block access to others. You are given a list of access conditions: for some pairs of sectors, the first sector must be fully cleared before work can begin on the second. Because a sector takes a full week to clear, a blocked sector can only be excavated in a week that is strictly later than the week its blocking sector is excavated. (If you follow any chain of these requirements, you will never find that a sector must be cleared before itself).

Assign every sector to a specific week so that all access conditions are strictly followed, no week is assigned more sectors than there are crews, and every sector is excavated within the $T$-week timeframe. If it is impossible to accommodate all these constraints, report that the excavation cannot be completed.

## Input
First line: four integers $n$ (number of sectors), $M$ (number of crews), $T$ (weeks before winter), and $m$ (number of access conditions).
Each of the next $m$ lines: two integers $a$ and $b$ — sector $a$ must finish before sector $b$ starts. Sectors are numbered 1 to $n$.

## Output
Print `YES` then $n$ integers (the week each sector is excavated, in 1..T); otherwise print `NO`.

## Example

**Input**
```text
4 2 3 3
1 2
1 3
2 4
```

**Output**
```text
YES
1 2 2 3
```
