# Project 01 — Artificial Intelligence 2025/26
## Class Timetable (CSP Problem)

---

### Introduction

This project aims to develop an intelligent agent capable of automatically generating class timetables for undergraduate programs at the Polytechnic Institute of Cávado and Ave (IPCA).

Timetable creation is a complex task, as it involves multiple constraints related to teachers, rooms, subjects, and student groups.  
By applying Artificial Intelligence techniques — specifically Constraint Satisfaction Problems (CSP) — the system is able to generate valid, coherent, and optimized schedules, reducing manual effort and minimizing conflicts.

---

### Project Structure

IA25_P01_G4
├── datasets/
│ └── timetable_dataset.txt
│ └── constants.py
├── outputs/
│ └── best_schedule.json
├── src/
│ └── helpers.py
├── IA25_P01_G4.ipynb
└── README.md

---

### Requirements and Installation

#### Software Requirements

> Python 3.9+  
> Jupyter Notebook (for documentation and interactive execution)  
> Operating system: Windows, macOS, or Linux

#### Required Libraries

Install dependencies using:

bash
pip install python-constraint

> The python-constraint library is used to model and solve Constraint Satisfaction Problems (CSPs).

---

### How to Run the Project

1. Open the file IA25_P01_G4.ipynb in Jupyter Notebook.

2. Execute all cells sequentially.

3. The result will be a file named best_schedule.json located in the outputs/ folder.

---

###Example Output (best_schedule.json)

json
{
    "UC11_1": { "slot": 14, "room": "Online", "teacher": "jo" },
    "UC12_1": { "slot": 12, "room": "Online", "teacher": "mike" },
    "UC13_1": { "slot": 20, "room": "Room2", "teacher": "rob" },
    "UC14_1": { "slot": 18, "room": "Lab01", "teacher": "rob" }
}
`

---

### Internal Functioning

1. Dataset Loading: Classes, subjects, teachers, and constraints are loaded from the timetable_dataset.txt file.

2. Variable Creation: The CSP defines variables for each class (time slot, room, teacher).

3. Constraint Application: The solver adds all hard constraints and soft constraints.

5. Exportation: The final schedule is saved in a human-readable JSON file.

---

###Expected Results

> Generation of conflict-free schedules

> Satisfaction of all hard constraints

> Minimization of soft constraint violations and class dispersion

> Flexibility to include future heuristic optimizations

---

###Project Authors
Developed within the Artificial Intelligence course — Academic Year 2025/2026 — Computer Systems Engineering, IPCA.

| Name              | Student Number |
|-------------------|----------------|
| Pedro Ribeiro     | 27960          |
| Ricardo Fernandes | 27961          |
| Carolina Branco   | 27983          |
| João Barbosa      | 27964          |
| Diogo Abreu       | 27975          |

GitHub Repository: https://github.com/DiogoAbreu05/IA25_P01_G4.git