import clips


# -------------------------------------------------
# Symptom keywords
# -------------------------------------------------

SYMPTOMS = {
    "S01": [
        "engine turns slowly",
        "engine turning slowly",
        "slow engine",
        "slowly when starting",
        "engine is slow"
    ],

    "S02": [
        "headlights dim",
        "headlights are dim",
        "dim headlights",
        "head lights dim"
    ],

    "S03": [
        "interior lights dim",
        "inside lights dim",
        "interior light is dim"
    ],

    "S04": [
        "electrical equipment strange",
        "electrical problems",
        "electrical equipment behaving strangely",
        "electrical system problem"
    ],

    "S05": [
        "rapid clicking",
        "clicking sound",
        "clicking when starting",
        "clicking noise when starting"
    ],

    "S06": [
        "engine cranks but does not start",
        "engine cranks but won't start",
        "engine does not start",
        "car won't start",
        "car does not start"
    ],

    "S07": [
        "tyre looks low",
        "tire looks low",
        "flat tyre",
        "flat tire",
        "low tyre",
        "low tire"
    ],

    "S08": [
        "tyre pressure warning",
        "tire pressure warning",
        "tyre pressure light",
        "tire pressure light",
        "pressure warning remains"
    ],

    "S09": [
        "tyre worn on one edge",
        "tire worn on one edge",
        "uneven tyre wear",
        "uneven tire wear",
        "tyre wear on one side",
        "tire wear on one side"
    ],

    "S10": [
        "brake squealing",
        "brakes squeal",
        "brake squealing noise",
        "high pitched brake noise",
        "high-pitched brake noise"
    ],

    "S11": [
        "brake grinding",
        "brakes grinding",
        "grinding brakes",
        "grinding noise when braking"
    ],

    "S12": [
        "car vibrates while braking",
        "car shakes while braking",
        "vibration when braking",
        "vibrates when braking",
        "shaking when braking"
    ],

    "S13": [
        "temperature gauge red",
        "temperature gauge in red",
        "temperature is in the red",
        "engine temperature high",
        "temperature gauge overheating"
    ],

    "S14": [
        "steam from bonnet",
        "steam from hood",
        "steam coming from bonnet",
        "steam coming from hood"
    ],

    "S15": [
        "coolant level low",
        "low coolant",
        "coolant is low",
        "coolant level is low"
    ],

    "S16": [
        "oil warning light",
        "oil light is on",
        "oil warning",
        "engine oil warning light"
    ],

    "S17": [
        "oil level low",
        "low engine oil",
        "engine oil is low",
        "low oil level"
    ],

    "S18": [
        "air conditioning not cold",
        "air conditioner not cold",
        "ac not cold",
        "ac is not cold",
        "air conditioning is not cold",
        "air conditioner blowing warm air"
    ],

    "S19": [
        "slow acceleration",
        "acceleration is slow",
        "car accelerates slowly",
        "slower acceleration",
        "slow to accelerate"
    ],

    "S20": [
        "engine hesitates",
        "hesitation during acceleration",
        "engine hesitation",
        "hesitates when accelerating",
        "car hesitates when accelerating"
    ]
}


# -------------------------------------------------
# Load CLIPS
# -------------------------------------------------

environment = clips.Environment()

environment.load("car_diagnosis.clp")
environment.reset()


# -------------------------------------------------
# Get user's problem
# -------------------------------------------------

print("=" * 60)
print("        CAR FAULT DIAGNOSIS EXPERT SYSTEM")
print("=" * 60)

print("\nDescribe the problem with your car.")
print("You can mention multiple problems in one sentence.")
print("\nExample:")
print("My car makes a clicking sound when starting and the")
print("headlights are dim.")

user_input = input("\nYour problem: ")

text = user_input.lower()


# -------------------------------------------------
# Identify symptoms
# -------------------------------------------------

detected_symptoms = []

for symptom_id, keywords in SYMPTOMS.items():

    for keyword in keywords:

        if keyword in text:
            detected_symptoms.append(symptom_id)
            break


# Remove duplicates
detected_symptoms = list(dict.fromkeys(detected_symptoms))


# -------------------------------------------------
# Update CLIPS facts
# -------------------------------------------------

for fact in environment.facts():

    if fact.template.name == "symptom":

        symptom_id = str(fact["id"])

        if symptom_id in detected_symptoms:
            fact.modify_slots(observed=clips.Symbol("yes"))


# -------------------------------------------------
# Show detected facts
# -------------------------------------------------

print("\n" + "-" * 60)
print("DETECTED SYMPTOMS")
print("-" * 60)

if detected_symptoms:

    for fact in environment.facts():

        if fact.template.name == "symptom":

            if str(fact["id"]) in detected_symptoms:
                print(
                    f"{fact['id']}: "
                    f"{fact['name']} "
                    f"-> observed yes"
                )

else:

    print("No known symptoms were detected.")


# -------------------------------------------------
# Run CLIPS inference engine
# -------------------------------------------------

environment.run()


# -------------------------------------------------
# Display rules that fired
# -------------------------------------------------

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


# -------------------------------------------------
# Display possible faults
# -------------------------------------------------

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


print("\n" + "=" * 60)
print("Diagnosis completed.")
print("=" * 60)