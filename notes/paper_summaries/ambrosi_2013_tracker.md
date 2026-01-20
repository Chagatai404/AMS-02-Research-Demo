# 📄 Ambrosi et al. (2013) — AMS-02 Track Reconstruction and Rigidity Measurement  
**Summary based on annotated PDF**  
*33rd International Cosmic Ray Conference (ICRC), Rio de Janeiro, 2013*  
PDF: *AMS-02 Track Reconstruction and Rigidity Measurement* :contentReference[oaicite:1]{index=1}

---

## 1. Overview

This paper explains how the **AMS-02 Silicon Tracker** reconstructs charged-particle trajectories and measures **rigidity and charge sign** with high precision. It covers:

- Tracker geometry and hardware  
- Cluster formation and hit reconstruction  
- Track-finding algorithms  
- Rigidity-fitting methods  
- Charge-confusion suppression using machine learning (BDT)

This paper is the **core technical reference for Week 1 of the AMS-02 demo** (track simulation and rigidity).

---

## 2. AMS-02 Tracker Hardware

- The Tracker consists of **2284 double-sided silicon microstrip sensors**  
- Each sensor size: **72 × 41 × 0.3 mm³**  
- **9 tracker layers** span the full height of AMS  
- Inner layers (L2–L8) are inside the magnetic field  
- Additional layers above TRD and ECAL extend the **lever arm for rigidity**

### Spatial Resolution:

- **~10 μm in bending (Y) direction**
- **~30 μm in non-bending (X) direction**

These resolutions allow precise curvature and charge-sign measurement.

---

## 3. From Raw Signals to 3D Hits

### Step 1 — Raw Clusters

- Raw tracker data are first grouped into **Raw Clusters**
- These are contiguous strips with signals above threshold
- Raw clusters are processed to form **TrClusters**

### Step 2 — 1D Position Reconstruction

- Each TrCluster gives:
  - One coordinate in **bending (Y)** or **non-bending (X)**
- The **center of gravity of strip signals** is used to estimate the hit position
- Depending on the incident angle, 2- or 3-strip reconstruction is used

### Step 3 — X/Y Correlation → 3D Hits (TrRecHit)

- X-side AND Y-side clusters are correlated to form:
  - **TrRecHit = full 3D space point**
- For Z ≥ 2 particles, the correlation is clean
- For Z = 1 (protons, electrons), ambiguity is higher due to low signal-to-noise

---

## 4. Track-Finding Strategy

The tracker has ~**196,000 readout channels**, producing ~**100 clusters per event**, but only ~**18 belong to the real track**.

### Algorithm Overview:

1. Track search begins in **inner layers (L3–L8)**
2. Uses **Y-projection first**
3. Builds a straight seed from:
   - One cluster in L3 or L4  
   - One cluster in L7 or L8  
4. If a third hit is found, a **circular fit** is tested
5. 3D candidates are built by X/Y combination
6. Tracks are tested with:
   - Linear fits
   - Path-integral fits
7. The best-χ² candidate is chosen

### Track Classes:

- **Inner**: no external hits
- **L1**: hit on layer 1 only
- **L9**: hit on layer 9 only
- **L19**: hits on both L1 and L9 (best rigidity resolution)

---

## 5. Rigidity Measurement Methods

Rigidity is measured from **track curvature in the magnetic field**.

Three independent fitting algorithms are used:

### (A) Path-Integral Fit — Straight-Segment Approximation  
### (C) Path-Integral Fit — Runge–Kutta Trajectory  
### (K) Monte-Carlo-Based Fit (best below 40 GV)

Why multiple fits?

- If A and C disagree → **bad reconstruction likely**
- K fit improves precision when:
  - Multiple scattering dominates  
  - Energy loss is important  

---

## 6. Rigidity Resolution & Maximum Detectable Rigidity (MDR)


### **100% Relative Error (MDR) for Protons**

| Track Type | MDR |
|------------|------|
| Inner      | 240 GV |
| L1         | 540 GV |
| L9         | 750 GV |
| L19        | **2000 GV** |

### **100% Relative Error (MDR) for Helium**

| Track Type | MDR |
|------------|------|
| Inner      | 400 GV |
| L1         | 1100 GV |
| L9         | 1600 GV |
| L19        | **3200 GV** |

✅ Larger track span  
→ smaller curvature error  
→ higher rigidity reach

---

## 7. Charge Confusion

Charge confusion = particle reconstructed with **wrong sign of curvature**.

### Two Physical Sources:

### (1) **Intrinsic (Resolution-Limited)**  
At high rigidity:
- Curvature → very small
- Gaussian uncertainty can cross zero curvature
- Wrong sign assigned  
✅ Unavoidable, but **predictable**

### (2) **Interaction-Induced**
- Particle scatters inside AMS material
- Trajectory kink appears
- Finite tracker resolution causes wrong curvature fit  
✅ Can be **suppressed with event features**

---

## 8. Boosted Decision Tree (BDT) for Charge Confusion

A **machine-learning classifier** using **22 event variables**:

Key inputs:
- Agreement between different rigidity fits  
- Presence of extra hits near track  
- Activity in TOF, ECAL, veto counters  

The BDT:

- Is trained on Monte-Carlo simulated data  
- Is tested on real ISS data  
- Shows very good agreement between simulation and real charge-confusion rates

This technique is critical for:

- e⁺/e⁻ separation  
- p̄/p ratio precision  
- Anti-nuclei searches  

---

## 9. Why This Paper Is Central to Your Project

### Week 1 — Track Simulation
- Layer geometry  
- Curvature → rigidity conversion  
- Track-finding logic  
- Bending vs non-bending coordinates  

### Week 2 — Particle Identification
- Track-detector association  
- Charge magnitude vs charge sign  

### Week 3 — Flux Reconstruction
- Rigidity resolution  
- Acceptance vs track class  

### Week 6 — Antimatter Physics
- Charge confusion limits  
- p̄/p and e⁺ excess reliability  

---

