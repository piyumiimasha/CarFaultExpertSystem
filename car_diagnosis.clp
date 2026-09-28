;; car_diagnosis.clp

(deftemplate symptom
   (slot id)
   (slot name)
   (slot observed
      (allowed-values yes no)
      (default no))
)

(deftemplate possible-fault
   (slot name)
)

(deftemplate rule-fired
   (slot rule-id)
)

(deftemplate explanation
   (slot rule-id)
   (slot message)
)

(deffacts initial-symptoms

   ;; S01 - Carwow
   (symptom
      (id S01)
      (name engine-turns-slowly)
      (observed no))

   ;; S02 - Carwow
   (symptom
      (id S02)
      (name headlights-dim)
      (observed no))

   ;; S03 - Carwow
   (symptom
      (id S03)
      (name interior-lights-dim)
      (observed no))

   ;; S04 - Carwow
   (symptom
      (id S04)
      (name electrical-equipment-strange)
      (observed no))

   ;; S05 - Carwow
   (symptom
      (id S05)
      (name rapid-clicking-when-starting)
      (observed no))

   ;; S06 - Carwow
   (symptom
      (id S06)
      (name engine-cranks-but-does-not-start)
      (observed no))

   ;; S07 - Carwow
   (symptom
      (id S07)
      (name tyre-looks-low)
      (observed no))

   ;; S08 - Carwow
   (symptom
      (id S08)
      (name tyre-pressure-warning-remains)
      (observed no))

   ;; S09 - Express Lube
   (symptom
      (id S09)
      (name tyre-worn-on-one-edge)
      (observed no))

   ;; S10 - Express Lube
   (symptom
      (id S10)
      (name brake-squealing)
      (observed no))

   ;; S11 - Express Lube
   (symptom
      (id S11)
      (name brake-grinding)
      (observed no))

   ;; S12 - Carwow
   (symptom
      (id S12)
      (name car-vibrates-while-braking)
      (observed no))

   ;; S13 - Carwow
   (symptom
      (id S13)
      (name temperature-gauge-red)
      (observed no))

   ;; S14 - Carwow
   (symptom
      (id S14)
      (name steam-from-bonnet)
      (observed no))

   ;; S15 - Carwow / Express Lube
   (symptom
      (id S15)
      (name coolant-level-low)
      (observed no))

   ;; S16 - Carwow
   (symptom
      (id S16)
      (name oil-warning-light)
      (observed no))

   ;; S17 - Carwow
   (symptom
      (id S17)
      (name oil-level-low)
      (observed no))

   ;; S18 - Carwow
   (symptom
      (id S18)
      (name air-conditioning-not-cold)
      (observed no))

   ;; S19 - Carwow
   (symptom
      (id S19)
      (name slow-acceleration)
      (observed no))

   ;; S20 - Carwow
   (symptom
      (id S20)
      (name hesitation-during-acceleration)
      (observed no))
)

;; ============================================
;; RULES WITH EXPLANATIONS
;; ============================================

;; R01 - Weak battery
(defrule R01-weak-battery-slow-engine
   (symptom
      (id S01)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name weak-battery)))
   (assert
      (rule-fired
         (rule-id R01)))
   (assert
      (explanation
         (rule-id R01)
         (message "The engine turns slowly, indicating a possible weak battery.")))
)


;; R02 - Weak battery
(defrule R02-weak-battery-dim-headlights
   (symptom
      (id S02)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name weak-battery)))
   (assert
      (rule-fired
         (rule-id R02)))
   (assert
      (explanation
         (rule-id R02)
         (message "Dim headlights can indicate a possible weak battery.")))
)


;; R03 - Weak battery
(defrule R03-weak-battery-dim-interior-lights
   (symptom
      (id S03)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name weak-battery)))
   (assert
      (rule-fired
         (rule-id R03)))
   (assert
      (explanation
         (rule-id R03)
         (message "Dim interior lights can indicate a possible weak battery.")))
)


;; R04 - Battery problem
(defrule R04-battery-problem-electrical
   (symptom
      (id S04)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name battery-problem)))
   (assert
      (rule-fired
         (rule-id R04)))
   (assert
      (explanation
         (rule-id R04)
         (message "Strange electrical equipment behaviour can indicate a battery problem.")))
)


;; R05 - Battery or connection problem
(defrule R05-battery-starting-problem
   (symptom
      (id S05)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name battery-or-connection-problem)))
   (assert
      (rule-fired
         (rule-id R05)))
   (assert
      (explanation
         (rule-id R05)
         (message "Rapid clicking when starting can indicate a weak battery or an electrical connection problem.")))
)


;; R06 - Fuel, ignition or engine management problem
(defrule R06-engine-does-not-start
   (symptom
      (id S06)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name fuel-ignition-or-engine-management-problem)))
   (assert
      (rule-fired
         (rule-id R06)))
   (assert
      (explanation
         (rule-id R06)
         (message "If the engine cranks but does not start, the fuel, ignition or engine management system may need investigation.")))
)


