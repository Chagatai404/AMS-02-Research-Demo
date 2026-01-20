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

### **Lorentz factor (γ)**
A relativistic correction factor that appears in the momentum and energy of high-speed particles.  
Defined as:

$$
\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
$$

where $v$ is the particle’s velocity and $c$ is the speed of light.

- For slow (non-relativistic) particles: $\gamma \approx 1$.  
- For cosmic rays, $v \approx c$, so $\gamma$ can be **hundreds or thousands**.

Used in the relativistic momentum formula:

$$
p = \gamma m v,
$$

and in calculations relating energy, momentum, and rigidity.  
Crucial for AMS-02 since most detected cosmic rays are ultra-relativistic.

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

Measure $r$ → determine momentum $p$.  
Direction of curvature → charge sign.

### **Cyclotron motion**
The circular (or helical) motion of a charged particle in a uniform magnetic field.

In a uniform $\vec B$ field, a particle with charge $q$, mass $m$, and velocity $\vec v$ experiences the Lorentz force:

$$
\vec F = q\, \vec v \times \vec B
$$

The component of $\vec v$ **perpendicular** to $\vec B$ causes circular motion with **cyclotron frequency**:

$$
\omega_c = \frac{|q| B}{\gamma m}
$$

($\omega_c = |q|B/m$ in the non-relativistic limit), and **radius**:

$$
r = \frac{p_\perp}{|q|B}
$$

where $p_\perp$ is the momentum component perpendicular to $\vec B$.

If there is also a velocity component **parallel** to $\vec B$, the motion becomes a **helix** (spiral) along the field lines.  
Cyclotron motion is the basic picture behind AMS-02 track bending, rigidity measurement, and the definition of the curvature radius.

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

- Electrons/positrons → $E/R \approx 1$ (full energy deposition).
- Protons → $E/R \ll 1$.

Used with BDTs for AMS lepton–hadron separation.

---

# 🛰️ AMS-02 Subsystems

### **TRD – Transition Radiation Detector**
Separates $e^\pm$ from protons using transition radiation + energy deposit patterns.

### **TOF – Time of Flight**
Measures speed $\beta = v/c$ and direction of travel.

### **Silicon Tracker**
Reconstructs particle trajectory → determines rigidity and charge sign.

### **Si-μstrip sensors (Silicon microstrip sensors)**
Thin (~300 μm) silicon wafers patterned with many parallel microscopic readout strips.  
When a charged particle crosses the silicon, it creates electron–hole pairs that drift under an electric field and are collected by nearby strips.

Each strip acts as a tiny independent detector, giving position accuracy of **5–10 μm**.

Used in AMS-02 to:
- precisely measure particle trajectories  
- determine curvature inside the magnetic field  
- identify charge sign  
- achieve high-resolution 3D track reconstruction  

AMS uses hundreds of Si-μstrip ladders arranged in X and Y layers to reconstruct the full 3D path of each cosmic ray.

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

### **Nuclei classes (primary, secondary, mixed)**
AMS-02 discovered that cosmic-ray nuclei group naturally into three classes based on their **spectral shapes**, **rigidity slopes**, and **hardening behavior** around ~300 GV.

**1. Primary nuclei**  
    Examples: He, C, O, Fe, Ne, Mg, Si  
-   Produced directly at cosmic-ray sources (SNRs, PWNe).  
-   Show similar power-law slopes.  
-   Display nearly identical spectral hardening.  
-   Experience little fragmentation in the ISM.

**2. Secondary nuclei**  
    Examples: Li, Be, B, F  
-   Not created in sources.  
-   Formed by **spallation** of heavier nuclei (e.g., C, O) in the ISM.  
-   Have **steeper spectra** and different hardening patterns.  
-   Their flux traces propagation path length rather than source physics.

**3. Mixed-origin nuclei**  
    Examples: N, Na, Al  
-   Contain both primary and secondary components.  
-   Spectral slopes and hardenings lie **between** primary and secondary groups.  
-   Nitrogen is the classic case (~80% secondary, ~20% primary).

These classes arise **naturally from AMS-02 data**: when spectral indices, hardening positions, and rigidity dependencies are plotted, nuclei cluster into these three groups without imposing any model.

### **Spectral hardening**
A change in the slope of a cosmic-ray energy or rigidity spectrum where the spectrum becomes **less steep (flattens)** at higher energies.  
Cosmic-ray fluxes usually follow a power-law:

$$
\Phi(R) \propto R^{-\gamma}
$$

A hardening occurs when the high-energy spectral index becomes smaller:

