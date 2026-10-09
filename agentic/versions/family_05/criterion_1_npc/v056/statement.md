# Problem A — Research Study Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

A pharmaceutical company is structuring a research study involving **k** patient groups, **k** drug variants, and **k** testing centers. Each of these components is identified by an integer from 1 to **k**.

The study will be divided into exactly **k** concurrent trial arms. Each trial arm is formed by assigning exactly one patient group to receive one drug variant at one testing center. To ensure comprehensive data collection without overlap, every patient group, drug variant, and testing center must be utilized in exactly one of the **k** trial arms.

Regulatory safety protocols dictate that only a specific list of **t** combinations of patient group, drug variant, and testing center are medically cleared for use. The study can only be configured using combinations from this list. 

Due to logistical limits, no single patient group is involved in more than **k**² cleared combinations. Additionally, for any cleared combination, the sum of its patient group, drug variant, and testing center identifiers is guaranteed to be at most 3**k**.

Your task is to determine if it is possible to configure the **k** trial arms using only the cleared combinations such that all components are used exactly once. If a valid configuration exists, you must output the selected combinations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³), representing the number of components in each category and the total number of medically cleared combinations, respectively.
The following **t** lines each contain three integers **d**, **f**, and **m** (1 ≤ d, f, m ≤ k). Each line describes a cleared combination consisting of patient group **d**, drug variant **f**, and testing center **m**.
No combination is listed more than once.

## Output

If a valid research study configuration is possible, print `YES` on the first line. Then, print **k** lines, each containing the three integers `d f m` representing a chosen trial arm. The trial arms can be listed in any order. Any valid set of **k** combinations that uses every patient group, drug variant, and testing center exactly once will be accepted.
If no such configuration is possible, print `NO`.

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

In Example 2, both cleared combinations use drug variant 1, so drug variant 2 can never be evaluated.
