# Stable Channel Configuration

Time limit: 2 s
Memory limit: 256 MB

## Description
A distributed cluster consists of $2q$ processing modules. These modules are strictly partitioned into two tiers of equal size: $q$ frontend modules (indexed $1$ through $q$) and $q$ backend modules (indexed $q+1$ through $2q$).

The architecture permits certain direct data channels to be established. You are provided with a catalogue of $t$ potential channels. Due to security policies, any potential channel always bridges exactly one frontend module and exactly one backend module.

A deployment configuration is formed by activating a specific subset of these potential channels. For a configuration to be stable, it must satisfy a strict load-balancing requirement: every single module in the cluster (both frontend and backend) must be an endpoint for exactly one active channel. If any module has zero active channels, it becomes isolated; if it has more than one, data collision occurs.

Your task is to analyze the catalogue and determine whether it is possible to activate a configuration that is stable for all $2q$ modules. If such a configuration can be formed, you must identify which channels to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of frontend modules (which is also the number of backend modules) and the number of potential data channels, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that a potential channel can be established between frontend module $a$ and backend module $b$.

## Output
If a stable configuration is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two modules of an activated channel in the configuration. If multiple stable configurations exist, you may output any of them. If no such configuration is possible, print `NO`.

## Example

### Input
```text
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```text
YES
1 4
2 6
3 5
```
