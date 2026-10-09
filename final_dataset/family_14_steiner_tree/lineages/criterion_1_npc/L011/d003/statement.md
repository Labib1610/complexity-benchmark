# Problem A — Pneumatic Infrastructure

Time limit: 5 s
Memory limit: 256 MB

## Description

A sprawling industrial park consists of **n** distinct operational sectors, identified by integers from 1 to **n**. To facilitate rapid material transfer, a number of proposed bidirectional pneumatic transit pipes can be installed between certain pairs of sectors. The financial expenditure required to lay down each proposed pipe is known in advance.

An upcoming regulatory review mandates that a specific subset of **t** sectors—designated as *compliance-essential*—must be fully integrated into a unified transit grid. Specifically, a continuous route of installed pipes must exist so that a payload can be successfully dispatched from any compliance-essential sector to any other. 

When designing this grid, you are not restricted to only connecting the compliance-essential sectors directly to one another. Any of the remaining non-essential sectors may be utilized as supplementary junctions; routing paths through these intermediate sectors is entirely optional but may be advantageous if it reduces the overall expenditure. 

Your task is to choose a subset of the proposed pipes to install such that the compliance-essential sectors are fully mutually accessible, while keeping the total financial expenditure of the installed pipes to the absolute minimum.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the identifiers of the compliance-essential sectors.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that a pneumatic pipe can be installed between sector **u** and sector **v** for a financial expenditure of **w**.  
It is guaranteed that the proposed pipes provide at least one valid way to integrate all compliance-essential sectors.

## Output

Output a single integer representing the minimum possible total financial expenditure required to satisfy the regulatory mandate.

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

In Example 1, installing the pipes that link sector 4 to sectors 1, 2, and 3 requires a total expenditure of 1 + 1 + 1 = 3. This successfully integrates the compliance-essential sectors (1, 2, and 3) into a single grid. Utilizing sector 4 as a junction is more cost-effective than forcing direct links solely between the compliance-essential sectors, which would incur an expenditure of at least 4. 

In Example 3, only one sector is flagged as compliance-essential. Since no connections are needed to link a single sector to itself, zero pipes are installed, resulting in an expenditure of 0.