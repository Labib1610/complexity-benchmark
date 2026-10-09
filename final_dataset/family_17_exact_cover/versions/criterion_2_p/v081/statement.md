# Problem B — Telemetry Drill Initialization

Time limit: 2 s
Memory limit: 256 MB

## Description
The remote segment contains a total of $2q$ hardware modules. Half of these modules (numbered $1$ through $q$) are designated as signal originators. The remaining half (numbered $q+1$ through $2q$) are designated as signal endpoints.

A valid telemetry link always incorporates exactly one originator and exactly one endpoint. You are given a roster of $t$ tested links that are known to function correctly without interference. 

Your objective is to designate a subset of these tested links for the upcoming drill. The drill requires absolute participation: every single module out of the $2q$ total must be incorporated into exactly one designated link. No module may participate in more than one link, and no module may be excluded.

Determine if there is a valid subset of links that satisfies this absolute participation requirement. If so, output the specific links to be designated.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of modules and the number of tested links, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a tested link between originator $a$ and endpoint $b$.

## Output
If a valid designation exists, print `YES` on the first line, followed by $q$ lines each containing the two module identifiers for a designated link in your selection. If no such designation is possible, print `NO`.

## Example
### Input
```text
3 4
1 4
2 5
3 5
2 6
```

### Output
```text
YES
1 4
3 5
2 6
```
