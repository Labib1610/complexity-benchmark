# Problem B — Festival Showcase

Time limit: 2 s   Memory limit: 256 MB

## Description

A film festival will showcase **k** directors, **k** films, and **k** screening rooms. The directors are numbered 1..k, the films are numbered 1..k, and the screening rooms are numbered 1..k.

Each director has submitted exactly one film, and no two directors submitted the same film. The organizers have collected a list of acceptable scheduling configurations, each specifying a director, their film, and a screening room.

The festival must select exactly **k** of these configurations. A valid selection must feature every director, every film, and every screening room exactly once. Determine whether such a selection is possible, and if so, report one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of directors (which is also the number of films and screening rooms) and the number of acceptable configurations.

Each of the next **t** lines contains three integers **d**, **f**, **s** (1 ≤ d, f, s ≤ k), representing an acceptable configuration of a director, a film, and a screening room. No configuration is listed more than once. Because each director submitted exactly one unique film, every configuration involving a given director will always list the same film, and different directors will always be listed with different films.

## Output

If a valid selection of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three integers `d f s` of one chosen configuration (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
