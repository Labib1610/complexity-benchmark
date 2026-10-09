# Telemetry Channel Calibration

Time limit: 2 s
Memory limit: 256 MB

## Description
A telemetry array consists of $2q$ transceiver units, numbered sequentially from $1$ to $2q$. A complete calibration requires establishing a set of active, isolated, two-way communication channels such that every single unit in the array is engaged in exactly one active channel.

Due to the array's internal wiring architecture, an active channel is only viable if it bridges a low-band unit (an ID less than or equal to $q$) and a high-band unit (an ID strictly greater than $q$). Furthermore, not all such bridges are stable. The engineering team has compiled a complete registry of specific unit pairs that have been tested and proven capable of maintaining a stable channel.

Given the registry of stable pairs, determine if it is possible to activate a set of channels that engages every unit exactly once, and if so, output the required configuration.

## Input
The first line contains two integers $q$ and $t$. The total number of units is $2q$. The value $q$ defines the size of each band; the hardware requires at least 1 unit per band and supports up to a maximum capacity of 100,000 units per band. The value $t$ denotes the total number of stable pairs in the registry, ranging from an empty log of 0 up to the diagnostic memory limit of 400,000 pairs.

Each of the following $t$ lines contains two integers $a$ and $b$. The first integer represents a low-band unit (an ID starting from 1 up to $q$) and the second represents a high-band unit (an ID strictly greater than $q$ up to the total unit count $2q$). These lines indicate that unit $a$ and unit $b$ can successfully maintain a stable channel.

## Output
If a valid calibration procedure is possible, output `YES` on the first line. Following this, output $q$ lines to describe the active channels. Each line must contain two integers: the ID of the low-band unit, followed by the ID of the high-band unit. If no valid configuration exists, output `NO`.

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
