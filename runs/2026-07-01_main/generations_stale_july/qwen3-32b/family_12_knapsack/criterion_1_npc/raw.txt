To solve this problem, we need to select a subset of investments such that their total cost does not exceed a given budget while maximizing the total value. Given the constraints, a direct dynamic programming approach is infeasible due to the large possible budget. Instead, we use a meet-in-the-middle technique to efficiently explore all possible subsets.

### Approach
1. **Split the Investments**: Divide the list of investments into two halves. This allows us to handle each half separately, reducing the problem size.
2. **Generate Subsets**: For each half, generate