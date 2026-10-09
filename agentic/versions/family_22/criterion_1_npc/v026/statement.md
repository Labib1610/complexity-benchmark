# Phase II: Dive Plan Generation

Time limit: 5 s   Memory limit: 256 MB

## Description
The overall oceanographic survey operation is structured into three distinct phases. 

In Phase I, an orbital satellite scans a designated oceanic sector to identify $n$ distinct hydrothermal vent sites. It generates a bathymetric map and establishes a set of $m$ acoustic calibration dependencies between these sites. This raw data is then passed down to Phase II.

In Phase II, your software must generate a valid deployment plan for a fleet of autonomous underwater vehicles (AUVs). The research vessel can conduct a maximum of $T$ consecutive dive cycles before its power reserves are depleted. During any single dive cycle, the vessel's launch bay can support at most $M$ active AUVs, meaning no more than $M$ vent sites can be surveyed in the same cycle. Furthermore, the acoustic calibration dependencies dictate that if site $a$ is required to calibrate the sensors for site $b$, the survey of site $a$ must occur in a dive cycle strictly prior to the dive cycle for site $b$. 

If a valid deployment plan can be generated, it will be uploaded to the vessel for physical execution. Afterwards, Phase III will commence, where the retrieved samples and telemetry are fed into a neural network for chemical classification.

Your task is exclusively to implement the Phase II planner. Given the output from Phase I, you must assign exactly one dive cycle (from 1 to $T$) to each of the $n$ vent sites. Your assignment must respect all calibration dependencies, and the AUV capacity limit $M$ must never be exceeded in any dive cycle. If no such assignment is possible, you must report that the mission cannot be completed.

## Input
The first line contains four integers $n, M, T, m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that the survey of site $a$ must be completed in a dive cycle strictly before the survey of site $b$.

## Output
Print `YES` then $n$ integers (the dive cycle assigned to each site, in order from site 1 to site $n$, each in the range 1 to $T$); otherwise print `NO`.

## Example 1

**Input:**
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output:**
```text
YES
1 1 2 3 3
```

## Example 2

**Input:**
```text
4 2 2 3
1 2
2 3
3 4
```

**Output:**
```text
NO
```
