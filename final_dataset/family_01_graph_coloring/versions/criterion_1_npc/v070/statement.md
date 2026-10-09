# Problem A — Environment Provisioning

Time limit: 2 s
Memory limit: 256 MB

You are designing the deployment layout for a system consisting of $n$ distinct processing modules. Each module must be provisioned in exactly one of three available execution environments, which are identified by the values 1, 2, and 3.

Before the system goes live, a validation script evaluates your environment assignments. The script contains a predefined list of $m$ security boundaries. Each boundary specifies a pair of modules that share sensitive data. When the script runs, it verifies the environments of the modules in each pair. If it finds that the two modules of any specified pair have been provisioned in the exact same execution environment, the script will raise a security violation and halt the deployment.

You must determine an assignment of environments for all $n$ modules such that the validation script completes without raising any violations. If no such assignment exists, the deployment must be canceled.

## Input
The first line contains two integers $n$ and $m$ — the number of modules and the number of security boundaries ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, representing a pair of modules that share a security boundary.

## Output
If it is impossible to provision the modules without a violation, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer (1, 2, or 3) is the environment assigned to module $i$. If multiple valid assignments exist, you may output any of them.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
