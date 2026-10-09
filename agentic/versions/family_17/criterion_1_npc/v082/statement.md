# Problem A — Zero-Waste Tasting Menu

Time limit: 5 s   Memory limit: 256 MB

## Description
A prestigious restaurant is designing its seasonal tasting menu. The pantry has been stocked with a specific inventory of ingredients, each assigned a unique ID number starting from 1 up to 3**q**. The executive chef has mandated that the new menu must consist of exactly **q** distinct courses.

Every course is created by combining exactly three ingredients. However, culinary balance is delicate: you cannot just mix any three items together. The kitchen staff has conducted extensive trials and compiled a master recipe book containing **t** harmonious flavor profiles. Each profile specifies a trio of ingredients that blend perfectly. An ingredient might appear in multiple different profiles in the recipe book, while some profiles might share no ingredients at all.

The restaurant operates under a strict full-utilization philosophy for this event. A proposed menu is only approved if it selects courses entirely from the master recipe book such that **every** single ingredient in the pantry is incorporated. Furthermore, no ingredient may be used in **more than one** course, ensuring that flavors remain distinct and unrepeated throughout the meal. In other words, the chosen profiles must account for the entire pantry with each ingredient's ID checked off precisely once.

You must determine whether it is possible to design an approved tasting menu from the given profiles. If it is, provide the list of courses to be served. If the recipe book cannot accommodate the pantry inventory under these rules, report that no approved menu exists. (Note that simply having a large number of profiles does not guarantee success, just as a small number does not guarantee failure.)

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The integer **q** dictates the number of courses to prepare, meaning the pantry holds ingredients numbered 1 through 3**q**.
Each of the next **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing a single harmonious flavor profile from the recipe book.

## Output
If an approved menu can be constructed, print `YES` on the first line, then **q** lines each with the three ingredients of one chosen profile.
Otherwise print `NO`.

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
