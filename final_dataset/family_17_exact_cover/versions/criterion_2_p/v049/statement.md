# Problem B — Festival Duet Programming

Time limit: 2 s   Memory limit: 256 MB

## Description
The festival organizers have compiled a comprehensive catalog of past musical collaborations. Each entry in this catalog links one vocalist to one instrumentalist, indicating that their stylistic differences have been resolved and they are capable of performing together. The invited musicians are identified by numbers from $1$ to $2q$. The first half of these numbers, from $1$ to $q$, represent vocalists. The second half, from $q+1$ to $2q$, represent instrumentalists.

Any performance at the grand finale must strictly adhere to this catalog. Specifically, a performance must be a duet consisting of one vocalist and one instrumentalist whose specific combination is listed in the organizers' records. Unlisted pairings are prohibited. Furthermore, the format of the finale imposes strict participation rules: no musician may perform more than once, and no musician may be left out.

Your task is to determine whether a valid set of collaborations can be selected from the catalog to satisfy the finale's format. You must find a schedule where every single invited artist is committed to exactly one performance, or report that this is impossible based on the provided records.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ is the number of vocalists (and also the number of instrumentalists) and $t$ is the number of recorded collaborations.

The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a vocalist $a$ and an instrumentalist $b$ who are allowed to perform together.

## Output
If a complete schedule is possible, print `YES` on the first line, then output $q$ lines each containing the two ID numbers of a scheduled duet. If it is impossible, print `NO`.

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
