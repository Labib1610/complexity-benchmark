# Relic Preservation Logistics

Time limit: 5 s   Memory limit: 256 MB

## Description
The historical society is organizing a grand exhibition of its relic collection. The mandate from the board of directors is absolute: every single relic in the collection must be showcased. Because these relics are highly fragile, they require specialized atmospheric conditions to prevent degradation.

Over the years, the society has drafted various preservation module blueprints. Each blueprint was meticulously engineered to stabilize the microclimate for a specific trio of relics. A module must contain exactly the three relics it was designed for—no more, no less—otherwise the atmospheric balance will fail. A relic cannot be placed in multiple modules, nor can it be left in storage.

Your job is to determine if a combination of modules can be constructed from the available blueprints such that every relic is safely housed in exactly one module. If a valid configuration is found, you must provide the list of modules to build. 

## Input
The first line provides two integers, $q$ and $t$. The value $q$ denotes the number of exhibition pedestals to be used. Because the exhibition must take place, at least one pedestal will be used, but the hall's fire safety rating restricts the maximum number of pedestals to 200. The total number of relics in the collection is exactly three times the number of pedestals, and they are labeled with integers starting from 1 up to the total collection size.

The value $t$ denotes the number of available preservation module blueprints in the society's archives. The archives might be completely empty, or they could contain up to the maximum physical filing capacity of 20,000 blueprints.

Following this are $t$ lines. Each line corresponds to a blueprint and contains three integers $a$, $b$, and $c$, representing the IDs of the three relics the module is engineered to hold. To ensure standardized filing, the three IDs are listed in strictly increasing order, and each refers to a valid relic from the collection.

## Output
If there is a valid way to house all relics according to the rules, output `YES` on the first line. Following that, output $q$ lines, each listing the three relic IDs for a chosen module.
If no such arrangement exists, output `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
