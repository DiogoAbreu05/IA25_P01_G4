# Project 01 — Artificial Intelligence 2025/26  
## Class Timetable Generation and Optimization (CSP Approach)

---

### 1. Introduction

This project aims to develop an **intelligent agent** capable of automatically generating class timetables for undergraduate programs at the Polytechnic Institute of Cávado and Ave (IPCA).

Timetable generation is a **Constraint Satisfaction Problem (CSP)** that involves multiple interdependent entities — teachers, rooms, courses, and student groups — each with specific restrictions.  
The objective is to produce **valid, coherent, and optimized timetables**, reducing manual effort and minimizing scheduling conflicts.

Two implementations were developed:

1. **Version 1** — Using the `python-constraint` library (basic CSP solver).  
2. **Version 2** — Using **Google OR-Tools CP-SAT Solver** (optimized approach with heuristics and soft constraints).

---

### 2. Implementations Overview

| Version | Library Used | Focus | Characteristics |
|----------|--------------|--------|----------------|
| **Version 1** | `python-constraint` | Basic CSP modeling | Educational, simple, and flexible |
| **Version 2** | `Google OR-Tools` | Optimization & heuristics | Advanced solver with high performance |

---

### 3. Project Structure

```
IA25_P01_G4/
├── datasets/
│ └── timetable_dataset.txt
├── outputs/
│ └── best_schedule.json
| └── best_schedule_pythonconstraint.json
├── src/
│ └── helpers.py
├── IA25_P01_G4.ipynb
├── IA25_P01_G4_PythonConstraint.ipynb
└── README.md
```

---

### 4. Requirements and Installation

#### Common Requirements
> Python 3.9+  
> Jupyter Notebook (optional, for interactive execution)  
> Compatible with Windows, macOS, and Linux

#### Library Installation

| Version | Installation Command |
|----------|----------------------|
| Python Constraint | `pip install python-constraint` |
| OR-Tools | `pip install ortools` |

---

### 5. How to Run the Project

#### Version 1 — Using `python-constraint`

1. Open the notebook **`IA25_P01_G4_PythonConstraint.ipynb`** in **Jupyter Notebook**.  
2. Execute all cells sequentially.  
3. The generated timetable will be exported to:  

   ```bash
   outputs/best_schedule_pythonconstraint.json
   ```

#### Version 2 — Using `Google OR-Tools`

1. Open the notebook **`IA25_P01_G4_ORT.ipynb`** in **Jupyter Notebook**.  
2. Execute all cells sequentially.  
3. The generated timetable will be exported to:  

   ```bash
   outputs/best_schedule.json
   ```

---

---

### 6. Version 1 — CSP with `python-constraint`

#### Overview

This implementation models the scheduling problem as a **Constraint Satisfaction Problem (CSP)** using the `python-constraint` library.  
It applies **hard constraints** to ensure that no conflicts occur among teachers, rooms, and student groups.

#### Internal Workflow

1. **Dataset Loading** — Data (teachers, rooms, and courses) is read from `timetable_dataset.txt`.  
2. **Variable Definition** — CSP variables represent time slots, rooms, and teachers for each class.  
3. **Constraint Application** — The solver applies all hard constraints such as:  
- Teachers cannot have overlapping classes.  
- Each room can only host one class per time slot.  
- Maximum of three lessons per class per day.  
- Online classes assigned to “Online” room.  
4. **Solving Process** — The solver uses **backtracking search** to find valid solutions.  
5. **Exportation** — The final valid schedule is exported to a structured JSON file.

#### Example Output

```json
{
"UC11_1": { "slot": 14, "room": "Online", "teacher": "jo" },
"UC12_1": { "slot": 12, "room": "Online", "teacher": "mike" },
"UC13_1": { "slot": 20, "room": "Room2", "teacher": "rob" },
"UC14_1": { "slot": 18, "room": "Lab01", "teacher": "rob" }
}
```

**Expected Results**

- Generation of conflict-free timetables

- Satisfaction of all hard constraints

- Flexibility for future improvements (soft constraints, heuristics)

- Educational and interpretable model

**Limitations**

- No optimization for soft constraints (e.g., minimizing room changes)

- No built-in heuristics (pure backtracking search)

- Reduced scalability for large datasets

### 7. Version 2 — Optimization with OR-Tools CP-SAT

#### Overview

This version enhances the previous implementation by using the **Google OR-Tools CP-SAT solver**, which combines **Constraint Programming (CP)** with **SAT-based optimization**.  
It introduces heuristic-based search and evaluates multiple candidate solutions to select the most efficient timetable.

