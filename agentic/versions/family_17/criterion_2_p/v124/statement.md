# Problem B — Relic Installation Module

Time limit: 2 s   Memory limit: 256 MB

## Description
The museum's upcoming grand opening requires a strict three-stage preparation process. 

**Stage 1:** Conservators conduct rigorous environmental testing on $q$ historical relics (assigned IDs $1$ through $q$) and $q$ climate-controlled vitrines (assigned IDs $q+1$ through $2q$). They produce a registry of all safe combinations, where a specific relic's structural needs are met by a specific vitrine's humidity controls.

**Stage 2:** The logistics software—which you are developing—must process this registry to generate a comprehensive assignment plan. The exhibition's design mandates that every single relic is displayed and every vitrine is utilized. A relic can only be placed in a vitrine if they are listed as a safe combination in the registry. Furthermore, each vitrine can hold at most one relic, and each relic must go into exactly one vitrine.

**Stage 3:** If your module successfully generates a plan, the installation crew will use your output to physically mount the relics and lock the vitrines. If your module determines that no such comprehensive assignment plan is possible, the entire exhibition must be redesigned by the board of directors.

Your task is to implement the software module for Stage 2.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of relics (which is also the number of vitrines) and the number of safe combinations in the registry, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that relic $a$ and vitrine $b$ form a safe combination.

## Output
If your module can generate a comprehensive assignment plan, print `YES` on the first line, followed by $q$ lines each containing the two IDs of a paired relic and vitrine in your plan. If the board of directors must redesign the exhibition because no valid plan exists, print `NO`.

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
