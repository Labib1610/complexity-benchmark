# Problem C — System Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

An interstellar spaceport processes **j** passengers through exactly **two** sequential security checkpoints. Every passenger first completes Checkpoint 1 (Identity Verification) and then proceeds to Checkpoint 2 (Customs Declaration). For each passenger, you are given their processing time at Checkpoint 1 and at Checkpoint 2. Each checkpoint processes only one passenger at a time, and a passenger reaches Checkpoint 2 only after finishing at Checkpoint 1.

The spaceport must complete all processing for the daily manifest by a strict deadline **T**: every passenger must be completely finished by time **T**.

Your task is to analyze the processing times and issue a diagnostic certificate. The facility's automated audit guarantees that exactly one of the following limit violations will always apply to the provided data. Print the one that holds:

- **Individual Delay:** A single passenger takes too long. If some passenger's two processing times add up to more than **T**, print: `JOB i` — where **i** (1-based) is such a passenger.
- **Checkpoint Bottleneck:** A checkpoint is overloaded. If the total processing time of all passengers at Checkpoint 1 (or Checkpoint 2) exceeds **T**, print: `LOAD c` — where **c** is 1 or 2 and the total processing time at Checkpoint **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T**.
Each of the next **j** lines contains two integers **p1** and **p2**: the processing times of a passenger at Checkpoint 1 and Checkpoint 2.

**Bounds:**
- The number of passengers **j** is at least 1. The facility has exactly 200 holding zones, each with a strict maximum capacity of 1,000 individuals, meaning **j** cannot exceed the total capacity of all holding zones combined.
- The deadline **T** is at least 1, and its maximum possible value is exactly the cube of one thousand.
- The processing times **p1** and **p2** are each at least 1, and are capped at the square of one thousand.

## Output

Print a single line: `JOB i` (a passenger whose **p1** + **p2** exceeds **T**) or `LOAD c` (a checkpoint **c** whose total load exceeds **T**).

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

In Example 1, passenger 1 requires 70 + 60 = 130 > 100 time units, so `JOB 1` is the correct diagnostic output. In Example 2, no single passenger's total time exceeds 150, but Checkpoint 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
