# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s
Memory limit: 256 MB

## Description
You are organizing a regional emergency readiness drill. The active roster contains $3q$ personnel, assigned IDs from $1$ to $3q$. 

Personnel are deployed by approving dispatch logs. You are provided with a registry of $t$ potential dispatch logs. Each log specifies a team of personnel who are certified to operate together. Because a standard response team requires a commander, a specialist, and a medic, each log contains exactly three distinct personnel IDs.

For the drill to be compliant, you must approve a collection of these logs following strict deployment mechanics:
- **Activation:** When a log is approved, the three personnel listed on it are immediately deployed into the field.
- **Exclusive assignment:** Once deployed, a person becomes unavailable for any other team. An approved log cannot include any personnel who are already deployed by a previously approved log.
- **Full mobilization:** The drill must successfully deploy all $3q$ personnel from the active roster.

Determine if there is a combination of logs you can approve to meet these requirements. If successful, provide the approved logs.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ is the total number of personnel and $t$ is the number of potential dispatch logs.
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of the personnel in one log.

## Output
If a compliant deployment can be formed, print `YES`, followed by $q$ lines each containing the three personnel IDs of an approved log.
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
