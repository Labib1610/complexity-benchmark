# Problem A — Synthetic Metabolism Design

Time limit: 5 s
Memory limit: 256 MB

## Description

You are engineering a synthetic metabolic network for a novel microorganism. The organism's internal chemistry can potentially support **n** distinct chemical compounds, numbered 1 to **n**. 

Through phenotypic screening, you have identified **t** vital compounds that must be present and mutually interconvertible in the organism's metabolism to ensure its survival. 

Biophysicists have provided a catalog of **m** reversible enzymatic reactions that can be spliced into the organism's genome. Each reaction establishes a bidirectional conversion pathway between two specific compounds and imposes a constant metabolic burden (measured in ATP equivalents) on the cell to maintain the corresponding enzyme.

Your task is to select a subset of these enzymatic reactions to engineer into the DNA. The selection must guarantee that a chain of valid reactions exists to convert between any pair of the **t** vital compounds, effectively integrating them into a single continuous metabolic cascade. The total metabolic burden of your selection is the sum of the metabolic burdens of the chosen reactions. You may freely include reactions involving any of the non-vital compounds if they serve as useful chemical intermediates to lower the total metabolic burden. 

Find the minimum possible total metabolic burden required to synthesize a network that safely integrates all **t** vital compounds.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the vital compounds.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an available enzymatic reaction can interconvert compound **u** and compound **v** with a metabolic burden of **w**.
It is guaranteed that the provided catalog of reactions is sufficient to integrate all vital compounds.

## Output

Print a single integer: the minimum total metabolic burden required to establish the necessary metabolic cascade among all vital compounds.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, utilizing compound 4 as a chemical intermediate (incurring a total burden of 1+1+1 = 3) is more energetically efficient than providing direct reactions between the three vital compounds (which would incur a burden of 2+2=4). 

In Example 3, there is only one vital compound. Since it does not need to be converted to any other vital compound to function, no reactions need to be engineered, resulting in a total metabolic burden of 0.
