# Problem B — Event Organization (Fixed Kitchens)

Time limit: 2 s   Memory limit: 256 MB

## Description

A festival must organize **k** complete culinary events. There are three groups, each with exactly **k** members:

- **k** chefs (group X), numbered 1..k,
- **k** kitchens (group Y), numbered 1..k,
- **k** menus (group Z), numbered 1..k.

An event consists of exactly one chef, one kitchen, and one menu. You are given a list of allowed combinations `(x, y, z)`.

In this festival **each chef is assigned to exactly one kitchen, and no two chefs share the same kitchen** — so the chef-to-kitchen pairing is already fixed. The only thing left to decide is the menus.

Choose exactly **k** allowed combinations so that every chef, every kitchen, and every menu is used in **exactly one** chosen event. Determine whether this is possible, and if so report one valid set of events.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. For each chef, every listed combination uses the same kitchen, and different chefs use different kitchens.

## Output

If a valid selection of **k** events exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen event (in any order). Any valid selection is accepted.

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

This is the same event-organization problem as Problem A. The only difference is the promise that each chef's kitchen is fixed and all distinct, which leaves only the menu choice. In Example 2 both chefs' only allowed menu is 1, so menu 2 can never be covered.
