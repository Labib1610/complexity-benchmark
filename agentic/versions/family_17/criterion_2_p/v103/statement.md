# Problem B — Array Calibration Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A satellite communication array consists of $2q$ transceivers, numbered sequentially from $1$ to $2q$. The array is structurally partitioned: transceivers $1$ through $q$ are designated as signal emitters, while transceivers $q+1$ through $2q$ are designated as signal receptors. 

A functional deployment requires at least one emitter. Because of the address register's physical architecture, the absolute maximum capacity for emitters is exactly one hundred thousand. 

The engineering team provides a log of $t$ stable transmission pathways. The log file can be completely empty, but its maximum size is strictly limited to four times the array's absolute maximum capacity for emitters. 

Each logged pathway connects exactly one emitter to exactly one receptor. 

Your objective is to activate a specific subset of these pathways to fully calibrate the array. A successful calibration means every single transceiver in the array—all $2q$ of them—is assigned to exactly one active pathway. No transceiver can be left dormant, and none can be assigned to multiple active pathways. Redundant pathways in the log can be ignored; you only need to establish one valid calibration configuration.

Determine if a full array calibration is possible. If it is, output the pathways to activate. Otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$, representing the number of emitters and the total number of logged pathways, respectively. The valid ranges for $q$ and $t$ are derived directly from the physical capacities and limits described previously.

Each of the subsequent $t$ lines contains two integers $a$ and $b$, representing a logged pathway between emitter $a$ and receptor $b$. The valid ranges for $a$ and $b$ follow strictly from their transceiver designations.

## Output
If a full calibration is possible, print `YES` on the first line, followed by $q$ lines each containing the two transceiver IDs of an activated pathway. If no such configuration exists, print `NO`.

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
