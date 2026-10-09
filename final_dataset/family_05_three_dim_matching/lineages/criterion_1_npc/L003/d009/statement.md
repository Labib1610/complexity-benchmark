# Quantum Resonance Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a quantum resonance core. The core consists of exactly **k** sequential stages, numbered from 1 to **k**.

You are provided with a catalog of **t** available modules. Each module is characterized by exactly 3 parameters: Frequency, Amplitude, and Phase. All parameter values are integers between 1 and **k**.

To achieve perfect stability, you must select exactly **k** modules from the catalog and assign one to each of the **k** stages such that all the following conditions are met:
1. The module assigned to stage $i$ must possess a Frequency parameter exactly equal to $i$ (for all $i$ from 1 to **k**).
2. No two modules selected for the core may share the same Amplitude parameter.
3. No two modules selected for the core may share the same Phase parameter.

Determine if such a stable core can be formed by selecting exactly **k** modules from the catalog.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents the number of stages in the core (and thus the number of modules required), and **t** is the total number of available modules in the catalog.

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

In Example 2, the two available modules are `1 1 1` and `2 1 2`. To fill the 2 stages, stage 1 must use a module with Frequency 1 (which is `1 1 1`) and stage 2 must use a module with Frequency 2 (which is `2 1 2`). However, both of these modules have an Amplitude of 1. This violates the rule that no two modules selected for the core may share the same Amplitude parameter. Thus, it is impossible to form a stable core.