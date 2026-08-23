# Environment Isolation

Time limit: 1 s   Memory limit: 256 MB

A cloud architecture upgrade requires migrating $n$ microservices into two newly provisioned virtual environments, designated as Environment 1 and Environment 2. Every microservice must be deployed into exactly one of these two environments.

During testing, engineers discovered $m$ critical interference issues. Certain pairs of microservices share hardcoded dependencies; if deployed into the same virtual environment, they will create race conditions and fail. To ensure system stability, any two microservices involved in an interference issue must be strictly separated into different environments.

You must evaluate whether a complete deployment is possible under these restrictions. If the migration can proceed, you must provide the deployment plan. Because the deployment script processes services in numerical order, if multiple valid plans exist, you must provide the one that is lexicographically smallest when written as a sequence of environment assignments.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of microservices and the number of interference issues, respectively.
The following $m$ lines each contain two integers $u$ and $v$, indicating that microservice $u$ and microservice $v$ interfere with each other. Microservices are identified by integers from 1 to $n$.

## Output
If a conflict-free deployment is impossible, print `NO` on a single line.
If it is possible, print `YES` on the first line. On the second line, print $n$ integers (each being 1 or 2) representing the environment assigned to each microservice, from 1 to $n$. This sequence must be the lexicographically smallest valid plan.

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