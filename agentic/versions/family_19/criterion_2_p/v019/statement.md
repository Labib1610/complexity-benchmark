# Bureaucratic Form Processing

Time limit: 2 s   Memory limit: 256 MB

## Description
A large administrative agency consists of a set of desks. Forms move between these desks according to strictly defined forwarding rules. You are evaluating a plan involving a specific number of desks, established forwarding rules, and exactly one active processing directive.

Under this directive, a designated Intake desk must route a precise target number of forms to a designated Archive desk. 

Each forwarding rule allows a specific desk to pass a non-negative whole number of forms to another specific desk. However, each rule has a strict upper limit on the number of forms it can handle. 

Desks other than the Intake and Archive desks act exclusively as intermediaries. They cannot create, destroy, or store forms. Therefore, for every intermediary desk, the total number of forms it receives across all rules must exactly equal the total number of forms it passes on. 

For the Intake desk, the total forms it passes on minus the total forms it receives must exactly equal the target number. For the Archive desk, the total forms it receives minus the total forms it passes on must exactly equal the target number. Factors like processing time, physical distance between desks, and the order of form submission are irrelevant—only the rule limits, the strict form conservation at intermediary desks, and the target total dictate the validity of a plan.

Determine if it is possible to route the target number of forms through the agency such that no forwarding rule's limit is exceeded. If it is, specify the number of forms to pass along each rule.

## Input
Line 1: Three integers `n` (the number of desks), `m` (the number of forwarding rules), and `1` (indicating the single directive).
Line 2: Three integers `s` (the Intake desk identifier), `t` (the Archive desk identifier), and `d` (the target number of forms).
Next `m` lines: Three integers `u`, `v`, and `cap`, representing a forwarding rule that allows desk `u` to pass up to `cap` forms to desk `v`.

## Output
If the target number of forms can be routed successfully, print `YES` on the first line. On the second line, print `m` integers representing the number of forms passed along each forwarding rule, in the exact order the rules were given in the input. If it is impossible, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output:**
```
YES
5 5 0 5 5
```