$$
\gamma_{\text{high}} < \gamma_{\text{low}}
$$

This means high-energy particles are **more abundant** than expected from a single power-law.  
AMS-02 observed spectral hardening around **200–300 GV** in many species, including protons, helium, and heavier nuclei.  
The effect suggests changes in **source acceleration**, **diffusion properties**, or **contributions from nearby astrophysical sources** (PWNe, SNRs).

### **p̄/p ratio (antiproton-to-proton ratio)**
The ratio of cosmic-ray antiprotons to protons as a function of rigidity:

$$
\frac{\bar{p}}{p} = \frac{\text{antiproton flux}}{\text{proton flux}}
$$

Antiprotons ($\bar{p}$) are produced mainly as **secondary particles** when high-energy cosmic-ray protons collide with interstellar gas in the ISM.  
Standard models predict that the p̄/p ratio should **decrease** with increasing rigidity because secondary production becomes less efficient at high energies.

AMS-02 discovered that the p̄/p ratio **flattens** above $\sim 60$–$100$ GV, rather than continuing to fall.  
This behavior:
- is near the limit of what conventional secondary models predict,  
- may hint at **additional sources** of antiprotons (e.g., dark matter annihilation, SNR interactions),  
- tightly constrains cosmic-ray propagation models and hadronic cross sections.

Used together with the B/C ratio to test whether cosmic-ray antimatter is purely secondary or has contributions from exotic or astrophysical sources.

### **Dark matter annihilation**
A theoretical process in which two dark matter particles destroy each other and produce Standard-Model particles:

$$
\chi + \chi \rightarrow \text{SM particles (} e^+, e^-, \bar{p}, \gamma, \nu, \dots)
$$

Whether annihilation occurs depends on the type of dark matter:
- **Dirac DM:** has a distinct antimatter partner ($\chi$ and $\bar{\chi}$); annihilation is $\chi + \bar{\chi}$.  
- **Majorana DM:** particle is its own antiparticle ($\chi = \bar{\chi}$); annihilation is $\chi + \chi$.  
- **Asymmetric DM:** anti–dark matter was depleted early, so present-day annihilation is nearly zero.

If annihilation occurs today in the Milky Way halo, it could produce measurable excesses in:
- **positrons (e⁺)**  
- **antiprotons (p̄)**  
- **gamma rays (γ)**  
- **anti-nuclei (e.g., antihelium)**  

AMS-02 searches for these signatures in cosmic-ray data.  
An unexpected rise in e⁺, flattening in p̄/p, or detection of antihelium could indicate dark matter annihilation or decay.

---

# 🌞 Radiation & Space Environment

### **Cherenkov radiation**
Emitted when a charged particle exceeds the phase velocity of light in a medium → used in RICH.

### **Geomagnetic cutoff**
The minimum rigidity a cosmic ray must have to penetrate Earth’s magnetic field and reach the atmosphere or a detector in low-Earth orbit.

Earth’s magnetic field acts as a shield:
- **Low-rigidity particles** (low momentum per unit charge) are strongly deflected and cannot reach Earth.
- **High-rigidity particles** overcome magnetic deflection and pass through.

The cutoff depends strongly on latitude:
- **High near the equator** (≈ 10–15 GV): only energetic cosmic rays get through.
- **Low near the poles** (≈ 0–1 GV): even low-energy cosmic rays can enter.

AMS-02 measures cosmic rays along an orbit of 51.6° inclination, so the geomagnetic cutoff varies continuously, **affecting low-rigidity (<10 GV) flux measurements**.

The cutoff must be accounted for to avoid contamination by atmospheric secondaries and to correctly determine the true cosmic-ray flux.

### **Solar modulation**
The process by which the Sun’s magnetic field and solar wind alter the intensity and energy spectrum of cosmic rays before they reach Earth.

Cosmic rays entering the **heliosphere** interact with:
- the expanding solar wind,
- the heliospheric magnetic field (HMF),
- magnetic turbulence and drift effects,
- transient solar events (CMEs, flares).

Effects:
- Strong suppression at **low rigidities** (<10–20 GV).
- Much weaker effect at high energies (>20–30 GV).
- Produces time variations linked to the **11-year solar cycle**.
- Causes 27-day periodicities due to solar rotation.
- Creates **charge-sign–dependent modulation**, since positive and negative particles drift differently.
- After solar magnetic polarity flips, e⁺/e⁻ and p/p̄ respond differently (as observed by AMS-02).

AMS-02 measures solar modulation directly with daily, monthly, and yearly cosmic-ray fluxes.

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

