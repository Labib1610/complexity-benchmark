# Synchronized Drone Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description
An orbital carrier has arrived at a planetary surface with a fleet of survey drones. To conduct a comprehensive scan, the mission requires deploying every single drone simultaneously. There are exactly as many drones as there are designated landing zones on the surface. Drones are identified by consecutive serial numbers starting from 1. The landing zones are assigned consecutive serial numbers in a block starting immediately after the highest drone number.

Atmospheric interference means that not every drone can safely navigate to every landing zone. The carrier's telemetry system has provided a strict list of cleared flight routes, each connecting one specific drone to one specific landing zone. A drone cannot be sent to a zone unless their exact pairing appears on this cleared list. Some drones have multiple cleared routes, and some landing zones can be reached by multiple drones. The sheer number of cleared routes or how much they overlap does not matter—only the specific pairings themselves.

A successful deployment protocol must activate a subset of these cleared routes such that every drone is routed to exactly one landing zone, and every landing zone receives exactly one drone. No drone may be left on the carrier, and no landing zone may remain empty or receive multiple drones. 

Determine if there is a valid deployment protocol that utilizes all drones and landing zones simultaneously. If such a protocol exists, provide the exact flight routes to activate; otherwise, report that a complete deployment is impossible.

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a b (1 ≤ a ≤ q < b ≤ 2q), representing a cleared flight route between drone a and landing zone b.

## Output
If a complete deployment is possible, print `YES` followed by q lines, each containing the drone and landing zone of a chosen flight route; otherwise print `NO`.

## Example

**Input:**
```
3 4
1 4
1 5
2 5
3 6
```

**Output:**
```
YES
1 4
2 5
3 6
```
