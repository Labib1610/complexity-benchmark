# Problem B — Museum Exhibition Layout

Time limit: 2 s   Memory limit: 256 MB

## Description
The museum is setting up a new exhibition wing. The inventory includes $q$ historical artifacts, assigned identification numbers $1$ through $q$, and $q$ preservation cabinets, assigned identification numbers $q+1$ through $2q$.

To be exhibited, an artifact must be placed inside a preservation cabinet. However, due to varying humidity and structural requirements, an artifact can only be stored in a cabinet if the two have been verified as a safe match. You will be provided with the complete registry of all verified artifact-cabinet pairs.

The exhibition requires a layout where no artifact is left in storage and no cabinet is left empty. Furthermore, each artifact can be assigned to only one cabinet, and any single cabinet can house at most one artifact at a time. 

Determine if a layout meeting these exhibition requirements is possible. If it can be done, provide the list of placements to be made. Otherwise, indicate that the inventory cannot be fully exhibited under the current safety matches.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of artifacts (and of cabinets) and the number of verified pairs, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that artifact $a$ and cabinet $b$ are a verified match.

## Output
If a valid layout is possible, print `YES` on the first line, followed by $q$ lines each containing the two identification numbers of a paired artifact and cabinet in your layout. If it is impossible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
1 5
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
