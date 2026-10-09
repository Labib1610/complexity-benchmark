# Problem A — Meeting the Deadline Across Parallel Threads

Time limit: 5 s   Memory limit: 256 MB

## Description
A compiler must complete a batch of functions before a hard build deadline. All functions take the same
amount of time — one cycle each — and are carried out on a bank of identical parallel threads. In any
single cycle, each thread handles at most one function, so the number of functions that can be in progress
during any one cycle is capped by the number of threads; there is no benefit to leaving a thread idle,
but there is also no penalty beyond the deadline.

The functions are not independent. Some functions produce data consumed by others, giving rise to
precedence requirements: whenever one function must finish before another can begin, the dependent function has to
be placed in a strictly later cycle than the function it depends on — being in the same cycle is not enough,
since data finished in a cycle is only available from the next cycle onward. Setup times, function
priorities, and which specific thread runs a function are irrelevant; a function may run on any thread, and only
the cycle it occupies matters.

The deadline is expressed as a maximum number of cycles. Assign every function a cycle within the deadline so
that all precedence requirements hold and no cycle is assigned more functions than there are threads, or
report that the batch cannot be finished by the deadline. (With few threads the per-cycle cap and the
precedence chains pull against each other, so a schedule that respects precedence may still overflow the
cycle capacity and vice versa.)

## Input
First line: four integers n, M, T, m. Each of the next m lines: two integers a b — function a must finish
before function b starts.

## Output
Print `YES` then n integers cycle[1..n] (the cycle of each function, in 1..T); otherwise `NO`.

## Example 1

**Input**
```
4 2 3 3
1 2
1 3
2 4
```

**Output**
```
YES
1 2 2 3
```

## Example 2

**Input**
```
4 1 3 3
1 2
1 3
2 4
```

**Output**
```
NO
```
