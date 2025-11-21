# 🌌 AMS-02 & Cosmic Ray Glossary
Short, working definitions so I can talk to physicists without getting lost :D.

---

# 🧱 Core Physics & Particles

### **Cosmic ray**
High-energy charged particle arriving from space (mostly protons, plus helium, electrons, heavier nuclei, and a small fraction of antiparticles).

### **Primary vs secondary cosmic rays**
- **Primary**: particles accelerated in astrophysical sources (e.g., supernovae).  
- **Secondary**: products of interactions of primaries with interstellar gas or Earth’s atmosphere.

### **Dark matter (in this context)**
Hypothetical form of matter that does not emit light but affects gravity. AMS-02 searches for indirect signatures (e.g., excess antiprotons or positrons in the flux).

---

# ⚛️ Kinematics & Motion in Magnetic Fields

### **Charge (q)**
Determines how strongly a particle feels electromagnetic forces and in which direction it bends in a magnetic field (sign).

### **Momentum (p)**
“Inertia in motion.” For relativistic particles:

$$
p \approx \gamma m v
$$

### **Rigidity (R)**
Momentum per unit charge:

$$
R = \frac{p}{|Z|e}
$$

AMS-02 often reports measurements in rigidity rather than raw momentum.

### **Lorentz force**

$$
\vec{F} = q \, \vec{v} \times \vec{B}
$$

Determines curvature and helical motion.

### **Curvature radius (r)**

$$
r = \frac{p}{|q|B}
$$

Measure \(r\) → determine momentum \(p\).  
Direction of curvature → charge sign.

---

# 📐 Detector & Measurement Concepts

### **Flux (Φ)**

$$
\Phi \approx \frac{N_{\text{signal}}}{A \cdot T \cdot \epsilon \cdot \Delta E}
$$

Particles per area, time, solid angle, and energy/rigidity.

### **Acceptance (A)**
Effective area × solid angle of the detector including geometry + cuts.

### **Exposure time (T)**
Total “live” time during which data were recorded.

### **Efficiency (ε)**
Probability a real particle is detected AND passes all cuts.

### **dE/dx (energy loss per unit length)**
Charged-particle energy loss in matter.  
Useful for particle identification.

### **E/R ratio (Energy–Rigidity ratio)**

$$
\frac{E_{\text{ECAL}}}{R_{\text{Tracker}}}
$$

- Electrons/positrons → \(E/R \approx 1\) (full energy deposition).
- Protons → \(E/R \ll 1\).

Used with BDTs for AMS lepton–hadron separation.

---

# 🛰️ AMS-02 Subsystems

### **TRD – Transition Radiation Detector**
Separates \(e^\pm\) from protons using transition radiation + energy deposit patterns.

### **TOF – Time of Flight**
Measures speed \( \beta = v/c \) and direction of travel.

### **Silicon Tracker**
Reconstructs particle trajectory → determines rigidity and charge sign.

### **ECAL – Electromagnetic Calorimeter**
Measures energy and shower shape of leptons/photons.

### **RICH – Ring Imaging Cherenkov Detector**
Measures velocity with Cherenkov light → isotope separation.

### **ACC – Anti-Coincidence Counters**
Reject side-entering particles to maintain clean event samples.

---

# 🌌 Cosmic-Ray Composition & Astrophysical Sources

### **ISM – Interstellar Medium**
Gas + dust filling space between stars.  
Cosmic rays diffuse, scatter, and undergo spallation in the ISM.

### **B/C ratio (Boron-to-Carbon ratio)**
Key observable in cosmic-ray propagation:

- **Boron**: mostly **secondary**, produced by spallation in the ISM.  
- **Carbon**: mostly **primary**.

Thus:

$$
\frac{B}{C}(E)
$$

informs us about:
- amount of material traversed  
- diffusion coefficient  
- transport models  
- distinguishing dark-matter vs pulsar/SNR scenarios

AMS-02 provides the highest precision B/C ratio measurements to date.

### **SNRs – Supernova Remnants**
Shock regions from exploded massive stars.  
Leading source candidates for **primary cosmic-ray acceleration** via diffusive shock acceleration.

Contribute to:
- hardening in electron spectra  
- possible features in nuclei spectra

### **PWNe – Pulsar Wind Nebulae**
Highly magnetized bubbles powered by pulsars.

Why important:
- Produce large numbers of high-energy **e⁺/e⁻ pairs**  
- Strong candidate explanation for the **positron excess** seen by AMS-02  
- Compete with dark-matter interpretations

---

# 🌞 Radiation & Space Environment

### **Cherenkov radiation**
Emitted when a charged particle exceeds the phase velocity of light in a medium → used in RICH.

### **Geomagnetic cutoff**
Minimum rigidity required for CRs to enter Earth’s magnetosphere at a given latitude.

### **Solar modulation**
Suppression of low-energy CRs due to solar wind + solar magnetic activity.

---

# 🧪 Data Analysis & Simulation Terms

### **Event**
One recorded particle passage with all detector information.

### **Selection / cuts**
Logical filters for quality, geometry, particle ID, etc.

### **Background**
Non-signal events that mimic signal.

### **Systematic uncertainty**
Non-statistical uncertainties (calibration, efficiency, modeling).

### **Monte Carlo simulations (MC)**
Computer simulations modeling:

- detector response  
- cosmic-ray propagation  
- shower formation in ECAL  
- acceptance & efficiency  
- charge confusion  
- background estimation  

AMS uses **Geant4-based full simulations** and fast MC for analysis and systematics.

---

