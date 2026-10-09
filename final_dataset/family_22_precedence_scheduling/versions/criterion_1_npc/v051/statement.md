# Problem A — Expedition Logistics

Time limit: 5 s
Memory limit: 256 MB

## Description
An archaeological expedition aims to excavate a historical site divided into $n$ distinct grid units, numbered 1 through $n$. The expedition operates under a strict permit that expires after $T$ weeks, so the entire excavation must be completed within this timeframe.

The site is worked by $M$ specialized teams. Every grid unit contains roughly the same volume of material, taking exactly one week for a single team to clear. A team can only focus on one unit per week, meaning that at most $M$ units can be excavated collectively in any given week. Since the units are homogeneous in their material composition, any team can be assigned to any unit, and only the timing of the excavation matters.

Because the site is fragile, the structural integrity of the trenches must be maintained. Certain grid units are structurally dependent on the prior clearance of others. If unit $b$ is structurally dependent on unit $a$, then unit $a$ must be excavated in a week strictly prior to the week unit $b$ is excavated. It is strictly forbidden to excavate them in the same week, as the exposed walls require the weekend to be properly reinforced before adjacent or deeper digging can commence.

Determine whether it is possible to schedule the excavation of all $n$ units within the $T$ weeks such that the weekly team capacity is never exceeded and all structural dependencies are respected. If a valid schedule exists, provide the week each unit should be excavated.

## Input
First line: four integers $n$, $M$, $T$, $m$.
Each of the next $m$ lines: two integers $a$ and $b$ — unit $a$ must be excavated in a strictly earlier week than unit $b$.

## Output
Print `YES` then $n$ integers (the week assigned to each unit 1 through $n$, taking values in 1..$T$); otherwise print `NO`.

## Example

**Input**
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output**
```text
YES
1 1 2 3 3
```
