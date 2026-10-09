# Problem B — Automated Pipeline Load Validation

Time limit: 2 s   Memory limit: 256 MB

## Description
The continuous integration pipeline for a distributed system involves three automated phases to ensure stability under heavy traffic. 

**Phase 1: Topology Extraction.** A static analysis tool scans the source code to identify $n$ service modules and $m$ unidirectional communication channels. It also identifies the number of distinct payload types involved in the test (which is always 1 for this test suite). This data is passed to the next phase.

**Phase 2: Stress Test Resolution (Your Task).** You must process the extracted topology to determine if a specific test load of $d$ discrete requests can be successfully transmitted from a designated generator module $s$ to a sink module $t$ in a single test tick. Each communication channel from module $u$ to module $v$ has a strict concurrency limit of $cap$ requests. The number of requests assigned to each channel must be a non-negative integer. At the generator module $s$, the net departure (requests sent minus requests received) must equal exactly $d$. At the sink module $t$, the net arrival (requests received minus requests sent) must equal exactly $d$. All other modules are stateless relays: their net departure and net arrival must be exactly zero (they must output exactly as many requests as they receive).

**Phase 3: Execution Plan Generation.** If the test load is sustainable, the test harness requires the exact number of requests allocated to each channel to configure the system's load balancer. If it is impossible to route the entire load $d$ through the network without exceeding channel limits, the test is aborted.

You must implement Phase 2 and produce the exact output required by Phase 3.

## Input
Line 1: Three integers $n$, $m$, and $1$.
Line 2: Three integers $s$, $t$, and $d$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, indicating a unidirectional channel from module $u$ to module $v$ with a concurrency limit of $cap$.

## Output
If the entire load $d$ can be routed, output `YES` on the first line. On the second line, output $m$ integers representing the number of requests assigned to each channel, in the exact order the channels were provided in the input. 
If the load cannot be routed, output `NO` on a single line.

## Example

### Input
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```
YES
5 5 0 5 5
```
