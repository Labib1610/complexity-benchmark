# Datacenter Synchronization Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A computing facility houses $2q$ processing units divided into two equal banks. Bank Alpha contains units $1$ through $q$, and Bank Beta contains units $q+1$ through $2q$.

Between these two banks, $t$ physical data links have been installed. Each data link connects exactly one unit from Bank Alpha to exactly one unit from Bank Beta. 

The activation of these links is governed by strict electrical constraints. If a processing unit is subjected to more than one active data link simultaneously, it will immediately trigger a thermal fault. Conversely, any processing unit that is left with zero active data links will remain completely isolated from the system's synchronization grid.

Your task is to determine whether there is a combination of active data links that successfully synchronizes the entire facility. Specifically, you must find a subset of the $t$ links that satisfies all electrical constraints without leaving any unit isolated. If such a configuration exists, you must provide the exact list of links to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100,000$, $0 \le t \le 400,000$), representing the number of processing units in each bank and the number of installed data links, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that a data link exists between Bank Alpha unit $a$ and Bank Beta unit $b$.

## Output
If a valid configuration is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two units of a chosen data link to activate. If multiple valid configurations exist, you may output any of them. If no such configuration is possible, print `NO`.

## Example

### Input
```text
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```text
YES
1 4
2 6
3 5
```
