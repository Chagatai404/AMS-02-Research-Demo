# 📚 AMS-02 Reading List

This document tracks the papers and resources I am studying to build a solid understanding of AMS-02 physics, detector subsystems, and cosmic-ray analysis.

---

## ⭐ Paper List (Week 1)

### **1. AMS-02 in space: physics results, overview, and challenges**  
**Nicola Tomassetti (2015)**  
*Nuclear and Particle Physics Proceedings 265–266, pp. 245–247*  
📄 *Personal annotated PDF in repo* (uploaded as: `AMS-02 physics results, overview, and challenges_251121_130512.pdf`) :contentReference[oaicite:1]{index=1}

**Why this paper matters:**  
- Gives a **complete overview** of the AMS-02 detector on the ISS.  
- Explains the purpose of each subdetector (TRD, TOF, Tracker, RICH, ECAL).  
- Shows how AMS distinguishes leptons vs hadrons using **redundant systems**.  
- Presents **lepton flux measurements (1–500 GeV)** and their implications.  
- Discusses **challenges** such as:
  - charge-confusion  
  - detector calibration  
  - systematic uncertainties  
  - solar modulation effects  
- Introduces the main open physics questions:
  - What sources cause the rise in positron fraction at high energies?
  - Is it dark matter annihilation or nearby astrophysical objects **(PWNe/SNRs)**?
  - How do we constrain propagation models with **B/C ratios**?

**Key Figures to revisit later:**  
- *Figure 1*: AMS-02 subsystem layout (page 2)  
- *Figure 2*: Positron fraction vs energy (page 3)  
---

### 2. The AMS-02 Detector on the ISS – Status and Highlights After 11 Years on Orbit  
**Valerio Vagelli, Maura Graziani (2023)**  
*Journal of Physics: Conference Series 2429 (2023) 012002* :contentReference[oaicite:1]{index=1}  

**Why this paper matters:**  
- Up-to-date **status report** after 11 years of AMS-02 operations on the ISS.  
- Describes:
  - Current detector performance and stability over time.  
  - Major physics results across **leptons, antiprotons, and nuclei** (incl. new spectral features and hardenings).  
  - Long-term, time-resolved flux measurements (solar-cycle effects, daily/monthly variations).  
- Shows how AMS-02 reached collider-like precision in cosmic-ray measurements.  
- Very useful for:
  - Understanding **what AMS-02 is doing *right now***.  
  - Motivating later modules on **time dependence** and **systematics**.

---

### 3. AMS-02 Track Reconstruction and Rigidity Measurement  
**G. Ambrosi et al. (2013), 33rd International Cosmic Ray Conference (ICRC)** :contentReference[oaicite:2]{index=2}  

**Why this paper matters:**  
- Focuses on the **Silicon Tracker**, which is central to Week 1 (track simulation).  
- Explains:
  - How raw silicon hits → clusters → 3D hits → tracks.  
  - Different **track-fitting algorithms** (path-integral fits, Runge–Kutta, Monte Carlo based fit).  
  - How **rigidity resolution** depends on track span (inner, L1, L9, L19) and energy.  
  - How **charge confusion** arises and how a **BDT** is used to identify bad tracks.  
- Directly relevant for:
  - Designing your **toy track-reconstruction pipeline**.  
  - Understanding **Maximum Detectable Rigidity (MDR)**.  
  - Connecting simulation choices (noise, misalignment, MC) to real AMS-02 performance.

---

## 🗂️ How This Reading List Will Be Used

Each listed paper will eventually have a dedicated summary under:
- *notes/paper_summaries/*