---

#### Internal Workflow

1. **Dataset Loading** — Input data is read from `datasets/timetable_dataset.txt`.  
2. **Variable Definition** — Time slot, room, teacher, and day variables are created for each class.  
3. **Constraint Modeling** — The following constraints are applied:
   - Teachers cannot teach two classes at the same time.  
   - Classes cannot overlap for the same student group.  
   - Rooms and time slots are exclusive.  
   - Online courses are fixed to the “Online” room.  
   - A class cannot exceed three lessons per day.  
4. **Heuristic Search & Optimization** — OR-Tools CP-SAT solver explores valid solutions using heuristics.  
5. **Evaluation & Export** — All valid solutions are evaluated, and the one minimizing room changes per teacher is selected as the best.

---

#### Implemented Heuristics

- **MRV — Minimum Remaining Values**  
  Chooses the variable with the smallest remaining domain first.  
  Reduces branching and improves search efficiency.

- **LCV — Least Constraining Value**  
  Chooses the value that restricts other variables the least.  
  Keeps more possibilities open for future assignments.

- **MRV + LCV Combination**  
  A hybrid strategy that balances exploration and exploitation, achieving faster convergence and higher-quality results.

---

#### Example Output

```json
{
  "UC11_1": { "slot": 14, "room": "Online", "teacher": "jo" },
  "UC12_1": { "slot": 12, "room": "Room1", "teacher": "mike" },
  "UC13_1": { "slot": 20, "room": "Room2", "teacher": "rob" },
  "UC14_1": { "slot": 18, "room": "Lab01", "teacher": "rob" }
}
```

**Expected Results**

- Conflict-free timetables respecting all constraints

- Minimized room changes per teacher

- Efficient use of available rooms and time slots

- Optimized performance through heuristics

### 8. Comparative Analysis

| **Aspect** | **python-constraint** | **OR-Tools CP-SAT** |
|-------------|----------------------|----------------------|
| **Solver Type** | Backtracking | CP-SAT (hybrid CP + SAT) |
| **Performance** | Slower for large datasets | Optimized and scalable |
| **Heuristic Support** | None | MRV + LCV implemented |
| **Optimization Level** | Hard constraints only | Hard + soft constraints |
| **Ease of Use** | Simple and educational | More complex but powerful |
| **Scalability** | Limited | High |

---

### 9. Critical Analysis and Future Improvements

#### Critical Analysis

The developed models successfully generate valid and conflict-free timetables.  
However, several limitations were identified:

- Limited solution diversity due to deterministic search behavior.  
- Exponential growth of search space with increasing dataset size.  
- Lack of weighted soft constraint optimization (e.g., consecutive classes, idle times).  
- Some solutions, while valid, may be impractical (e.g., scattered classes).

#### Future Improvements

1. **Multi-objective optimization** — Combine multiple soft constraints with weighted scoring.  
2. **Post-processing optimization** — Apply metaheuristics (e.g., simulated annealing, genetic algorithms).  
3. **Partial randomization** — Introduce stochastic variable selection for solution diversity.  
4. **Visualization tools** — Add timetable visualization using Matplotlib or a web UI.  
5. **Scalability testing** — Evaluate both solvers on larger datasets.

---

### 10. Conclusion

This project demonstrated the **practical application of Artificial Intelligence** and **Constraint Programming** to real-world scheduling problems.  

The first implementation, using **python-constraint**, provided a clear and interpretable foundation for CSP-based timetabling.  
The second implementation, using **Google OR-Tools CP-SAT**, introduced heuristic optimization and scalability, producing more efficient and realistic schedules.

#### Key Achievements

- Successful modeling of real scheduling constraints  
- Automation of a traditionally manual, error-prone task  
- Exploration of AI-based optimization techniques  

#### Future Work

- Multi-objective optimization frameworks  
- Advanced visualization and user interfaces  
- Hybrid metaheuristic approaches for post-optimization  

---

### 11. Authors

Developed for the **Artificial Intelligence** course (Academic Year 2025/2026) — *Computer Systems Engineering, IPCA.*

| **Name** | **Student Number** |
|-----------|--------------------|
| Pedro Ribeiro | 27960 |
| Ricardo Fernandes | 27961 |
| Carolina Branco | 27983 |
| João Barbosa | 27964 |
| Diogo Abreu | 27975 |

GitHub Repository: https://github.com/DiogoAbreu05/IA25_P01_G4.git