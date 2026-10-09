# Botanical Extraction

Time limit: 1 s   Memory limit: 256 MB

## Description
You are formulating a new botanical beverage containing `n` distinct herbal extracts. During the preparation process, each herb (numbered 1 through `n`) must be steeped in exactly one of two solvent bases: Ethanol (represented as 1) or Aqueous Glycerin (represented as 0). 

Due to complex chemical interactions, certain combinations of solvents will cause the beverage to cloud or precipitate. The laboratory has provided a list of `m` chemical safety mandates. Each mandate specifies two acceptable extraction states. A positive integer `x` indicates that herb `|x|` is steeped in Ethanol, while a negative integer `-x` indicates that herb `|x|` is steeped in Aqueous Glycerin. To ensure the final product remains stable, every mandate must have at least one of its two specified states realized in the final recipe.

Your task is to analyze the laboratory's mandates and determine if there is a complete recipe (assigning exactly one solvent to each of the `n` herbs) that satisfies all `m` mandates simultaneously. If such a recipe exists, you must provide it. If the chemical constraints contradict each other making a stable beverage impossible, you must reject the formulation.

## Input
The first line contains two integers `n` and `m` (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5) — the number of herbal extracts and the number of safety mandates, respectively.
Each of the next `m` lines contains two non-zero integers `l1` and `l2` (|l1|, |l2| ≤ n). These represent the two extraction states for that mandate. To prevent precipitation, at least one of these two states must be present in your final recipe.

## Output
If no stable formulation is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output `n` space-separated integers `s1, s2, ..., sn`, where each `si` is either 1 (Ethanol) or 0 (Aqueous Glycerin), representing the solvent used for herb `i`. If multiple stable recipes exist, you may output any of them.

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
