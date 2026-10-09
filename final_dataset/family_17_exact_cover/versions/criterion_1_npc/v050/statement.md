# Problem A — Comprehensive Field Activation

Time limit: 5 s   Memory limit: 256 MB

## Description
A regional crisis response agency manages a pool of active personnel. Staff members are tracked using identification codes from 1 up to a maximum of 3**q**.

Standard operating procedure dictates that field units must be formed according to a provided catalog of joint-training records. Each record in the catalog specifies three personnel who are cleared to operate together as a unit. Staff members may be listed in several different records, but any combination not explicitly present in the catalog cannot be fielded.

During a full-scale readiness drill, command must select a series of these records to form the deployment. The activation is subject to strict personnel regulations: every single staff member must be assigned to exactly one active unit. They cannot be left at the base, nor can they be split across multiple assignments.

You must evaluate the catalog to determine if it is possible to form a valid deployment. If it is possible, output the units that should be activated. Otherwise, indicate that it cannot be done.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The total number of personnel is 3**q**.
The following **t** lines each contain three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing a cleared unit of three personnel.

## Output
If a valid deployment exists, print `YES` on the first line, followed by **q** lines. Each of these lines must contain the three identification codes of an activated unit.
If no such deployment is possible, print `NO`.

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
