# Problem A — Regional Readiness Drill Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate maintains an archive of historically certified response configurations. Each record in this archive strictly dictates the joint participation of three specific individuals, identified by their badge numbers. Command may only utilize setups from this established archive; no new configurations can be created on the fly.

The active roster for an upcoming drill is sized based on a scale factor $q$. There are $3q$ personnel on duty, assigned consecutive badge numbers from $1$ to $3q$. To manage assignments, every person on the roster is initially issued one digital deployment token.

Activating a configuration from the archive requires simultaneously consuming the individual tokens of its three assigned members. Consequently, a configuration can only be initialized if all three of its required members currently hold their unconsumed tokens.

The drill is considered fully staffed if and only if the roster's entire token pool is completely exhausted. Your task is to determine if command can identify a selection of the certified records to activate such that every individual is deployed exactly once. If such a selection exists, output the chosen records. Otherwise, indicate that it is impossible.

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
