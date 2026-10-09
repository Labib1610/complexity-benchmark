# Problem A — Curating the Grand Exhibition

Time limit: 5 s   Memory limit: 256 MB

## Description
A prestigious museum is preparing a new grand exhibition. The collection designated for this event consists of exactly 3q unique historical artifacts, which are numbered consecutively from 1 to 3q.

The exhibition space is divided into a series of display pavilions, and each pavilion is custom-built to showcase exactly three artifacts. The head curator is notoriously strict about thematic coherence. Over the years, the curatorial team has compiled a catalog of harmonizing triads—specific groupings of exactly three artifacts that complement each other perfectly in terms of history, style, and scale. An artifact can belong to multiple harmonizing triads in the catalog, but a pavilion can only be set up using one of these pre-approved triads. No undocumented combinations are allowed, regardless of how appealing they might seem.

The museum director has mandated that every single artifact in the designated collection must be displayed. Furthermore, because each artifact is unique, it cannot physically appear in more than one pavilion. A complete exhibition layout must therefore assign the entire collection into a selection of these pre-approved triads, leaving no artifact in storage and placing no artifact in multiple pavilions. 

Your task is to determine if it is possible to select a set of harmonizing triads from the catalog that perfectly organizes all 3q artifacts under these strict rules. If such an arrangement exists, provide the selection of triads. If the catalog's combinations cannot accommodate the entire collection, report that it is impossible. (Note that simply having a large number of triads does not guarantee a valid layout, while a very small catalog might still perfectly arrange the collection.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the following **t** lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), representing the ID numbers of the artifacts that make up one allowed triad.

## Output
If a valid exhibition layout can be formed, print `YES` on the first line. Then, output **q** lines, each containing the three artifact IDs of a chosen triad.
If no such layout is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
