# Problem A — Regional Readiness Drill Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. The active roster is sized based on a scale factor $q$, meaning there are $3q$ personnel on duty, assigned consecutive badge numbers from 1 to $3q$.

To execute the drill, command must activate a series of response configurations. To manage assignments, every person on the roster is initially issued one digital deployment token. Activating a configuration requires simultaneously consuming the individual tokens of its three assigned members. A configuration can only be initialized if all three of its required members currently hold their unconsumed token.

Configurations cannot be created on the fly. Command may only activate setups from an archive of historically certified records. Each certified record strictly dictates the participation of three specific badge numbers. 

The drill is considered fully staffed if and only if command can designate a selection of the certified records to activate such that the roster's entire token pool is completely exhausted. This operational rule guarantees that every individual is deployed and no individual is assigned to conflicting duties.

Your task is to determine if command can fully staff the drill using the provided archive. If achievable, output the chosen records. Otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the badge numbers in a certified record.

## Output
If a valid selection exists, print `YES`, followed by $q$ lines, each containing the three badge numbers of one activated record.
Otherwise, print `NO`.

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
