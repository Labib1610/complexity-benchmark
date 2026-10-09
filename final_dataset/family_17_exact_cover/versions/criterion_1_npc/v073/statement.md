# Orbital Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The interstellar colonization initiative has finalized a pool of $3q$ specialists, each assigned a unique ID from $1$ to $3q$. The mission requires deploying these specialists into orbital habitats.

Each habitat is engineered to support exactly three specialists. Due to the extreme psychological and technical demands of the mission, arbitrary groupings are not permitted. The evaluation board has conducted extensive simulations and identified a master roster of $t$ viable habitat crews. Each viable crew consists of three specific specialists who have demonstrated perfect synergy.

The mission director must finalize a deployment manifest by selecting a subset of these viable crews. The final manifest must adhere to two absolute constraints:
1. A specialist can only be assigned to a single habitat. Assigning an individual to multiple crews will result in scheduling conflicts and is strictly forbidden.
2. Every single specialist in the pool must be assigned to a habitat. Leaving anyone behind compromises the mission objectives.

Your task is to determine whether it is possible to select a set of viable crews from the master roster such that all $3q$ specialists are assigned exactly once. If a valid deployment manifest can be formed, you must also provide the chosen crews.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of three specialists who form a viable crew.

## Output
If a valid deployment manifest exists, print `YES`, followed by $q$ lines each containing the three specialist IDs of one chosen crew.
Otherwise print `NO`.

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
