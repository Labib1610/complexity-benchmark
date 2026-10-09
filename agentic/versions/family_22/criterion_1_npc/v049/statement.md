# Problem A — Assembly Cycle Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description
A complex assembly involves $n$ distinct modules, numbered $1$ to $n$. Each module requires exactly one operational cycle to complete. During operation, the system provides $M$ concurrent slots per cycle; thus, at most $M$ modules can be active during any single cycle. 

Furthermore, certain modules rely on data feeds from others. When a data feed exists from module $a$ to module $b$, module $b$ cannot become active until the cycle immediately following the one in which module $a$ completes. It is not sufficient for $a$ and $b$ to operate in the same cycle, as the data from $a$ only becomes available after its cycle finishes.

The system operates under a strict deadline of $T$ total cycles. 

Your task is to determine if there exists a valid allocation of cycles to all $n$ modules such that no cycle exceeds the concurrent slot limit, all data feed requirements are strictly respected, and every module is allocated exactly one cycle between $1$ and $T$ inclusive. If such an allocation exists, provide it; otherwise, report that it is impossible.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the following $m$ lines contains two integers $a$ and $b$, indicating a data feed from module $a$ to module $b$.

## Output
Print `YES` then $n$ integers (the cycle assigned to each module $1 \dots n$, in the range $1 \dots T$); otherwise print `NO`.

## Example

### Input
```text
4 2 3 3
1 2
1 3
2 4
```

### Output
```text
YES
1 2 2 3
```
