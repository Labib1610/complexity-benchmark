# Problem B — Tiered Channel Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
A synchronization protocol requires configuring connections within a system of $2q$ data modules. The system is partitioned into a primary tier consisting of modules with IDs from $1$ to $q$, and a secondary tier consisting of modules with IDs from $q+1$ to $2q$.

During the initial scan, $t$ potential channels were identified. Each potential channel bridges one module from the primary tier to one module from the secondary tier.

Your objective is to finalize a specific selection of these channels. To ensure absolute system stability, every module in the entire system—across both tiers—must be utilized by precisely one finalized channel. If a module is ignored, data is lost; if a module is utilized by multiple finalized channels, a collision occurs.

Determine if a valid selection of channels exists. If it does, output the channels to be finalized; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $2q$ is the total number of modules and $t$ is the number of potential channels.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a potential channel between module $a$ and module $b$.

## Output
If there is a valid selection that meets the stability requirement, print `YES` on the first line, followed by $q$ lines. Each of these lines must contain the two module IDs of a finalized channel. If no such selection is possible, print `NO`.

## Example

**Input**
```text
3 4
1 4
1 5
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
