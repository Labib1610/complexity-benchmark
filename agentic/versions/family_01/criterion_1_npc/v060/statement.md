# Artifact Curation

Time limit: 2 s   Memory limit: 256 MB

You are organizing a special exhibition for a museum featuring a collection of rare historical artifacts. The museum has designated exactly three separate climate-controlled display halls (labeled 1, 2, and 3) to house this collection. 

Before the exhibition opens, the conservation team conducted a chemical analysis of the artifacts. They discovered that certain pairs of items emit trace gases that will degrade each other over time if they share the same enclosed airspace. To prevent irreversible damage, you must ensure that no two reactive artifacts are placed in the same display hall. 

Every artifact must be assigned to exactly one of the three halls. If the conservation constraints make it impossible to display the entire collection safely across the three halls, the exhibition plans must be canceled. 

Your task is to determine a safe placement for all the artifacts. If a safe arrangement exists, you must provide one. Otherwise, report that the collection cannot be displayed under these conditions.

## Input
The first line contains two integers $n$ and $m$ — the number of artifacts and the number of reactive pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The artifacts are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of artifacts that are reactive.

## Output
If there is no way to assign the artifacts to the display halls without causing a reaction, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $h_1, h_2, \dots, h_n$ (each in {1, 2, 3}), where $h_i$ is the display hall assigned to artifact $i$. If there are multiple safe assignments, any safe assignment is accepted.

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
