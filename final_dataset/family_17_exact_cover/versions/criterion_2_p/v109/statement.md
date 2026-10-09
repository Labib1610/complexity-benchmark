# Problem B — Autonomous Fleet Docking

Time limit: 2 s   Memory limit: 256 MB

## Description
An automated warehouse operates a fleet of aerial delivery drones and an equal number of charging bays. The system components are tracked by ID numbers from $1$ to $2q$. The drones are assigned IDs from $1$ to $q$, and the charging bays are assigned IDs from $q+1$ to $2q$.

Due to varying battery models and firmware versions, a drone cannot simply dock at any bay. The engineering team has provided a verified compatibility list. Each entry in this list specifies one drone and one charging bay that are capable of establishing a connection.

At the end of the shift, the facility must execute a complete maintenance cycle. For this to happen, every single drone must be securely docked in a compatible charging bay. The docking process imposes strict physical rules: a drone can only dock at one bay, and a bay can only accommodate one drone. Furthermore, no component can be left idle; every drone must be docked, and every charging bay must be occupied.

Your task is to determine whether it is possible to dock the entire fleet according to these requirements. If a valid configuration exists, you must provide the specific assignments. Otherwise, you must report that a complete docking is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The value $q$ specifies the number of drones (which is also the number of charging bays), while $t$ indicates the total number of verified compatible connections.

The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that drone $a$ is compatible with charging bay $b$.

## Output
If all drones can be simultaneously docked in compatible bays, output `YES` on the first line. Then, output $q$ lines, each containing the ID of a drone and the ID of its assigned charging bay. If no such configuration is possible, output `NO`.

## Example 1

### Input
```text
3 4
1 4
2 4
2 5
3 6
```

### Output
```text
YES
1 4
2 5
3 6
```

## Example 2

### Input
```text
2 2
1 3
2 3
```

### Output
```text
NO
```
