# Problem B — Festival Duet Programming

Time limit: 2 s   Memory limit: 256 MB

## Description
The annual music festival organizers are managing a roster of exactly $2q$ invited artists. These individuals are split evenly between two distinct roles: vocalists are assigned identification numbers from $1$ up to $q$, while instrumentalists hold identification numbers from $q+1$ up to $2q$.

The organizers have compiled a comprehensive catalog of past rehearsal sessions. Each entry in this catalog documents a specific vocalist and a specific instrumentalist who have successfully practiced a joint act together. For the upcoming finale, any joint act must strictly be chosen from this catalog of approved collaborations; unlisted combinations are prohibited. 

The grand finale demands that every single invited artist takes the stage. Your task is to determine whether a set of joint acts can be selected from the catalog such that every vocalist and every instrumentalist is committed to exactly one performance. If a schedule covering all $2q$ artists exactly once can be arranged, you must output the chosen acts. If no such arrangement exists, you must report that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ is the number of vocalists (and also the number of instrumentalists) and $t$ is the number of recorded catalog entries.

The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a vocalist $a$ and an instrumentalist $b$ who have practiced together.

## Output
If a complete schedule is possible, print `YES` on the first line, then output $q$ lines each containing the two ID numbers of a scheduled joint act. If it is impossible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
2 4
2 5
3 6
```

### Output
```text
YES
1 4
2 5
3 6
```

## Example 2

### Input
```text
2 2
1 3
2 3
```

### Output
```text
NO
```
