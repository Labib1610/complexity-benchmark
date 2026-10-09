# Problem A — Diplomatic Translation

Time limit: 5 s   Memory limit: 256 MB

## Description

A galactic council includes representatives who speak various languages, indexed from $1$ to $n$. Within this assembly, a specific subset of $t$ languages are designated as *core* dialects. To maintain diplomatic harmony, the council must guarantee that any statement originating in one core dialect can be flawlessly translated into every other core dialect.

To achieve this, the council may employ bilingual linguists. Each candidate linguist is proficient in exactly two distinct languages and demands a fixed salary for their services. Once a linguist is employed, they can perform unlimited bidirectional translations between their two languages. Translations can be routed through multiple linguists: if one linguist translates from language A to language B, another can take the result in language B and translate it to language C. The council is fully authorized to hire linguists for non-core dialects, provided that using them as intermediary steps reduces the overall financial burden.

The council operates under the following logistical guarantees:
- The total number of candidate linguists available for hire across the galaxy will never exceed 4,950.
- The minimum cumulative salary required to establish the necessary communication network is guaranteed to be strictly less than 100,000,000.

Determine the minimum total salary the council must allocate to hire a group of linguists that enables full mutual translation among all core dialects.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line lists $t$ distinct integers representing the indices of the core dialects.
Each of the subsequent $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1,000,000$). This indicates that a linguist is available to translate between language $u$ and language $v$ for a salary of $w$.
It is assured that the available pool of linguists is sufficient to establish the necessary translations.

## Output

Output a single integer representing the minimum total salary required to employ the linguists.

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

In Example 1, employing linguists who speak the non-core dialect 4 (total salaries 1+1+1 = 3) is more economical than hiring linguists to translate directly between the three core dialects (which would require a total salary of 4). In Example 3, there is only one core dialect, so no linguists need to be hired.
