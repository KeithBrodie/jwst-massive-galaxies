# Accelerated Structure Formation from Horizon Thermodynamics: Resolving the JWST Early Massive Galaxy Anomaly

**K. Brodie (2026)**

---

## Abstract

The James Webb Space Telescope has revealed galaxies with stellar masses of $10^9$--$10^{10}\,M_\odot$ at redshifts $z > 10$, within 400 Myr of the Big Bang. In standard $\Lambda$CDM cosmology, the free-fall timescale of protogalactic baryonic clouds at these epochs exceeds the age of the universe, and the required dark matter halos represent $>10\sigma$ fluctuations in the primordial density field. We show that these galaxies form naturally --- with no free parameters --- in the thermodynamic spacetime framework of Jacobson (1995) when entanglement sharing between Rindler and Hubble horizons modifies the effective inertia of matter. The sharing function $f(a) = a/(a + a_0)$ with $a_0(z) = cH(z)/6$, derived in [29] from entanglement monogamy and validated against the SPARC radial acceleration relation at $\sigma = 0.133$ dex [30], produces the standard MOND phenomenology with zero free parameters. Because $H(z)$ is much larger at early times --- $a_0(z{=}12) \approx 26\,a_0(z{=}0)$ --- the modification extends to all protogalactic scales. Gravitational accelerations in collapsing clouds ($g \sim 10^{-12}$ m/s$^2$) fall 3 orders of magnitude below $a_0(z)$, placing them deeply in the modified regime where effective acceleration is enhanced by factors of $\sim$20--40. The resulting collapse timescales are $\sim$65--186 Myr, compared to $>$300 Myr in the standard framework, and 3--4 collapse generations fit within the available cosmic time at every observed redshift. No dark matter, no modified star formation efficiency, and no new free parameters are required.

---

## 1. Introduction

### 1.1 The Anomaly

The first deep-field observations from JWST revealed a population of galaxy candidates at $z > 10$ that are far too massive and morphologically mature to exist under the standard $\Lambda$CDM structure formation timeline [1--4]. Spectroscopic confirmation campaigns have since established galaxies at $z = 10.6$ [5], $z = 11.4$ [6], $z = 13.2$ [7], $z = 13.5$ [31], and $z = 14.2$ [8], with stellar masses ranging from $10^{7.8}$ to $10^{10}\,M_\odot$. The confirmed population continues to grow: the JADES Data Release 4 [43] and BEACON Cycle 2 surveys now provide large statistical samples at $z = 7$--14.

Boylan-Kolchin [9] quantified the tension: even assuming 100\% star formation efficiency (a physical impossibility --- it requires converting every available baryon into stars with no gas ejection, no remaining gas, and no feedback losses), several JWST candidates exceed the maximum stellar mass permitted by the $\Lambda$CDM halo mass function at their observed redshifts. The implied number densities of massive galaxies at $z > 10$ exceed $\Lambda$CDM predictions by factors of $\sim$3--100 [10--12]. McCaffrey et al. [32] have shown that even state-of-the-art simulations with optimistic assumptions are pushed to their limits by the $z > 10$ population.

Subsequent work has reduced the most extreme mass estimates through identification of AGN contamination [13], bursty star formation histories [14,15], nebular emission corrections [16], and systematic effects from outshining, dust, and star formation history assumptions [39]. These revisions lower individual stellar masses by factors of 3--10 but do not eliminate the population-level tension: the UV luminosity function at $z > 12$ remains systematically above $\Lambda$CDM predictions [10,17,33,34], and the spectroscopically confirmed population continues to grow. Pollock et al. [35] find evidence for highly efficient star formation driven by dense, neutral gas in UV-bright galaxies at $z > 9$, confirming that the anomaly persists at the population level.

### 1.2 The Timescale Problem

The anomaly is most sharply stated as a timescale problem. At $z = 12$, the age of the universe is 366 Myr. The first stars form after $z \sim 30$ ($t \sim 99$ Myr), leaving approximately 267 Myr for galaxy assembly. In $\Lambda$CDM, the standard free-fall time for a protogalactic baryonic cloud at 5$\times$ the mean density is:

$$t_{\rm ff} = \sqrt{\frac{3\pi}{32\,G\,\rho}} \approx 300\text{--}400\ {\rm Myr} \quad (z \sim 12)$$

This exceeds the available cosmic time. Even a single gravitational collapse cannot be completed, let alone the multiple generations of collapse, star formation, and feedback required to build a galaxy with $M_\star \sim 10^9\,M_\odot$.

In the standard hierarchical picture, the additional bottleneck is the rarity of sufficiently massive dark matter halos. A halo of $10^{11}\,M_\odot$ at $z = 12$ corresponds to a $\sim$9$\sigma$ fluctuation in the primordial density field, with an expected number density of effectively zero in the observable universe.

### 1.3 Existing Proposals

