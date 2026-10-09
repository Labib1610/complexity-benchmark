# Problem A — Gallery Curation

Time limit: 5 s   Memory limit: 256 MB

## Description

A gallery is planning its grand opening. In the inventory, there are **k** sculptures, **k** pedestals, and **k** security sensors. All items are indexed from 1 to **k** within their respective categories.

To set up a display station, the curator must assemble a triad consisting of one sculpture, one pedestal, and one sensor. However, due to weight limits and sensor ranges, only specific triads are stable. A catalog of stable triads is provided.

The curator wants to deploy all the items from the inventory to create exactly **k** display stations. A station cannot function if it is missing any of its three components, and physical components cannot be split or shared among multiple stations. 

Determine if it is possible to organize the gallery in this manner. If it can be done, provide the list of triads to be built.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the inventory size for each category and the number of stable triads in the catalog.
Following this are **t** lines. Each line provides three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), indicating that sculpture **x**, pedestal **y**, and sensor **z** can be combined into a stable triad. No triad is repeated in the catalog.

## Output

If the gallery can be fully organized, output `YES` on the first line. Then, output **k** lines, each detailing the sculpture, pedestal, and sensor of a chosen triad. Any valid arrangement that incorporates every item from the inventory is acceptable, and the triads can be listed in any sequence.

If such an arrangement cannot be achieved, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

In Example 2, both stable triads require pedestal 1, meaning pedestal 2 will inevitably be left unused, making a complete deployment impossible.