;; R07 - Low tyre pressure
(defrule R07-low-tyre-pressure
   (symptom
      (id S07)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name low-tyre-pressure)))
   (assert
      (rule-fired
         (rule-id R07)))
   (assert
      (explanation
         (rule-id R07)
         (message "A visibly low tyre can indicate low tyre pressure.")))
)


;; R08 - Tyre or TPMS problem
(defrule R08-tyre-pressure-warning
   (symptom
      (id S08)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name slow-puncture-damaged-tyre-or-tpms-problem)))
   (assert
      (rule-fired
         (rule-id R08)))
   (assert
      (explanation
         (rule-id R08)
         (message "A tyre pressure warning that remains can indicate a slow puncture, damaged tyre or TPMS problem.")))
)


;; R09 - Wheel alignment problem
(defrule R09-wheel-alignment
   (symptom
      (id S09)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name wheel-alignment-problem)))
   (assert
      (rule-fired
         (rule-id R09)))
   (assert
      (explanation
         (rule-id R09)
         (message "Tyre wear on one edge can indicate a wheel alignment problem.")))
)


;; R10 - Worn brake pads
(defrule R10-worn-brake-pads
   (symptom
      (id S10)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name worn-brake-pads)))
   (assert
      (rule-fired
         (rule-id R10)))
   (assert
      (explanation
         (rule-id R10)
         (message "High-pitched brake squealing can indicate worn brake pads.")))
)


;; R11 - Serious brake wear
(defrule R11-serious-brake-wear
   (symptom
      (id S11)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name serious-brake-wear)))
   (assert
      (rule-fired
         (rule-id R11)))
   (assert
      (explanation
         (rule-id R11)
         (message "Grinding noises from the brakes can indicate serious brake wear.")))
)


;; R12 - Brake problem
(defrule R12-brake-problem
   (symptom
      (id S12)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name brake-problem)))
   (assert
      (rule-fired
         (rule-id R12)))
   (assert
      (explanation
         (rule-id R12)
         (message "Vibration while braking can indicate a brake problem.")))
)


;; R13 - Engine overheating
(defrule R13-engine-overheating
   (symptom
      (id S13)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name engine-overheating)))
   (assert
      (rule-fired
         (rule-id R13)))
   (assert
      (explanation
         (rule-id R13)
         (message "A temperature gauge entering the red zone indicates engine overheating.")))
)


;; R14 - Engine overheating
(defrule R14-steam-from-bonnet
   (symptom
      (id S14)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name engine-overheating)))
   (assert
      (rule-fired
         (rule-id R14)))
   (assert
      (explanation
         (rule-id R14)
         (message "Steam coming from the bonnet can indicate engine overheating.")))
)


;; R15 - Cooling system problem
(defrule R15-cooling-system-problem
   (symptom
      (id S15)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name cooling-system-problem)))
   (assert
      (rule-fired
         (rule-id R15)))
   (assert
      (explanation
         (rule-id R15)
         (message "A low coolant level can indicate a problem with the cooling system.")))
)


;; R16 - Oil pressure or oil problem
(defrule R16-oil-warning
   (symptom
      (id S16)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name oil-pressure-or-oil-problem)))
   (assert
      (rule-fired
         (rule-id R16)))
   (assert
      (explanation
         (rule-id R16)
         (message "An oil warning light can indicate an oil pressure or engine oil problem.")))
)


;; R17 - Low engine oil
(defrule R17-low-engine-oil
   (symptom
      (id S17)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name low-engine-oil)))
   (assert
      (rule-fired
         (rule-id R17)))
   (assert
      (explanation
         (rule-id R17)
         (message "A low engine oil level indicates a possible low-engine-oil problem.")))
)


;; R18 - Air conditioning system problem
(defrule R18-air-conditioning-problem
   (symptom
      (id S18)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name air-conditioning-system-problem)))
   (assert
      (rule-fired
         (rule-id R18)))
   (assert
      (explanation
         (rule-id R18)
         (message "Air conditioning that does not produce cold air can indicate an A/C system problem.")))
)


;; R19 - Engine performance problem
(defrule R19-slow-acceleration
   (symptom
      (id S19)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name engine-performance-problem)))
   (assert
      (rule-fired
         (rule-id R19)))
   (assert
      (explanation
         (rule-id R19)
         (message "Slower-than-normal acceleration can indicate an engine performance problem.")))
)


;; R20 - Engine performance problem
(defrule R20-acceleration-hesitation
   (symptom
      (id S20)
      (observed yes))
   =>
   (assert
      (possible-fault
         (name engine-performance-problem)))
   (assert
      (rule-fired
         (rule-id R20)))
   (assert
      (explanation
         (rule-id R20)
         (message "Engine hesitation during acceleration can indicate an engine performance problem.")))
)