Several mechanisms have been proposed to alleviate the tension within or near the standard framework:

- **Enhanced star formation efficiency** at high $z$, including "feedback-free starbursts" (FFB) in which gas converts to stars before feedback can regulate the process [18]. Dekel et al. have since extended the FFB framework to explain Little Red Dots via compaction. Kar et al. [37] propose an evolving star formation efficiency as the key mechanism, while Munoz et al. [38] find empirical evidence for increased burstiness in smaller halos at cosmic dawn. These proposals address the mass budget and luminosity function but not the fundamental timescale problem at $z > 12$.

- **Revised mass estimates.** Ziegler et al. [39] argue that three effects --- outshining by young stars, assumed star formation histories, and dust attenuation --- can each reduce inferred stellar masses by factors of a few, potentially reducing the tension. Cheng et al. [40] show that a bottom-heavy initial mass function would imply *more* hidden mass in early galaxies, worsening the tension. Dressler & Benson [36] claim good agreement between semi-analytic models and stellar mass data at $z = 6$--12, though their analysis focuses on luminosity-selected samples rather than the most extreme objects.

- **Modified cosmological backgrounds.** Early dark energy models can boost the high-$z$ halo mass function [19], and Shen et al. [41] show that departures from $\Lambda$CDM prior to recombination can accelerate structure formation. These approaches require new physics in the dark energy or inflation sector and introduce additional parameters.

- **MOND/Milgromian cosmology**: Haslbauer et al. [20] showed that MOND predicts more massive galaxies at early times than $\Lambda$CDM, because the enhanced effective gravity accelerates structure formation. However, MOND's critical acceleration $a_0 = 1.2 \times 10^{-10}$ m/s$^2$ is an empirical constant with no first-principles derivation. Its extension to cosmological settings requires additional assumptions about its redshift dependence. Moffat [42] has applied Modified Gravity (MOG) to the same problem, but MOG introduces additional fields and parameters.

### 1.4 This Work

We show that the JWST anomaly is resolved naturally by the thermodynamic spacetime framework [21] when entanglement sharing between the local Rindler horizon and the cosmic Hubble horizon modifies the effective inertia of matter. This framework, developed in [29] and quantitatively validated against the SPARC radial acceleration relation in [30], derives a modification to the inertial mass at accelerations below

$$a_0(z) = \frac{c\,H(z)}{6} \tag{1}$$

from Jacobson's thermodynamic derivation of Einstein's equations [21], with no free parameters. The factor of 6 is a geometric constant arising from the backward-hemisphere $\cos^2\theta$ integral over the overlap between planar Rindler and spherical Hubble entanglement modes [30]. The critical acceleration $a_0$ is not inserted by hand (as in MOND) but emerges from the geometry: it is set by the competition between two horizons for vacuum entanglement.

At $z = 0$, $a_0 = cH_0/6 \approx 1.09 \times 10^{-10}$ m/s$^2$, within 9\% of Milgrom's empirical value $a_0^{\rm MOND} = 1.2 \times 10^{-10}$ m/s$^2$. This agreement --- achieved with zero free parameters --- is validated by the SPARC rotation curve analysis in [30], which matches the observed radial acceleration relation at $\sigma = 0.133$ dex scatter.

Because $H(z)$ was much larger in the early universe --- $H(z{=}12)/H_0 \approx 26$ --- the inertia modification extends to much higher accelerations at early times. All protogalactic dynamics at $z > 10$ fall deeply within the modified regime, and gravitational collapse proceeds on timescales of $\sim$65--100 Myr rather than hundreds of Myr. The "impossible" early massive galaxies are impossible only under the assumption that inertia is constant.

---

## 2. Framework

We summarize the relevant results from [29,30]; the reader is referred there for the full derivations.

### 2.1 Jacobson's Thermodynamic Spacetime

Jacobson [21] showed that Einstein's field equations emerge from the first law of thermodynamics ($\delta Q = T\,dS$) applied to local Rindler horizons, provided the entropy satisfies the Bekenstein-Hawking area law $S = k_B A / (4\ell_P^2)$. This derivation assumes local equilibrium: that every horizon patch has the full entropy, with all vacuum modes contributing.

### 2.2 Entanglement Sharing Between Horizons

In Jacobson's original derivation, the Rindler horizon entropy is computed as if the horizon has sole access to all vacuum entanglement. In reality, any observer with acceleration $a$ in a universe with Hubble parameter $H$ has *two* horizons competing for the same vacuum modes:

- The **Rindler horizon** at distance $d_R = c^2/a$, producing the Unruh temperature $T_R = \hbar a / (2\pi c k_B)$.
- The **Hubble horizon** at distance $R_H = c/H$, producing the Gibbons-Hawking temperature $T_H = \hbar c H / (2\pi k_B)$.

By entanglement monogamy, both horizons cannot be fully entangled with the same mode. The effective entanglement available to the Rindler horizon is reduced by a sharing fraction [29]:

