# Operation Transit Roster

Time limit: 2 s   Memory limit: 256 MB

## Description
The logistics division must dispatch a convoy consisting of operators and their assigned transit machines. The operation demands absolute resource utilization: every single operator and every single transit machine must be deployed.

The division maintains identical quantities of operators and machines. Operators are issued sequential identification tags starting from $1$. The transit machines are given identification tags immediately following the operators' tags, continuing consecutively.

You are given a log of safety approvals. Each approval pairs a specific operator with a specific transit machine, indicating that they are legally allowed to operate together. A valid convoy roster consists of a selection of these approvals such that each operator and each machine is included in exactly one selected approval, with no resources left out and no resources shared between approvals.

Determine if such a comprehensive roster can be formed. If it is possible, output the roster; otherwise, declare it impossible.

## Input
The first line contains two integers: the number of operators (which is identical to the number of transit machines) and the number of safety approvals. The deployment scale is bounded by the staging area, which accommodates at least one operator and up to a maximum capacity of one hundred thousand operators. The central database may have zero safety approvals, up to a maximum of four hundred thousand records.

Following this are as many lines as there are safety approvals. Each line provides two integers: the operator's tag and the transit machine's tag. Operator tags start at $1$ and go up to the total number of operators. Transit machine tags take the subsequent values, starting strictly greater than the number of operators and reaching at most twice the number of operators.

## Output
If a comprehensive roster can be formed, print `YES` on the first line. Following this, print exactly as many lines as there are operators, each containing the operator's tag and the transit machine's tag of a selected approval from your roster. If such an assignment is impossible, print `NO`.

## Example

**Input:**
```
3 5
1 4
1 5
2 4
2 6
3 5
```

**Output:**
```
YES
1 4
3 5
2 6
```
