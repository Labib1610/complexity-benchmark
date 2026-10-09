# Sequential Processing with Prerequisite Mapping

Time limit: 2 s   Memory limit: 256 MB

## Description
A manufacturing cell is assigned a workload of $n$ distinct operations, numbered 1 to $n$. The operations are uniform, each requiring exactly one time unit to complete. The cell is strictly sequential, meaning it can only handle a single operation at any given time until the entire workload is finished.

The operations are linked by $m$ pre-execution mandates. A mandate specifies that a certain operation must be fully processed before another specific operation can be initiated. Consequently, the first operation must occupy an earlier position in the execution sequence than the second operation. 

To ensure the integrity of the data provided, the input is guaranteed to satisfy the following structural condition: if you tally the total number of times any operation acts as a prerequisite, and add the total number of times any operation acts as a dependent across all mandates, the sum will be exactly $2m$. Furthermore, any valid execution sequence must satisfy the capacity rule: the position difference between any two operations in the sequence is strictly less than $n$.

Your objective is to determine a complete, sequential arrangement of all $n$ operations that strictly complies with every given mandate. If the mandates contain contradictory loops (meaning it is impossible to satisfy all conditions simultaneously), you must report that the configuration is invalid. 

## Input
The first line contains two integers $n$ and $m$, representing the number of operations and the number of mandates.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must explicitly finish before operation $b$ can begin.

## Output
If a valid sequential arrangement exists, print `YES` on the first line, followed by a sequence of $n$ integers on the second line representing a compliant execution order. If no such arrangement is possible, print `NO`.

## Example

**Input:**
4 4
1 2
1 3
2 4
3 4

**Output:**
YES
1 2 3 4
