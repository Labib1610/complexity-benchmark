# Problem B — Component Testing Phases

Time limit: 2 s   Memory limit: 256 MB

## Description
A testing facility evaluates connections between two types of hardware: signal generators and analyzers. Each scheduled test links exactly one generator to exactly one analyzer. A test never links two generators or two analyzers. Individual components may be involved in several different tests over the course of the campaign.

Testing is divided into discrete, numbered phases (1, 2, 3, ...). Each test occupies exactly one phase. A strict safety requirement dictates that a component (whether a generator or an analyzer) can participate in at most one test per phase. 

Let $K$ be the maximum number of tests involving any single component. Because this busiest component cannot run multiple tests in the same phase, at least $K$ phases are strictly necessary. Your operational goal is to schedule all tests using **no more** than $K$ phases in total. (The rule that tests only occur between two distinct types of hardware guarantees this $K$-phase schedule is always achievable). 

Assign every test a phase drawn from the range $1 \dots K$ so that no component is ever double-booked in any phase.

## Input
First line: three integers $n_G$, $n_A$, $m$ ($1 \le n_G, n_A \le 100000$, $0 \le m \le 400000$).
Next $m$ lines: two integers $u$ and $v$ ($1 \le u \le n_G$, $1 \le v \le n_A$), representing a test between generator $u$ and analyzer $v$.

## Output
Print `YES`, followed by a line containing $m$ integers in the range $1 \dots K$ — the phase assigned to test $i$, in the order they appear in the input. Any two tests that involve the same component must be assigned different phases.

## Example

**Input**
```text
3 3 4
1 1
1 2
2 2
3 3
```

**Output**
```text
YES
1 2 1 1
```
