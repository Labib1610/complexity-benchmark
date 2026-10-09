# Logistics Provisioning Phase: Deployment Manifest

Time limit: 5 s
Memory limit: 256 MB

## Description
The regional readiness exercise relies on a two-phase personnel allocation pipeline. First, an automated analytics engine processes historical mission logs to identify synergistic triads—groups of exactly three personnel who are cleared to deploy together. Personnel are identified by sequential integers starting from 1. The engine provides a comprehensive database of these authorized triads.

In the second phase, your module is responsible for generating the final deployment manifest. You are given a target number of deployment units to form. The exercise parameters guarantee a perfectly balanced roster: the total number of personnel is exactly three times the target number of units, meaning there are no surplus individuals.

Your objective is to select a subset of the authorized triads such that every individual on the roster is assigned exactly once. Because an individual can only be deployed in one place, no personnel ID may appear in more than one selected triad. Notice that due to the perfect balance of the roster, any valid selection of exactly **q** non-overlapping triads will automatically fulfill the requirement of covering the entire roster without omissions. 

If a valid deployment manifest can be assembled from the provided triads, output it. If the database does not contain a configuration that assigns everyone exactly once, your module must flag this so human coordinators can adjust the exercise parameters.

## Input
The first line provides two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The value **q** is the required number of deployment units, establishing a total roster size of 3q personnel (numbered 1 through 3q). The value **t** represents the total number of authorized triads in the database.

Following this, there are **t** lines representing the database. Each line contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), specifying the IDs of three individuals who may form a unit.

## Output
If a valid deployment manifest can be formed, print `YES` on the first line. Then, print **q** lines, each containing the three IDs of the individuals in one of the selected units. 
If it is impossible to assign everyone exactly once using the provided triads, print `NO`.

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
