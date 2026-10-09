# Nutritional Phase Distribution

**Time limit:** 2 s  
**Memory limit:** 256 MB  

You are formulating a daily nutritional plan using $n$ distinct ingredients. The plan is divided into exactly three sequential phases, identified by the integers 1, 2, and 3. Each ingredient must be assigned to exactly one of these phases.

In most culinary scenarios, ingredients blend seamlessly. However, certain specific pairs of ingredients undergo severe enzymatic degradation if they are processed in the same phase. You are provided with a complete list of these $m$ interacting pairs.

If the plan only allowed two phases, assigning the ingredients would be a simple matter of checking if conflicting items can be placed in opposite phases. Because you have exactly three phases at your disposal, you have significantly more flexibility. Furthermore, any ingredient that interacts with at most two others can always be safely accommodated provided the rest of the plan is valid. Your task is to determine whether this flexibility is sufficient to assign every ingredient to one of the three phases such that no two interacting ingredients share the same phase.

## Input
The first line contains two integers $n$ and $m$ — the number of ingredients and the number of interacting pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interacting pair of ingredients that cannot be placed in the same phase. Ingredients are numbered from 1 to $n$.

## Output
If no valid plan can be formed, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the phase assigned to ingredient $i$. Any valid plan is accepted.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```
