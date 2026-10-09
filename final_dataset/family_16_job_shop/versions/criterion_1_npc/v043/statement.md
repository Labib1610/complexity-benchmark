# Problem A — Bureaucratic Bottleneck

Time limit: 5 s   Memory limit: 256 MB

## Description

A government agency employs **m** distinct clerks and must fully process **j** dossiers. 

Each dossier comes with a strictly ordered routing slip that mandates a sequence of processing steps. Each step dictates exactly which clerk must handle the dossier, and how many minutes they will take to complete their work.

The bureaucratic protocols are inflexible:
- A dossier must strictly follow the order of steps on its routing slip. It cannot advance to the next step until the current step is entirely completed.
- A clerk can possess and work on at most one dossier at any given time.
- Once a clerk begins a step for a dossier, they must work on it continuously until that step's required minutes have completely elapsed. 

There is no time lost when transferring dossiers. A dossier can begin its next step at the exact moment its previous step finishes, and a clerk can begin working on a new dossier at the exact moment they finish another.

You must coordinate the passing of dossiers among the clerks to end the workday as early as possible. What is the minimum total time required to completely process all dossiers?

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of dossiers and the number of clerks, respectively. Clerks are numbered from 1 to **m**.

Each of the next **j** lines describes the routing slip for one dossier. The line begins with an integer **o**, representing the number of steps for that dossier. This is followed by **o** pairs of integers `clerk duration` (1 ≤ clerk ≤ m, 1 ≤ duration ≤ 1000), listing the steps in the exact order they must be performed. 

The total number of steps across all dossiers is at most 50.

## Output

Print a single integer: the minimum total time required to completely process all dossiers.

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

In Example 1, two identical dossiers each pass through clerks 1, 2, and 3 (2 minutes each). The second dossier trails the first through the sequence and finishes at time 8. In Example 3, the two dossiers use different clerks and are handled simultaneously, finishing at time 4.
