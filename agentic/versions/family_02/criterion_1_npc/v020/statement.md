# Problem A — Nutrient Blend Formulation

Time limit: 2 s   Memory limit: 256 MB

## Description

A biotechnology firm is developing a new synthetic nutrient blend comprising **n** distinct ingredients. During the manufacturing process, each ingredient must be permanently set to one of two structural forms: Activated or Dormant. There is no intermediate state, and no ingredient can be omitted.

Quality control has identified **m** potential instability reactions that could ruin the batch. To prevent these reactions, the engineers have introduced a set of **m** chemical stabilizers, one for each potential instability. However, a stabilizer only works if the blend contains a specific trigger. Each stabilizer lists exactly three trigger conditions, where a condition specifies a particular ingredient and the structural form (Activated or Dormant) it must take. 

For a stabilizer to successfully prevent its corresponding instability, **at least one** of its three trigger conditions must be present in the final blend. If a stabilizer detects none of its three required conditions, it fails to activate, and the batch is ruined. A single ingredient's state will often affect many different stabilizers, sometimes being demanded Activated by one and Dormant by another. The stabilizers may overlap heavily or barely at all—what matters is strictly whether each stabilizer's specific conditions are met.

Your task is to determine whether there exists a single, comprehensive formulation—assigning every one of the **n** ingredients to either the Activated or Dormant form—that successfully activates **every** stabilizer simultaneously. If such a formulation exists, you must provide one. Otherwise, you must declare that the blend cannot be stabilized.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of ingredients and the number of stabilizers, respectively.

Each of the following m lines describes the trigger conditions for one stabilizer. Each line contains three non-zero integers, $l_1, l_2, l_3$, where the absolute value $|l_i|$ (which is $\le n$) represents the ingredient index. 
- A positive integer $l_i$ means the stabilizer can be triggered if ingredient $|l_i|$ is in the **Activated** form.
- A negative integer $l_i$ means the stabilizer can be triggered if ingredient $|l_i|$ is in the **Dormant** form.

For the batch to be viable, every stabilizer must have at least one of its three conditions met.

## Output
If no viable formulation exists that satisfies all stabilizers, print a single line containing `NO`.

If a valid formulation is possible, print `YES` on the first line. On the second line, print n space-separated integers $s_1, s_2, \dots, s_n$ (each either `0` or `1`), where $s_i = 1$ if ingredient $i$ is Activated, and $s_i = 0$ if ingredient $i$ is Dormant. If multiple satisfying formulations exist, any of them will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each stabilizer lists exactly three trigger conditions. The same ingredient index may appear more than once in a single stabilizer's list.
