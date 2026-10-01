# Car Fault Expert System

## User Manual

### Required Software

- Python 3.x
- CLIPS Python library (`clipspy`)
- `diagnosis.py`
- `car_diagnosis.clp`

Keep the two program files in the same folder.

###  Installation

Install Python 3.x if it is not already installed. To verify the installation, open Command Prompt and run:

```text
python --version
```

Install `clipspy` from the project folder using:

```text
pip install clipspy
```

###  Project Folder Setup

The folder should contain:

```text
Car_Fault_Diagnosis/
├── diagnosis.py
└── car_diagnosis.clp
```

- `diagnosis.py` - Main Python program and user interface.
- `car_diagnosis.clp` - CLIPS knowledge base containing the facts and diagnostic rules.

Important: Both files must be kept in the same folder because the Python program loads `car_diagnosis.clp`.

Do not rename `car_diagnosis.clp` unless the corresponding filename is also changed in `diagnosis.py`.

###  Starting the Expert System

Open Command Prompt in the project folder and run:

```text
python diagnosis.py
```

###  Using the System

1. Select one of the six problem categories.
2. Answer the displayed symptom questions using `YES` or `NO`.
3. Review the observed facts identified from the answers.
4. Select one of the three diagnosis modes.
5. Review the inference results and explanations produced by the selected mode.
6. If using **Check a Possible Fault**, another fault can be selected if the first selected fault cannot be proved.

Invalid answers such as `maybe`, `yes123`, or `abc` are rejected. The question is repeated until a valid `YES` or `NO` response is provided.

####  Diagnose from My Symptoms

This option starts with the symptoms provided by the user and uses forward chaining to identify possible faults.

The reasoning follows:

```text
Observed Symptoms -> Rules -> Possible Faults
```

The system displays the applicable rules and the possible faults derived from the observed symptoms.

####  Check a Possible Fault

This option allows the user to start with a possible fault and verify whether the observed symptoms support it.

The reasoning follows:

```text
Possible Fault -> Supporting Rule -> Required Symptom -> Fact
```

If the selected fault cannot be proved, the system allows the user to select another relevant fault. Previously checked faults are not offered again.

#### Compare Both Approaches

This option runs both forward and backward reasoning and displays their results.

It allows the user to compare the conclusions obtained using the two inference approaches.
