# Pipeline Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility operates **m** shared resources and must process **j** independent linear pipelines. Each pipeline is a strictly ordered sequence of tasks. Each task requires exclusive use of a specific resource for a predetermined duration.

The execution rules are as follows:
- A pipeline processes its tasks strictly in the order they are provided. A task may only begin after the immediately preceding task in the same pipeline has completely finished.
- A resource can only be utilized by one task at a time.
- Once a task begins, it holds its resource continuously for its full duration (no interruptions).

Because each of the **j** pipelines is strictly linear and must be executed in its exact given order, the structural progress of the system is characterized simply by how many tasks have been completed in each pipeline. With at most 50 tasks across all pipelines, the number of such progress states is highly restricted. 

Your objective is to find the most efficient valid sequence of task initiations that transitions the system from zero completed tasks to all tasks completed. Schedule the tasks to minimize the time at which the final task in the system finishes.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of pipelines and the number of shared resources.

Each of the next **j** lines describes a single pipeline. Each line begins with an integer **o**, the number of tasks in that pipeline. This is followed by **o** pairs of integers. Each pair provides the `resource_id` (1 ≤ resource_id ≤ m) and the `duration` (1 ≤ duration ≤ 1000) for a task, listed in the exact order they must be executed.

The total number of tasks across all pipelines is at most 50.

## Output

Print a single integer: the earliest possible time at which all pipelines are completely finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical pipelines each pass through resources 1, 2, and 3 (taking 2 time units each). The second pipeline trails the first through the resources and finishes at time 8. In Example 3, the two pipelines use different resources and run in parallel, both finishing by time 4.