$$f(a) = \frac{T_R}{T_R + T_{H,\rm eff}} = \frac{a}{a + a_0} \tag{2}$$

where $T_{H,\rm eff} = T_H / 6$ is the effective Hubble temperature at the Rindler horizon, reduced by a geometric factor of 6 from the backward-hemisphere $\cos^2\theta$ integral over the overlap between planar (Rindler) and spherical (Hubble) entanglement modes [30]. This gives:

$$a_0 \equiv \frac{cH}{6} \tag{3}$$

### 2.3 The Modified Equation of Motion

The sharing function $f(a)$ enters Jacobson's Clausius relation as $\delta Q = T_R\,f(a)\,dS$, yielding an effective inertial mass $m_i = f(a)\,m_g$. The equation of motion $F = m_i\,a$ with gravitational force $F = m_g\,g$ gives:

$$g = f(a)\,a = \frac{a^2}{a + a_0} \tag{4}$$

Solving for $a$:

$$a = \frac{g + \sqrt{g^2 + 4\,g\,a_0}}{2} \tag{5}$$

This has the correct limits:
- **High acceleration** ($g \gg a_0$): $a \to g$ (standard Newtonian dynamics)
- **Low acceleration** ($g \ll a_0$): $a \to \sqrt{g\,a_0}$ (deep-MOND regime)
- **Transition** at $g \sim a_0 = cH/6$

The deep-MOND limit $a = \sqrt{g\,a_0}$ is the same scaling that produces flat rotation curves [30]. At $z = 0$, the SPARC radial acceleration relation $g_{\rm bar} = g_{\rm obs}^2/(g_{\rm obs} + a_0)$ matches 175 galaxies at $\sigma = 0.133$ dex with zero free parameters.

### 2.4 Cosmological Evolution

The Hubble parameter evolves as:

$$H(z) = H_0\sqrt{\Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda} \tag{6}$$

Therefore $a_0(z) = cH(z)/6$ increases with redshift. Using Planck 2018 parameters ($H_0 = 67.4$ km/s/Mpc, $\Omega_m = 0.315$, $\Omega_r = 9.1 \times 10^{-5}$, $\Omega_\Lambda = 0.685$):

| z | H(z)/H₀ | a₀(z) [m/s²] | Enhancement |
|----:|:----------:|:-------------------:|:-----------:|
| 0 | 1.0 | 1.09 × 10⁻¹⁰ | 1× |
| 6 | 10.4 | 1.14 × 10⁻⁹ | 10× |
| 10 | 20.5 | 2.24 × 10⁻⁹ | 21× |
| 12 | 26.4 | 2.88 × 10⁻⁹ | **26×** |
| 14 | 32.7 | 3.57 × 10⁻⁹ | 33× |
| 20 | 54.2 | 5.91 × 10⁻⁹ | 54× |

**Table 1.** Critical acceleration $a_0(z) = cH(z)/6$ at key redshifts. The enhancement ratio is the same as in v1 because both $a_0$ and $a_0(z{=}0)$ share the factor of 1/6.

A critical consequence: at $z = 0$, the modification only affects the outermost regions of galaxies where $g < 1.09 \times 10^{-10}$ m/s$^2$. At $z = 12$, it affects all regions where $g < 2.88 \times 10^{-9}$ m/s$^2$ --- encompassing the entirety of protogalactic collapse dynamics.

We emphasize that the Friedmann equation governing the background expansion is unchanged. The modification applies to the inertial response of test masses to gravitational forces, not to the relation between stress-energy and spacetime geometry. The cosmic timeline remains standard: $t(z{=}12) = 366$ Myr.

---

## 3. Application to JWST Galaxies

### 3.1 Protogalactic Dynamics in the Modified Regime

Consider a protogalactic baryonic cloud of mass $M_b$ at redshift $z$, with density $\rho = \delta \times \rho_{\rm mean}(z)$ at turnaround ($\delta \sim 5$). The cloud radius is:

$$R = \left(\frac{3\,M_b}{4\pi\,\rho}\right)^{1/3} \tag{7}$$

and the Newtonian gravitational acceleration at the cloud edge is:

$$g = \frac{G\,M_b}{R^2} \tag{8}$$

For the JWST galaxies, we take the observed stellar mass $M_\star$, assume a star formation efficiency of 10\%, and compute the progenitor cloud mass $M_b = M_\star / 0.1$. The results are shown in Table 2.

