# Datacenter Upgrade

Time limit: 2 s
Memory limit: 256 MB

## Description
A datacenter is phasing out its old hardware. The facility contains $2q$ servers. Servers $1$ through $q$ operate on a deprecated instruction set, while servers $q+1$ through $2q$ run the current standard.

Engineers have identified $t$ viable synchronization channels. Each channel can synchronize the state of one deprecated server with one current server.

The facility's power constraints dictate a strict synchronization policy: you must select a subset of these channels to turn on such that every single server in the facility is involved in exactly one turned-on channel. No server may be left out, and no server may participate in more than one channel.

Determine whether such a configuration exists. If it does, provide the pairs of servers that should be synchronized. Otherwise, indicate that the policy cannot be satisfied.

## Input
The first line provides $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), the number of deprecated servers (which is also the number of current servers) and the total number of viable channels.
The following $t$ lines each provide two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a viable synchronization channel between deprecated server $a$ and current server $b$.

## Output
If the strict synchronization policy can be met, output `YES` on the first line. Following this, output $q$ lines, each containing the two server IDs of a turned-on channel from your selection.
If it is impossible to meet the policy, output `NO`.

## Example 1

### Input
```
3 4
1 4
2 4
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

## Example 2

### Input
```
2 2
1 3
2 3
```

### Output
```
NO
```
