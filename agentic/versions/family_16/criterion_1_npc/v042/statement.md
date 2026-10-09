# Problem A — Album Production

Time limit: 5 s   Memory limit: 256 MB

## Description

An independent record label is finalizing its next compilation album. There are **j** songs to produce, and the studio facility has **m** specialized rooms (such as the vocal booth or the mixing suite).

For each song, the producer has laid out a strict sequence of required recording and editing sessions. Each session must take place in a specific room and takes a predetermined amount of time. The production process must adhere to the following constraints:

- The sessions for any single song must be completed in the exact order specified. A session for a song can only begin after its immediately preceding session has concluded.
- A studio room can only accommodate one session at a time.
- Once a session begins in a room, it must continue without interruption until it is finished.

The label wants to complete the album as soon as possible. Determine the earliest possible time at which all sessions for all songs are completely finished.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of songs and the number of studio rooms, respectively.
The following **j** lines each detail the production sequence for one song. Each line starts with an integer **o**, the number of sessions required for that song. This is followed by **o** pairs of integers `room duration` (1 ≤ room ≤ m, 1 ≤ duration ≤ 1000), indicating the room number and the time needed for each session, in the order they must be performed.
The total number of sessions across all songs will not exceed 50.

## Output

Print a single integer: the earliest possible time at which all songs are completely finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two distinct songs require the identical process: room 1 for 2 units of time, room 2 for 2 units, and room 3 for 2 units. The second song must wait for the first to clear each room, finishing at time 8. In Example 3, the two songs require different rooms, so they can be produced simultaneously, finishing at time 4.
