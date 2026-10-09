# Centrifuge Balancing

Time limit: 5 s   Memory limit: 256 MB

## Description
A geology research facility is analyzing a batch of $3q$ soil samples, sequentially labeled $1$ through $3q$. 

The analysis is performed using a high-speed centrifuge. To maintain rotational stability, the centrifuge must always be loaded with exactly three samples whose combined mass distribution is perfectly balanced. Through preliminary testing, the facility has identified $t$ specific groups of three samples that achieve this required balance. These safe groups are recorded in a safety registry.

The facility must process the entire batch of $3q$ samples under the following operational constraints:
- The processing is destructive. Once a sample is placed in the centrifuge and analyzed, it is completely consumed and cannot be involved in any subsequent run.
- Every single sample from the batch must be analyzed.
- Every run of the centrifuge must exactly match one of the groups listed in the safety registry.

Determine if there is a valid selection of runs that successfully consumes all $3q$ samples. If such a selection is possible, you must also provide the groups of samples to be loaded in each run.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a group of three samples that is recorded in the safety registry.

## Output
If a valid selection exists, print `YES` on the first line, followed by $q$ lines, each containing the three samples of a selected run. If no such selection is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
