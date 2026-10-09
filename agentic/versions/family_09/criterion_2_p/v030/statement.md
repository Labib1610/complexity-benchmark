# Safe Process Allocation

Time limit: 2 s
Memory limit: 256 MB

## Description

A distributed computing system contains **n** processes (numbered 1 to **n**) and **m** known data races. Each data race occurs when two specific processes attempt to access the same memory resource simultaneously.

The system execution is governed by an alternating global clock cycle, divided strictly into a "Tick" phase and a "Tock" phase. The architecture guarantees that every data race occurs exclusively between a process scheduled during the Tick phase and a process scheduled during the Tock phase. Consequently, there are no data races between any two processes that operate within the same phase. (The specific phase assignments are internal and not provided to you, but the system is guaranteed to adhere to this structural property).

A collection of processes is deemed **safe** if no two processes in the collection share a data race.

Given a target capacity **k**, determine whether a safe collection of exactly **k** processes can be deployed. If such a collection exists, you must report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 100000, 0 ≤ **m** ≤ 400000, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a data race between process **u** and process **v**. No data race is listed twice, and the connections are guaranteed to strictly follow the alternating clock phase structure described above.

## Output

If a safe collection of **k** processes exists, print `YES` on the first line, then on the second line print **k** distinct process numbers forming such a collection, separated by spaces. Any collection in which no two processes have a data race is accepted.

If no such collection exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```
