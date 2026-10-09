# Complete Neutralization

Time limit: 2 s   Memory limit: 256 MB

## Description
A hazardous waste processing facility needs to neutralize a batch of volatile materials. The batch contains exactly $2q$ discrete material samples. The first $q$ samples are acidic isotopes (labelled $1$ through $q$), and the remaining $q$ samples are alkaline reagents (labelled $q+1$ through $2q$). 

You are provided with a database of $t$ safe fusion procedures. Each procedure explicitly combines one specific acidic isotope with one specific alkaline reagent to produce an inert byproduct. 

Your goal is to design a complete neutralization schedule by selecting a subset of these $t$ procedures. Since there are $t$ available procedures, there are $2^t$ possible schedules (subsets) to consider. A schedule is only successful if it meets the following strict constraints:
- **Total Consumption**: Every single material sample (all acidic isotopes and all alkaline reagents) must be processed by the chosen schedule.
- **Single Use**: Each material sample is entirely consumed when a procedure is executed. Therefore, no sample may appear in more than one selected procedure.

Determine whether a valid schedule exists within the $2^t$ search space. If it does, extract and output the chosen procedures; otherwise, report that no schedule can be formed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a safe fusion procedure between acidic isotope $a$ and alkaline reagent $b$.

## Output
If a valid schedule is possible, print `YES` followed by $q$ lines, each containing the two labels of a selected procedure. If no valid schedule exists, print `NO`.

## Example

### Input
```
3 4
1 4
2 5
3 6
1 5
```

### Output
```
YES
1 4
2 5
3 6
```
