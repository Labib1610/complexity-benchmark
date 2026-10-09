# Problem B — Directorate Deployment Schedule

Time limit: 2 s   Memory limit: 256 MB

## Description
During a remote operations drill, a series of hardware-compatibility tests generates a certification log. This log contains $t$ entries, where each entry specifies a successful interface between a particular human controller and a particular remote platform. The personnel acting as controllers are assigned integer identifiers ranging from $1$ to $q$. The remote platforms are assigned identifiers ranging from $q+1$ to $2q$.

Operational safety protocols dictate that an active operational link must consist of exactly one controller and exactly one platform, and this specific pair must be explicitly recorded in the certification log. Furthermore, concurrent links must be strictly isolated: a controller cannot be involved in more than one active link at a time, and a platform cannot receive inputs from more than one controller simultaneously.

The directorate wishes to evaluate the overall readiness of the system. To do this, they require a deployment schedule that achieves full utilization of all available assets. Your task is to determine whether it is possible to establish a set of concurrent links such that every single one of the $q$ controllers and every single one of the $q$ platforms is actively engaged in exactly one link.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ represents the total number of controllers (equal to the number of platforms) and $t$ represents the number of successful interface entries in the certification log.
Each of the subsequent $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting that controller $a$ and platform $b$ successfully interfaced.

## Output
If a state of full utilization can be achieved, output `YES` on the first line. On the following $q$ lines, output the integer identifiers of the controller and its linked platform for each active link. If there are multiple valid configurations, any of them is acceptable.
If full utilization is impossible under the safety protocols, output `NO`.

## Example

### Input
```text
2 3
1 3
1 4
2 3
```

### Output
```text
YES
1 4
2 3
```
