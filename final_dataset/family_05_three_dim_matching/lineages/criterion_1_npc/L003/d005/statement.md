# Codebook Generation

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a transmission codebook. The alphabet size is **k**, meaning all valid symbols are integers from 1 to **k**.

You are provided with a pool of **t** valid codewords. Each codeword has a length of exactly 3 symbols.

Your task is to select exactly **k** codewords from this pool to form your codebook. To ensure maximum error correction capability, the Hamming distance between every pair of distinct codewords in your selected codebook must be exactly 3. (The Hamming distance between two codewords of equal length is the number of positions at which their corresponding symbols differ).

Determine if such a codebook can be formed.

## Input

The first line provides two integers, **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³). Here, **k** represents both the alphabet size and the number of codewords required, and **t** is the total number of valid codewords in the pool.
The next **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a codeword in the pool. Every codeword in the input is distinct.

## Output

If a valid codebook can be formed, output `YES` on the initial line. Following this, output **k** lines each containing three integers `x y z`, specifying the codewords used for your codebook. If several valid codebooks exist, supplying any one of them is sufficient. The codewords may be printed in any sequence.

If it is impossible to find **k** codewords satisfying the condition, output `NO`.

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

In Example 2, the two available codewords are `1 1 1` and `2 1 2`. Their Hamming distance is 2 (they differ in the first and third positions, but share the symbol `1` in the second position). Since they do not have a Hamming distance of 3, they cannot both be selected. With only 2 codewords available, it is impossible to select 2 that satisfy the requirement.