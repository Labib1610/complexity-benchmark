# Problem A — Resonant Hyperspace

Time limit: 5 s   Memory limit: 256 MB

## Description

A starfleet must execute a sequence of exactly **k** hyperspace jumps. The fleet's instruments operate using three independent navigational domains: pulsar frequencies, gravimetric distortions, and subspace harmonics. Each domain consists of **k** distinct settings, indexed from 1 to **k**.

The navigational computer has identified exactly **t** stable synchronization vectors. Each stable vector is a specific triplet `(x, y, z)`, indicating that pulsar frequency **x**, gravimetric distortion **y**, and subspace harmonic **z** can be safely synchronized to produce a single jump.

To prevent a catastrophic resonant collapse of the local space-time, the fleet must select exactly **k** stable vectors from the computer's list to form the sequence of jumps. This selection must satisfy a strict non-interference condition: no two selected vectors may have the same pulsar frequency, no two may have the same gravimetric distortion, and no two may have the same subspace harmonic.

Determine whether such a selection of exactly **k** stable vectors is possible. If it exists, provide one valid set of vectors.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of settings in each navigational domain and the total number of stable synchronization vectors.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a stable vector consisting of pulsar frequency **x**, gravimetric distortion **y**, and subspace harmonic **z**. All listed vectors are distinct.

## Output

If a safe sequence of **k** jumps is possible, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of one selected vector. Any valid selection of **k** vectors that satisfies the non-interference condition is accepted; the chosen vectors may be printed in any order.

If no such sequence is possible, print `NO`.

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

In Example 2, both stable vectors share gravimetric distortion 1, so they cannot both be selected. A selection of 2 vectors is therefore impossible.