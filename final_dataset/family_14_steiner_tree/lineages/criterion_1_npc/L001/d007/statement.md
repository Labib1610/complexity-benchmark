# Problem A — Format Conversion

Time limit: 5 s   Memory limit: 256 MB

## Description

You are developing a unified document reader that must support **n** distinct data formats, indexed 1 through **n**. 
Your specific objective is to ensure the reader can successfully parse a set of **t** critical formats: $c_1, c_2, \dots, c_t$.

To achieve this, you must first designate exactly one of the **n** formats to act as the reader's native internal format. 
The reader can inherently only parse its native format. To support other formats, you can install bidirectional format converters.
You are provided with a list of **m** available converters. Installing a converter between format $u$ and format $v$ incurs a one-time licensing cost of $w$. 
Once a set of converters is installed, translation can be chained: any format that is linked to the native internal format through a sequence of installed converters is successfully parsed by the reader.

You must choose which converters to install, and which format to designate as the native internal format, such that all **t** critical formats can be parsed. You only pay the licensing cost for each installed converter once, regardless of how many critical formats rely on it in their translation sequence to the native format.

Determine the minimum total licensing cost required. (The choice of the native format itself is free. If $t=1$, you can simply designate $c_1$ as the native format and install 0 converters).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of data formats, the number of available converters, and the number of critical formats.
The second line contains **t** distinct integers $c_1, c_2, \dots, c_t$: the indices of the critical formats.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a bidirectional converter between format u and format v can be installed for a cost of w.
It is guaranteed that a valid set of converters exists to satisfy the requirement.

## Output

Print a single integer: the minimum total licensing cost.

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

In Example 1, the critical formats are 1, 2, and 3. You can designate format 4 as the native internal format. You then install converters between (1,4), (2,4), and (3,4) for a total cost of 1+1+1 = 3. 
Because formats 1, 2, and 3 can all be translated to the native format 4 via the installed converters, all critical formats are successfully parsed. 
Alternatively, you could designate format 2 as the native format and install converters (1,2) and (2,3) for a total cost of 2+2 = 4. The minimum cost is 3.

In Example 3, there is only one critical format ($t=1$), so you can designate it as the native format. No converters are needed, and the minimum cost is 0.