# Problem A — Composite Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description
You manage a manufacturing process that must produce $q$ composite components. The facility holds a total of $3q$ distinct raw materials in its inventory, numbered sequentially from $1$ to $3q$. You have exactly one unit of each raw material.

A composite component is synthesized by fusing together a specific combination of three raw materials. You are provided with a technical manual containing $t$ known fusion formulas. Each formula specifies three materials that can be successfully fused. 

Your production target is to synthesize exactly $q$ composite components. Each time you apply a formula to create a component, the three materials listed in that formula are completely consumed. Consequently, a raw material cannot be utilized in more than one component.

Determine whether it is possible to reach the production target of $q$ components using the available inventory and the known formulas. If it is achievable, output the specific formulas you will apply.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ is the target number of composite components to synthesize, and $t$ is the number of known fusion formulas. 

Each of the subsequent $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), indicating that materials $a$, $b$, and $c$ can be fused to create one component.

## Output
If the production target can be met, print `YES` on the first line. On the next $q$ lines, print the three materials for each selected formula in your production plan. If no such plan is possible, print `NO`.

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
