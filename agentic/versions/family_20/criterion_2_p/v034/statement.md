# Problem B — Diagnostic Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
A facility tests signal integrity by establishing connections between Transmitters and Receivers. Every trial links exactly one Transmitter to exactly one Receiver. A trial never links two Transmitters together, nor does it link two Receivers together. 

Trials are organized into a sequence of discrete time slots. A hardware constraint dictates that any single component—whether a Transmitter or a Receiver—can participate in at most one trial per time slot. 

Certain components will be involved in multiple trials. The single most heavily utilized component across the entire facility dictates an unavoidable baseline: if a component is scheduled for $K$ trials, those trials must be distributed across at least $K$ distinct time slots. The operations goal is to assign every trial a time slot drawn from a restricted pool of available time slots. The total number of time slots in this pool must be exactly equal to the participation count of the most heavily utilized component. The structural separation between Transmitters and Receivers guarantees that this compact schedule is always mathematically possible.

The facility's testing chambers can house a minimum of one and a maximum capacity of one hundred thousand Transmitters, and an equal capacity range for Receivers. A single testing campaign can log anywhere from zero up to four hundred thousand trials. 

## Input
The first line provides three integers: the total count of Transmitters, the total count of Receivers, and the total count of trials.
Following this is one line for each trial, each containing two integers: the identifier of the Transmitter and the identifier of the Receiver. 
Transmitter hardware is tagged with integer IDs starting at one and ending at the total number of Transmitters present. Receiver hardware follows an identical ID tagging scheme from one up to the number of Receivers present.

## Output
First, output `YES`. 
On the next line, output a space-separated sequence of integers, one for each trial, corresponding to the time slot assigned to it, in the exact order the trials were provided in the input. Time slots must be represented by integers starting from 1 up to the participation count of the most heavily utilized component.

## Example

**Input**
```
4 4 5
1 2
1 3
2 3
3 4
4 4
```

**Output**
```
YES
1 2 1 1 2
```
