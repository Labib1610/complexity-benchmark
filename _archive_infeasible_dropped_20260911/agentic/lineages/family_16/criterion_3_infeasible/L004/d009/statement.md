# Problem C — Impossible Pixel Compositing: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **j** rendering jobs. For each job $k$ (where $k$ is a 1-based index from 1 to **j**), you must generate two 1-dimensional pixel arrays: Load 1 and Load 2. 

The number of opaque pixels in Load 1 for job $k$ must exactly equal **p1**.
The number of opaque pixels in Load 2 for job $k$ must exactly equal **p2**.
All other pixels in the arrays are transparent.

A valid render must satisfy three rules:

- **Rule 1 (Canvas Boundary):** All pixel arrays are strictly constrained to a fixed canvas width of exactly **T** pixels. Every opaque pixel must be placed at an integer coordinate from 1 to **T**.
- **Rule 2 (Collision-Free Overlay):** For a given load type (Load 1 or Load 2), if we overlay that specific load across all **j** jobs, no two jobs may place an opaque pixel at the same horizontal coordinate.
- **Rule 3 (Streak Integrity):** For any single job $k$, overlaying its Load 1 and its Load 2 together (forming a new array where a pixel is opaque if it was opaque in either Load 1 or Load 2) must result in a single unbroken horizontal streak of opaque pixels (with no transparent gaps). Furthermore, every opaque pixel originating from Load 1 must be positioned strictly to the left of every opaque pixel originating from Load 2.

For all test cases provided in this problem, it is guaranteed that no valid rendering can satisfy all three rules simultaneously. Your task is to certify this impossibility by identifying a localized contradiction. Exactly one of the following two types of certificates will be valid for the given input. Print the one that applies:

- **Job-specific contradiction:** There is a single job **i** (1-based index) such that Rule 1 (for job **i**) and Rule 3 (for job **i**) cannot be simultaneously satisfied, even if we completely ignore Rule 2 and all other jobs. Print: `JOB i`.
- **Load-specific contradiction:** There is a single load type **c** (where **c** is 1 or 2) such that Rule 1 (for load **c**) and Rule 2 (for load **c**) cannot be simultaneously satisfied, even if we completely ignore Rule 3 and the other load type. Print: `LOAD c`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required number of opaque pixels for Load 1 and Load 2 respectively, for that job.

## Output

Print a single line containing the certificate of impossibility: either `JOB i` (where i is the job index) or `LOAD c` (where c is the load type, 1 or 2).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, consider job 1. The required sizes dictate that Load 1 has 70 opaque pixels and Load 2 has 60 opaque pixels. By Rule 3, overlaying them must form an unbroken streak, and all opaque pixels in Load 1 must strictly precede those in Load 2. This forces the two arrays to form a single continuous block that is 130 pixels wide. However, Rule 1 restricts the canvas width to **100** pixels, making it too narrow to accommodate the streak. Thus, Rule 1 and Rule 3 cannot be simultaneously satisfied for job 1. `JOB 1` is the correct certificate. 

In Example 2, no single job violates the rules on its own. However, consider Load 1. Rule 2 requires the four Load 1 arrays (each having 50 opaque pixels) to be entirely collision-free when overlaid. This requires 200 distinct horizontal coordinates to be available on the canvas. Since Rule 1 restricts the canvas to a width of **150** pixels, it is impossible to fit all of them without overlap. Thus, Rule 1 and Rule 2 cannot be simultaneously satisfied for Load 1, making `LOAD 1` the correct certificate.