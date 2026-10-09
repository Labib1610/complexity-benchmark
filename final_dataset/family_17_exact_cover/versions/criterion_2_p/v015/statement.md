# Telemetry Link Synchronization

Time limit: 2 s
Memory limit: 256 MB

## Description
The agency must execute a synchronized telemetry test requiring exactly one dedicated communication link for every deployed asset. The assets consist of ground controllers, assigned sequential IDs starting from 1, and orbital platforms, assigned sequential IDs immediately following the controllers. The total number of controllers is equal to the total number of platforms.

A link can only be established if the specific controller-platform hardware combination has passed prior compatibility certification. The certification database provides all compatible combinations. To ensure full system saturation during the test, every controller and every platform must be actively linked. Furthermore, to prevent signal interference, no controller may link to more than one platform, and no platform may link to more than one controller.

Determine if it is possible to configure the links such that all conditions are met, and if so, provide the configuration.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ is the number of controllers (and also the number of platforms) and $t$ is the number of certified combinations.

Each of the next $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ are certified to link.

## Output
If a configuration meeting all requirements is possible, output `YES` on the first line, followed by $q$ lines each containing the ID of a controller and the ID of its linked platform. If no such configuration exists, output `NO`.

## Example

**Input**
```text
3 4
1 4
2 4
2 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
