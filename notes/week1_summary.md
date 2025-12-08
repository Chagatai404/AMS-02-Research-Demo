# Week 1 – Charged Particle Motion in a Magnetic Field and Track Reconstruction

This document explains **what was built in Week 1**, the **physics and mathematics behind it**, and **how each major code block works**. The goal is to fully understand and clearly explain how a magnetic spectrometer (like AMS‑02) measures particle momentum and charge sign from track curvature.

---

## 1. Overview: What Week 1 Achieves

In Week 1, a **mini magnetic spectrometer simulator** was built:

1. Started with a **charged particle with a given rigidity** (momentum per charge, in GV).
2. Converted this into **relativistic momentum, velocity, and Lorentz factor**.
3. Simulated its motion in a **uniform magnetic field** using a **Boris pusher** (a physics‑accurate numerical integrator).
4. The motion becomes a **3D helix**.
5. Placed **silicon tracker layers** at fixed z positions.
6. Intersections of the helical track with these layers were estimated to generate **hit points**.
7. Added **measurement noise** to simulate detector resolution.
8. From these noisy hits **the curvature was reconstructed by circle fitting**.
9. From curvature **momentum and rigidity** were recovered and the **detector resolution and bias** was evaluated.

This reproduces, in simplified form, the exact principle behind **AMS‑02 rigidity measurement**.

---

## 2. Core Physics: Why Charged Particles Bend

### 2.1 Lorentz Force

The fundamental law governing the motion is the **Lorentz force**:

[ \vec{F} = q , \vec{v} \times \vec{B} ]

* ( q ): particle charge
* ( \vec{v} ): velocity
* ( \vec{B} ): magnetic field

Key consequence:

* The force is always **perpendicular to the velocity**
* Therefore the magnetic field **does no work**
* The **speed stays constant**, only the **direction changes**

This causes **circular/helical motion in the plane perpendicular to the magnetic field**.

---

### 2.2 Decomposing the Velocity

The velocity is splited into two parts:

* Parallel to the field:
  [ \vec{v}_{||} = v \cos\theta ]
* Perpendicular to the field:
  [ \vec{v}_{\perp} = v \sin\theta ]

where ( \theta ) is the **pitch angle** between ( \vec{v} ) and ( \vec{B} ).

Results:

* ( \vec{v}_{\perp} ) → circular motion
* ( \vec{v}_{||} ) → straight-line drift

Together they form a **helix**.

---

### 2.3 Cyclotron Frequency and Curvature Radius

The bending frequency (gyrofrequency) is:

* Non‑relativistic:
  [ \omega_c = \frac{|q| B}{m} ]
* Relativistic:
  [ \omega_c = \frac{|q| B}{\gamma m} ]

The curvature radius of the circular projection is:

[ R = \frac{p_{\perp}}{|q| B} ]

with:

[ p_{\perp} = p \sin\theta ]

This is the **fundamental magnetic spectrometer equation**.

---

## 3. Relativistic Kinematics and Rigidity

In high‑energy physics:

[ E^2 = p^2 + m^2 ]

is used. From this:

[ \gamma = \frac{E}{m}, \quad \beta = \frac{v}{c} = \sqrt{1 - \frac{1}{\gamma^2}} ]

### Rigidity

Rigidity is defined as:

[ \mathcal{R} = \frac{p}{Z} ]  (in GV)

So:

[ p = Z \mathcal{R} ]

Rigidity is what AMS actually measures from curvature.

---

## 4. Numerical Method: The Boris Algorithm

*Reference:https://www.particleincell.com/2011/vxb-rotation/*

A generic ODE solver is **not** used for final tracking. Instead the **Boris pusher** is used, which is:

* Symplectic (energy‑conserving)
* Time‑reversible
* Stable for long trajectories
* Standard in plasma physics and beam dynamics

### Key Idea

Instead of integrating acceleration directly, Boris:

1. **Rotates the velocity vector around the magnetic field** by the correct gyro‑angle
2. Moves the particle forward using the rotated velocity

This exactly preserves speed in a pure magnetic field.

---

## 5. Structure of the Physics Engine

### 5.1 Rigidity → ( \beta, \gamma, p )

Mathematically:

