# Accelerated Structure Formation from Horizon Thermodynamics: Resolving the JWST Early Massive Galaxy Anomaly

**Author:** Keith Brodie (2026)
https://doi.org/10.5281/zenodo.18665075

## Summary

JWST has revealed galaxies with stellar masses of 10⁹–10¹⁰ M☉ at redshifts z > 10, within 400 Myr of the Big Bang — a >5σ tension with ΛCDM structure formation timescales. We show that these galaxies form naturally, with no free parameters, in the thermodynamic spacetime framework of Jacobson (1995) when entanglement sharing between Rindler and Hubble horizons modifies the effective inertia of matter.

The sharing function f(a) = a/(a + a₀) with a₀(z) = cH(z)/6, derived from entanglement monogamy and validated against the SPARC radial acceleration relation (σ = 0.133 dex, zero free parameters), produces MOND phenomenology with a₀ = 1.09×10⁻¹⁰ m/s² (9% from Milgrom). Because H(z) is much larger at early times, the modification extends to all protogalactic scales at z > 10. Gravitational collapse timescales drop from >300 Myr (standard) to ~65–186 Myr (modified), and 3–4 collapse generations become available within the cosmic time budget.

Every spectroscopically confirmed JWST galaxy at z > 7 forms within this framework. No dark matter, no modified star formation efficiency, and no new parameters are required.

## Key Result

| Galaxy | z | Standard t_ff [Myr] | Modified t_mod [Myr] | Collapse generations available |
|--------|---:|---:|---:|---:|
| JADES-GS-z14-0 | 14.2 | 306 | **65** | 2.9 |
| JADES-GS-z13-0 | 13.2 | 339 | **64** | 3.4 |
| GN-z11 | 10.6 | 460 | **101** | 3.3 |
| CEERS-3 | 7.5 | 733 | **186** | 3.2 |

## Files

- `Draft-v2.md` — Full paper text (Markdown)
- `jwst_modified_inertia.py` — Complete numerical analysis script (reproduces all tables and figures)
- `fig_jwst_analysis.png` — Four-panel summary figure

## Running the Code

```bash
pip install numpy scipy matplotlib
python jwst_modified_inertia.py
```

Requires only `numpy`, `scipy`, and `matplotlib`.

## Related Papers

1. **Paper 1:** K. Brodie, "Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime" (2026). [DOI: 10.5281/zenodo.18664800](https://doi.org/10.5281/zenodo.18664800)

2. **Paper 4:** K. Brodie, "MOND from Horizon Thermodynamics: Deriving the Radial Acceleration Relation with Zero Free Parameters" (2026). [DOI: 10.5281/zenodo.18677307](https://doi.org/10.5281/zenodo.18677307)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
