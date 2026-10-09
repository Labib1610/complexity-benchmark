# Pipeline Maintenance Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
You manage a high-pressure gas distribution network composed of mixing valves and connecting pipelines. The network design ensures that every mixing valve connects to exactly three pipelines.

You must schedule routine depressurization and inspection for every pipeline in the network. The inspection cycle consists of exactly three non-overlapping operational shifts. Taking a pipeline offline for inspection requires assigning it to one of these three shifts.

If two or more pipelines connected to the same valve are depressurized during the same shift, the resulting pressure imbalance will rupture the valve's internal seals. Consequently, at any single valve, you can never inspect multiple connected pipelines simultaneously. Because every valve connects to exactly three pipelines and there are only three shifts available, each of the three pipelines meeting at a valve must be assigned to a distinct shift.

You must determine whether it is possible to assign every pipeline to one of the three shifts such that no valve has multiple connected pipelines assigned to the same shift. If a valid schedule exists, you must also provide the shift assignment for each pipeline.

## Input
The first line provides two integers **n** and **m** (n is even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of mixing valves and the number of pipelines, respectively. Valves are numbered 1 to n.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a pipeline connecting valve u and valve v.

## Output
If a safe inspection schedule is possible, print `YES` on the first line. On the second line, print **m** integers, each either 1, 2, or 3, representing the shift assigned to each pipeline in the order they were given in the input. If multiple valid schedules exist, you may output any of them.
Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
