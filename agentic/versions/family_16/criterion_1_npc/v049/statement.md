# Problem A — Facility Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A production environment is equipped with **m** processing stations. It has been tasked with fulfilling **j** assembly commissions.

Every assembly commission consists of a predetermined series of procedural steps. Each step is defined by two parameters: the exact processing station it requires, and the precise number of minutes it takes to complete.

The execution of these commissions is governed by three unyielding rules:
- **Step Precedence:** Within any single commission, a step can only be initiated after the step immediately preceding it in the series has been fully completed.
- **Station Isolation:** No processing station may execute more than one step simultaneously.
- **Continuous Commitment:** Once a step begins on a station, it cannot be halted, swapped, or paused. It must occupy the station continuously for its full duration.

Your responsibility is to orchestrate the timing of these steps. You must find the absolute earliest minute by which every step of every assembly commission can be successfully completed.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of assembly commissions and processing stations, respectively.
Each of the subsequent **j** lines details a single commission. The line begins with an integer **o** (the number of procedural steps in the commission), followed by **o** pairs of integers. Each pair consists of `station duration` (1 ≤ station ≤ m, 1 ≤ duration ≤ 1000), indicating the required processing station and the minutes needed for that step. The procedural steps are listed in the exact sequence they must be executed.
The total number of procedural steps across all assembly commissions combined will not exceed 50.

## Output

Print a single integer: the minimum possible minutes to completely finish all commissions.

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

In Example 1, two identical assembly commissions each pass through processing stations 1, 2, and 3 (taking 2 minutes each). The second commission trails the first through the sequence and finishes at minute 8. In Example 3, the two commissions require different processing stations and run simultaneously, finishing at minute 4.
