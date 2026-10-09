# Problem A — Acoustic Resonance Suppression

Time limit: 5 s   Memory limit: 256 MB

## Description
A reverberation chamber must undergo acoustic stress testing across **3q** discrete frequency bands, indexed sequentially from 1 to **3q**. To prevent structural fatigue, all **3q** bands must be actively dampened during the test.

The facility maintains a catalog of **t** certified Helmholtz resonator configurations. Each configuration is geometrically tuned to absorb acoustic energy in exactly three specific frequency bands.

When installed in the chamber, a resonator completely neutralizes its three target bands. However, the installation must be strictly non-overlapping: if two selected resonators target the same frequency band, their interacting acoustic fields produce destructive interference that invalidates the test calibration. Consequently, each of the **3q** frequency bands must be neutralized by exactly one resonator.

You must determine whether it is possible to authorize a deployment of exactly **q** resonator configurations from the catalog that collectively dampen all **3q** bands without any overlap. If such a deployment is possible, provide the list of configurations to install. If no valid combination exists within the catalog, report that the deployment is impossible.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the following **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), specifying the three frequency bands neutralized by one certified resonator configuration.

## Output
If a valid deployment exists, output `YES` on the first line, followed by **q** lines each containing the three frequency bands of one selected resonator configuration.
Otherwise, output `NO`.

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
