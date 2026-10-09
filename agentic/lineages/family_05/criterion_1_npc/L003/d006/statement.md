# Alloy Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

You are synthesizing a specialized alloy. The target grade is **k**, meaning all valid material ratings are integers from 1 to **k**.

You are provided with a catalog of **t** available components. Each component is defined by exactly 3 ratings: Hardness, Malleability, and Conductivity.

Your task is to select exactly **k** components from this catalog to form your alloy. To ensure maximum stability, the alloy must be perfectly balanced. We define the *diversity* of a rating category as the number of unique integer values present in that category across your selected components. An alloy is perfectly balanced if and only if the product of the diversities of its three rating categories is exactly **k**³.

Determine if such an alloy can be formed using exactly **k** components from the catalog.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents both the target grade and the number of components required, and **t** is the total number of available components in the catalog.
The next **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing the Hardness, Malleability, and Conductivity ratings of a component in the catalog. Every component listed in the input is distinct. You may choose only among these listed components, and each component from the catalog may be selected at most once.

## Output

If a perfectly balanced alloy can be formed, output `YES` on the initial line. Following this, output **k** lines each containing three integers `x y z`, specifying the components used for your alloy. If several valid selections exist, supplying any one of them is sufficient. The components may be printed in any sequence.

If it is impossible to find **k** components satisfying the condition, output `NO`.

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

In Example 2, the two available components are `1 1 1` and `2 1 2`. If both are selected, the Hardness diversity is 2 (ratings 1 and 2), the Malleability diversity is 1 (both have rating 1), and the Conductivity diversity is 2 (ratings 1 and 2). The product of their diversities is 2 × 1 × 2 = 4. Since the required product is k³ = 2³ = 8, they do not form a perfectly balanced alloy. With only 2 components available, it is impossible to select 2 that satisfy the requirement.