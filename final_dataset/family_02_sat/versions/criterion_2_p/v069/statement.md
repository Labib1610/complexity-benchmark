# Problem B — Cinematic Continuity

Time limit: 1 s   Memory limit: 256 MB

## Description

A film director is scheduling the shooting of $n$ scenes. Each scene must be filmed either during the day (represented by position 1) or at night (represented by position 0). 

The script supervisor has identified $m$ continuity requirements. Every requirement specifies exactly two preferred lighting conditions, where a condition is a scene index and its required time of day. For the final cut to be acceptable, at least one of the two conditions in every requirement must be met. Because each requirement couples only a pair of scenes, failing to meet one condition forces the other condition to be adopted—the continuity rules propagate as chains of forced consequences. The production team sometimes fears this requires testing all combinations, but the pairwise structure makes the consequences fully deducible. 

Determine whether a single global day/night schedule of all $n$ scenes satisfies every two-condition requirement at once, and if so report one; otherwise report that the requirements are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 10^5, 0 ≤ $m$ ≤ 2·10^5).
Each of the next $m$ lines contains two non-zero signed integers $l_1$ $l_2$, with $|l_i| \le n$. A positive integer indicates the corresponding scene must be filmed during the day (1), and a negative integer indicates the scene (given by the absolute value) must be filmed at night (0). At least one of the two stated conditions must hold for each requirement.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1$ $s_2$ … $s_n$ (each in {0, 1}) forming any valid schedule.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid schedules may exist; any one is accepted. The same scene index may appear in multiple requirements.
