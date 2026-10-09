# Network Deployment Phase II

Time limit: 2 s   Memory limit: 256 MB

## Description
The deployment of the regional sensor network is executed in a strict three-phase workflow. 

**Phase I: Topology Survey.** Automated surveyors have already mapped the terrain to identify viable line-of-sight communication channels. The facility contains $2q$ nodes. Nodes numbered $1$ through $q$ are designated as uplinks, while nodes $q+1$ through $2q$ operate as downlinks. The survey has generated a list of $t$ viable channels, each connecting one uplink to one downlink. This raw data is passed directly to your module.

**Phase II: Routing Configuration.** This is your task. You must process the survey data to establish the active routing configuration. To ensure load balancing and avoid signal interference, your configuration must filter the raw channels down to a strict subset. In this subset, every single node in the facility (all $2q$ of them) must be activated by exactly one selected channel. If any node is left disconnected, or if any node is assigned to multiple channels, the configuration is invalid.

**Phase III: Frequency Calibration.** Once you provide a valid configuration, the automated calibration sequence will take over, tuning the frequencies across your selected channels and initializing data transfer. 

Your program must determine if Phase II can be successfully completed. If a valid configuration exists, output it so Phase III can begin. Otherwise, report the failure.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a viable channel identified during Phase I between uplink $a$ and downlink $b$.

## Output
If the Phase II configuration can be successfully established, print `YES` on the first line. Then, output $q$ lines, each containing the two nodes of a selected channel. If no valid configuration is possible, print `NO`.

## Example

**Input**
```
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
