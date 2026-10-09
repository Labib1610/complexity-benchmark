# Problem B — Concurrent Calibration Sessions

Time limit: 2 s   Memory limit: 256 MB

## Description
A testing facility operates a set of mechanical actuators and a set of diagnostic sensors. A campaign consists of a series of calibration tests, where each test requires linking exactly one actuator to exactly one sensor. 

To expedite the campaign, tests are grouped into concurrent sessions, numbered 1, 2, 3, and so on. The strict physical constraint is that a single piece of equipment (whether an actuator or a sensor) can only participate in one test per session. Therefore, any two tests that require the same actuator cannot be scheduled in the same session, and any two tests that require the same sensor cannot be scheduled in the same session. Actuators and sensors are separate pools of equipment; an actuator and a sensor are never the same item, even if they share the same numeric ID.

The length of the entire campaign is determined by the number of sessions used. Clearly, if the busiest piece of equipment in the facility is required for $K$ different tests overall, the campaign will require at least $K$ sessions. Your task is to schedule all tests into exactly $K$ sessions. Due to the strict separation between the pool of actuators and the pool of sensors, it is a mathematical guarantee that such a compressed schedule is always possible.

Assign each test a session number from $1$ to $K$ such that no equipment is double-booked during any session. 

## Input
The first line contains three integers $nA$, $nB$, and $m$ ($1 \le nA, nB \le 100000$, $0 \le m \le 400000$), representing the number of actuators, the number of sensors, and the total number of calibration tests, respectively. 

The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le nA$, $1 \le v \le nB$), indicating that a test requires actuator $u$ and sensor $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $i$-th integer is the session number (from $1$ to $K$) assigned to the $i$-th test in the input order. $K$ is the maximum number of times any single piece of equipment is used in the input.

## Example

**Input**
```text
3 3 4
1 1
1 2
2 2
3 3
```

**Output**
```text
YES
1 2 1 1
```
