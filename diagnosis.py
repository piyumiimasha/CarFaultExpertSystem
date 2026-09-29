import clips


# ============================================================
# CAR FAULT DIAGNOSIS EXPERT SYSTEM
# User-Friendly CLI
# Forward Chaining + Backward Chaining
# ============================================================


# ============================================================
# DISPLAY HELPERS
# ============================================================

WIDTH = 70


def line(char="─"):
    print(char * WIDTH)


def title(text):
    print()
    print("╔" + "═" * (WIDTH - 2) + "╗")
    print("║" + text.center(WIDTH - 2) + "║")
    print("╚" + "═" * (WIDTH - 2) + "╝")


def section(text):
    print()
    print("┌" + "─" * (WIDTH - 2) + "┐")
    print("│" + text.center(WIDTH - 2) + "│")
    print("└" + "─" * (WIDTH - 2) + "┘")


def clean_name(name):
    return str(name).replace("-", " ").title()


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
# BACKWARD-CHAINING KNOWLEDGE BASE
# ============================================================

BACKWARD_RULES = {
    "weak-battery": [
        ("R01", "S01"),
        ("R02", "S02"),
        ("R03", "S03")
    ],

    "battery-problem": [
        ("R04", "S04")
    ],

    "battery-or-connection-problem": [
        ("R05", "S05")
    ],

    "fuel-ignition-or-engine-management-problem": [
        ("R06", "S06")
    ],

    "low-tyre-pressure": [
        ("R07", "S07")
    ],

    "slow-puncture-damaged-tyre-or-tpms-problem": [
        ("R08", "S08")
    ],

    "wheel-alignment-problem": [
        ("R09", "S09")
    ],

    "worn-brake-pads": [
        ("R10", "S10")
    ],

    "serious-brake-wear": [
        ("R11", "S11")
    ],

    "brake-problem": [
        ("R12", "S12")
    ],

    "engine-overheating": [
        ("R13", "S13"),
        ("R14", "S14")
    ],

    "cooling-system-problem": [
        ("R15", "S15")
    ],

    "oil-pressure-or-oil-problem": [
        ("R16", "S16")
    ],

    "low-engine-oil": [
        ("R17", "S17")
    ],

    "air-conditioning-system-problem": [
        ("R18", "S18")
    ],

    "engine-performance-problem": [
        ("R19", "S19"),
        ("R20", "S20")
    ]
}


# ============================================================
# CATEGORY-RELEVANT BACKWARD GOALS
# ============================================================

def relevant_goals(category_symptoms):
    """Return backward goals whose rules use symptoms in this category."""

    goals = []

    for goal, rules in BACKWARD_RULES.items():

        if any(
            symptom_id in category_symptoms
            for _, symptom_id in rules
        ):
            goals.append(goal)

    return goals


# ============================================================
# BACKWARD CHAINING ENGINE
# ============================================================

def backward_chain(goal, observed_symptoms):

    """
    Goal-driven backward chaining.

    Goal
      ↓
    Search rules capable of proving the goal
      ↓
    Check required symptom
      ↓
    If symptom is observed -> goal proved
    """

    trace = []

    trace.append(
        f"GOAL: {clean_name(goal)}"
    )

    supporting_rules = BACKWARD_RULES.get(goal, [])

    if not supporting_rules:

        trace.append(
            "No rule was found for this goal."
        )

        return False, trace

    for rule_id, symptom_id in supporting_rules:

        trace.append(
            f"Checking {rule_id} -> requires {symptom_id}"
        )

        if symptom_id in observed_symptoms:

            trace.append(
                f"{symptom_id} = YES  ✓"
            )

            trace.append(
                f"{rule_id} satisfies the goal."
            )

            trace.append(
                f"GOAL PROVED: {clean_name(goal)}  ✓"
            )

            return True, trace

        else:

            trace.append(
                f"{symptom_id} = NO  ✗"
            )

            trace.append(
                f"{rule_id} cannot prove the goal."
            )

    trace.append(
        f"GOAL NOT PROVED: {clean_name(goal)}  ✗"
    )

    return False, trace


# ============================================================
# RUN BACKWARD CHAINING
# ============================================================


