# Microservice Deployment

Time limit: 2 s   Memory limit: 256 MB

You are tasked with deploying a system of $n$ microservices. Each microservice must be assigned to exactly one of 3 available server zones, identified by the integers 1, 2, and 3.

The system contains $m$ unidirectional data streams. Each stream is defined by a pair of 1-based indices $u$ and $v$, indicating that the microservice at index $u$ streams data to the microservice at index $v$. 

To ensure fault tolerance, the deployment must satisfy a strict separation rule for every stream: whenever a microservice $u$ streams data to a microservice $v$, the server zone assigned to $v$ must be strictly different from the server zone assigned to $u$.

Your objective is to determine if at least one deployment configuration can be constructed that satisfies this separation rule for all $m$ streams simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). 
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a unidirectional stream from the microservice at index $u$ to the microservice at index $v$. 

## Output
If no valid deployment configuration can be constructed, output `NO` on a single line.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers representing the zone assignments for microservices 1 through $n$. If there are multiple valid configurations, any of them will be accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```