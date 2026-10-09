# Problem B — Migration Window Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A software team is planning to execute a set of distinct database migrations. These migrations must be scheduled into a sequence of consecutive maintenance windows. The windows are numbered starting from the smallest positive integer, incrementing by one for each subsequent window, until the highest window number exactly matches the total count of migrations. Each migration must be assigned to exactly one maintenance window, and no window can be left unused.

The migrations are related through a strict architectural hierarchy. There is a single foundational migration, and every other migration relies directly on exactly one other migration in the hierarchy. This means the relationships form a single, unified structure spanning all migrations without any closed loops.

When two migrations share a dependency link, the "wait time" for that link is calculated as the absolute difference between their assigned maintenance window numbers. The team has a maximum cumulative wait time budget that applies to the sum of the wait times across all dependency links. There is no limit on individual wait times, nor any rule about which migration in a link must be executed first, as long as the total sum of wait times across all links is within the budget.

Determine an assignment of migrations to maintenance windows such that the total cumulative wait time is less than or equal to the budget, or state that it is impossible.

## Input
First line: three integers $n$, $m$, and $B$. 
Each of the next $m$ lines: two integers $u$ and $v$ — a dependency link. 
(The hierarchy ensures $m$ is exactly one less than $n$.)

## Output
Print `YES` then a line with $n$ integers — the maintenance window assigned to migration 1, 2, ..., $n$ — such that the total wait time is at most $B$. Otherwise print `NO`.

## Example

**Input:**
4 3 4
1 2
1 3
1 4

**Output:**
YES
2 1 3 4
