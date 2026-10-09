# Problem A — Accelerated Degree Program

Time limit: 5 s   Memory limit: 256 MB

## Description
A university offers an accelerated degree where a student must complete a set of core modules before their scholarship expires. Each module takes exactly one academic term to complete. To ensure students do not overwork themselves, the university imposes a strict enrollment cap: a student may register for at most $M$ modules during any single term. There is no penalty for taking fewer than $M$ modules in a term, and no bonus for finishing the degree early, as long as all required modules are completed by the deadline.

The curriculum has a rigid structure. Certain foundational modules act as strict prerequisites for more advanced ones. When one module is a prerequisite for another, the foundational module must be fully completed in a strictly earlier term before the advanced module can be taken. They cannot be taken concurrently in the same term, because the knowledge from the foundational module is only available for use in subsequent terms. Module difficulty or specific instructors are irrelevant; only the term in which a module is taken matters.

You are given the total number of required modules $n$, the enrollment cap per term $M$, the scholarship duration in terms $T$, and the number of prerequisite rules $m$. Assign every module to a term within the scholarship duration so that all prerequisite rules are respected and no term exceeds the enrollment cap, or report that the degree cannot be finished in time. (Note that a schedule respecting all prerequisites might still exceed the enrollment cap in some terms, and vice versa, so both constraints must be carefully balanced).

## Input
First line: four integers $n$, $M$, $T$, $m$. 
Each of the next $m$ lines: two integers $a$ $b$ — module $a$ must be completed before module $b$ is taken.

## Output
Print `YES` then $n$ integers $term[1 \dots n]$ (the term of each module, for modules $1$ through $n$ respectively, in $1 \dots T$); otherwise `NO`.

## Example

### Input
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```text
YES
1 1 2 3 3
```
