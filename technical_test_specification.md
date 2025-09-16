# Research Engineer Technical Test: Route Construction Problem

## Overview

You are tasked with solving a route construction optimization problem. Given three sets of 2D coordinate points, your objective is to construct an optimal path that maximizes the number of goal points visited while satisfying specific constraints.

## Problem Statement

### Input Format

The input dataset contains 100 problem instances to solve. For each problem instance, you will receive three sets of 2D coordinates:

- **Start Points**: A set of valid starting positions
- **End Points**: A set of valid ending positions
- **Goal Points**: A set of points you should attempt to visit

All coordinates are specified as `[x, y]` pairs where both `x` and `y` are integers in the range `[-1000, 1000]`.

### Objective

Construct a path (sequence of coordinates) that:
- **Begins** at one of the provided start points
- **Ends** at one of the provided end points
- **Visits the maximum number of goal points possible**

### Solution Paths

A coordinate `pᵢ` consists of the points `xᵢ` and `yᵢ`. A path is defined as a sequence of 2D coordinates `P = [p₁, p₂, ..., pₙ]` connected by straight line segments. Each line segment connects consecutive coordinates `pᵢ` and `pᵢ₊₁`.

**Visiting Goal Points**: A goal point is considered "visited" if and only if its exact coordinates appear in your submitted solution path.

Your solution path may include coordinates that **are not** present in any of the three input sets.

## Constraints

Your solution must satisfy ALL of the following constraints:

1. **Point Limit**: Maximum of 100 coordinates in your path sequence
2. **Length Limit**: Total cumulative length of all line segments must be strictly less than 2000
3. **No Self-Intersection**: The path cannot cross, overlap, or touch itself at any point
4. **No Repeated Visits**: Each coordinate can be visited at most once

### Constraint Details

**Length Calculation**: The cumulative length is the sum of Euclidean distances between consecutive coordinates in your sequence.

**Self-Intersection**: A path violates this constraint if any two non-adjacent line segments intersect. Adjacent line segments are those that are consecutive in your submitted coordinate sequence and share a common endpoint.


## Solution Format

Submit your solutions as a JSON where keys are instance names and values are arrays of coordinate pairs:

```json
{
  "instance_001": [
    [-900, 0],
    [-400, 0],
    [0, 0],
    [400, 0],
    [900, 0]
  ],
  "instance_002": [
    [100, -800],
    [200, -100],
    [800, 300]
  ]
}
```

**Requirements:**
- Keys must match the provided instance names exactly
- For each solution array: first coordinate must be a valid start point, last coordinate must be a valid end point
- All coordinates must be within the bounds `[-1000, 1000]`
- Integer coordinates only (no decimal places)

## Code Quality Requirements

Your implementation should be **production-ready** and follow software engineering best practices.

### Executable Solution
Your submission must include a main executable file named `solve.py` that can be run from the command line:

```bash
python solve.py --input instances.json --output solution.json
```

**Required Command Line Arguments:**
- `--input` (required): Path to the input JSON file containing problem instances
- `--output` (required): Path where the solution JSON file should be written

You are free to add additional command line arguments as needed, such as `--verbose` for detailed logging or `--timeout` for execution limits.


## Example Instance

**Input:**
```json
{
  "instance_001": {
    "start_points": [[-800, -600], [200, -900]],
    "end_points": [[700, 800], [-400, 0]],
    "goal_points": [
      [-200, -300], 
      [100, 200], 
      [500, -100], 
      [-400, 300], 
      [300, 600],
      [-100, 0]
    ]
  }
}
```

**Example Solution:**
```json
{
  "instance_001": [
     [-800, -600],
     [-200, -300],
     [-100, -300], 
     [-100, 0], 
     [-400, 0]
  ]
}
```

**Solution Analysis:**
- Starts at `[-800, -600]` (valid start point)
- Visits 2 valid goal points: `[-200, -300]` and `[-100, 0]`
- Ends at `[-400, 0]` (valid end point)
- Total length approximately 1370 (within constraint)
- No self-intersection
- Point count: 5 ≤ 100

