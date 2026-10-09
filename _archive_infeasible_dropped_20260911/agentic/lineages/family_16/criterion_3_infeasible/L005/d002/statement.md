# Problem C — Schedule Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant must route **j** jobs through two sequential processing stations. Every job must be fully processed at station 1 before it can be transferred to station 2. The required processing duration for each job at station 1 and station 2 is provided. A station can process only a single job at any given moment.

The plant operates under a strict completion deadline **T**. For a production run to be successful, all jobs must clear station 2 by time **T**.

For every given configuration, no valid schedule exists that can meet the deadline. You must provide a structural certificate proving this impossibility. Exactly one of the following two proof categories will apply to the configuration, and you must output the certificate for the uniquely applicable category:

- **Routing Delay:** A localized bottleneck exists within a single item. Output `JOB i`, where **i** (1-based index) is a job that, even if it were granted exclusive use of the plant and experienced zero wait time, would still complete after time **T**. If multiple jobs qualify, you may output any one of them.

- **Throughput Saturation:** A capacity deficit exists at a specific facility. Output `LOAD c`, where **c** is the station number (1 or 2) that, even if it never sat idle and processed all its assigned tasks back-to-back starting from time 0, would still be operating after time **T**. If both stations qualify, you may output either one.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing duration of a job at station 1 and station 2, respectively.

## Output

Print a single line containing the exact certificate for the uniquely applicable category: either `JOB i` for a routing delay or `LOAD c` for throughput saturation.

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

In Example 1, job 1 takes 70 time units at station 1 and then needs 60 at station 2. Even without any interference from other jobs, it finishes at time 130, missing the deadline of 100. Thus, a routing delay certificate `JOB 1` is printed. 
In Example 2, no single job is inherently too long for the 150 deadline. However, station 1 has to complete four tasks of 50 time units each. Even if it operates non-stop, it will be working until time 200. This misses the deadline, so a throughput saturation certificate `LOAD 1` is printed.