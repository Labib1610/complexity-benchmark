# Problem A — Botanical Nutrient Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
A botanical research facility executes a three-stage workflow to cultivate a rare flora. 

Stage 1 is the Pre-Processing Phase, where raw compounds are refined into exactly $n$ distinct nutrient vials, numbered 1 to $n$. This stage is already finished.

Stage 2 is the Administration Phase, which is the segment you must plan. The greenhouse's automated manifold operates on a daily cycle. The manifold's physical limitations mean it can safely deliver a maximum of $M$ vials during any single day. Because of the plant's biological absorption rates, there are strict sequential dependencies. You are given $m$ rules of the form $(a, b)$, which mandate that vial $a$ must be fully absorbed before vial $b$ is introduced. Since absorption requires overnight resting, vial $a$ must be administered on a strictly earlier day than vial $b$. They cannot be delivered on the same day. The Administration Phase has a rigid, finite window of $T$ consecutive days to administer the entire set of $n$ vials.

Stage 3 is the Observation Phase, which monitors the plant's growth. However, Stage 3 can only proceed if Stage 2 is successfully completed without violating the manifold limit or any absorption rules.

Your task is to determine if a valid daily schedule exists for Stage 2. You must allocate every one of the $n$ vials to a specific day (from 1 to $T$). If a valid schedule exists, output it so the workflow can proceed to Stage 3; otherwise, report that the protocol cannot be completed within the window.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
The following $m$ lines each contain two integers $a$ and $b$, indicating that vial $a$ must be administered on a strictly earlier day than vial $b$.

## Output
Print `YES` followed by $n$ integers $d_1, d_2, \dots, d_n$ (the day assigned to each vial, in the range 1 to $T$); otherwise, print `NO`. If multiple valid assignments exist, any of them will be accepted.

## Example
**Input:**
```
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output:**
```
YES
1 1 2 3 3
```