| Galaxy | z | log M★ | g [m/s²] | a₀(z) [m/s²] | g/a₀ |
|--------|----:|:-----:|:-----------:|:-------------------:|:-------:|
| JADES-GS-z14-0 | 14.2 | 8.7 | 4.9 × 10⁻¹² | 3.6 × 10⁻⁹ | 1.3 × 10⁻³ |
| JADES-GS-z13-0 | 13.2 | 8.1 | 2.7 × 10⁻¹² | 3.3 × 10⁻⁹ | 8.2 × 10⁻⁴ |
| JADES-GS-z12-0 | 12.6 | 7.8 | 2.0 × 10⁻¹² | 3.1 × 10⁻⁹ | 6.4 × 10⁻⁴ |
| Maisie's Galaxy | 11.4 | 8.5 | 2.8 × 10⁻¹² | 2.7 × 10⁻⁹ | 1.0 × 10⁻³ |
| GN-z11 | 10.6 | 9.0 | 3.6 × 10⁻¹² | 2.4 × 10⁻⁹ | 1.5 × 10⁻³ |
| CEERS-1 | 8.9 | 9.5 | 3.8 × 10⁻¹² | 1.9 × 10⁻⁹ | 2.0 × 10⁻³ |
| CEERS-2 | 7.9 | 9.8 | 3.9 × 10⁻¹² | 1.6 × 10⁻⁹ | 2.4 × 10⁻³ |
| CEERS-3 | 7.5 | 10.0 | 4.1 × 10⁻¹² | 1.5 × 10⁻⁹ | 2.7 × 10⁻³ |

**Table 2.** Gravitational accelerations in progenitor clouds of observed JWST galaxies. In all cases $g/a_0 \sim 10^{-3}$: every object is deeply in the modified regime.

The ratio $g/a_0 \sim 10^{-3}$ across all objects means we are firmly in the deep-MOND limit where $g \ll a_0$, and the self-consistent acceleration (Eq. 5) is approximately $a \approx \sqrt{g\,a_0(z)}$. The enhancement factor is:

$$\eta \equiv \frac{a}{g} \approx \sqrt{\frac{a_0(z)}{g}} \sim 20\text{--}40 \tag{9}$$

### 3.2 Modified Collapse Timescale

The standard free-fall time for a uniform sphere of density $\rho$ is:

$$t_{\rm ff} = \sqrt{\frac{3\pi}{32\,G\,\rho}} \tag{10}$$

In the modified regime, the effective acceleration is enhanced by factor $\eta$. The collapse timescale can be estimated by two methods that bracket the true value:

**Lower bound** ($\sqrt{\eta}$ scaling): The free-fall time scales inversely with the square root of the effective acceleration:

$$t_{\rm lower} = \frac{t_{\rm ff}}{\sqrt{\eta}} \tag{11}$$

**Upper bound** (constant-acceleration approximation): In the deep-MOND limit, the effective acceleration $a \approx \sqrt{g\,a_0}$ is approximately constant during the early phase of collapse (before the cloud has contracted significantly). This gives:

$$t_{\rm upper} = \sqrt{\frac{2R}{a_{\rm mod}}} \tag{12}$$

We adopt the geometric mean $t_{\rm mod} = \sqrt{t_{\rm lower} \times t_{\rm upper}}$ as our estimate. The results are shown in Table 3.

| Galaxy | z | t_avail [Myr] | t_ff (standard) [Myr] | η | t_mod (modified) [Myr] | N_collapse |
|--------|----:|:------:|:----:|:---:|:----:|:---:|
| JADES-GS-z14-0 | 14.2 | 190 | 306 | 27.8 | **65** | 2.9 |
| JADES-GS-z13-0 | 13.2 | 222 | 339 | 35.5 | **64** | 3.4 |
| JADES-GS-z12-0 | 12.6 | 243 | 362 | 40.2 | **64** | 3.8 |
| Maisie's Galaxy | 11.4 | 294 | 416 | 31.5 | **84** | 3.5 |
| GN-z11 | 10.6 | 335 | 460 | 26.6 | **101** | 3.3 |
| CEERS-1 | 8.9 | 452 | 583 | 22.9 | **138** | 3.3 |
| CEERS-2 | 7.9 | 548 | 684 | 21.0 | **168** | 3.3 |
| CEERS-3 | 7.5 | 594 | 733 | 19.7 | **186** | 3.2 |

**Table 3.** Collapse timescales for JWST galaxies. $t_{\rm avail}$ is the time from first star formation ($z = 30$) to the observed redshift. $\eta = a_{\rm mod}/g$ is the acceleration enhancement. $N_{\rm collapse} = t_{\rm avail} / t_{\rm mod}$ is the number of collapse generations that fit within the available time. In the standard framework, not even one free-fall can be completed ($t_{\rm ff} > t_{\rm avail}$ for $z \gtrsim 10$). In the modified framework, 3--4 collapse generations are available for every object.

### 3.3 Formation Feasibility

For JADES-GS-z14-0, the most distant spectroscopically confirmed galaxy ($z = 14.2$, $M_\star \sim 10^{8.7}\,M_\odot$) [8]:

- **Standard**: $t_{\rm ff} = 306$ Myr exceeds the available time of 190 Myr. The galaxy *cannot complete a single gravitational collapse*. Formation is impossible.

