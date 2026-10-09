# Problem B — Facility Tracks

Time limit: 1 s   Memory limit: 256 MB

The manufacturing plant requires every staff member to be placed on either track 1 or track 2. Certain pairs of staff members have a history of unsafe interactions and are strictly prohibited from being placed on the same track.

You are given the list of unsafe interactions. Your task is to determine if it is possible to assign every staff member a track such that no two individuals involved in an unsafe interaction share a track.

If a valid track assignment can be formed, you must also provide it. When multiple valid configurations exist, you must choose the one whose sequence of track numbers (ordered from staff member 1 to $n$) is the smallest when compared position by position from left to right. 

## Input
The first line contains the staff headcount $n$ and the number of unsafe interaction records $m$. The facility's roster size $n$ ranges from a single person up to a maximum capacity of $200,000$ personnel. The number of logged hazards $m$ can be as low as zero and reaches up to the system limit of $200,000$.

Each of the following $m$ lines contains two integers $u$ and $v$, identifying a pair of staff members who cannot share a track. Staff members are identified by integers from 1 to $n$.

## Output
If the staff cannot be completely assigned under these rules, output a single line with the word NO.

Otherwise, output YES on the first line. On the second line, output $n$ integers representing the track assignments (each either 1 or 2). This sequence must be the smallest valid sequence when compared position by position from left to right.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
