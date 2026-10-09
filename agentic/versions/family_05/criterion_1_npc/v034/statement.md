# Problem A — Vault Configurations

Time limit: 5 s   Memory limit: 256 MB

## Description

You are attempting to open a high-security vault. The vault mechanism relies on a sequence of configurations applied to a digital lock. The lock features three separate dials (the left dial, the center dial, and the right dial). Each dial can be set to an integer value from 1 to **k**.

You have intercepted a list of stable configurations. A stable configuration is a specific state of the three dials that does not trigger the alarm. 

To successfully open the vault, you must select exactly **k** configurations from the intercepted list. However, the vault's tumbler system requires a unique distribution of stress: across your chosen **k** configurations, every value from 1 to **k** must be used exactly once on the left dial, exactly once on the center dial, and exactly once on the right dial. 

Determine if such a selection of **k** configurations exists. If it does, report one valid set.

## Input

The first line contains two integers **k** and **t**. Due to the mechanical constraints of the vault's internal gears, the maximum dial value **k** is at least 1 and at most 22. The total number of intercepted stable configurations **t** ranges from 0 up to the maximum possible number of unique dial states (which is **k** cubed).

Each of the next **t** lines contains three integers **l**, **c**, and **r**, representing the left, center, and right dial values of a stable configuration. Every dial value is guaranteed to be a valid setting from 1 to **k** inclusive. No configuration is listed more than once.

## Output

If a valid selection of **k** configurations can be chosen, print `YES` on the first line. Then, print **k** lines, each containing the three dial values `l c r` of one chosen configuration. Any selection that meets the vault's mechanical requirements is accepted. The configurations may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both stable configurations require the center dial to be set to 1. Consequently, the value 2 can never be applied to the center dial in any selection, making it impossible to satisfy the vault's conditions.
