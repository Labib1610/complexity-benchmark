# Orbital Thermal Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
The orbital station requires a complete thermal synchronization of its exterior panels. There are $2q$ panels in total, uniquely identified by numbers from 1 to $2q$.

To synchronize the station, panels must be paired up by installing thermal conduits. Each conduit connects exactly two panels. A conduit can only be installed if it is listed in the pre-approved safety manifest, which contains $t$ permissible pairs. Due to the station's geometry, every pair in the manifest connects one sun-facing panel (whose identifier is at most $q$) with one deep-space-facing panel (whose identifier is strictly greater than $q$).

A complete synchronization demands that every single panel from 1 to $2q$ is connected to exactly one installed conduit. No panel may be left without a conduit, and no panel may be connected to more than one.

You must determine whether it is possible to achieve a complete synchronization using only the pairs from the manifest. If it can be done, output the pairs to install; otherwise, state that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of panels and the number of permissible pairs, respectively.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a permissible pair between panel $a$ and panel $b$.

## Output
If a complete synchronization is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two panel identifiers of an installed conduit. If it is not possible, print `NO`.

## Example

**Input**
```text
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
