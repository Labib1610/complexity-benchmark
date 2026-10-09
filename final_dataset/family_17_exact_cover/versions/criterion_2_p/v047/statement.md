# Complete Asset Synchronization Roster

Time limit: 2 s   Memory limit: 256 MB

## Description
The agency manages an inventory of assets divided into two equal-sized groups: controllers and platforms. There are $q$ controllers, assigned consecutive identification numbers from $1$ to $q$. There are $q$ platforms, assigned consecutive identification numbers from $q+1$ to $2q$.

Due to hardware compatibility, an asset from the controller group can only synchronize with an asset from the platform group if their specific pairing is officially certified. You are provided with a list of $t$ certified pairings. 

Furthermore, the directorate guarantees that all certified pairings $(a, b)$ in the list strictly adhere to the following safety protocols:
- **Index Summation Bound:** The sum of their identification numbers is strictly greater than $q+1$ and does not exceed $3q$.
- **Index Separation Bound:** The absolute difference between their identification numbers is at least $1$ and at most $2q-1$.

Your task is to formulate a complete synchronization roster for an upcoming operation. A valid roster must select a subset of the officially certified pairings such that every single controller and every single platform is committed to exactly one selected pairing. No asset may be left unassigned, and no asset may participate in more than one selected pairing. 

Determine if such a comprehensive roster can be formed. If it is possible, output the roster; otherwise, indicate that full synchronization is unachievable.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100,000$, $0 \le t \le 400,000$), representing the number of controllers (and the number of platforms) and the number of certified pairings, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a certified pairing between controller $a$ and platform $b$.

## Output
If a complete synchronization roster is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two identification numbers of a selected pairing. If there are multiple valid rosters, any of them is acceptable.
If no such roster can be formed, print `NO`.

## Example

### Input
```
2 3
1 3
1 4
2 3
```

### Output
```
YES
1 4
2 3
```
