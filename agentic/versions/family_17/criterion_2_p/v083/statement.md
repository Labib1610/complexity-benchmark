# Telemetry Link Synchronization

Time limit: 2 s
Memory limit: 256 MB

## Description
The agency is preparing a full-scale telemetry diagnostic involving $2q$ communication assets, numbered $1$ through $2q$. The assets are divided into two operational tiers: terrestrial arrays (IDs $1$ through $q$) and orbital relays (IDs $q+1$ through $2q$).

To conduct the diagnostic, the system must be partitioned into exactly $q$ independent, two-way data channels. Each channel operates by bridging exactly one terrestrial array and exactly one orbital relay. 

Channels cannot be formed arbitrarily. Because of hardware variances, a channel can only be established if the two specific assets have been successfully calibrated together in advance. You are provided with the registry of all calibrated pairs.

For the diagnostic to be valid, every single asset—both terrestrial and orbital—must be actively engaged in exactly one channel. No asset can be left idle, and no asset can participate in more than one channel simultaneously.

Determine if there is a valid configuration of channels that engages every asset exactly once. If such a configuration exists, you must also provide it.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ is the number of terrestrial arrays (which is also the number of orbital relays) and $t$ is the number of calibrated pairs.

Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting that terrestrial array $a$ and orbital relay $b$ are calibrated to form a channel.

## Output
If a valid configuration is possible, print `YES` on the first line. Then, output $q$ lines, each containing the identifier of a terrestrial array and the identifier of the orbital relay it is bridged with in that configuration. If no such configuration is possible, print `NO`.

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
