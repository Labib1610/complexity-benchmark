# Problem B — Intermodal Terminal Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
A major logistics hub is responsible for direct cargo transfers from maritime vessels to railcars. The maritime docking area is divided into 100 zones, each capable of hosting exactly 1,000 vessels. The rail yard is organized into 200 tracks, each accommodating exactly 500 railcars. The daily operations system caps the total number of cargo transfers to exactly four times the facility's maximum total number of maritime vessels.

Transfers occur in discrete, hourly windows. Each maritime vessel has a single active crane, meaning it can discharge no more than one cargo unit per hour. Likewise, each railcar has a single receiving deck, allowing it to take on at most one cargo unit per hour.

The port authority first calculates the maximum number of cargo units associated with any single maritime vessel or railcar. Let this peak volume be $H$. Since the busiest piece of equipment needs $H$ separate hourly windows, the entire transfer process will take a minimum of $H$ hours.

You must allocate exactly one hourly window (an integer from 1 to $H$) to each scheduled cargo transfer. The allocation must ensure all transfers are completed in $H$ hours without any vessel or railcar exceeding its limit of one unit per hour. The structural properties of these direct transfers ensure such a timetable is always achievable.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$, representing the number of maritime vessels, the number of railcars, and the total number of cargo units to transfer. The values of $n_L$ and $n_R$ are at least 1, and $m$ can be as low as 0. The upper limits for these three integers are strictly dictated by the facility's maximum capacities described above.

The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating that a cargo unit must be moved from maritime vessel $u$ to railcar $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ space-separated integers, where the $i$-th integer represents the hourly window (from 1 to $H$) assigned to the $i$-th cargo unit given in the input.

## Example
### Input
```
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```
YES
1 2 1 2 1
```
