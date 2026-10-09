# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate requires a full deployment of its remote assets for the upcoming drill. There are $2q$ assets in the operational pool. The assets numbered $1$ through $q$ operate as controllers. The assets numbered $q+1$ through $2q$ operate as platforms.

During the drill, assets must operate in pairs. A valid operational pair must consist of one controller and one platform, and this specific duo must appear on the pre-approved certification list. 

Your task is to formulate a deployment schedule that activates a specific set of pre-approved pairs. This schedule must ensure that every single asset in the operational pool (all $q$ controllers and all $q$ platforms) is assigned to exactly one active pair. No asset may be left unassigned, and no asset may participate in more than one active pair. 

Evaluate whether the certification list allows for such a comprehensive schedule. If a valid configuration exists, output it; otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (which is also the number of platforms) and the total number of pre-approved pairs.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that controller $a$ and platform $b$ are certified to operate together.

## Output
If a valid deployment schedule can be formed, print `YES` on the first line, followed by $q$ lines each containing the two integers of one activated pair. If no such schedule is possible, print `NO`.

## Example

**Input**
```
3 4
1 4
2 5
3 5
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
