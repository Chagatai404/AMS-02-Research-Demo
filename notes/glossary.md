# 🌌 AMS-02 & Cosmic Ray Glossary
Short, working definitions so I can talk to physicists without getting lost :D.

---

## 🧱 Core Physics & Particles

### **Cosmic ray**
High-energy charged particle arriving from space (mostly protons, plus helium, electrons, heavier nuclei, and a small fraction of antiparticles).

### **Primary vs secondary cosmic rays**
- **Primary**: particles accelerated in astrophysical sources (e.g., supernovae).  
- **Secondary**: products of interactions of primaries with interstellar gas or Earth’s atmosphere.

### **Dark matter (in this context)**
Hypothetical form of matter that does not emit light but affects gravity. AMS-02 searches for indirect signatures (e.g., excess antiprotons or positrons in the flux).

---

## ⚛️ Kinematics & Motion in Magnetic Fields

### **Charge (q)**
Determines how strongly a particle feels electromagnetic forces and in which direction it bends in a magnetic field (sign).

### **Momentum (p)**
“Inertia in motion.” For relativistic particles:

$$
p \approx \gamma m v
$$

### **Rigidity (R)**
Momentum per unit charge. Defined as:

$$
R = \frac{p}{|Z|e}
$$

AMS-02 often reports measurements in rigidity rather than raw momentum.

### **Lorentz force**
Force on a charged particle in a magnetic field:

$$
\vec{F} = q \, \vec{v} \times \vec{B}
$$

This leads to circular or helical motion.

### **Curvature radius (r)**
In a uniform magnetic field:

$$
r = \frac{p}{|q|B}
$$

Measuring curvature \(r\) → estimate momentum \(p\).  
Direction of curvature → determines charge sign.

---

## 📐 Detector & Measurement Concepts

### **Flux (Φ)**
Number of particles per unit area, per unit time, per unit solid angle, per unit energy (or rigidity):

$$
\Phi \approx \frac{N_{\text{signal}}}{A \cdot T \cdot \epsilon \cdot \Delta E}
$$

### **Acceptance (A)**
Effective area × solid angle of the detector for a given selection. Includes geometry + cuts.

### **Exposure time (T)**
Total “live time” during which the detector was recording valid data.

### **Efficiency (ε)**
Probability that a real particle crossing the detector is detected AND passes all cuts.

### **dE/dx (energy loss per unit length)**
Average energy lost by a charged particle per unit path length.  
Different particles leave different dE/dx signatures → useful for identification.

---

## 🛰️ AMS-02 Subsystems

### **TRD – Transition Radiation Detector**
Separates electrons/positrons from protons using transition radiation + energy deposit patterns.

### **TOF – Time of Flight**
Measures time taken to cross scintillator planes → gives speed \( \beta = v/c \) and direction (up-going vs down-going).

### **Silicon Tracker**
Measures the trajectory inside the magnetic field → determines curvature, rigidity, and charge sign.

### **ECAL – Electromagnetic Calorimeter**
Absorbs electrons, positrons, and photons; measures energy.  
Shower shape helps classify particle type.

### **RICH – Ring Imaging Cherenkov Detector**
Measures velocity very precisely using Cherenkov light.  
Helps isotope separation + particle ID.

---

## 🌞 Radiation & Space Environment

### **Cherenkov radiation**
Light emitted when a charged particle travels faster than the phase velocity of light in a medium.  
Forms a cone → used by RICH.

### **Geomagnetic cutoff**
Minimum rigidity a cosmic ray must have to reach a given location in Earth’s magnetosphere.  
Low-rigidity particles are deflected away.

### **Solar modulation**
Suppression of low-energy cosmic rays due to solar wind + solar magnetic activity.  
Higher solar activity → greater suppression.

---

## 🧪 Data & Analysis Terms

### **Event**
A single recorded passage of a particle through the detector (all hits, times, energies, etc.).

### **Selection / cuts**
Logical criteria deciding whether an event is kept (quality cuts, ID cuts, geometry cuts, etc.).

### **Background**
Events mimicking signal but not the particle/process of interest.

### **Systematic uncertainty**
Non-statistical uncertainties from imperfect knowledge of efficiencies, calibrations, models, etc.  
Not reduced by collecting more data.

