# Galactic Manifest

Time limit: 1 s
Memory limit: 256 MB

## Description

An interstellar conglomerate is preparing to exploit $j$ star systems. To do so, they will deploy two specialized vessels: a Surveyor and a Harvester. 

The conglomerate must establish a single master manifest—a strict list ordering all $j$ systems. Both vessels will visit the systems exactly in the order dictated by this manifest.

The mechanics of the exploitation are as follows:
- The Surveyor handles the systems back-to-back in the chosen manifest, charting one system at a time.
- The Harvester also handles the systems in the exact same manifest, extracting resources from one system at a time.
- For any given system, the Harvester can only commence extraction once two conditions are met: the Harvester has finished extraction for the preceding system on the manifest (if it is not the first system), AND the Surveyor has completely finished charting this current system.
- Once either vessel begins its respective task in a system, it works continuously until that task is completed.

For each system, you are provided the number of cycles it takes for the Surveyor to chart it, and the number of cycles it takes for the Harvester to extract its resources.

You must determine the optimal manifest. Your objective is to find the arrangement of systems that minimizes the total cycles elapsed from the moment the Surveyor begins charting the first system until the moment the Harvester completes extraction in the final system, and report this minimum possible total time.

## Input

The first line contains a single integer $j$ ($1 \le j \le 200000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the cycles required to chart the system and the cycles required to extract resources for that system, respectively.

## Output

Print a single integer: the smallest possible time at which all systems can be completely exploited.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, if the given systems (1-indexed) are placed on the manifest in the order 3, then 2, then 1:
- **System 3**: The Surveyor works from cycle 0 to 1. The Harvester works from 1 to 4.
- **System 2**: The Surveyor works from cycle 1 to 3. The Harvester waits until cycle 4, then works from 4 to 8.
- **System 1**: The Surveyor works from cycle 3 to 6. The Harvester waits until cycle 8, then works from 8 to 10.

The final completion time is 10. No other manifest arrangement results in a smaller total time.