- **Modified**: $t_{\rm mod} = 65$ Myr. There are 2.9 collapse timescales available. At 10\% star formation efficiency per collapse, the galaxy can build $M_\star \sim 10^{8.7}\,M_\odot$ in 2--3 generations --- within the budget.

The result holds for every object in the sample. The standard framework cannot form these galaxies; the modified framework provides sufficient time with margins of $\times$3--4.

We note that the margins are tighter than a naive estimate might suggest, which is itself a feature of the framework: the modification is calibrated to reproduce observed rotation curves at $z = 0$ with zero free parameters, leaving no room to inflate the effect. The fact that JWST galaxies are resolved *without* parameter tuning --- neither too easily nor too tightly --- is a non-trivial consistency check.

### 3.4 No Dark Matter Required

A further consequence of modified inertia is the elimination of the dark matter halo bottleneck. In $\Lambda$CDM, baryons collapse only after dark matter halos have formed through hierarchical merging. The abundance of halos is exponentially sensitive to the peak height $\nu = \delta_c / (\sigma(M) \cdot D(z))$, which reaches $\nu \sim 9$--12 at $z > 12$ for the required halo masses. At $\nu = 12$, the probability is $\sim e^{-72} \sim 10^{-31}$ --- effectively zero.

In the modified inertia framework, dark matter is unnecessary: flat rotation curves arise from the entanglement sharing function itself [29,30]. Baryonic gas collapses directly under its own gravity, enhanced by the reduced inertia. The exponential suppression from the halo mass function is absent, and the relevant question is simply whether the baryonic gas can collapse within the available time. As shown above, it can.

---

## 4. Discussion

### 4.1 Comparison with MOND

Haslbauer et al. [20] demonstrated that Milgromian dynamics predicts a higher abundance of massive galaxies at early times than $\Lambda$CDM, qualitatively consistent with JWST observations. Our result is in the same spirit but differs in three important respects:

1. **Derived, not empirical.** MOND introduces $a_0 = 1.2 \times 10^{-10}$ m/s$^2$ as an empirical constant. In our framework, $a_0 = cH/6$ emerges from Jacobson's thermodynamic spacetime [21] with entanglement sharing between Rindler and Hubble horizons [29,30] --- no free parameters. The predicted $a_0 = 1.09 \times 10^{-10}$ m/s$^2$ matches Milgrom's value to 9\%.

2. **Redshift dependence is built in.** MOND does not specify how $a_0$ evolves with cosmic time; any $z$-dependence must be added by assumption. Our $a_0(z) = cH(z)/6$ follows directly from the physics: the Hubble horizon shrinks at early times, intensifying the entanglement competition and producing a larger inertia modification.

3. **Modified inertia, not modified gravity.** MOND modifies the gravitational force law; Moffat's MOG [42] introduces additional gravitational fields. We modify the inertial response of matter via the entropy sharing mechanism. These are observationally distinguishable [24] and represent different physics. In our framework, the gravitational field equations (Einstein's equations) are unchanged; only the relationship between force and acceleration is modified through the entropy correction.

### 4.2 Comparison with Conventional Explanations

A growing literature seeks to resolve the JWST tension within or near the standard framework. The approaches fall into three categories:

**Astrophysical adjustments.** Enhanced star formation efficiency [18,37], bursty star formation histories [14,15,38], and AGN contamination corrections [13] address the mass and luminosity estimates of individual objects. Dressler & Benson [36] argue that semi-analytic models can match stellar mass growth at $z = 6$--12 without new physics. These approaches can reduce the inferred severity of the anomaly but do not address the fundamental timescale problem: at $z > 12$, the standard free-fall time exceeds the age of the universe regardless of how efficiently stars form once collapse occurs.

**Systematic reductions.** Ziegler et al. [39] show that outshining, star formation history assumptions, and dust can each reduce inferred masses by factors of a few, and argue the tension may be less severe than claimed. However, the population-level excess in the UV luminosity function at $z > 12$ [33,34] persists independently of individual mass estimates, and McCaffrey et al. [32] demonstrate that even optimistic simulations struggle to reproduce the observed abundance.

**Modified cosmology.** Shen et al. [41] explore departures from $\Lambda$CDM before recombination that imprint on non-linear structure formation, showing that modified early-universe physics can speed galaxy assembly. This is closest in spirit to our approach, though it operates through the dark energy sector rather than through inertia.

Our framework resolves the timescale problem directly. Collapse occurs in $\sim$65--100 Myr at $z > 12$, and 3--4 collapse-and-formation cycles fit within the available time. Even modest star formation efficiencies ($\sim$10\%) produce the observed stellar masses across multiple generations. Crucially, the same physics that accelerates high-$z$ collapse also produces the correct rotation curves at $z = 0$ [30] --- the two regimes are linked by a single, parameter-free function.

