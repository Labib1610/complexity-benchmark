# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
During the upcoming directorate drill, the entire remote hardware segment must be activated to stress-test the local power grid. The hardware inventory contains $q$ controllers, assigned identification numbers $1$ through $q$, and $q$ platforms, assigned identification numbers $q+1$ through $2q$.

To operate, a controller must be hardware-linked to a platform. However, due to firmware discrepancies, a link can only be established if the specific controller and platform have been pre-certified to communicate. You will be provided with the log of all pre-certified hardware pairs.

The drill requires establishing a configuration of active links such that no controller or platform is left idle. Furthermore, to avoid electrical faults, a single piece of hardware cannot support more than one active link at a time. 

Determine if a configuration meeting these operational limits is possible. If it can be done, provide the list of active links to be established. Otherwise, indicate that the inventory cannot be fully utilized under the current certifications.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (and platforms) and the number of pre-certified pairs, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ are certified to communicate.

## Output
If a valid configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two identification numbers of an active link in your configuration. If it is impossible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
1 5
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
