# Summary of 2404.00238v1.md

**Token Usage**: Input: 9767, Output: 837, Total: 10604

---

### Main Idea

- **Primary Research Objective:** The paper addresses the challenge of creating a uniform, large-area Fermi gas in two dimensions (2D) for studying quantum phenomena. It aims to produce a flat, disk-shaped sample of 6Li atoms with a consistent area density.
- **Motivation and Significance:** Exploring 2D quantum phenomena in ultracold atom experiments requires samples with high density uniformity. Existing methods either compress 3D samples or use optical lattices, but these have limitations. The paper's method aims to create a flat, homogeneous 2D Fermi gas by directly homogenizing the in-plane trapping potential.
- **Proposed Approach:** The authors use a programmable optical potential, adjusted via a spatial light modulator (SLM) within a feedback loop, to flatten the in-plane trapping potential. This approach allows for a uniform area density, even at low atomic densities required for achieving the 2D regime.

### Technologies

- **Experimental Setup:** The experiment begins with a degenerate Fermi gas of 6Li prepared via sympathetic cooling with 23Na atoms in a magnetic trap. This is then transferred to an oblate optical dipole trap (ODT) formed by a 1064-nm laser beam.
- **Spatial Light Modulator (SLM):** A 532-nm laser beam, shaped by a liquid-crystal on silicon (LCoS) SLM, creates a repulsive optical potential to compensate for the ODT and magnetic field. The SLM modulates the intensity profile of the compensation laser beam.
- **Feedback Optimization:** The spatial profile of the SLM beam is optimized using a feedback technique based on the measured in-situ column density distribution of the trapped sample. A fuzzy logic feedback system is used to calculate phase adjustments for the SLM, driving the system towards the desired density distribution.
- **Imaging and Analysis:** Absorption imaging is used to measure the in-situ density distribution. FFT filtering and low-pass filtering are applied to the images to reduce noise and interference. The spatial resolution of the imaging system is characterized using a square wave potential.
- **Trap Configurations:** Two trap configurations are used: one with a ring-shaped wall potential (trap 1) and one without (trap 2).
- **Evaluation Metrics:** The uniformity of the sample is quantified using the relative density deviation (∆n2D/n2D), which represents the standard deviation of the column density within a specified region. Spatial variation of the transverse trapping frequency (ωz) is measured using parametric heating.

### Results

- **Density Uniformity:** The feedback homogenization process significantly flattens the in-situ density profile of the Fermi gas. After approximately 50 feedback loops, the relative column density deviation is reduced to 3.98% in trap 1 and 8.22% in trap 2.
- **Trap Bottom Potential:** The standard deviation of the trap bottom potential is estimated to be approximately kB × 3.5 nK for trap 1 and kB × 6.1 nK for trap 2, which is less than 20% of the transverse confinement energy (¯hωz = kB × 34 nK).
- **Dimensional Crossover:** By reducing the atom number in trap 2, the authors explore the crossover from a 3D to a 2D regime. They observe that the sample maintains a flat density profile even at low atomic densities. Experimental data for the relative density deviation as a function of column density are consistent with 3D model predictions for n2D > 2/l2z and with 2D model predictions for n2D < 1/l2z, indicating a crossover from 3D to 2D.
- **Spatial Variation of ωz:** Measurement of the transverse trapping frequency ωz shows a dipole-like structure across the sample, attributed to imperfections in the ODT. After homogenization, the mean value of ωz increases by approximately 2π × 40 Hz.
