# The Royal Banquet (Fixed Chairs)

Time limit: 2 s   Memory limit: 256 MB

## Description

A royal banquet requires organizing a grand feast. There are three groups of items, each containing exactly **k** elements:

- **k** nobles, numbered starting from 1,
- **k** ancestral chairs, numbered starting from 1,
- **k** silver platters, numbered starting from 1.

A serving arrangement consists of exactly one noble, one ancestral chair, and one silver platter. You are provided with a list of acceptable arrangements `(x, y, z)`.

By ancient tradition, each noble is permitted to sit in exactly one specific ancestral chair, and no two nobles claim the same chair. The noble-to-chair association is therefore already established. The only remaining task is to distribute the silver platters.

You must choose exactly **k** acceptable arrangements so that every noble, every ancestral chair, and every silver platter is included in **exactly one** chosen arrangement. Determine whether such a selection is possible, and if so, report one valid set of arrangements.

## Input

The first line contains two integers **k** and **t**. 
The integer **k** represents the size of each group. The grand hall is built with exactly twenty wings, each containing sixty ancestral chairs, so **k** is at least 1 and at most the total capacity of these wings.
The integer **t** represents the number of acceptable arrangements. It is at least 0, and at most the total number of possible pairs consisting of one noble and one silver platter.

Each of the next **t** lines contains three integers **x**, **y**, and **z**, representing an acceptable arrangement of a noble, an ancestral chair, and a silver platter. All identifiers are positive integers that do not exceed the group size **k**. No arrangement is listed more than once. For each noble, every listed arrangement features the same ancestral chair, and different nobles are associated with different chairs.

## Output

If a valid selection of **k** arrangements exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen arrangement (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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

This is similar to a general triplet selection problem, but with the crucial guarantee that each noble's chair is fixed and distinct. This leaves only the silver platter as the flexible choice. In Example 2, both nobles only have acceptable arrangements involving platter 1, which means platter 2 can never be distributed.
