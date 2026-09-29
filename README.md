# Car Fault Expert System

## 8. User Manual

### 8.1 Required Software

- Python 3.x
- CLIPS Python library (`clipspy`)
- `diagnosis.py`
- `car_diagnosis.clp`

Keep the two program files in the same folder.

### 8.2 Installation

Install Python 3.x if it is not already installed. To verify the installation, open Command Prompt and run:

```text
python --version
```

Install `clipspy` from the project folder:

```text
pip install clipspy
```

### 8.3 Project Folder Setup

The folder should contain:

```text
Car_Fault_Diagnosis/
├── diagnosis.py
└── car_diagnosis.clp
```

Do not rename `car_diagnosis.clp` unless the filename is also changed in the Python program.

### 8.4 Starting the Expert System

Open Command Prompt in the project folder and run:

```text
python diagnosis.py
```

### 8.5 Using the System

1. Select one of the six problem categories.
2. Answer the displayed symptom questions using `YES` or `NO`.
3. Review the identified facts.
4. Review the forward-chaining rules that fired.
5. Review the backward-chaining goal checks.
6. Review the possible faults and explanations.

Invalid answers, such as `maybe`, are rejected. The question is repeated until a valid `YES` or `NO` response is provided.

### 8.6 Example

For a starting problem, if the user reports dim headlights (`S02`) and rapid clicking when starting (`S05`), the system can trigger `R02` and `R05`. It then displays the corresponding possible battery-related faults and reasoning.
