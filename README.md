# Artificial Intelligence Project  2025/26  
## Class Timetable Optimization (CSP with OR-Tools)

---

### Introduction

This project implements an intelligent system capable of automatically generating class timetables for undergraduate courses at the Polytechnic Institute of Cávado and Ave (IPCA).

Timetabling is a complex **Constraint Satisfaction Problem (CSP)** that involves multiple interdependent variables — teachers, classrooms, courses, and student groups — each with specific constraints.  
By leveraging **Google OR-Tools CP-SAT Solver**, the system creates **optimized, conflict-free schedules** that respect all defined constraints and minimize unnecessary transitions (e.g., room changes for teachers).

---

### Project Structure

...
IA25_P01_G4/
├── datasets/
│ └── timetable_dataset.txt
├── outputs/
│ └── best_schedule.json
├── src/
│ ├── helpers.py
│ └── timetable_solver.py
├── IA25_P01_G4.ipynb
└── README.md
...

---

### Requirements and Installation

#### Software Requirements
> Python 3.9+  
> Jupyter Notebook (optional, for running interactively)  
> Works on Windows, macOS, or Linux

#### Required Libraries

```bash
pip install ortools
```
> OR-Tools (by Google) is used to model and solve the Constraint Programming problem efficiently.

---

### How to Run the Project

1. Open the file IA25_P01_G4.ipynb in Jupyter Notebook (or run src/timetable_solver.py directly).

2. Execute all cells sequentially.

3. The system will read the input data from datasets/timetable_dataset.txt, build the CSP, and start the search process.

4. The final optimized schedule will be exported as:

```bash
outputs/best_schedule.json
```

---

### Heuristics Implemented

The solver uses two independent heuristics to improve search efficiency, defined in src/helpers.py.

#### MRV — Minimum Remaining Values

> Chooses the variable with the smallest remaining domain first.
> Prioritizes the most constrained variables, reducing branching early.
> Implemented using cp_model.CHOOSE_MIN_DOMAIN_SIZE.

#### LCV — Least Constraining Value

> Chooses the value that constrains other variables the least.
> Keeps more options open for future assignments.
> Implemented using cp_model.SELECT_MIN_VALUE.

#### MRV + LCV Combination

> The combination of MRV (for variable selection) and LCV (for value selection) offers a balanced and effective approach to exploring the search space.
> This setup yields faster, conflict-free solutions with improved efficiency.

---

### Internal Workflow

1. Dataset Loading
The system reads data from timetable_dataset.txt, defining:
- Classes and their courses
- Teachers and their assigned courses
- Timeslot and room restrictions
- Online class configurations

2. Variable Definition
Each class session (lesson) has:
- A timeslot variable
- A room variable
- A teacher variable
- A day variable

3. Constraint Modeling
The following constraints are applied:
- Teachers cannot teach two classes at the same time
- Classes cannot overlap for the same group
- Room and timeslot restrictions are enforced
- Online classes are fixed to “Online” room
- A class cannot exceed 3 lessons per day

4. Heuristic Search & Optimization
OR-Tools CP-SAT explores all valid solutions within a configurable time limit (default: 30s) using the selected heuristics.

5. Solution Evaluation & Export
All valid solutions are collected, and the one minimizing room changes per teacher is selected as the “best”.
The final schedule is exported to JSON for readability.

---

### Example Output (best_schedule.json)

```json

{
    "UC11_1": { "slot": 14, "room": "Online", "teacher": "jo" },
    "UC12_1": { "slot": 12, "room": "Room1", "teacher": "mike" },
    "UC13_1": { "slot": 20, "room": "Room2", "teacher": "rob" },
    "UC14_1": { "slot": 18, "room": "Lab01", "teacher": "rob" }
}

```

---

### Expected Results

- Conflict-free timetables respecting all constraints
- Minimized room changes for teachers
- Efficient use of rooms and timeslots
- Modular structure allowing new heuristics and constraints to be added easily

---

### Authors

Developed for the Artificial Intelligence course (2025/2026) - Computer Systems Engineering, IPCA

| Name              | Student Number |
|-------------------|----------------|
| Pedro Ribeiro     | 27960          |
| Ricardo Fernandes | 27961          |
| Carolina Branco   | 27983          |
| João Barbosa      | 27964          |
| Diogo Abreu       | 27975          |

---

### GitHub Repository: 
https://github.com/DiogoAbreu05/IA25_P01_G4
