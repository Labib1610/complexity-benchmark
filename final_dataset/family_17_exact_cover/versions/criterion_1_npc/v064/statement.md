# Problem A — Trinary Polymer Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description
A hazardous waste disposal facility is processing a batch of distinct volatile chemical precursors. The current batch contains exactly 3q precursors, which are sequentially numbered starting from 1 up to 3q.

To safely neutralize these chemicals, they must be synthesized into inert trinary polymers. A successful synthesis reaction always requires exactly three distinct precursors. The facility maintains a strict catalog of validated synthesis recipes. Due to complex chemical affinities, only the specific three-precursor combinations listed in this catalog will successfully form an inert polymer. Unlisted combinations will fail and are strictly prohibited. Some recipes may share common precursors with other recipes, but a precursor can only actually be consumed once.

The facility's safety mandate requires total neutralization of the batch. This means every single precursor must be completely consumed by the chosen reactions. Furthermore, each precursor is provided in a fixed indivisible quantity, meaning it can participate in exactly one synthesis reaction. No precursor may be left unreacted, and no precursor may be split or used in more than one reaction.

You must determine whether it is possible to select a set of recipes from the catalog that will perfectly consume all 3q precursors without any omissions or overlaps. If such a set of reactions exists, you must also provide the list of recipes to be executed.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000), where 3q represents the total number of precursors and t represents the number of validated synthesis recipes in the catalog.
Each of the following **t** lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q) representing the three precursors required for that specific recipe.

## Output
If there is a valid selection of recipes that perfectly consumes all precursors, print `YES` on the first line, followed by **q** lines each containing the three precursors of a chosen recipe.
If no such selection is possible, print `NO`.

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
