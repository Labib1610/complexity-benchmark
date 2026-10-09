# Orbital Relay Configuration

Time limit: 5 s
Memory limit: 256 MB

## Description

An orbital network requires the activation of **k** independent relay channels. The network components are divided into three distinct categories, each containing exactly **k** available resources:
- **k** satellites, identified by integers 1 through k,
- **k** transmission frequencies, identified by integers 1 through k,
- **k** encryption keys, identified by integers 1 through k.

A single relay channel must be configured using exactly one satellite, one transmission frequency, and one encryption key. However, due to hardware limitations, only specific combinations of these three resources are compatible. You will be provided with a list of **t** compatible configurations, each given as a triplet `(x, y, z)`. 

Your objective is to activate exactly **k** compatible configurations such that every satellite, every transmission frequency, and every encryption key is utilized in **exactly one** active channel. 

To assist with network diagnostics, the system guarantees the following operational constraints on all provided input data:
- No individual satellite, transmission frequency, or encryption key appears in more than $k^2$ compatible configurations.
- For any given compatible configuration `(x, y, z)`, the product of its identifiers ($x \times y \times z$) will never exceed 10,648.

Determine if it is possible to successfully configure the **k** relay channels. If a valid setup exists, report one such setup.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³), representing the number of resources in each category and the total number of compatible configurations, respectively.
Each of the subsequent **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), describing a compatible configuration consisting of satellite **x**, frequency **y**, and key **z**. All listed configurations are unique.

## Output

If a valid selection of **k** channels exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of an activated channel. Any valid selection where every resource is used exactly once will be accepted. The channels may be printed in any order.

If no such selection is possible, print `NO`.

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

In Example 2, both compatible configurations require frequency 1, meaning frequency 2 can never be utilized, making a complete setup impossible.