## Evaluation Criteria

Solutions will be evaluated in two phases:

### Phase 1: Constraint Validation

Each solution must satisfy ALL constraints:

- **Valid Endpoints**: First coordinate is a start point, last coordinate is an end point
- **Point Limit**: Solution contains ≤ 100 coordinates 
- **Length Constraint**: Total cumulative length is strictly < 2000. Length calculations should use standard floating-point arithmetic. Constraint checking will use tolerance of 1e-10 for length comparisons.
- **No Self-Intersection**:  Line segments cannot cross at interior points. Segments may share endpoints if they are adjacent in the path sequence.
- **Coordinate Bounds**: All coordinates are within `[-1000, 1000]` range
- **Format Compliance**: Valid JSON structure

**Integer Precision**: All constraint checks and scoring will use exact integer comparisons.

### Phase 2: Performance Scoring (for valid solutions only)

Evaluate your solution across the 100 problem instances. Reported performance metrics should include:

1. **Goal Points**: Total number of goal points visited across all instances (higher is better)
2. **Runtime Analysis**: Total execution time for all instances

Include any other performance metrics you choose to report.

## Submission Guidelines

### Repository Requirements

1. **Create a private GitHub repository** for your submission
2. **Commit regularly** as you develop your solution to show your progress
3. **Include the following files in the root directory**:
   - `solve.py`: Main executable Python file (see Code Quality Requirements)
   - `solution.json`: Your solutions in the required JSON format
   - `report.ipynb`: Jupyter notebook with your analysis and findings
   - Additional Python source code files containing your implementation
   - `README.md`: Brief overview of your approach and how to run your code
   - `requirements.txt`: List of Python dependencies (if any)
4. Repository shared with guillaume@algo1.ai

### File Format Requirements

1. **solution.json**: Valid JSON mapping instance names to coordinate arrays
2. **Integer coordinates**: All coordinates must be integers (no decimal places)
3. **Encoding**: UTF-8 text encoding for all files

## Input Delivery Format

You will receive the problem instances as a JSON file with the following structure:

```json
{
  "instance_001": {
    "start_points": [[-900, 0], [0, -800]],
    "end_points": [[900, 0], [0, 800]],
    "goal_points": [[0, 0], [400, 0], [-400, 0]]
  },
  "instance_002": {
    "start_points": [[100, -900], [-200, 300]],
    "end_points": [[800, 100], [-100, 900]],
    "goal_points": [[-100, -200], [300, 400], [500, -100]]
  },
   ...
}
```

## Frequently Asked Questions

**Q: What format should coordinates be in?**  
A: All coordinates must be integers in your JSON output. No decimal places are allowed.

**Q: Are there time limits for computation?**  
A: Efficient solutions are preferred, and runtime performance is part of the evaluation criteria. The priority is to maximise the number of goal points visited.

**Q: What programming language should I use?**  
A: You must use Python for your implementation.

**Q: What if my algorithm doesn't find a valid solution for a problem instance?**  
A: Returning an empty path (i.e., `[]`) is acceptable, as no solution that violates the constraints should be submitted.

**Q: Can I use external libraries and resources?**  
A: Yes, you can use external python libraries and online resources including the use of LLM coding agents. You **may not** use off the shelf solvers, and you must implement the optimization algorithm on your own. 


## Runtime Performance Requirements

Your submission must include runtime performance analysis:

- Track and report execution time for each problem instance
- Analyze the computational complexity of your approach
- Compare different algorithmic strategies you attempted
- Document performance optimizations implemented

## Notebook Submission

In addition to your solution code, submit a Jupyter notebook (`report.ipynb`) that includes:

1. **Approach Overview**: Description of your algorithmic strategy and reasoning, including all approaches considered
2. **Implementation Details**: Key components of your solution
3. **Performance Analysis**: Runtime analysis across different instance types and sizes
4. **Results Summary**: Final performance metrics and insights gained
5. **Visualizations**: Any relevant graphs or charts that illustrate your findings
