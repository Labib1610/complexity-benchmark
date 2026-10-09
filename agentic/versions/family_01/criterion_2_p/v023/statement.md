# Orbital Payload Configuration

Time limit: 1 s   Memory limit: 256 MB

An orbital platform is being fitted with $n$ sensory modules, numbered 1 to $n$. Each module must be wired to one of two redundant power buses, labeled 1 and 2.

Certain pairs of modules generate electromagnetic interference if they draw power from the same bus. You are provided with $m$ such interfering pairs. Your task is to determine if it is possible to assign every module to a bus such that no interfering pair shares a bus.

## Input
The first line contains two integers: the number of modules $n$ and the number of interfering pairs $m$. The platform requires at least a single module to operate, and its chassis accommodates a strict upper limit of two hundred thousand modules. The diagnostic system can register anywhere from a minimum of zero up to a maximum of two hundred thousand interference pairs.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that module $u$ and module $v$ interfere with each other.

## Output
If there is no way to safely wire all modules, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers (each `1` or `2`) representing the bus assignment for modules 1 through $n$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
