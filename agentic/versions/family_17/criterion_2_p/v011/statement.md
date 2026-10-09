# Problem B — Festival Duet Programming

Time limit: 2 s   Memory limit: 256 MB

## Description
The annual music festival concludes with a grand finale where every invited artist must perform. The organizers have booked two equally sized groups of musicians: vocalists (assigned ID numbers consecutively from $1$ to $q$) and instrumentalists (assigned ID numbers consecutively from $q+1$ to $2q$). The finale's format demands that every single invited artist participates in exactly one duet, which must consist of one vocalist and one instrumentalist.

Due to stylistic differences, a duet can only be formed if the specific vocalist and instrumentalist have previously rehearsed together. The organizers have compiled a catalog of all successful past collaborations. A vocalist and an instrumentalist may only perform together if their specific combination appears in this catalog; unlisted pairings are strictly prohibited. While some musicians might have rehearsed with many different partners, the only goal is selecting a valid set of collaborations such that no one is left out and no one performs twice.

Determine if it is possible to schedule the duets such that every vocalist and every instrumentalist is committed to exactly one performance. If such a comprehensive schedule exists, output one valid configuration. Otherwise, report that a full schedule cannot be formed from the given catalog.

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