def run_backward_chaining(observed_symptoms, category_symptoms):
    section("BACKWARD CHAINING")

    print()
    print("  Reasoning direction:")
    print("  POSSIBLE FAULT  →  RULE  →  REQUIRED SYMPTOM  →  FACT")
    print()

    available_goals = relevant_goals(category_symptoms)
    checked_goals = []

    while len(checked_goals) < len(available_goals):

        remaining_goals = [
            goal for goal in available_goals
            if goal not in checked_goals
        ]

        section("SELECT POSSIBLE FAULT")

        print()
        print("  Choose a possible fault to check:")
        print()

        for index, goal in enumerate(remaining_goals, start=1):
            print(f"  [{index}] {clean_name(goal)}")

        print()

        while True:
            choice = input(
                f"  Enter fault number (1-{len(remaining_goals)}): "
            ).strip()

            if choice.isdigit() and 1 <= int(choice) <= len(remaining_goals):
                goal = remaining_goals[int(choice) - 1]
                break

            print(
                f"  ! Invalid choice. Please select 1-{len(remaining_goals)}."
            )

        checked_goals.append(goal)

        proved, trace = backward_chain(goal, observed_symptoms)

        print()
        print("  " + "─" * (WIDTH - 4))
        print(f"  GOAL: {clean_name(goal)}")
        print("  " + "─" * (WIDTH - 4))

        for step in trace[1:]:
            print("  " + step)

        print()
        print("  BACKWARD CHAINING RESULT")
        print("  " + "─" * 35)

        if proved:
            print(f"  ✓ {clean_name(goal)}")
            return [goal]

        print("  ✗ Selected fault could not be proved.")

        if len(checked_goals) == len(available_goals):
            break

        while True:
            again = input(
                "\n  Would you like to check another possible fault? (yes/no): "
            ).strip().lower()

            if again in ["yes", "y"]:
                break

            if again in ["no", "n"]:
                return []

            print("  ! Please answer yes or no.")

    print()
    print("  All relevant possible faults have been checked.")
    print("  No selected fault could be proved from the observed symptoms.")

    return []


# ============================================================
# YES / NO INPUT
# ============================================================

def ask_question(symptom_id):

    question = QUESTIONS[symptom_id]

    while True:

        answer = input(
            f"  {symptom_id}  {question}\n"
            f"  > "
        ).strip().lower()

        if answer in ["yes", "y"]:
            return True

        if answer in ["no", "n"]:
            return False

        print(
            "  ! Invalid input. Please enter YES or NO."
        )
        print()


# ============================================================
# COLLECT SYMPTOMS
# ============================================================

def collect_symptoms(category_symptoms):

    observed_symptoms = []
    negative_symptoms = []

    for symptom_id in category_symptoms:

        answer = ask_question(symptom_id)

        if answer:
            observed_symptoms.append(symptom_id)
        else:
            negative_symptoms.append(symptom_id)

        print()

    return observed_symptoms, negative_symptoms


# ============================================================
# DISPLAY OBSERVED FACTS
# ============================================================

def display_facts(observed_symptoms, category_symptoms):

    section("OBSERVED FACTS")

    print()

    for symptom_id in category_symptoms:

        if symptom_id in observed_symptoms:

            print(
                f"  ✓ {symptom_id} = YES  |  "
                f"{QUESTIONS[symptom_id]}"
            )

        else:

            print(
                f"  ✗ {symptom_id} = NO   |  "
                f"{QUESTIONS[symptom_id]}"
            )


# ============================================================
# FORWARD CHAINING
# ============================================================

def run_forward_chaining(environment):

    section("1. FORWARD CHAINING")

    print()
    print("  Reasoning direction:")
    print("  OBSERVED FACTS  →  RULES  →  POSSIBLE FAULTS")
    print()
    print("  Running CLIPS inference engine...")

    environment.run()

    rules_fired = []
    forward_faults = []

    for fact in environment.facts():

        if fact.template.name == "rule-fired":

            rule_id = str(fact["rule-id"])

            if rule_id not in rules_fired:

                rules_fired.append(rule_id)

    for fact in environment.facts():

        if fact.template.name == "possible-fault":

            fault = str(fact["name"])

            if fault not in forward_faults:

                forward_faults.append(fault)

    print()
    print("  RULES FIRED")
    print("  " + "─" * 35)

    if rules_fired:

        for rule_id in rules_fired:
            print(f"  ✓ {rule_id}")

    else:

        print("  No rules were triggered.")

    print()
    print("  POSSIBLE FAULTS")
    print("  " + "─" * 35)

    if forward_faults:

        for fault in forward_faults:
            print(f"  → {clean_name(fault)}")

    else:

        print("  No fault identified.")

    return rules_fired, forward_faults


# ============================================================
# FORWARD CHAINING EXPLANATION
# ============================================================

def display_explanations(environment):

    section("3. RULE-BASED EXPLANATION")

    explanations_found = False

    print()

    for fact in environment.facts():

        if fact.template.name == "explanation":

            explanations_found = True

            print(
                f"  {fact['rule-id']}: "
                f"{fact['message']}"
            )

    if not explanations_found:

        print("  No explanation was generated.")


# ============================================================
# FINAL RESULT
# ============================================================

