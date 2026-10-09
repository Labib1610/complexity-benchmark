# Problem B — Fleet Mobilization

Time limit: 2 s   Memory limit: 256 MB

## Description

The galactic defense command must mobilize exactly **k** strike teams. There are three categories of assets available, each containing exactly **k** elements:

- **k** pilots, identified by integers 1 through k,
- **k** starfighters, identified by integers 1 through k,
- **k** distinct missions, identified by integers 1 through k.

A valid strike team consists of exactly one pilot, one starfighter, and one mission. You are provided with a comprehensive list of feasible deployment configurations `(pilot, starfighter, mission)`.

Due to strict biometric hardware locks, each pilot is only capable of operating one specific starfighter. Consequently, in the provided list of feasible deployments, any given pilot is always paired with the same starfighter, and no two pilots are ever paired with the same starfighter. The only variable remaining is the assignment of missions.

Your objective is to select exactly **k** feasible deployments from the list such that every pilot, every starfighter, and every mission is utilized in exactly one strike team. Determine if such a mobilization is possible, and if so, output one valid set of deployments.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of elements in each asset category and the total number of feasible deployments.
Each of the subsequent **t** lines contains three integers **p**, **s**, **m** (1 ≤ p, s, m ≤ k), representing a feasible deployment consisting of pilot **p**, starfighter **s**, and mission **m**. No deployment configuration is listed more than once. In this list, a given pilot **p** will only ever appear alongside one specific starfighter **s**, and each pilot is associated with a distinct starfighter.

## Output

If a valid mobilization of **k** strike teams is possible, output `YES` on the first line. Then, output **k** lines, each containing the three integers `p s m` of a chosen deployment (in any order). Any valid mobilization is accepted.

If no valid mobilization exists, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
