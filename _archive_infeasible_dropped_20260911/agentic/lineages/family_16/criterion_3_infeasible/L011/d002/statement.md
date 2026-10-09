# Problem C — Unattainable Target: Provide Evidence

Time limit: 2 s   Memory limit: 256 MB

## Description

A ground station needs to route $j$ data transmissions through a relay satellite. Every transmission is sent on the uplink frequency first, and then broadcast on the downlink frequency. For each transmission, you are given its duration on the uplink and its duration on the downlink. Each frequency can carry only one transmission at a time, and a transmission can only start its downlink after its uplink has entirely finished.

There is a hard time limit $T$: every transmission must be completely finished by millisecond $T$.

You do not need to find an order; for every input in this problem, no sequence of transmissions can possibly finish by the limit $T$. Your task is to output a certificate that proves the limit is unattainable. Every input is guaranteed to satisfy exactly one of the following properties. Print the certificate for the one that holds:

- A fundamental delay in a single transmission: At least one transmission cannot meet the deadline even if it were granted exclusive access to the relay satellite without any other transmissions competing for either frequency. Print: `JOB i` — where $i$ (1-based) is such a transmission.

- A fundamental capacity shortfall on a single frequency: At least one frequency cannot process all the work assigned to it by the deadline, even under an idealised relaxation where transmissions are not delayed by the operations of the other frequency. Print: `LOAD c` — where $c$ is 1 (for the uplink) or 2 (for the downlink) and is such a frequency.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the durations of a transmission on the uplink and the downlink.

## Output

Print a single line: `JOB i` (where $i$ is a transmission that cannot meet the limit in isolation) or `LOAD c` (where $c$ is a frequency that cannot process its assigned work by the limit).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, transmission 1 requires 70 milliseconds on the uplink and 60 milliseconds on the downlink. Even without competing transmissions, it requires 130 milliseconds sequentially, which exceeds the 100 millisecond limit. Thus, `JOB 1` is the certificate.

In Example 2, no single transmission violates the limit in isolation. However, the uplink frequency is assigned four transmissions of 50 milliseconds each, totalling 200 milliseconds of work. Even if we ignore the downlink entirely, processing this raw volume on the uplink exceeds the 150 millisecond limit, so `LOAD 1` is the certificate.