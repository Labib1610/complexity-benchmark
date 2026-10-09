# Universal Translation

Time limit: 5 s   Memory limit: 256 MB

## Description

As the organizer of an interstellar summit, you are tasked with distributing a vital unified broadcast to populations across a galactic federation. The federation recognizes $n$ distinct languages, numbered 1 through $n$. Among these, there is a specific target subset of $t$ priority languages that absolutely must receive the message.

You have the flexibility to draft the initial broadcast in any single language out of the $n$ available options. 

To propagate the message to the remaining target populations, you can enlist the help of $m$ independent bilingual translators. Each translator specializes in a specific pair of languages and requires a one-time retainer fee to begin work. Once retained, they operate autonomously: as soon as the broadcast is published in one of their two languages, they will instantly translate and release it in their other language.

Your goal is to trigger a self-sustaining translation cascade. By carefully selecting your initial drafting language and retaining a specific combination of translators, you can ensure that the translations naturally ripple outwards. The operation is a success if the cascade ultimately produces versions of the broadcast in all $t$ priority languages. (Naturally, if your initial drafting language is one of the $t$ targets, that population requires no further translation).

Determine the absolute minimum total retainer fee required to retain a group of translators capable of cascading the broadcast to every priority language from an optimally chosen starting language.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ $n$ ≤ 100, 0 ≤ $m$ ≤ $n$·($n$−1)/2, 1 ≤ $t$ ≤ 10).
The second line lists $t$ distinct integers representing the priority languages.
The subsequent $m$ lines each contain three integers $u$, $v$, and $w$ (1 ≤ $u$, $v$ ≤ $n$, $u \neq v$, 1 ≤ $w$ ≤ 1000000), indicating that a translator is available for languages $u$ and $v$ at a retainer fee of $w$.
It is guaranteed that a valid cascade is always possible.

## Output

Output a single integer representing the minimum total retainer fee needed to cascade the broadcast to all priority languages.

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

In Example 1, you can select language 4 for your initial draft. By retaining translators for the pairs 1-4, 2-4, and 3-4 (costing 1+1+1 = 3), the cascade will automatically yield versions in the priority languages 1, 2, and 3. This approach is more cost-effective than paying translators to bridge the priority languages directly (which would total 4). 
In Example 3, there is only a single priority language. Drafting the broadcast directly in this language fulfills the requirement immediately, costing 0 in translator fees.