# Accelerated Structure Formation from Horizon Thermodynamics: Resolving the JWST Early Massive Galaxy Anomaly

**Author:** Keith Brodie (2026)
https://zenodo.org/records/18665076

## Summary

JWST has revealed galaxies with stellar masses of 10⁹–10¹⁰ M☉ at redshifts z > 10, within 400 Myr of the Big Bang — a >5σ tension with ΛCDM structure formation timescales. We show that these galaxies form naturally, with no free parameters, in the thermodynamic spacetime framework of Jacobson (1995) when the Hubble horizon is imposed as a finite outer boundary on the vacuum mode spectrum.

This boundary condition modifies inertia at accelerations below a₀(z) = cH(z). Because H(z) is much larger at early times, the modification extends to all protogalactic scales at z > 10. Gravitational collapse timescales drop from >300 Myr (standard) to ~5–18 Myr (modified), and 30–60 collapse generations become available within the cosmic time budget.

Every spectroscopically confirmed JWST galaxy at z > 7 forms easily in this framework. No dark matter, no modified star formation efficiency, and no new parameters are required.

## Key Result

| Galaxy | z | Standard t_ff [Myr] | Modified t_mod [Myr] | Collapse generations available |
|--------|---:|---:|---:|---:|
| JADES-GS-z14-0 | 14.2 | 306 | **5.2** | 37 |
| JADES-GS-z13-0 | 13.2 | 339 | **4.5** | 50 |
| GN-z11 | 10.6 | 460 | **8.1** | 41 |
| CEERS-3 | 7.5 | 733 | **17.6** | 34 |

## Files

- `Draft-v1.md` — Full paper text (Markdown)
- `jwst_modified_inertia.py` — Complete numerical analysis script (reproduces all tables and figures)
- `fig_jwst_analysis.png` — Four-panel summary figure

## Running the Code

```bash
pip install numpy scipy matplotlib
python jwst_modified_inertia.py
```

Requires only `numpy`, `scipy`, and `matplotlib`.

## Related Papers

1. **Paper 1:** K. Brodie, "Quantized Inertia as a Boundary Correction to Jacobson's Thermodynamic Spacetime" (2026). [DOI: 10.5281/zenodo.18664801](https://doi.org/10.5281/zenodo.18664801)

2. **Paper 2:** K. Brodie, "Karlsson's Redshift Periodicity as an Efimov Spectrum" (2026). [DOI: 10.5281/zenodo.18664931](https://doi.org/10.5281/zenodo.18664931)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
