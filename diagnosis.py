import clips


# ============================================================
# PROBLEM CATEGORIES
# ============================================================

CATEGORIES = {
    "1": {
        "name": "Starting Problem",
        "symptoms": ["S01", "S02", "S03", "S04", "S05", "S06"]
    },

    "2": {
        "name": "Braking Problem",
        "symptoms": ["S10", "S11", "S12"]
    },

    "3": {
        "name": "Tyre Problem",
        "symptoms": ["S07", "S08", "S09"]
    },

    "4": {
        "name": "Engine / Temperature Problem",
        "symptoms": ["S13", "S14", "S15", "S19", "S20"]
    },

    "5": {
        "name": "Oil Problem",
        "symptoms": ["S16", "S17"]
    },

    "6": {
        "name": "Air Conditioning Problem",
        "symptoms": ["S18"]
    }
}


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = {
    "S01": "Does the engine turn slowly when starting?",
    "S02": "Are the headlights dim?",
    "S03": "Are the interior lights dim?",
    "S04": "Is the electrical equipment behaving strangely?",
    "S05": "Does the car make a rapid clicking sound when starting?",
    "S06": "Does the engine crank but not start?",

    "S07": "Does a tyre look low?",
    "S08": "Does the tyre pressure warning remain on?",
    "S09": "Is a tyre worn on one edge?",

    "S10": "Do the brakes make a squealing noise?",
    "S11": "Do the brakes make a grinding noise?",
    "S12": "Does the car vibrate while braking?",

    "S13": "Is the temperature gauge in the red?",
    "S14": "Is steam coming from the bonnet?",
    "S15": "Is the coolant level low?",

    "S16": "Is the oil warning light on?",
    "S17": "Is the engine oil level low?",

    "S18": "Is the air conditioning not producing cold air?",

    "S19": "Is the car accelerating slowly?",
    "S20": "Does the engine hesitate during acceleration?"
}


# ============================================================
# BACKWARD-CHAINING RULE INDEX
# ============================================================

BACKWARD_RULES = {
    "weak-battery": [("R01", "S01"), ("R02", "S02"), ("R03", "S03")],
    "battery-problem": [("R04", "S04")],
    "battery-or-connection-problem": [("R05", "S05")],
    "fuel-ignition-or-engine-management-problem": [("R06", "S06")],
    "low-tyre-pressure": [("R07", "S07")],
    "slow-puncture-damaged-tyre-or-tpms-problem": [("R08", "S08")],
    "wheel-alignment-problem": [("R09", "S09")],
    "worn-brake-pads": [("R10", "S10")],
    "serious-brake-wear": [("R11", "S11")],
    "brake-problem": [("R12", "S12")],
    "engine-overheating": [("R13", "S13"), ("R14", "S14")],
    "cooling-system-problem": [("R15", "S15")],
    "oil-pressure-or-oil-problem": [("R16", "S16")],
    "low-engine-oil": [("R17", "S17")],
    "air-conditioning-system-problem": [("R18", "S18")],
    "engine-performance-problem": [("R19", "S19"), ("R20", "S20")]
}


def backward_chain(goal, observed_symptoms):
    """Check whether an observed symptom supports a proposed fault goal."""

    supporting_rules = BACKWARD_RULES.get(goal, [])
    supported_by = [
        (rule_id, symptom_id)
        for rule_id, symptom_id in supporting_rules
        if symptom_id in observed_symptoms
    ]

    return supported_by


# ============================================================
# YES / NO FUNCTION
# ============================================================

def ask_question(question):

    while True:

        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        else:
            print("Please answer yes or no.")


# ============================================================
# LOAD CLIPS
# ============================================================

environment = clips.Environment()

environment.load("car_diagnosis.clp")

environment.reset()


# ============================================================
# MAIN USER INTERFACE
# ============================================================

print("=" * 60)
print("        CAR FAULT DIAGNOSIS EXPERT SYSTEM")
print("=" * 60)

print("\nWhat type of problem are you experiencing?\n")

print("1. Starting problem")
print("2. Braking problem")
print("3. Tyre problem")
print("4. Engine / temperature problem")
print("5. Oil problem")
print("6. Air conditioning problem")


# ============================================================
# GET CATEGORY
# ============================================================

while True:

    category = input("\nSelect an option (1-6): ").strip()

    if category in CATEGORIES:
        break

    print("Please select a number from 1 to 6.")


selected_category = CATEGORIES[category]

print("\n" + "-" * 60)
print(selected_category["name"].upper())
print("-" * 60)

print("\nPlease answer the following questions.\n")


# ============================================================
# ASK RELEVANT QUESTIONS
# ============================================================

observed_symptoms = []

for symptom_id in selected_category["symptoms"]:

    question = QUESTIONS[symptom_id]

    answer = ask_question(question)

    if answer:
        observed_symptoms.append(symptom_id)


# ============================================================
# UPDATE CLIPS FACTS
# ============================================================

for fact in environment.facts():

    if fact.template.name == "symptom":

        symptom_id = str(fact["id"])

        if symptom_id in observed_symptoms:

            fact.modify_slots(
                observed=clips.Symbol("yes")
            )


# ============================================================
# DISPLAY FACTS
# ============================================================

print("\n" + "-" * 60)
print("FACTS IDENTIFIED")
print("-" * 60)

if observed_symptoms:

    for fact in environment.facts():

        if fact.template.name == "symptom":

            symptom_id = str(fact["id"])

            if symptom_id in observed_symptoms:

                print(
                    f"{fact['id']}: "
                    f"{fact['name']} "
                    f"-> observed yes"
                )

else:

    print("No symptoms were reported.")


# ============================================================
# FORWARD CHAINING
# ============================================================

print("\n" + "-" * 60)
print("FORWARD CHAINING")
print("-" * 60)

print("Running inference engine...")

environment.run()


# ============================================================
# RULES APPLIED
# ============================================================

print("\n" + "-" * 60)
print("RULES APPLIED")
print("-" * 60)

rules_fired = []

for fact in environment.facts():

    if fact.template.name == "rule-fired":

        rule_id = str(fact["rule-id"])

        if rule_id not in rules_fired:

            rules_fired.append(rule_id)

            print(rule_id)


if not rules_fired:
    print("No rules were triggered.")


# ============================================================
# POSSIBLE FAULTS
# ============================================================

print("\n" + "-" * 60)
print("POSSIBLE FAULTS")
print("-" * 60)

faults = []

for fact in environment.facts():

    if fact.template.name == "possible-fault":

        fault = str(fact["name"])

        if fault not in faults:

            faults.append(fault)


if faults:

    for fault in faults:
        print("•", fault)

else:

    print("No possible fault could be determined.")


# ============================================================
# REASONING / EXPLANATION
# ============================================================

print("\n" + "-" * 60)
print("REASONING / EXPLANATION")
print("-" * 60)

explanations_found = False

for fact in environment.facts():

    if fact.template.name == "explanation":

        explanations_found = True

        print(
            f"{fact['rule-id']}: "
            f"{fact['message']}"
        )


if not explanations_found:

    print("No explanation was generated.")


# ============================================================
# FINISH
# ============================================================

print("\n" + "=" * 60)
print("Diagnosis completed.")
print("=" * 60)