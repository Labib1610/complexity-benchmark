# Problem A — Focus Group Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

An exclusive social network is organizing a focus group. To ensure fresh perspectives, they want to form a panel where absolutely no prior relationships exist among its members. Specifically, they need a group of exactly **k** users such that there is no friendship between any two individuals in the chosen group.

Given the network's current user base and the list of mutual friendships, determine if such a completely unacquainted panel of the requested size can be formed, and if so, identify the members.

## Input

The first line provides three integers: **n**, **m**, and **k**.
* The network's user headcount **n** is a positive integer that is bounded by the platform's strict server limit of 46 users.
* The total number of friendships **m** can be anywhere from zero up to the maximum possible number of distinct pairs among the **n** users.
* The requested panel size **k** is at least 1 and naturally cannot exceed the total user headcount **n**.

Following this are **m** lines, each containing two distinct integers **u** and **v**, representing a friendship between the user with ID **u** and the user with ID **v**. User IDs are assigned sequentially starting from 1 up to **n**. No friendship is listed more than once.

## Output

If a panel of exactly **k** users with no mutual friendships exists, print `YES` on the first line. On the second line, print the **k** distinct user IDs forming the panel, separated by spaces. If there are multiple valid panels, any one is accepted.

If no such panel can be formed, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
