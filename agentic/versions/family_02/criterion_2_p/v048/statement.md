# Problem B — Phase B: Configuration Resolution

Time limit: 1 s   Memory limit: 256 MB

## Description

You are building the configuration module for a factory's automated diagnostic pipeline. The pipeline operates in three sequential stages. In Stage A, automated sensors scan the facility to compile a list of structural requirements based on current conditions. Your module handles Stage B: analyzing these requirements to find a globally viable hardware state. If your module successfully finds a valid state, Stage C takes over to physically adjust the equipment.

During Stage B, your module processes data for $n$ distinct hardware pieces. Each hardware piece must be assigned a final status of either 'active' (represented by 1) or 'standby' (represented by 0). The Stage A scan provides a list of $m$ critical requirements. Each requirement contains exactly two potential hardware statuses. For the entire system to be viable, the final assigned state of the hardware must match at least one of the two statuses listed in every single requirement.

Your task is to execute Stage B. Determine if there is a way to assign a status to all $n$ hardware pieces such that every requirement is fulfilled simultaneously. If a valid assignment exists, output it so Stage C can commence. If it is impossible to satisfy all requirements, you must reject the setup.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of hardware pieces and the number of Stage A requirements, respectively.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two potential statuses for a requirement. A positive integer $x$ indicates a desired status where hardware piece $x$ is 'active' (1). A negative integer $x$ indicates a desired status where hardware piece $|x|$ is 'standby' (0).

## Output
If Stage C cannot proceed because no assignment satisfies all requirements, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each being 0 or 1), representing the chosen status for each hardware piece from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid status assignments may exist; any one is accepted. The same hardware piece may appear in multiple requirements.
