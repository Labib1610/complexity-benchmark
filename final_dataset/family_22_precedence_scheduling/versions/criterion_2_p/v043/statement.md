# Exhibition Layout

Time limit: 2 s   Memory limit: 256 MB

## Description
You are curating a museum exhibition featuring $n$ distinct historical artifacts, numbered 1 to $n$. The artifacts will be arranged in a single long hallway, occupying $n$ sequential display pedestals from the entrance to the exit. Visitors will view them strictly in this physical sequence.

The museum's historians have provided a list of $m$ narrative constraints. Each constraint specifies two artifacts, $a$ and $b$, and requires that artifact $a$ must be placed on a pedestal that visitors reach before they reach the pedestal holding artifact $b$. This ensures the story builds correctly.

Your task is to assign each of the $n$ artifacts to exactly one of the $n$ pedestals such that every narrative constraint is satisfied. Sometimes, the historians might provide a contradictory set of constraints that cannot all be met simultaneously (for example, if a chain of rules logically requires an artifact to be encountered before itself). If a valid physical sequence exists across the pedestals, you must provide one. Otherwise, you must declare that the layout is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of artifacts and the number of narrative constraints.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that artifact $a$ must be placed closer to the entrance than artifact $b$.

## Output
If a valid arrangement is possible, print `YES` on the first line, followed by a second line containing a sequence of $n$ integers. This sequence must list the artifact identifiers in order from the entrance to the exit. If there are multiple valid arrangements, any one will be accepted.
If no such arrangement is possible, print `NO`.

## Example

### Input
```text
4 4
1 2
1 3
2 4
3 4
```

### Output
```text
YES
1 2 3 4
```
