# Problem A — Translating for the Delegated Languages

Time limit: 5 s   Memory limit: 256 MB

## Description

A global summit involves **n** distinct languages (numbered 1 to n). To enable seamless communication, you have the option to purchase translation modules. Each module is available for a specific fee and provides a directed translation service. Specifically, a module described by a source **u**, a target **v**, and a fee **w** permits translation only from **u** to **v**. However, the summit's communication protocol guarantees that whenever a module is purchased, the vendor must automatically provision the reverse translation pathway (from **v** to **u**) completely free of charge.

A specific group of **t** languages are designated as **delegated**. Your goal is to guarantee that any document starting in a delegated language can be accurately translated into every other delegated language. Documents may be routed through any number of consecutive translation steps using the modules you purchase, and these intermediate steps may utilize languages that are not delegated.

Find the minimum total fee required to purchase a valid combination of modules that fulfills this connectivity goal.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the ids of the delegated languages.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). These represent a translation module from language u to language v that can be purchased for fee w.
It is guaranteed that the available modules can fulfill the requirement.

## Output

Output a single integer representing the minimum total fee to purchase a valid combination of modules.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, acquiring the modules involving language 4 (total fee 1+1+1 = 3) allows documents to be translated between any ordered pair among 1, 2, and 3. This is cheaper than acquiring modules to translate between the three delegated languages directly (which would cost 4). In Example 3 there is only one delegated language, so no modules need to be acquired.