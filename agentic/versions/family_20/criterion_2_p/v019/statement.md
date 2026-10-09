# Problem B — Acoustic Resonance Campaign

Time limit: 2 s   Memory limit: 256 MB

## Description
An acoustics laboratory is preparing a series of resonance tests. The facility contains a bank of $N_E$ acoustic emitters and a separate bank of $N_C$ resonance chambers. Each planned test couples exactly one emitter with exactly one chamber; tests never couple two emitters or two chambers.

Tests are executed in discrete, numbered phases: 1, 2, 3, and so on. A single phase can accommodate multiple tests simultaneously, but physical limitations dictate that an individual emitter can participate in at most one test per phase. Likewise, an individual resonance chamber can participate in at most one test per phase. 

The overall length of the testing schedule is dictated by the single most heavily utilized piece of hardware across the entire facility. Let $D$ be the maximum number of tests involving any single emitter or any single chamber. Because that specific piece of hardware requires $D$ separate phases, the entire campaign requires a minimum of $D$ phases. 

Your objective is to schedule all tests using no more than this unavoidable minimum—exactly $D$ phases. Assign each test a phase from $1$ to $D$ such that no emitter and no chamber is scheduled for more than one test in the same phase. The strict division between the two hardware banks guarantees that a schedule fitting within exactly $D$ phases is always achievable.

## Input
The first line contains three integers $N_E$, $N_C$, and $M$ ($1 \le N_E, N_C \le 100000$, $0 \le M \le 400000$).
The next $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_E$, $1 \le v \le N_C$), indicating a test coupling emitter $u$ with chamber $v$.

## Output
Print `YES`, then a second line containing $M$ integers in the range $1 \dots D$. The $i$-th integer represents the phase assigned to the $i$-th test from the input. Tests sharing any emitter or chamber must be assigned different phases.

### Example

**Input**
```text
3 4 5
1 2
1 3
2 3
3 1
3 4
```

**Output**
```text
YES
1 2 1 1 2
```
