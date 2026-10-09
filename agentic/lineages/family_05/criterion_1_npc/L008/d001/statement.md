# Problem A — Grand Potion Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

You are participating in the Grand Synthesis, an alchemical trial where you must simultaneously brew **k** distinct elixirs. The trial provides you with three sets of ingredients: **k** base liquids, **k** rare catalysts, and **k** elemental essences. The ingredients in each set are numbered from 1 to **k**. The alchemy guild limits the trial to a maximum of 22 simultaneous elixirs (and at least 1) due to spatial constraints.

An elixir can only be brewed by combining one base liquid, one rare catalyst, and one elemental essence. However, only certain combinations are chemically stable. You have transcribed a list of **t** stable recipes from an ancient grimoire. The grimoire might contain no stable recipes at all, or it might contain every possible combination up to the theoretical maximum of k·k·k.

Your objective is to select recipes from your list to brew the elixirs. A successful Grand Synthesis requires that you choose exactly **k** recipes to prepare, such that:
- Every base liquid is consumed in exactly one chosen recipe.
- Every rare catalyst is consumed in exactly one chosen recipe.
- Every elemental essence is consumed in exactly one chosen recipe.

Determine if it is possible to achieve a successful Grand Synthesis, and if so, report the recipes you have chosen.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of ingredients in each of the three sets, and the number of stable recipes.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), describing a stable recipe that combines base liquid **x**, rare catalyst **y**, and elemental essence **z**. No recipe appears more than once in the list.

## Output

If a successful Grand Synthesis of **k** recipes is possible, output `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of a chosen recipe. Any valid selection of recipes where every base liquid, rare catalyst, and elemental essence is used exactly once is accepted. The chosen recipes can be printed in any order.

If no such selection of recipes exists, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

## Note

In Example 2, both stable recipes require rare catalyst 1, meaning rare catalyst 2 can never be consumed in any chosen recipe.