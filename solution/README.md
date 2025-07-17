# Vehicle Routing Problem (VRP) Project

## Overview
This project addresses the classic Vehicle Routing Problem (VRP), where the goal is to determine optimal routes for a fleet of vehicles delivering goods to a set of customers from a central depot, minimizing the total transportation cost while respecting vehicle capacity constraints.

The solution implements a constructive heuristic (Nearest Neighbor) followed by local search metaheuristics (Relocation, Swap, and 2-Opt moves) to improve the initial solution.

## Directory Structure
- `solution/` — Main implementation (solver, model, checker, input/output)
- `solution_2/`, `VRP_CandW/` — Alternative or experimental implementations
- `Edu_Files/` — Educational materials, example solutions, and visualizations

## How It Works
- **Modeling**: The problem is modeled using Python classes for nodes (customers, depot), routes, and the overall model.
- **Input**: Reads instance data from `Instance.txt` (customer locations, demands, vehicle capacity).
- **Solving**: 
  1. Builds an initial solution using the Nearest Neighbor heuristic.
  2. Improves the solution using Variable Neighborhood Descent (VND) with Relocation, Swap, and 2-Opt moves.
- **Output**: Writes the solution (total cost, number of routes, and each route's sequence) to `output.txt`.
- **Validation**: A solution checker (`sol_checker.py`) verifies feasibility and cost.

## Input Format (`Instance.txt`)
- Line 1: `CAPACITY,<vehicle_capacity>`
- Line 2: `EMPTY_VEHICLE_WEIGHT,<weight>`
- Line 3: `CUSTOMERS,<number_of_customers>`
- Line 4: `NODES INFO`
- Line 5: `ID,XCOORD,YCOORD,DEMAND`
- Lines 6+: One line per node (depot first, then customers):
  - `ID`: Node ID (0 for depot)
  - `XCOORD`, `YCOORD`: Coordinates
  - `DEMAND`: Customer demand (0 for depot)

## How to Run
1. Place your instance file as `Instance.txt` in the `solution/` directory.
2. Run the main script:
   ```bash
   python3 main.py
   ```
   This will generate `output.txt` with the solution.

## Output Format (`output.txt`)
- Line 1: `Cost:`
- Line 2: Total cost (objective value)
- Line 3: `Routes:`
- Line 4: Number of routes used
- Lines 5+: Each line is a route, listing node IDs in visiting order (starting and ending at depot 0)

Example:
```
Cost:
37500.25603492787
Routes:
28
0,259,77,282,129,178,271,115,281,286
...
```

## Solution Checker
To validate your solution:
```bash
python3 sol_checker.py
```
This checks for cost consistency, capacity violations, and ensures each customer is visited exactly once.

## Team Members
- t8220146 (Ιωαννης Ταμπακης)
- t8220029 (Διονυσης Γλυτσος)
- t8220043 (Θοδωρης Ζαρκαλης)

## References
- Project statement and data: see `Edu_Files/comp24-25.pdf`
- Algorithms: Nearest Neighbor, Variable Neighborhood Descent (VND)