# Problem B — Briefing Sessions at a Two-Sided Conference

Time limit: 2 s   Memory limit: 256 MB

## Description
A conference event brings together a group of morning presenters and a group of afternoon reviewers. The organizers have a list of planned briefing sessions. Each session on this list requires the attendance of exactly one specific morning presenter and exactly one specific afternoon reviewer.

The schedule is divided into numbered time slots (1, 2, 3, and so on). Whenever a briefing session takes place, it occupies its assigned time slot entirely. A fundamental restriction on the schedule is that a person cannot be in two places at once. Therefore, if two different briefing sessions involve the same morning presenter, they must be assigned to different time slots. Similarly, if two different briefing sessions involve the same afternoon reviewer, they must also be assigned to distinct time slots.

Some participants are more active than others. By counting the number of sessions for each participant, the organizers can identify the busiest individual—the one who must attend the highest number of sessions across the entire event. Let this maximum number of sessions for a single participant be called the peak load. Because this busiest participant cannot attend more than one session per time slot, the schedule will inherently require at least a number of time slots equal to the peak load.

The organizers' goal is to build a highly compressed schedule. You must assign every planned briefing session to a time slot such that the total number of time slots used does not exceed the peak load. In other words, every session must be given a time slot numbered from 1 up to the peak load, ensuring that no participant is double-booked. (The two-sided nature of the participant groups ensures that such a compressed schedule is always mathematically possible.)

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$).
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a briefing session between morning presenter $u$ and afternoon reviewer $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ integers in the range $1$ to the peak load. The $i$-th integer is the time slot assigned to the $i$-th briefing session in the input order. Any two sessions sharing a common participant must be assigned different time slots.

## Example

### Input
```text
3 3 4
1 1
1 2
2 1
3 3
```

### Output
```text
YES
1 2 2 1
```
