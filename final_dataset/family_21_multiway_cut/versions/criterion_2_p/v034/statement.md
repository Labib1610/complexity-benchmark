# Problem B — Reactive Material Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
An underground complex contains a number of chambers. Certain pairs of these chambers are joined by two-way transit tubes. Each tube requires a specific amount of resources to permanently collapse.

Two designated chambers hold reactive materials that must never mix. You must select a set of tubes to collapse such that no sequence of intact tubes allows transit between the first designated chamber and the second. Once a tube is collapsed, nothing can pass through it.

The remaining chambers do not matter; they can maintain contact with either of the designated chambers, or neither. The only restriction is the resource limit: the combined resource requirement of the collapsed tubes must not be greater than the allocated reserve.

Determine a valid set of tubes to collapse that satisfies the resource limit, or state if it is impossible.

## Input
The first line provides five integers: the total count of chambers, the total count of transit tubes, the identifier of the first designated chamber, the identifier of the second designated chamber, and the allocated resource reserve. 
The following lines provide the details of each transit tube. Each line contains three integers: the identifiers of the two chambers the tube joins, and the resources required to collapse it.

## Output
If the objective can be met without exceeding the resource reserve, print `YES` on the first line. On the second line, print the tally of collapsed tubes. Then, print one line for each collapsed tube containing the two chamber identifiers as they appeared in the input.
If the objective cannot be met, print `NO`.

## Example 1

### Input
3 2 1 3 10
1 2 4
2 3 5

### Output
YES
1
1 2

## Example 2

### Input
3 2 1 3 3
1 2 4
2 3 5

### Output
NO
