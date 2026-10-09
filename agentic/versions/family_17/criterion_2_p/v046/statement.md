# Problem B — Directorate Deployment Schedule

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate is generating the deployment schedule for a remote operations drill. 
The drill requires pairing a set of $q$ human controllers with an equal-sized set of $q$ remote platforms. 
Controllers are identified by integers from $1$ to $q$, and platforms are identified by integers from $q+1$ to $2q$. 
The deployment must achieve full utilization, meaning every controller is assigned to exactly one platform and every platform is assigned to exactly one controller. 

You are provided with a certification log containing $t$ entries, where each entry lists a specific controller and a specific platform that are hardware-compatible. 
A deployment pair is only permitted if it appears in this certification log. 
Determine whether it is possible to form a complete deployment schedule for all $2q$ assets under these rules.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (which is also the number of platforms) and the number of certified combinations.
Each of the next $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ is compatible with platform $b$.

## Output
If a complete deployment schedule is possible, print `YES` on the first line, followed by $q$ lines each containing the ID of a controller and the ID of their assigned platform. If multiple valid schedules exist, you may output any of them.
If no such schedule can be formed, print `NO`.

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
