# Orientation Curriculum

Time limit: 2 s   Memory limit: 256 MB

## Description
A corporate trainer is finalizing the schedule for a new employee orientation program consisting of $n$ distinct training modules. The modules will be presented one at a time in a continuous sequence until all $n$ are delivered.

Certain modules establish foundational concepts that are assumed by other modules. When module $a$ establishes a foundation for module $b$, the trainer must ensure that $a$ is presented earlier in the sequence than $b$. The only restriction on the schedule is this collection of foundational requirements.

A valid schedule is any complete sequence of all $n$ modules that satisfies every foundational requirement simultaneously. Produce such a sequence, or report that the requirements inherently contradict each other, making it impossible to form a valid schedule.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that module $a$ must be presented earlier in the sequence than module $b$.

## Output
Print `YES` followed by a sequence of $n$ distinct integers from 1 to $n$ representing a valid presentation order; otherwise, print `NO`.

## Example 1

### Input
```
4 4
1 2
1 3
2 4
3 4
```

### Output
```
YES
1 2 3 4
```

## Example 2

### Input
```
3 3
1 2
2 3
3 1
```

### Output
```
NO
```
