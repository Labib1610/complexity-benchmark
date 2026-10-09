# Logistics Provisioning Phase: Unit Assignment

Time limit: 5 s
Memory limit: 256 MB

## Description
The regional readiness exercise employs a multiphase pipeline to allocate personnel. During the preliminary phase, an automated system analyzes historical mission logs to identify robust working relationships. It condenses these relationships into a structured compatibility database. 

The personnel roster forms a contiguous block of sequential IDs from 1 to 3q. To facilitate sequential processing, every record in the compatibility database is internally sorted. Each record contains exactly three distinct personnel IDs in strictly increasing order, representing an authorized deployment combination. Because the data is highly regular—every unit requires exactly three members, the total roster is exactly three times the target number of units, and all records are uniformly structured—the database is optimized for streamlined extraction.

Your module handles the unit assignment phase. You must process the structured database and extract a subset of exactly **q** records such that every single person on the roster is assigned. Because an individual cannot be physically present in multiple places, no personnel ID may appear more than once among your chosen records.

If the database does not allow for a perfect, non-overlapping allocation of all personnel, your module must flag this so human coordinators can intervene.

## Input
The first line provides two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The integer **q** represents the required number of units, implying a total contiguous roster of 3q personnel (numbered 1 through 3q). The integer **t** is the total number of authorized records in the compatibility database.

Following this, there are **t** lines representing the database records. Each line contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), specifying the IDs of three individuals who may form a unit.

## Output
If a valid assignment can be formed, print `YES` on the first line. Then, print **q** lines, each containing the three IDs of the individuals in one of the selected units. 
If it is impossible to assign everyone exactly once using the provided combinations, print `NO`.

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
