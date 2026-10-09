# Quantum Resonance Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a quantum resonance core. The core requires exactly **k** modules to operate.

You are provided with a catalog of **t** available modules. Each module is characterized by exactly 3 parameters: Frequency, Amplitude, and Phase.

When a set of exactly **k** modules is selected, we evaluate its stability by constructing a characteristic matrix for each parameter category. For a given category (e.g., Frequency), let the values of the **k** selected modules be $v_1, v_2, \dots, v_k$. The order in which the chosen modules are indexed does not affect whether the final determinant evaluates to zero. We define a $k \times k$ matrix $M$ where the entry in the $r$-th row and $c$-th column (for $1 \le r, c \le k$) is given by $M_{r, c} = (v_c)^{r-1}$. 

For the core to be perfectly stable, the determinant of this characteristic matrix must be non-zero for *each* of the three parameter categories—Frequency, Amplitude, and Phase—independently. 

*System Architecture Note:* The catalog order may be adversarial, with decoy modules arranged specifically to make a fixed-parameter, first-available depth-first search explore exponentially many dead ends. 

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

In Example 2, the two available modules are `1 1 1` and `2 1 2`. If both are selected, the Amplitude values are $v_1 = 1$ and $v_2 = 1$. The $2 \times 2$ characteristic matrix for Amplitude has $M_{1,1} = 1^0 = 1$, $M_{1,2} = 1^0 = 1$, $M_{2,1} = 1^1 = 1$, and $M_{2,2} = 1^1 = 1$. The matrix is $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, which has a determinant of $1 \times 1 - 1 \times 1 = 0$. Because the determinant for Amplitude is zero, they do not form a perfectly stable core. With only 2 modules available, it is impossible to select 2 that satisfy the requirement.