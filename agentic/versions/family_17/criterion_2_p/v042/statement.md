# Problem B — Full-Capacity Observatory Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
The summit observatory operates a dual-array interferometry system. The system relies on two equally sized hardware collections: primary reflectors and secondary digitizers. The primary reflectors are assigned sequential hardware IDs starting from 1. The secondary digitizers are assigned IDs in the block immediately following the primary reflectors.

Due to microscopic surface imperfections and atmospheric distortions, a primary reflector cannot simply bounce a signal to any digitizer. Calibration tests have produced a definitive catalog of viable optical pathways. Each viable pathway links one specific primary reflector to one specific secondary digitizer. 

To achieve the necessary resolution for the upcoming deep-sky survey, the observatory must run at absolute maximum capacity. A valid survey configuration requires selecting a subset of the viable optical pathways such that every single primary reflector and every single secondary digitizer is utilized exactly once. No piece of hardware can be left idle, and no piece of hardware can participate in more than one active pathway. The total number of viable pathways is often much larger than the number of devices, but only the exact combinations listed in the catalog may be used.

Determine if it is possible to configure the observatory to engage all equipment simultaneously under these strict pairing rules. If a complete configuration exists, provide one. Otherwise, declare that a full capacity configuration is impossible.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).  
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a viable optical pathway between primary reflector $a$ and secondary digitizer $b$.

## Output
If a full capacity configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated pathway. If it is impossible, print `NO`.

## Example

**Input:**
```
3 4
1 4
1 5
2 5
3 6
```

**Output:**
```
YES
1 4
2 5
3 6
```