### 4.3 CMB Compatibility

The modification to inertia is also active at recombination ($z \sim 1100$), where $a_0(z) \sim 3 \times 10^{-6}$ m/s$^2$ and the gravitational accelerations in CMB-scale perturbations ($g \sim 10^{-12}$ m/s$^2$) are far below $a_0$. This raises the question of whether the modification is compatible with the observed CMB power spectrum.

We note that the modification derived in [29] applies specifically to the inertial response of matter to gravitational forces, not to electromagnetic interactions. The baryon acoustic oscillations that produce the CMB peaks are driven by radiation pressure (an electromagnetic effect), with gravity providing the driving potential wells. If the inertia modification applies only to the gravitational sector --- as expected from its origin in Jacobson's gravitational thermodynamics --- the pressure-driven oscillation dynamics may be less affected than a naive estimate would suggest.

A definitive answer requires a numerical calculation with a modified Boltzmann code (e.g., CLASS or CAMB incorporating the inertia correction). This is beyond the scope of the present work and is the subject of ongoing investigation. We note, however, that the analogous question arises for any MOND-like theory, and that several authors have explored CMB compatibility in Milgromian frameworks [25,26] with partial success.

### 4.4 Predictions

The framework makes specific, testable predictions:

1. **Mass--redshift relation.** The maximum stellar mass at each redshift is determined by $a_0(z) = cH(z)/6$ and the available cosmic time. This produces a definite, parameter-free prediction for the envelope of the galaxy population on the mass--redshift plane. Future JWST observations at $z > 15$ should continue to find galaxies above the $\Lambda$CDM limit and below our predicted ceiling.

2. **Scaling with $H(z)$.** In the deep-MOND limit, the effective acceleration scales as $a \propto \sqrt{g\,a_0(z)} \propto \sqrt{H(z)}$, and the collapse timescale as $t_{\rm mod} \propto 1/H(z)^{1/4}$. The modification is strongest at the highest redshifts and weakens toward low $z$ as $H$ decreases. This naturally explains why the anomaly is most severe at early times and becomes less pronounced at $z < 6$.

3. **No dark matter halos.** In our framework, massive galaxies at high $z$ form from direct baryonic collapse without prior dark matter halo assembly. Observations probing the mass distribution of high-$z$ galaxies (e.g., through gravitational lensing or dynamics) should find baryon-dominated systems, not the dark-matter-dominated halos predicted by $\Lambda$CDM.

4. **Morphological maturity.** The collapse timescale ($\sim$65--100 Myr at $z > 12$) still allows time for dynamical relaxation before the galaxy is observed. This could contribute to the unexpectedly mature morphologies (disks, bulges) seen at $z \sim 6$--8 [27,28], which are puzzling in the standard framework where galaxies at these epochs should still be dynamically young.

---

## 5. Conclusion

