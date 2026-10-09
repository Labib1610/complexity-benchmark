# Problem B — Complete Neutralization Protocol

Time limit: 2 s
Memory limit: 256 MB

## Description
A chemical disposal facility needs to neutralize a stockpile of hazardous reagents. The inventory consists of two equally sized groups: $q$ acidic compounds and $q$ alkaline compounds. The acidic compounds are assigned identification numbers from $1$ to $q$, and the alkaline compounds are assigned identification numbers from $q+1$ to $2q$.

To achieve neutralization, the facility must combine one acidic compound with one alkaline compound. However, due to volatile secondary reactions, not all combinations are safe. The facility's chemists have tested the compounds and produced a definitive catalog of safe acid-alkali pairs. Any combination not explicitly listed in this catalog is strictly prohibited. The catalog may list the same safe combination multiple times; such repetitions are incidental and do not change whether a combination is safe.

The disposal protocol mandates a complete cleanout of the inventory. You must determine if it is possible to pair up the reagents such that:
- Every acidic compound is used in exactly one pair.
- Every alkaline compound is used in exactly one pair.
- Every formed pair is listed in the safe catalog.

Because there are $q$ acids and $q$ alkalis, a complete cleanout will form exactly $q$ pairs and leave no compounds behind. Decide whether the catalog of safe pairs admits such a complete one-to-one neutralization of all reagents. If it does, output one such valid pairing configuration; otherwise, report that a complete cleanout is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of acidic compounds (which is also the number of alkaline compounds) and the number of safe combinations in the catalog.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that acidic compound $a$ can be safely combined with alkaline compound $b$.

## Output
If possible, print `YES` then $q$ lines each with the two identification numbers of one chosen pair; otherwise `NO`.

## Example 1

### Input
3 4
1 4
1 5
2 6
3 5

### Output
YES
1 4
3 5
2 6

## Example 2

### Input
2 2
1 3
2 3

### Output
NO
