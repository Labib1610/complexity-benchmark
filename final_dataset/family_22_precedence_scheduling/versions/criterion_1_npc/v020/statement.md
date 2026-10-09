# Problem A — Museum Exhibit Curation

Time limit: 5 s   Memory limit: 256 MB

## Description
A museum is planning a new linear exhibit featuring a collection of ancient relics. The exhibit is housed in a long corridor divided into a sequence of distinct rooms. Visitors will walk through these rooms sequentially, starting at the first room and ending at the final room.

There are a limited number of rooms available, and to avoid overcrowding the displays, each room can hold at most a specific maximum number of relics. All display pedestals within a room are identical, and the exact placement of a relic within a room does not matter. The only thing that matters is which room a relic is assigned to.

The curator has established a set of narrative rules for the exhibit. Certain relics provide essential historical context for others. If relic $a$ provides context for relic $b$, then visitors must see relic $a$ in a room strictly before the room containing relic $b$. Placing them in the same room is not allowed, because visitors might look at them in the wrong order. 

Given the total number of relics, the maximum number of relics each room can hold, the total number of rooms, and the curator's narrative rules, determine if it is possible to assign every relic to a room such that all capacity limits and narrative rules are satisfied. If it is possible, provide a valid room assignment for each relic. (With limited room capacity, a layout that satisfies all narrative rules might require placing too many relics in a single room, and resolving this crowding might push relics past the final available room.)

## Input
First line: four integers $n, M, T, m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — relic $a$ must be placed in a room strictly before relic $b$.

## Output
Print `YES` then $n$ integers (the room number of each relic, in $1..T$); otherwise `NO`.

### Example 1

**Input**
```text
4 2 3 3
1 2
1 3
2 4
```

**Output**
```text
YES
1 2 2 3
```
