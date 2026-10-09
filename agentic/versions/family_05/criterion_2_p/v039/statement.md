# Airline Schedule (Fixed Certifications)

Time limit: 2 s   Memory limit: 256 MB

## Description

An airline must assign exactly **k** daily flights. The schedule requires coordinating three resources, each containing exactly **k** members:

- **k** pilots, numbered 1..k,
- **k** aircraft, numbered 1..k,
- **k** flight paths, numbered 1..k.

A valid flight assignment consists of exactly one pilot, one aircraft, and one flight path. You are provided with a list of technically feasible combinations `(x, y, z)` based on weather, maintenance, and pilot scheduling rules.

Due to strict regulatory requirements, **each pilot is certified to fly exactly one specific aircraft, and no two pilots are certified on the same aircraft**. Consequently, the pilot-to-aircraft pairings are fixed in advance. The central task is to allocate the flight paths.

Select exactly **k** feasible combinations so that every pilot, every aircraft, and every flight path is utilized in **exactly one** assigned flight. Determine whether such a schedule is possible, and if so, output one valid set of flights.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of each resource and the number of feasible combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a feasible flight combination of pilot **x**, aircraft **y**, and flight path **z**. No combination is listed more than once. Consistent with the certification rules, for each pilot, every listed combination uses the same aircraft, and different pilots use different aircraft.

## Output

If a valid schedule of **k** flights exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one scheduled flight (in any order). Any valid schedule is accepted.

If no valid schedule exists, print `NO`.

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

## Note

In Example 2, both pilots' only feasible flight path is 1, so flight path 2 can never be covered.