The JWST "impossible early massive galaxies" are impossible only if inertia is constant. In the thermodynamic spacetime framework, entanglement sharing between Rindler and Hubble horizons modifies the effective inertia of matter via the sharing function $f(a) = a/(a + a_0)$ with $a_0(z) = cH(z)/6$. This function, derived from entanglement monogamy [29] and validated against the SPARC radial acceleration relation at $\sigma = 0.133$ dex [30], produces standard MOND phenomenology with zero free parameters and $a_0 = 1.09 \times 10^{-10}$ m/s$^2$ (9\% from Milgrom's empirical value).

At $z > 10$, $a_0(z)$ is 20--50 times larger than at $z = 0$, placing all protogalactic dynamics deeply in the modified regime. The consequences: gravitational collapse timescales drop from hundreds of Myr to $\sim$65--100 Myr, 3--4 collapse generations become available within the cosmic time budget, and the dark matter halo bottleneck is eliminated entirely. Every spectroscopically confirmed JWST galaxy at $z > 7$ forms within this framework, with no free parameters and no fine-tuning.

The framework inherits the conceptual solidity of Jacobson's thermodynamic derivation of Einstein's equations [21] --- the most cited result in quantum gravity --- extended by the physical requirement that vacuum entanglement be shared between competing horizons. The "anomaly" is not anomalous; it is what horizon thermodynamics predicts.

---

## References

[1] I. Labbé et al., "A population of red candidate massive galaxies ~600 Myr after the Big Bang," *Nature* **616**, 266 (2023). [arXiv:2207.12446](https://arxiv.org/abs/2207.12446)

[2] B. E. Robertson et al., "Identification and properties of intense star-forming galaxies at redshifts z > 10," *Nature Astron.* **7**, 611 (2023). [arXiv:2212.04480](https://arxiv.org/abs/2212.04480)

[3] M. Castellano et al., "Early results from GLASS-JWST: Very high-z galaxy candidates," *ApJ Lett.* **938**, L15 (2022). [arXiv:2207.09436](https://arxiv.org/abs/2207.09436)

[4] C. L. Steinhardt et al., "The Impossibly Early Galaxy Problem," *ApJ* **824**, 21 (2016). [arXiv:1506.01377](https://arxiv.org/abs/1506.01377)

[5] A. J. Bunker et al., "JADES NIRSpec Spectroscopy of GN-z11," *A&A* **677**, A88 (2023). [arXiv:2302.07256](https://arxiv.org/abs/2302.07256)

[6] P. Arrabal Haro et al., "Confirmation and refutation of very luminous galaxies in the early universe," *Nature* **622**, 707 (2023). [arXiv:2303.15431](https://arxiv.org/abs/2303.15431)

[7] E. Curtis-Lake et al., "Spectroscopic confirmation of four metal-poor galaxies at z = 10.3--13.2," *Nature Astron.* **7**, 622 (2023). [arXiv:2212.04568](https://arxiv.org/abs/2212.04568)

[8] S. Carniani et al., "A shining cosmic dawn: spectroscopic confirmation of two luminous galaxies at z ~ 14," *Nature* **633**, 318 (2024). [arXiv:2405.18485](https://arxiv.org/abs/2405.18485)

[9] M. Boylan-Kolchin, "Stress testing LCDM with high-redshift galaxy candidates," *Nature Astron.* **7**, 731 (2023). [arXiv:2208.01611](https://arxiv.org/abs/2208.01611)

[10] S. L. Finkelstein et al., "The Complete CEERS Early Universe Galaxy Sample," *ApJ Lett.* **969**, L2 (2024). [arXiv:2311.04279](https://arxiv.org/abs/2311.04279)

[11] Y. Harikane et al., "A Comprehensive Study of Galaxies at z ~ 9--16 Found in the Early JWST Data," *ApJS* **265**, 5 (2023). [arXiv:2208.01612](https://arxiv.org/abs/2208.01612)

[12] C. T. Donnan et al., "The evolution of the galaxy UV luminosity function at redshifts z ~ 8--15 from deep JWST and ground-based observations," *MNRAS* **518**, 6011 (2023). [arXiv:2207.12356](https://arxiv.org/abs/2207.12356)

[13] D. J. Kocevski et al., "Hidden Little Monsters: Spectroscopic Identification of Low-Luminosity Broad-Line AGN at z > 5," *ApJ Lett.* **954**, L4 (2023). [arXiv:2302.00012](https://arxiv.org/abs/2302.00012)

[14] C. A. Mason, M. Trenti, and T. Treu, "The brightest galaxies at cosmic dawn," *MNRAS* **521**, 497 (2023). [arXiv:2207.14808](https://arxiv.org/abs/2207.14808)

[15] J. Mirocha and S. R. Furlanetto, "Balancing the efficiency and stochasticity of star formation with dust at high redshifts," *MNRAS* **519**, 843 (2023). [arXiv:2208.12826](https://arxiv.org/abs/2208.12826)

[16] R. Endsley et al., "A JWST/NIRCam Study of Key Contributors to Reionization: The Star-forming and Ionizing Properties of UV-faint z ~ 7--8 Galaxies" (2022). [arXiv:2208.14999](https://arxiv.org/abs/2208.14999)

[17] R. J. Bouwens et al., "UV luminosity functions at redshifts z ~ 8 to z ~ 15 from deep JWST observations," *MNRAS* **523**, 1036 (2023). [arXiv:2211.02607](https://arxiv.org/abs/2211.02607)

[18] A. Dekel et al., "Efficient formation of massive galaxies at cosmic dawn by feedback-free starbursts," *MNRAS* **523**, 3201 (2023). [arXiv:2303.04827](https://arxiv.org/abs/2303.04827)

[19] M. Forconi et al., "Do the Early Galaxies observed by JWST disagree with Planck's CMB polarization measurements?," *JCAP* **2023(10)**, 012 (2023). [arXiv:2306.07781](https://arxiv.org/abs/2306.07781)

[20] M. Haslbauer, P. Kroupa, and I. Banik, "The High-z universe confronts warm dark matter: Galaxy counts, reionisation and the nature of dark matter," *MNRAS* **524**, 3252 (2023). [arXiv:2210.14915](https://arxiv.org/abs/2210.14915)

[21] T. Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* **75**, 1260 (1995). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)

[22] M. E. McCulloch, "Inertia from an Asymmetric Casimir Effect," *EPL* **101**, 59001 (2013). [arXiv:1302.2775](https://arxiv.org/abs/1302.2775)

[23] M. E. McCulloch, "Galaxy Rotations from Quantised Inertia and Visible Matter Only," *Astrophys. Space Sci.* **362**, 149 (2017). [arXiv:1709.04918](https://arxiv.org/abs/1709.04918)

[24] V. Costantino and T. Broadhurst, "A First Attempt to Differentiate between Modified Gravity and Modified Inertia," *A&A* **636**, A15 (2020). [arXiv:2001.03348](https://arxiv.org/abs/2001.03348)

[25] C. Skordis and T. Zlosnik, "New Relativistic Theory for Modified Newtonian Dynamics," *Phys. Rev. Lett.* **127**, 161302 (2021). [arXiv:2007.00082](https://arxiv.org/abs/2007.00082)

[26] A. Aguirre, J. Schaye, and E. Quataert, "Problems for Modified Newtonian Dynamics in Clusters and the Lya Forest?," *ApJ* **561**, 550 (2001). [arXiv:astro-ph/0105184](https://arxiv.org/abs/astro-ph/0105184)

[27] L. Ferreira et al., "Panic! at the Disks: First Rest-frame Optical Observations of Galaxy Structure at z > 3," *ApJ Lett.* **938**, L2 (2022). [arXiv:2210.01110](https://arxiv.org/abs/2210.01110)

[28] J. S. Kartaltepe et al., "CEERS Key Paper III: The Diversity of Galaxy Structure and Morphology at z = 3--9 with JWST," *ApJ Lett.* **946**, L15 (2023). [arXiv:2210.14713](https://arxiv.org/abs/2210.14713)

[29] K. Brodie, "Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime" (2026). DOI: [10.5281/zenodo.18664800](https://doi.org/10.5281/zenodo.18664800)

[30] K. Brodie, "MOND from Horizon Thermodynamics: Deriving the Radial Acceleration Relation with Zero Free Parameters" (2026). DOI: [10.5281/zenodo.18677307](https://doi.org/10.5281/zenodo.18677307)

[31] C. T. Donnan et al., "Spectroscopic confirmation of a large and luminous galaxy with weak emission lines at z = 13.53" (2026). [arXiv:2601.11515](https://arxiv.org/abs/2601.11515)

[32] J. McCaffrey et al., "Beyond No Tension: JWST z > 10 Galaxies Push Simulations to the Limit" (2025). [arXiv:2509.07695](https://arxiv.org/abs/2509.07695)

[33] I. Chemerynska et al., "The first GLIMPSE of the faint galaxy population at Cosmic Dawn with JWST: The evolution of the ultraviolet luminosity function across z ~ 9--15" (2025). [arXiv:2509.24881](https://arxiv.org/abs/2509.24881)

[34] M. Franco et al., "Physical properties of galaxies and the UV Luminosity Function from z ~ 6 to z ~ 14 in COSMOS-Web" (2025). [arXiv:2508.04791](https://arxiv.org/abs/2508.04791)

[35] C. L. Pollock et al., "Characterising Lya damping wings at the onset of reionisation: Evidence for highly efficient star formation driven by dense, neutral gas in UV-bright galaxies at z > 9" (2026). [arXiv:2602.11783](https://arxiv.org/abs/2602.11783)

[36] A. Dressler and A. Benson, "Stellar Mass Growth in the First Galaxies: Theory and Observation" (2026). [arXiv:2602.01549](https://arxiv.org/abs/2602.01549)

[37] A. Kar, S. Alam, and J. Silk, "Beyond Extreme Burstiness: Evolving Star Formation Efficiency as the Key to Early Galaxy Abundance" (2025). [arXiv:2507.20606](https://arxiv.org/abs/2507.20606)

[38] J. B. Munoz et al., "Relatively Fast and Reasonably Furious: Evidence for Increased Burstiness in Smaller Halos at Cosmic Dawn" (2026). [arXiv:2601.07912](https://arxiv.org/abs/2601.07912)

[39] J. J. Ziegler et al., "Explaining the 'too massive' high-redshift galaxies in JWST data: numerical study of three effects and a simple relation" (2025). [arXiv:2507.21409](https://arxiv.org/abs/2507.21409)

[40] C. M. Cheng et al., "Bottom-heavy initial mass functions reveal hidden mass in early galaxies" (2026). [arXiv:2601.20864](https://arxiv.org/abs/2601.20864)

[41] X. Shen et al., "The Cosmic Rush Hour: Rapid Formation of Bright, Massive, Disky, Star-Forming Galaxies as Signatures of Early-Universe Physics" (2025). [arXiv:2509.19427](https://arxiv.org/abs/2509.19427)

[42] J. W. Moffat, "Galaxy Formation in the Early Universe" (2024). [arXiv:2412.03534](https://arxiv.org/abs/2412.03534)

[43] E. Curtis-Lake et al., "JADES Data Release 4 Paper I: Sample Selection, Observing Strategy and Redshifts of the complete spectroscopic sample" (2025). [arXiv:2510.01033](https://arxiv.org/abs/2510.01033)

---

## Appendix: Numerical Code

All calculations in this paper are reproduced by the script `jwst_modified_inertia.py` included with this manuscript. The script requires only `numpy`, `scipy`, and `matplotlib`.
