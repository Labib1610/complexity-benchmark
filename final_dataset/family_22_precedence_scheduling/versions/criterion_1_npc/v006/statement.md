# Problem A — Meeting the Deadline Across a Compute Cluster

Time limit: 5 s   Memory limit: 256 MB

## Description
A data engineering team must complete a batch of nightly extraction jobs before a hard reporting deadline. All jobs take the same amount of time — one hour each — and are carried out on a cluster of identical compute nodes. In any single hour, each node handles at most one job, so the number of jobs that can be running during any one hour is capped by the number of nodes; there is no benefit to leaving a node idle, but there is also no penalty beyond the deadline.

The jobs are not independent. Some jobs produce intermediate tables queried by others, giving rise to dependency requirements: whenever one job must finish before another can begin, the dependent job has to be placed in a strictly later hour than the job it depends on — being in the same hour is not enough, since a table finished in an hour is only queryable from the next hour onward. Setup times, job priorities, and which specific node runs a job are irrelevant; a job may run on any node, and only the hour it occupies matters.

The deadline is expressed as a maximum number of hours. Assign every job an hour within the deadline so that all dependency requirements hold and no hour is assigned more jobs than there are nodes, or report that the batch cannot be finished by the deadline. (With few nodes the per-hour cap and the dependency chains pull against each other, so a schedule that respects dependencies may still overflow the hourly capacity and vice versa.)

## Input
First line: four integers n, M, T, m. 
Each of the next m lines: two integers a b — job a must finish before job b starts.

## Output
Print `YES` then n integers hour[1..n] (the hour of each job, in 1..T); otherwise `NO`.

## Example

**Input:**
```
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output:**
```
YES
1 1 2 3 3
```
