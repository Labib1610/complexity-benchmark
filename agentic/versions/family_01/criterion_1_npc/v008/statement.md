# Problem A — Shift Assignment Module

Time limit: 2 s   Memory limit: 256 MB

A factory's automated scheduling pipeline consists of three stages. First, the human resources department collects reports of interpersonal conflicts among the n workers. Second, the shift assignment module must allocate every worker to exactly one of the three operational shifts (labeled 1, 2, and 3) so that no conflicting pair shares a shift. Finally, the payroll system processes the resulting schedule to calculate shift differentials.

Your task is to implement the second stage: given the conflict reports from the first stage, assign the shifts or report that a valid schedule is impossible.

## Input
The first line contains two integers n and m — the number of workers and the number of conflict pairs (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2).
Each of the next m lines contains two integers u v — a conflicting pair.

## Output
If no valid assignment exists for the payroll system to process, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s₁ s₂ … sₙ (each in {1,2,3}), where sᵢ is the shift of worker i. Any valid assignment is accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
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
NO
```
