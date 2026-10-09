# Problem A — Synthesizer Protocol Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

A synthetic biology lab is programming an automated synthesizer to execute a batch of parallel reactions. The synthesizer must perform exactly **k** parallel reactions. To do this, the lab relies on three separate inventories, each containing exactly **k** distinct resources:

- **k** genetic promoters
- **k** binding domains
- **k** terminator sequences

Each resource in an inventory is assigned a unique integer identifier starting from 1 up to **k**.

A single reaction is formed by combining exactly one promoter, one binding domain, and one terminator sequence. Due to biochemical folding constraints, only certain specific triples of these resources will fold correctly. The researchers have compiled a database of all functional triples.

A complete protocol requires selecting exactly **k** functional triples from the database such that every single promoter, binding domain, and terminator sequence from the inventories is incorporated into exactly one reaction. No resource may be left unused, and no resource may be reused.

Determine whether it is possible to configure a complete protocol, and if so, report the triples to be used.

## Input

The first line contains two integers **k** and **t**: the number of items in each resource inventory, and the total number of functional triples recorded in the database. 

The synthesizer physically contains a 22-slot reaction block. Thus, the number of parallel reactions **k** is at least 1 and at most the number of slots in the block. The database might be empty, or it might contain every conceivable combination formed by picking one promoter, one binding domain, and one terminator from the **k** available of each type. Thus **t** ranges from 0 up to this theoretical maximum.

Each of the next **t** lines contains three integers **e**, **s**, **p**, representing a functional triple consisting of promoter **e**, binding domain **s**, and terminator sequence **p**. Resource identifiers are always positive integers that do not exceed the number of parallel reactions being performed. No triple is listed more than once in the database.

## Output

If a complete protocol of **k** reactions exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `e s p` of a chosen triple. Any selection that uses every promoter, binding domain, and terminator sequence exactly once will be accepted. You may print the chosen triples in any order.

If no complete protocol exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both functional triples require binding domain 1. Consequently, binding domain 2 can never be utilized, making a complete protocol impossible.
