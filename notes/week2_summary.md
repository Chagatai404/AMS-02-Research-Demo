# Week 2 – Multi-Detector Particle Identification (PID)

## Overview

Week 2 extends the **tracker-only spectrometer developed in Week 1** into a simplified **AMS-02–like multi-detector system** capable of performing **particle identification (PID)**.

While Week 1 focused on **rigidity reconstruction from track curvature**, Week 2 introduces additional detector observables that allow the system to **distinguish between particle species** such as electrons, protons, and heavier nuclei.

The goal is to reproduce the **core principle used in AMS-02**: combining information from multiple detectors to classify cosmic ray particles.

---

# 1. From Tracker Reconstruction to Particle Identification

### Week 1 recap

In Week 1 a **simulated silicon tracker** was built that could:

1. Simulate charged particle motion in a magnetic field
2. Generate silicon tracker hits
3. Reconstruct track curvature via circle fitting
4. Recover **particle rigidity**

Rigidity is defined as:

```
R = p / Z
```

where  
- `p` = momentum  
- `Z` = particle charge.

The tracker therefore measures **momentum per charge**, but *cannot uniquely determine the particle species*.

To identify particles we need **additional observables**.

---

# 2. AMS-02 Multi-Detector Concept

Real cosmic-ray experiments like **AMS-02** combine several detectors, each measuring different physical properties.

The simplified Week 2 model includes the following subsystems.

---

## 2.1 Silicon Tracker

Provides:

- Rigidity `R` from track curvature
- Charge estimate from ionization energy loss (dE/dx)

Observables:

```
-R_tracker
-Z_trk
```

There is a full Week 1 tracker integration for the Week 2 project, which is optional to turn on and off for faster dataset generation.

---

## 2.2 Time of Flight (TOF)

Measures the **particle velocity** from travel time between scintillator planes.

```
β = v / c
```

Observables:

```
-beta_tof
-Z_tof
```

The charge estimate comes from **energy deposition**, which approximately scales with `Z²`.

---

## 2.3 Ring Imaging Cherenkov (RICH)

Measures velocity with very high precision using **Cherenkov radiation**.

Cherenkov angle relation:

```
cos(θc) = 1 / (n β)
```

Observables:

```
-beta_rich
-Z_rich
```

RICH provides the **most precise velocity measurement** in the system.

---

## 2.4 Transition Radiation Detector (TRD)

Separates **leptons (e±)** from hadrons.

Transition radiation intensity increases with the **Lorentz factor**

```
γ = E / m
```

Electrons therefore produce a much stronger signal than protons at the same rigidity.

Observable:

```
-TRD_e_like
```

Values close to **1 → electron-like**  
Values close to **0 → hadron-like**

---

## 2.5 Electromagnetic Calorimeter (ECAL)

Measures the **energy deposited by the particle shower**.

Important PID variable:

```
E / p
```

- electrons → `E/p ≈ 1`
- hadrons → `E/p < 1`

Observables:

```
-E_ecal
-E_over_p
-shower_shape
```

---

# 3. Particle Species in the Simulation

The Week 2 model simulates several cosmic-ray species:

### Leptons
- e⁻
- e⁺

### Light nuclei
- H (proton)
- He

### Intermediate nuclei
- C
- O

### Heavy nuclei
- Si
- Fe

These represent a simplified set of **cosmic-ray charge groups** commonly studied in space experiments.

---

# 4. Event Generation Pipeline

Each simulated event follows this pipeline:

```
Choose particle species
       ↓
Sample true rigidity
       ↓
Compute true velocity β
       ↓
Generate detector responses
    - Tracker
    - TOF
    - RICH
    - TRD
    - ECAL
       ↓
Store observables in dataset
       ↓
Train ML classifier
       ↓
Evaluate particle identification accuracy
```

The output dataset contains detector observables such as:

```
R_tracker
beta_tof
beta_rich
Z_trk
Z_tof
Z_rich
TRD_e_like
E_over_p
shower_shape
```

---

# 5. Machine Learning Particle Identification

A **RandomForest classifier** was trained to identify particle species from detector observables.

Example model configuration:

```python
RandomForestClassifier(
    n_estimators=300,
    min_samples_leaf=2,
    random_state=42
)
```

The model learns correlations between detector responses and particle type.

Evaluation metrics include:

- **Confusion matrices**
- **Nuclei separation**
- **Accuracy vs rigidity**
- **Feature importance**

---

# 6. Integration with Week 1 Tracker

The simple implementation uses a **parameterized tracker resolution model**.

However, the full framework is designed to integrate directly with the **Week 1 tracker simulation**.

This connects the **physics-based tracker simulation** to the **PID framework**.

---

# 7. Key Results

The Week 2 model demonstrates that combining multiple detectors enables effective particle identification.

Key observations:

- **Electrons** are strongly separated from hadrons using  
  - TRD signal  
  - ECAL shower variables.

- **Charge measurements** from tracker, TOF, and RICH allow separation of nuclei by `Z`.

- PID performance depends on **rigidity** because detector resolutions change with energy.

- The full **Week 1 tracker integration** slightly increases model accuracy.

---

# 8. Week 2 Deliverables

Week 2 produced:

- `week2_research.md` – overview of AMS-02 subsystems and physics
- **PID event generator** producing simulated detector responses
- **Multi-class dataset** for cosmic-ray particles
- **Machine learning classifier** for particle identification
- **Performance plots and confusion matrices**

These components together form a simplified **cosmic-ray particle identification pipeline**.

---