def display_final_result(forward_faults, backward_faults):

    title("FINAL RESULT")

    print()

    print("  FORWARD CHAINING")
    print("  " + "─" * 35)

    if forward_faults:

        for fault in forward_faults:
            print(f"  ✓ {clean_name(fault)}")

    else:

        print("  No fault identified.")

    print()

    print("  BACKWARD CHAINING")
    print("  " + "─" * 35)

    if backward_faults:

        for fault in backward_faults:
            print(f"  ✓ {clean_name(fault)}")

    else:

        print("  No fault goal proved.")

    print()

    forward_set = set(forward_faults)
    backward_set = set(backward_faults)

    print("  INFERENCE CONSISTENCY")
    print("  " + "─" * 35)

    if forward_set == backward_set:

        print(
            "  ✓ Both inference methods produced "
            "the same conclusions."
        )

    elif forward_set.intersection(backward_set):

        print(
            "  ✓ The inference methods have "
            "common conclusions."
        )

    else:

        print(
            "  ! The inference methods produced "
            "different conclusions."
        )

    print()
    print(
        "  Note: The system identifies possible faults "
        "based on the supplied symptoms."
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    # --------------------------------------------------------
    # Create CLIPS environment
    # --------------------------------------------------------

    environment = clips.Environment()

    try:

        environment.load("car_diagnosis.clp")

    except Exception as error:

        print()
        print("ERROR: Could not load car_diagnosis.clp")
        print()
        print(f"Details: {error}")
        print()
        print(
            "Make sure car_diagnosis.clp is in the "
            "same folder as this Python file."
        )

        return

    environment.reset()

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    title(
        "CAR FAULT DIAGNOSIS EXPERT SYSTEM"
    )

    print(
        "\n  Symptom-Based and Goal-Based Diagnosis"
    )

    print(
        "  Expert System for Possible Vehicle Fault Diagnosis"
    )

    # --------------------------------------------------------
    # Category selection
    # --------------------------------------------------------

    section("SELECT PROBLEM CATEGORY")

    print()

    for key, category in CATEGORIES.items():

        print(
            f"  [{key}] {category['name']}"
        )

    print()

    while True:

        category = input(
            "  Enter category number (1-6): "
        ).strip()

        if category in CATEGORIES:
            break

        print(
            "  ! Invalid choice. Please select 1-6."
        )

    selected_category = CATEGORIES[category]

    category_symptoms = selected_category["symptoms"]

    print()
    print(
        f"  Selected: {selected_category['name']}"
    )

    # --------------------------------------------------------
    # Collect symptoms
    # --------------------------------------------------------

    section("SYMPTOM COLLECTION")

    print()
    print(
        "  Answer each question with YES or NO."
    )
    print()

    observed_symptoms, negative_symptoms = (
        collect_symptoms(category_symptoms)
    )

    # --------------------------------------------------------
    # Display facts
    # --------------------------------------------------------

    display_facts(
        observed_symptoms,
        category_symptoms
    )

    # --------------------------------------------------------
    # Update CLIPS facts
    # --------------------------------------------------------

    for fact in environment.facts():

        if fact.template.name == "symptom":

            symptom_id = str(fact["id"])

            if symptom_id in observed_symptoms:

                fact.modify_slots(
                    observed=clips.Symbol("yes")
                )

    # --------------------------------------------------------
    # Select diagnosis mode
    # --------------------------------------------------------

    section("CHOOSE DIAGNOSIS MODE")

    print()
    print("  [1] Diagnose from My Symptoms")
    print("      Start with your answers and find possible faults.")
    print()
    print("  [2] Check a Possible Fault")
    print("      Start with a possible fault and verify the symptoms.")
    print()
    print("  [3] Compare Both Approaches")
    print("      Run both reasoning methods and compare the results.")
    print()

    while True:
        mode = input("  Enter your choice (1-3): ").strip()
        if mode in ["1", "2", "3"]:
            break
        print("  ! Invalid choice. Please select 1-3.")

    # Run selected inference method
    rules_fired = []
    forward_faults = []
    backward_faults = []

    if mode in ["1", "3"]:
        rules_fired, forward_faults = run_forward_chaining(environment)

    if mode in ["2", "3"]:
        backward_faults = run_backward_chaining(
            observed_symptoms, category_symptoms
        )

    # Explanation
    display_explanations(environment)

    # Final result
    if mode == "1":
        title("FINAL RESULT")
        print()
        print("  DIAGNOSIS FROM MY SYMPTOMS")
        print("  " + "─" * 35)
        if forward_faults:
            for fault in forward_faults:
                print(f"  ✓ {clean_name(fault)}")
        else:
            print("  No fault identified.")

    elif mode == "2":
        title("FINAL RESULT")
        print()
        print("  POSSIBLE FAULT CHECK")
        print("  " + "─" * 35)
        if backward_faults:
            for fault in backward_faults:
                print(f"  ✓ {clean_name(fault)}")
        else:
            print("  ✗ Selected fault was not proved.")

    else:
        display_final_result(forward_faults, backward_faults)

    # Finish
    # --------------------------------------------------------

    print()
    print(
        "╔" + "═" * (WIDTH - 2) + "╗"
    )

    print(
        "║" +
        "Diagnosis completed.".center(WIDTH - 2) +
        "║"
    )

    print(
        "╚" + "═" * (WIDTH - 2) + "╝"
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
