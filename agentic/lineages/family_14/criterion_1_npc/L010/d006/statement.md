# Problem A — Value Unification Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A formal system contains **n** distinct elements, numbered 1 to **n**. Initially, no two distinct elements are known to be interchangeable.

You are provided with **m** potential bidirectional equivalences. Each equivalence can be established by paying a one-time cost of **w** energy units. Once an equivalence between element **u** and element **v** is established, they are considered interchangeable. Furthermore, interchangeability is transitive: if **a** is interchangeable with **b**, and **b** is interchangeable with **c**, then **a** is interchangeable with **c**. You may use any established equivalences, and the transitivity property applies across any sequence of them.

You are given a list of **t** distinct target elements. Your objective is to establish a subset of equivalences such that all **t** target elements become mutually interchangeable. You may establish equivalences involving any of the **n** elements to serve as intermediate steps to achieve this.

Determine the absolute minimum total energy cost required to establish such a set of equivalences.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identities of the target elements.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an equivalence between element **u** and element **v** can be established for a cost of **w** energy units.
It is guaranteed that some subset of equivalences allows all target elements to be made mutually interchangeable.

## Output

Output a single integer representing the minimum total energy cost required.

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

In Example 1, establishing equivalences between element 4 and elements 1, 2, and 3 costs 1 + 1 + 1 = 3. Because of transitivity, elements 1, 2, and 3 all become mutually interchangeable. This costs less than establishing equivalences directly among 1, 2, and 3 (which would cost 2 + 2 = 4).

In Example 3, with only one target element, the condition is already met without any equivalences, so the minimum cost is 0.