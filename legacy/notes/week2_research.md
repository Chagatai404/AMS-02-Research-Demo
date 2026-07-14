# Week 2 – AMS-02 Subsystems and Multi-Detector Particle Identification

## 1. Goal

Extend the Week 1 tracker-only toy spectrometer into a simplified,
multi-detector AMS-02–like system that can:

- Reconstruct particle rigidity with the silicon tracker.
- Measure charge Z and velocity β with multiple detectors (TOF, RICH, TRD, ECAL).
- Perform toy particle identification (PID) for leptons (e±) and nuclei from He up to Fe.

---

## 2. Real AMS-02 subsystems and what they measure

### 2.1 Silicon Tracker + Magnet
- Measures track curvature → rigidity R = p / Z.
- Independent measurement of charge Z via dE/dx in silicon.
- Used for sign of charge (matter vs antimatter).

### 2.2 Time-of-Flight (TOF)
- Scintillator planes above and below the magnet.
- Provides:
  - Trigger (start/stop for the event).
  - Direction (upgoing vs downgoing).
  - Velocity β from time-of-flight over known distance.
  - Additional Z measurement from dE/dx.

### 2.3 Ring Imaging Cherenkov (RICH)
- Radiator + photodetector matrix.
- Measures β with very high precision from Cherenkov angle.
- Also gives an independent measurement of Z from Cherenkov light yield.

### 2.4 Transition Radiation Detector (TRD)
- Gas-filled straw tubes + radiator materials.
- Strongly γ-dependent signal:
  - Large signal for e± at high γ (transition radiation + ionization).
  - Much smaller signal for protons and heavy nuclei at same rigidity.
- Also usable as a Z-dependent dE/dx measurement for heavy ions.

### 2.5 Electromagnetic Calorimeter (ECAL)
- Sampling calorimeter at the bottom.
- Measures:
  - Electromagnetic shower energy E.
  - Shower shape (EM-like vs hadronic).
  - E/p ratio:
    - E/p ≈ 1 for electrons/positrons.
    - E/p < 1 for hadrons.

### 2.6 Anticoincidence Counter (ACC)
- Surrounds the tracker inside the magnet bore.
- Used to veto particles entering from the side.

---

## 3. Target species for the Week 2 toy model

- Leptons:
  - e⁻, e⁺
- Light nuclei:
  - H (Z=1), He (Z=2)
- Intermediate nuclei:
  - C (Z=6), O (Z=8)
- Heavy nuclei:
  - Si (Z=14), Fe (Z=26)

(We can later group them into charge bins such as H, He, CNO, Ne–Si, Fe.)

---

## 4. Toy observables per event

For each simulated event we will generate:

- **Global truth**
  - `species_label` ∈ {e-, e+, p, He, C, O, Si, Fe}
  - `Z_true`, `A_true`
  - True rigidity `R_true` [GV]
  - True β (`beta_true`)

- **Tracker**
  - `R_tracker` = R_true + Gaussian noise (resolution from Week 1 study).
  - `Z_trk` ≈ Z_true + noise (toy dE/dx).

- **TOF**
  - `beta_tof` ≈ beta_true + N(0, σ_β_TOF).
  - `Z_tof` ≈ Z_true + noise (dE/dx ∝ Z²).

- **RICH**
  - `beta_rich` ≈ beta_true + N(0, σ_β_RICH), with σ_β_RICH ≪ σ_β_TOF.
  - `Z_rich` ≈ Z_true + small noise.

- **TRD**
  - `TRD_e_like` in [0, 1]:
    - peaked near 1 for e± at high γ.
    - peaked near 0 for p and heavier nuclei at the same R.
  - Optional: add a weak Z dependence for nuclei.

- **ECAL**
  - `E_ecal` ∝ particle energy with noise.
  - `E_over_p`:
    - ≈ 1 ± small noise for e±.
    - ≈ 0.4–0.8 for hadrons, with fluctuations.
  - `shower_shape`:
    - scalar EM-likeness score in [0, 1].

---

## 5. Physics approximations used

- Tracker curvature relation: R_circle = p⊥ / (|q| B).
- Rigidity R = p / Z (in GV).
- dE/dx scales approximately like Z² at fixed βγ (for non-saturated Bethe-Bloch).
- TOF measures β from L / Δt with percent-level resolution.
- RICH measures β from Cherenkov angle cos θ_c = 1/(n β) with 10⁻³–10⁻⁴ precision.
- TRD signal rises with γ for relativistic leptons and saturates at high γ.
- ECAL provides EM shower energy and shape, giving strong lepton/hadron separation via E/p and shower topology.

---

## 6. Week 2 deliverables

1. This `week2_research.md` document.
2. A Python module implementing a toy "AMS-02 event generator" that:
   - Takes (species, R_true) as input.
   - Simulates β and all subsystem observables with realistic-ish resolutions.
   - Returns a dictionary or row suitable for a pandas DataFrame.
3. A notebook that:
   - Generates a multi-class dataset (e± + H–Fe).
   - Trains a simple classifier (e.g., RandomForest) to identify species from detector observables.
   - Evaluates confusion matrices and feature importance.
