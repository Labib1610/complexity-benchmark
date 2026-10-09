# Optical Network Saturation

Time limit: 2 s   Memory limit: 256 MB

## Description
You are configuring the hardware topology for a new optical switch. The switch contains exactly $q$ transmitting diodes (numbered $1$ through $q$) and exactly $q$ receiving sensors (numbered $q+1$ through $2q$).

During the initial calibration, a diagnostic tool tested all possible physical alignments and produced a discrete list of viable optical pathways. Each viable pathway allows data to flow from one specific transmitting diode to one specific receiving sensor.

Your task is to determine if the switch can achieve full saturation. Full saturation requires selecting a subset of the viable pathways such that every single transmitting diode is utilized by exactly one selected pathway, and every single receiving sensor is utilized by exactly one selected pathway. No diode or sensor may be left isolated, nor may any participate in more than one pathway. You are restricted to using only the pathways validated during the calibration phase.

If full saturation is achievable, you must output the exact configuration of pathways to be activated. If it is impossible to satisfy these requirements using only the viable pathways, you must output a specific rejection signal so the configuration process can be aborted.

## Input
The first line of the input contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of transmitting diodes (which is equal to the number of receiving sensors) and the total number of viable optical pathways identified during calibration.
This is followed by $t$ lines, each containing two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that a viable optical pathway exists between transmitting diode $a$ and receiving sensor $b$.

## Output
If the switch can achieve full saturation, print `YES` on the first line. Following this, print $q$ lines, each containing the two identifiers (the diode and the sensor) of a pathway selected for the configuration.
If full saturation is impossible from the given viable pathways, print `NO`.

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
