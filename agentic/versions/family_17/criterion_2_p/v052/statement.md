# Telemetry Channel Calibration

Time limit: 2 s
Memory limit: 256 MB

## Description
A telemetry array is built from $2q$ interconnected transceiver modules, assigned unique sequential IDs from $1$ to $2q$. The upcoming calibration procedure requires activating distinct, non-overlapping two-way links between modules. For the procedure to be valid, every module in the array must be an endpoint of exactly one active link.

Due to the array's internal wiring architecture, a link can only successfully transmit data if it connects a module from the first half of the ID space (values up to $q$) with a module from the second half (values strictly greater than $q$). Furthermore, not all such pairs are stable. The engineering team has conducted tests and compiled a complete registry of specific module pairs capable of maintaining a stable link.

Given the registry of stable pairs, determine if it is possible to activate a set of links that covers every module exactly once, and if so, output the required configuration.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The total number of modules is $2q$, and $t$ represents the number of stable pairs in the registry.

Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that module $a$ and module $b$ can maintain a stable link.

## Output
If a valid calibration procedure is possible, output `YES` on the first line. Following this, output $q$ lines to describe the active links. Each line must contain two integers: the ID of the module from the first half of the ID space, followed by the ID of the module from the second half. If no valid configuration exists, output `NO`.

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
