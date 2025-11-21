# AMS-02 & Cosmic Ray Glossary

Short, working definitions so I can talk to physicists without getting lost :D.

---

## Core Physics & Particles

- **Cosmic ray**  
  High-energy charged particle arriving from space (mostly protons, plus helium, electrons, heavier nuclei, and a small fraction of antiparticles).

- **Primary vs secondary cosmic rays**  
  *Primary*: particles accelerated in astrophysical sources (e.g., supernovae).  
  *Secondary*: products of interactions of primaries with interstellar gas or Earth’s atmosphere.

- **Dark matter (in this context)**  
  Hypothetical form of matter that does not emit light but affects gravity. AMS-02 searches for indirect signatures (e.g. excess antiprotons or positrons in the flux).

---

## Kinematics & Motion in Magnetic Fields

- **Charge (\(q\))**  
  Determines how strongly a particle feels electromagnetic forces and in which direction it bends in a magnetic field (sign).

- **Momentum (\(p\))**  
  “Inertia in motion.” For relativistic particles, \( p \approx \gamma m v \).

- **Rigidity (\(R\))**  
  Defined as \( R = \frac{p}{|Z|e} \).  
  It’s basically momentum per unit charge. Detectors like AMS often work in terms of rigidity instead of raw momentum.

- **Lorentz force**  
  \( \mathbf{F} = q\, \mathbf{v} \times \mathbf{B} \).  
  Gives the force on a moving charged particle in a magnetic field. Leads to circular/helical motion.

- **Curvature radius (\(r\))**  
  In a uniform magnetic field, the track radius is  
  \[
    r = \frac{p}{|q|B}
  \]  
  Measuring \(r\) → estimate \(p\); the direction of curvature → sign of \(q\).

---

## Detector & Measurement Concepts

- **Flux (\(\Phi\))**  
  Number of particles per unit area, per unit time, per unit solid angle, per unit energy (or rigidity).  
  Roughly:  
  \[
    \Phi \approx \frac{N_{\text{signal}}}{A \cdot T \cdot \epsilon \cdot \Delta E}
  \]

- **Acceptance (\(A\))**  
  Effective area × solid angle of the detector for a given selection. Includes geometric constraints and selection cuts.

- **Exposure time (\(T\))**  
  Total “live” time during which the detector was recording data.

- **Efficiency (\(\epsilon\))**  
  Probability that a real particle crossing the detector is actually detected and passes all selection cuts.

- **dE/dx (energy loss per unit length)**  
  Average energy lost by a charged particle per unit path length in a material. Different particles show different dE/dx patterns → useful for identification.

---

## AMS-02 Subsystems (Conceptual)

- **TRD – Transition Radiation Detector**  
  Distinguishes light particles (like electrons/positrons) from heavier ones (like protons) using transition radiation and energy deposit patterns.

- **TOF – Time of Flight**  
  Measures the time a particle takes to cross between scintillator planes → gives its speed (\(\beta = v/c\)) and direction (up-going vs down-going).

- **Silicon Tracker**  
  Measures the particle’s trajectory in the magnetic field with high precision → determines curvature, rigidity, and charge sign.

- **ECAL – Electromagnetic Calorimeter**  
  Absorbs and measures the energy of electrons, positrons, and photons. The pattern of the energy “shower” helps classify the particle.

- **RICH – Ring Imaging Cherenkov Detector**  
  Measures velocity very precisely using Čerenkov light. Useful for separating isotopes and improving particle ID.

---

## Radiation & Space Environment

- **:Cherenkov radiation**  
  Light emitted when a charged particle travels through a medium faster than light travels in that medium. Forms a cone → used by RICH.

- **Geomagnetic cutoff**  
  Minimum rigidity a cosmic ray must have to reach a given point in Earth’s magnetosphere. Low-rigidity particles are deflected away.

- **Solar modulation**  
  Change in low-energy cosmic-ray flux due to the solar wind and solar magnetic activity. Stronger solar activity → more suppression of low-energy flux.

---

## Data & Analysis Terms

- **Event**  
  One recorded passage of a particle through the detector (all hits, times, energies, etc. for that particle).

- **Selection / cuts**  
  Logical conditions used to decide whether an event is kept in the analysis (quality cuts, ID cuts, etc.).

- **Background**  
  Events that mimic the signal but are not the type of particle or process we are truly interested in.

- **Systematic uncertainty**  
  Non-statistical uncertainty from imperfect knowledge of efficiencies, calibrations, models, etc. Not reduced by just collecting more data.