[
p = Z \mathcal{R},\quad
E = \sqrt{p^2 + m^2},\quad
\gamma = \frac{E}{m},\quad
\beta = \sqrt{1 - \frac{1}{\gamma^2}}
]

Used to build the relativistic velocity magnitude:

[ v = \beta c ]

---

### 5.2 Building the Velocity Vector from Pitch Angle

[
\vec{v} = v_{||} \hat{B} + v_{\perp} \hat{e}_{\perp}
]

Where:

[
v_{||} = v \cos\theta,
\quad
v_{\perp} = v \sin\theta
]

This controls how tightly the helix winds.

---

### 5.3 Relativistic Boris Update

We use an **effective mass**:

[ m_{eff} = \gamma m ]

Then the Boris update rotates ( \vec{v} ) by:

[ \Delta \theta = \omega_c \Delta t = \frac{qB}{\gamma m} \Delta t ]

Position update:

[ \vec{r}_{n+1} = \vec{r}*n + \vec{v}*{n+1} \Delta t ]

---

## 6. Charge Sign and Bending Direction

From:

[ \vec{F} = q \vec{v} \times \vec{B} ]

Changing the **sign of ( q )** reverses the bending direction.

Thus:

* Proton (Z = +1) → bends one way
* Antiproton (Z = −1) → bends the opposite way

This is how AMS identifies antimatter.

---

## 7. Track Reconstruction by Circle Fitting

In the x–y bending plane, the track is approximately a circle:

[ (x - x_c)^2 + (y - y_c)^2 = R^2 ]

Rewrite this as:

[ x^2 + y^2 + A x + B y + C = 0 ]

Then solve for ( A, B, C ) using **least‑squares fitting**.

Recovered values:

[
x_c = -A/2,\quad y_c = -B/2,\quad R = \sqrt{x_c^2 + y_c^2 - C}
]

From the fitted radius momentum is recovered:

[ p_{\perp} = |q| B R ]

---

## 8. Silicon Tracker Simulation

### 8.1 Geometry

Tracker layers at fixed z are placed:

[ z_1, z_2, ..., z_7 ]

These are planes where the detector records hit points.

---

### 8.2 Track–Layer Intersection

Between two simulation steps:

[ z_1 \le z_L \le z_2 ]

Interpolate:

[
\alpha = \frac{z_L - z_1}{z_2 - z_1},\quad
x_L = x_1 + \alpha(x_2 - x_1)
]

This gives the ideal hit location.

---

### 8.3 Measurement Noise

Real detectors are not perfect. Gaussian noise is added:

[
x_{meas} = x_{true} + \mathcal{N}(0, \sigma),
\quad
y_{meas} = y_{true} + \mathcal{N}(0, \sigma)
]

Typical value used:

[ \sigma = 50 ; \mu\text{m} ]

---

## 9. Curvature Resolution and Performance Analysis

For each event:

1. Simulate a track
2. Generate noisy hits
3. Fit a circle
4. Compute relative error:

[ \delta R = \frac{R_{fit} - R_{true}}{R_{true}} ]

### Performance Metrics

* **Bias**: mean of ( \delta R )
* **Resolution**: Gaussian σ of ( \delta R )
* **Resolution vs Rigidity**: harder at high R
* **Resolution vs Pitch**: degrades as tracks become more parallel to z
* **Pull distribution**:

[ \text{pull} = \frac{R_{fit} - R_{true}}{\sigma} ]

Correct error model → pulls follow ( \mathcal{N}(0,1) )

---

## 10. Libraries and Their Roles

| Library    | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| NumPy      | Vector math, cross products, linear algebra, random numbers |
| SciPy      | Gaussian fitting (`norm.fit`), ODE solver (`solve.ivp`)     |
| Pandas     | Store event and hit tables                                  |
| Matplotlib | All trajectory and performance plots                        |

---

## 11. Conceptual Pipeline

```
Rigidity (GV)
   ↓
Relativistic kinematics (p, γ, β)
   ↓
Initial velocity with pitch angle
   ↓
Boris pusher in magnetic field
   ↓
3D helical trajectory
   ↓
Tracker layer intersections
   ↓
Gaussian hit smearing
   ↓
Circle fitting
   ↓
Curvature → Rigidity reconstruction
   ↓
Detector resolution analysis
```
---