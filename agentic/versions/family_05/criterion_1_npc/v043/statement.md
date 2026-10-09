# Problem A — Processor Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description

A system manages three independent memory banks: bank A, bank B, and bank C. Each bank contains exactly **k** registers, numbered 1 through **k**. All registers initially start in an unlocked state.

You are given a list of **t** valid execution commands. Each command is specified by three integers `(x, y, z)`, which target register `x` in bank A, register `y` in bank B, and register `z` in bank C.

When a command is executed, it changes the state of its three target registers from unlocked to locked. A command can only be executed if all three of its target registers are currently in the unlocked state.

Your goal is to successfully execute exactly **k** commands from the provided list.

Determine whether it is possible to achieve this, and if so, report a valid set of commands to execute.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of registers per bank and the number of available commands.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a single command targeting register **x** in bank A, **y** in bank B, and **z** in bank C. No command is listed more than once.

## Output

If it is possible to execute exactly **k** commands, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of a chosen command. Any valid choice of **k** commands that respects the locking rules is accepted; the commands may be printed in any order.

If no such set of commands can be executed, print `NO`.

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

In Example 2, both commands target register 1 in bank B. Once either command is executed, register 1 in bank B becomes locked, making the other command invalid. Therefore, it is impossible to execute 2 commands.
