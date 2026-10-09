# Problem A — Meeting the Maintenance Window Across Parallel Servers

Time limit: 5 s   Memory limit: 256 MB

## Description
A data center must process a daily batch of reporting jobs within a strict maintenance window. All jobs take the same amount of time — one minute each — and are carried out on a cluster of identical parallel servers. In any single minute, each server handles at most one job, so the number of jobs that can be in progress during any one minute is capped by the number of servers; there is no benefit to leaving a server idle, but there is also no penalty beyond the window.

The jobs are not independent. Some jobs produce data consumed by others, giving rise to precedence requirements: whenever one job must finish before another can begin, the dependent job has to be placed in a strictly later minute than the job it depends on — being in the same minute is not enough, since data generated in a minute is only available from the next minute onward. Setup times, job priorities, and which specific server runs a job are irrelevant; a job may run on any server, and only the minute it occupies matters.

The maintenance window is expressed as a maximum number of minutes. Assign every job a minute within the window so that all precedence requirements hold and no minute is assigned more jobs than there are servers, or report that the batch cannot be finished by the end of the window. (With few servers the per-minute cap and the precedence chains pull against each other, so a schedule that respects precedence may still overflow the server capacity and vice versa.)

## Input
First line: four integers $n, M, T, m$. Each of the next $m$ lines: two integers $a$ $b$ — job $a$ must finish before job $b$ starts.

## Output
Print `YES` then $n$ integers minute[1..n] (the minute of each job, in 1..T); otherwise `NO`.

## Example

**Input:**
```text
4 2 3 3
1 2
1 3
2 4
```

**Output:**
```text
YES
1 2 2 3
```
