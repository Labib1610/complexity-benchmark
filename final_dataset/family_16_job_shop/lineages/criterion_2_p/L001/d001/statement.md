# Consecutive Treatments

Time limit: 1 s   Memory limit: 256 MB

## Description

A dispatcher oversees **j** dossiers that require two consecutive treatments: an initial review followed by a final sign-off. For each dossier, you are given the duration of its initial review and the duration of its final sign-off.

The protocol is governed by the following mechanics:
- The dispatcher arranges all dossiers into a single stack, which dictates the order of processing.
- The initial reviewer takes dossiers from the top of the stack one by one.
- The moment a dossier completes its initial review, it is placed into an inbox for the final sign-off desk.
- The final sign-off desk processes dossiers from this inbox one by one in the order they arrive. If the desk is currently occupied with a previous dossier, the newly arrived dossier waits in the inbox.

Arrange the stack to minimize the time at which the last dossier completes its final sign-off. Output that smallest possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a dossier's initial review and final sign-off.

## Output

Print a single integer: the smallest possible time at which all dossiers have completed their final sign-off.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single dossier takes 5 for the initial review and then 3 for the final sign-off, completing at time 8.