# Life Support Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
A deep-space habitat relies on an atmospheric processing unit equipped with exactly $q$ oxygen extractors (identified by numbers $1$ through $q$) and exactly $q$ distribution vents (identified by numbers $q+1$ through $2q$).

Following a micro-meteoroid impact, the internal pneumatic network sustained severe damage. Automated diagnostics have compiled a list of all intact pipes. Every intact pipe safely connects a single extractor to a single vent. 

To safely restart the atmospheric processing unit, the station's computer must establish a balanced airflow configuration. A balanced configuration requires that every single extractor routes oxygen to exactly one vent, and every single vent receives oxygen from exactly one extractor. You may only activate pipes that the diagnostics have confirmed as intact. No extractor may be disabled, no vent may be left unpressurized, and no extractor or vent may be involved in more than one activated connection.

If a balanced configuration is achievable, you must output the exact pipe connections to activate. If the intact pipes cannot support a balanced configuration, you must output a failure code so the crew can prepare for evacuation.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of extractors (which is identical to the number of vents) and the total number of intact pipes identified by the diagnostics.
This is followed by $t$ lines, each containing two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that an intact pipe exists between extractor $a$ and vent $b$.

## Output
If the restart sequence can proceed, print `YES` followed by $q$ lines, each containing the two identifiers of an activated connection.
If a balanced configuration is impossible using only the intact pipes, print `NO`.

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
