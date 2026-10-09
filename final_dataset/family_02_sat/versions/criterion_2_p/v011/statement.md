# Problem B — Exhibition Lighting

Time limit: 1 s   Memory limit: 256 MB

## Description

A museum is preparing an exhibition featuring **n** distinct artworks. For each artwork, the curator must select exactly one of two lighting styles: Spotlight or Ambient.

The exhibition is funded by various sponsors, who have submitted a total of **m** mandates. Every mandate specifies exactly two desired lighting conditions for specific artworks. A condition is simply a particular artwork paired with a requested lighting style. A mandate is considered fulfilled if the final lighting setup satisfies at least one of its two conditions. 

The curator must decide whether there exists a single, comprehensive lighting plan for all **n** artworks that successfully fulfills every sponsor mandate simultaneously. If such a plan exists, you must provide one. Otherwise, you must declare that the mandates are mutually contradictory and no such plan can be formed.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5), representing the number of artworks and the number of sponsor mandates, respectively.
Each of the following m lines corresponds to a mandate and contains two non-zero signed integers l1 and l2, where |li| ≤ n.
A positive integer v represents the condition that artwork v is lit with a Spotlight.
A negative integer v represents the condition that artwork |v| is lit with Ambient light.
For each mandate, at least one of the two conditions must be met by the final lighting plan.

## Output
If there is no valid lighting plan that fulfills all mandates, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output n space-separated integers s1, s2, …, sn representing a valid lighting plan. Each si must be 1 if artwork i receives a Spotlight, and 0 if artwork i receives Ambient light.

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
Multiple valid lighting plans may exist; any one is accepted. The same artwork may appear in multiple mandates.
