# Quantum Resonance Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a quantum resonance core. The core requires exactly **k** modules to operate.

You are provided with a catalog of **t** available modules. Each module is characterized by exactly 3 parameters: Frequency, Amplitude, and Phase.

When a set of exactly **k** modules is selected, the *interference signature* of a parameter category (e.g., Frequency) is calculated as the sum of $2^{v-1}$ over the **k** selected modules, where $v$ is the module's value for that parameter. For the core to be perfectly stable, the interference signature for *each* of the three parameter categories—Frequency, Amplitude, and Phase—must independently be exactly $2^k - 1$.

Determine if such a stable core can be formed by selecting exactly **k** modules from the catalog.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents the number of modules required, and **t** is the total number of available modules in the catalog.
The next **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing the Frequency, Amplitude, and Phase parameters of a module in the catalog. Every module listed in the input is distinct. You may choose only among these listed modules, and each module from the catalog may be selected at most once.

## Output

If a perfectly stable core can be formed, output `YES` on the initial line. Following this, output **k** lines each containing three integers `x y z`, specifying the modules used for your core. If several valid selections exist, supplying any one of them is sufficient. The modules may be printed in any sequence.

If it is impossible to find **k** modules satisfying the condition, output `NO`.

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

In Example 2, the two available modules are `1 1 1` and `2 1 2`. If both are selected, the Frequency interference signature is $2^{1-1} + 2^{2-1} = 1 + 2 = 3$. The Amplitude interference signature is $2^{1-1} + 2^{1-1} = 1 + 1 = 2$. The Phase interference signature is $2^{1-1} + 2^{2-1} = 1 + 2 = 3$. Since the required signature for each category is $2^k - 1 = 2^2 - 1 = 3$, they do not form a perfectly stable core because the Amplitude signature is 2. With only 2 modules available, it is impossible to select 2 that satisfy the requirement.