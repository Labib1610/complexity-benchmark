# Problem B — Exhibition Lighting

Time limit: 1 s   Memory limit: 256 MB

## Description
A modern gallery houses **n** distinct installations. The gallery is supported by various benefactors who have submitted **m** specific directives regarding the presentation of the pieces. 

A directive consists of exactly two presentation preferences. A single preference targets a specific installation and dictates its lighting mode: it must be either Focused or Diffused. Every installation is required to be set to exactly one of these two modes. For a directive to be considered respected, the final gallery arrangement must successfully incorporate at least one of its two preferences. 

After reviewing all the submitted materials, the gallery director needs to establish whether there is a universal configuration for all **n** installations that respects every benefactor's directive concurrently. If such a configuration is possible, you must provide it. If the directives are irreconcilable, you must declare that no such arrangement exists.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5), representing the number of installations and the number of benefactor directives.
Each of the following m lines corresponds to a directive and contains two non-zero signed integers l1 and l2, where |li| ≤ n.
A positive integer v indicates a preference that installation v is set to Focused lighting.
A negative integer v indicates a preference that installation |v| is set to Diffused lighting.
For each directive, at least one of the two preferences must be incorporated in the final arrangement.

## Output
If there is no valid arrangement that respects all directives, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output n space-separated integers s1, s2, …, sn representing a valid arrangement. Each si must be 1 if installation i receives Focused lighting, and 0 if installation i receives Diffused lighting.

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
