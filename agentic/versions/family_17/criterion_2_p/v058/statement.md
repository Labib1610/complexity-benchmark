# Network Integration Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A distributed computing environment consists of $2q$ discrete modules, split evenly into two tiers. Tier A contains $q$ modules indexed $1$ through $q$, while Tier B contains $q$ modules indexed $q+1$ through $2q$.

Between these tiers, a set of $t$ potential communication channels has been physically wired. Each wired channel bridges exactly one module from Tier A and exactly one module from Tier B. 

When a channel is activated, it permanently binds the two modules it connects. A module can only participate in a single active channel; attempting to bind a module to multiple active channels simultaneously will trigger a hardware fault. Conversely, any module that remains unbound by an active channel will be entirely isolated from the network.

Your task is to determine whether there is a combination of active channels that successfully integrates the entire environment. Specifically, you must find a subset of the $t$ channels such that no hardware faults occur and no module is left isolated. If such a configuration exists, you must provide the exact list of channels to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100,000$, $0 \le t \le 400,000$), representing the number of modules in each tier and the number of available communication channels, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that a potential channel exists between Tier A module $a$ and Tier B module $b$.

## Output
If a valid configuration is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two modules of a chosen channel to activate. If multiple valid configurations exist, you may output any of them. If no such configuration is possible, print `NO`.

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
