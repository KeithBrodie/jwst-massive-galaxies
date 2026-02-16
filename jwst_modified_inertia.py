"""
JWST Massive Early Galaxies: Modified Inertia Analysis
=======================================================

Core calculation for Paper 3.

Physics: Jacobson thermodynamic spacetime + finite Hubble boundary
         → modified inertia with a_0(z) = c H(z)
         → accelerated gravitational collapse at high z

Compares modified collapse timescales against JWST observations.
"""

import numpy as np
from scipy import integrate
from scipy.optimize import brentq
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.size'] = 11

# =============================================================
# CONSTANTS
# =============================================================
c = 2.998e8          # m/s
G = 6.674e-11        # m^3 kg^-1 s^-2
H0_km = 67.4         # km/s/Mpc
Mpc = 3.0857e22      # m
H0 = H0_km * 1e3 / Mpc  # 1/s
kpc = 3.0857e19      # m
Msun = 1.989e30      # kg
Gyr = 3.1557e16      # s
Myr = 3.1557e13      # s

# Cosmological parameters (Planck 2018)
Om = 0.315           # matter density
Or = 9.1e-5          # radiation density
OL = 0.685           # dark energy density
Ob = 0.0493          # baryon density
fb = Ob / Om         # baryon fraction = 0.156

# Present-day critical acceleration
a0_now = c * H0      # = 6.55e-10 m/s^2

# =============================================================
# COSMOLOGICAL FUNCTIONS
# =============================================================

def E(z):
    """Dimensionless Hubble parameter H(z)/H0."""
    return np.sqrt(Om * (1+z)**3 + Or * (1+z)**4 + OL)

def H(z):
    """Hubble parameter in 1/s."""
    return H0 * E(z)

def a0(z):
    """Critical acceleration a_0(z) = c H(z) in m/s^2."""
    return c * H(z)

def age_at_z(z):
    """Age of universe at redshift z, in seconds."""
    def integrand(zp):
        return 1.0 / ((1 + zp) * E(zp))
    result, _ = integrate.quad(integrand, z, np.inf)
    return result / H0

def growth_factor(z):
    """Unnormalized linear growth factor D(z)."""
    def integrand(zp):
        return (1 + zp) / E(zp)**3
    result, _ = integrate.quad(integrand, z, np.inf)
    return E(z) * result

# Normalize growth factor
D0 = growth_factor(0)

def D_norm(z):
    """Growth factor normalized to D(0) = 1."""
    return growth_factor(z) / D0

def peak_height(z, sigma0=2.0, delta_c=1.686):
    """Peak height nu for halo collapse."""
    return delta_c / (sigma0 * D_norm(z))


# =============================================================
# JWST GALAXY DATA
# =============================================================
# Format: (name, z_spec, log10_Mstar, log10_Mstar_err, reference, notes)
# Stellar masses after best current revisions (AGN corrections etc.)

jwst_galaxies = [
    # Spectroscopically confirmed, most robust
    ("JADES-GS-z14-0",   14.2,  8.7, 0.4, "Carniani+24", "Most distant confirmed"),
    ("JADES-GS-z13-0",   13.2,  8.1, 0.3, "Curtis-Lake+23", "Spectroscopic"),
    ("JADES-GS-z12-0",   12.6,  7.8, 0.3, "Curtis-Lake+23", "Spectroscopic"),
    ("Maisie's Galaxy",   11.4,  8.5, 0.4, "Arrabal Haro+23", "Revised from z_phot~14"),
    ("GN-z11",            10.6,  9.0, 0.3, "Bunker+23", "AGN signatures"),
    # Labbé et al. candidates (revised masses after AGN/SFH corrections)
    ("CEERS-1",            8.9,  9.5, 0.5, "Labbe+23/Barro+24", "Mass revised down"),
    ("CEERS-2",            7.9,  9.8, 0.5, "Labbe+23/Barro+24", "Mass revised down"),
    ("CEERS-3",            7.5, 10.0, 0.5, "Labbe+23/Barro+24", "Most massive candidate"),
]


# =============================================================
# MODIFIED INERTIA PHYSICS
# =============================================================

def modified_acceleration(g_newt, z):
    """
    Self-consistent acceleration under modified inertia.

    From m_i(a) = m_g [1 - (a0/a)^2], the equation of motion gives:
        a^2 - g*a - a0^2 = 0
    Solution: a = (g + sqrt(g^2 + 4*a0^2)) / 2

    Parameters:
        g_newt: Newtonian gravitational acceleration (m/s^2)
        z: redshift (determines a0)
    Returns:
        a_mod: modified acceleration (m/s^2)
        eta: enhancement factor a_mod / g_newt
    """
    a0z = a0(z)
    a_mod = (g_newt + np.sqrt(g_newt**2 + 4 * a0z**2)) / 2
    eta = a_mod / g_newt
    return a_mod, eta


def collapse_timescale(M_baryonic, z, overdensity=5.0):
    """
    Compute collapse timescale for a protogalactic cloud.

    Standard free-fall from turnaround radius, then modified version.

    Parameters:
        M_baryonic: baryonic mass in kg
        z: redshift
        overdensity: factor above mean density at turnaround
    Returns:
        dict with standard and modified timescales
    """
    # Mean matter density at z
    rho_crit_0 = 3 * H0**2 / (8 * np.pi * G)
    rho_mean = rho_crit_0 * Om * (1 + z)**3

    # Cloud density at turnaround
    rho_cloud = overdensity * rho_mean

    # Cloud radius (uniform sphere)
    R = (3 * M_baryonic / (4 * np.pi * rho_cloud))**(1.0/3.0)

    # Gravitational acceleration at cloud edge
    g_edge = G * M_baryonic / R**2

    # Standard free-fall time
    t_ff_std = np.sqrt(3 * np.pi / (32 * G * rho_cloud))

    # Modified acceleration and enhancement
    a_mod, eta = modified_acceleration(g_edge, z)

    # Modified collapse: two estimates
    # 1) sqrt(eta) scaling of free-fall time
    t_ff_mod_eta = t_ff_std / np.sqrt(eta)

    # 2) Constant-acceleration approximation (deep QI: a ~ a0)
    a0z = a0(z)
    t_ff_mod_const = np.sqrt(2 * R / a0z)

    # Geometric mean of the two estimates
    t_ff_mod_geom = np.sqrt(t_ff_mod_eta * t_ff_mod_const)

    return {
        'M_baryonic': M_baryonic,
        'z': z,
        'rho_cloud': rho_cloud,
        'R_kpc': R / kpc,
        'g_edge': g_edge,
        'a0_z': a0z,
        'g_over_a0': g_edge / a0z,
        'eta': eta,
        't_ff_std_Myr': t_ff_std / Myr,
        't_ff_mod_eta_Myr': t_ff_mod_eta / Myr,
        't_ff_mod_const_Myr': t_ff_mod_const / Myr,
        't_ff_mod_geom_Myr': t_ff_mod_geom / Myr,
    }


def max_stellar_mass_standard(z, sfe=0.1):
    """
    Maximum stellar mass at redshift z in standard LCDM.

    Uses Press-Schechter: the most massive halo expected in
    the observable volume at redshift z.

    Approximate: M_halo,max where nu(M, z) ~ 4-5
    (a few expected in Hubble volume).
    """
    # sigma(M) ~ sigma_8 * (M / M_8)^{-alpha} with alpha ~ 0.3-0.5
    # For simplicity, use the growth factor scaling
    sigma_8 = 0.811  # Planck 2018
    Dz = D_norm(z)

    # At z=0, 4-sigma halos have M ~ 10^15 Msun
    # sigma(M) * D(z) = delta_c / nu, with nu ~ 4
    # sigma(M) = delta_c / (nu * D(z))
    # Map sigma(M) to M using approximate relation:
    # sigma(M) ~ sigma_8 * (M / 10^{13} Msun)^{-1/3} (rough)
    nu_target = 4.0
    sigma_needed = 1.686 / (nu_target * Dz)

    # Invert: M = 10^{13} * (sigma_8 / sigma_needed)^3 Msun
    M_halo = 1e13 * Msun * (sigma_8 / sigma_needed)**3
    M_star = sfe * fb * M_halo

    return M_star, M_halo


def max_stellar_mass_modified(z, t_sf_fraction=0.5):
    """
    Maximum stellar mass at redshift z with modified inertia.

    In modified inertia framework (no dark matter):
    - Baryonic gas collapses directly
    - Collapse timescale is ~10-30 Myr
    - Multiple generations of collapse possible
    - Limited by available baryonic mass and cosmic time

    Parameters:
        z: redshift
        t_sf_fraction: fraction of available time spent forming stars
    Returns:
        M_star_max in kg
    """
    # Time available from z=30 to z
    t_avail = age_at_z(z) - age_at_z(30)

    # Star formation time
    t_sf = t_sf_fraction * t_avail

    # In modified regime, collapse takes ~20 Myr
    # Number of collapse generations possible
    t_collapse_typical = 20 * Myr  # conservative estimate
    n_generations = t_sf / t_collapse_typical

    # Baryonic mass within a comoving volume of ~(1 Mpc)^3
    rho_crit_0 = 3 * H0**2 / (8 * np.pi * G)
    rho_baryon_0 = rho_crit_0 * Ob
    V_comoving = (1 * Mpc)**3  # 1 Mpc^3
    M_baryon_available = rho_baryon_0 * V_comoving

    # With SFE ~ 10% per collapse and multiple generations,
    # effective SFE can reach 30-50%
    effective_sfe = 1 - (1 - 0.1)**n_generations  # compound efficiency
    effective_sfe = min(effective_sfe, 0.5)  # cap at 50%

    M_star = effective_sfe * M_baryon_available

    return M_star


# =============================================================
# MAIN CALCULATIONS
# =============================================================

def print_header(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def run_analysis():
    """Run the full analysis and generate outputs."""

    # ---------------------------------------------------------
    # 1. a_0(z) evolution
    # ---------------------------------------------------------
    print_header("1. CRITICAL ACCELERATION a_0(z) = cH(z)")
    print(f"{'z':>4s}  {'H(z)/H0':>8s}  {'a0(z) [m/s^2]':>14s}  {'a0(z)/a0(0)':>12s}  {'t(z) [Myr]':>11s}")
    print("-" * 60)

    z_list = [0, 2, 4, 6, 8, 10, 12, 14, 17, 20]
    for z in z_list:
        a0z = a0(z)
        t = age_at_z(z)
        print(f"{z:4d}  {E(z):8.1f}  {a0z:14.2e}  {a0z/a0_now:12.1f}  {t/Myr:11.0f}")

    # ---------------------------------------------------------
    # 2. Analysis of each JWST galaxy
    # ---------------------------------------------------------
    print_header("2. JWST GALAXY COLLAPSE ANALYSIS")

    results = []
    for name, z, logM, logM_err, ref, notes in jwst_galaxies:
        M_star = 10**logM * Msun
        # Baryonic mass of progenitor cloud (assume SFE ~ 10-30%)
        M_bary = M_star / 0.1  # gas mass needed at 10% SFE

        r = collapse_timescale(M_bary, z)

        t_universe = age_at_z(z) / Myr
        t_first_stars = age_at_z(30) / Myr
        t_avail = t_universe - t_first_stars

        results.append((name, z, logM, r, t_avail, t_universe))

        print(f"--- {name} (z={z}, log M*={logM}) ---")
        print(f"  Progenitor baryonic mass: {M_bary/Msun:.1e} Msun")
        print(f"  Cloud radius at turnaround: {r['R_kpc']:.1f} kpc")
        print(f"  Edge gravitational accel: {r['g_edge']:.2e} m/s^2")
        print(f"  a_0(z={z}): {r['a0_z']:.2e} m/s^2")
        print(f"  g/a_0 = {r['g_over_a0']:.2e}  (deep QI regime: << 1)")
        print(f"  Enhancement factor eta: {r['eta']:.0f}")
        print(f"  Standard free-fall: {r['t_ff_std_Myr']:.0f} Myr")
        print(f"  Modified (sqrt eta): {r['t_ff_mod_eta_Myr']:.1f} Myr")
        print(f"  Modified (const accel): {r['t_ff_mod_const_Myr']:.1f} Myr")
        print(f"  Modified (geometric mean): {r['t_ff_mod_geom_Myr']:.1f} Myr")
        print(f"  Age of universe: {t_universe:.0f} Myr")
        print(f"  Time available (from z=30): {t_avail:.0f} Myr")
        can_form = r['t_ff_mod_geom_Myr'] < t_avail
        can_form_std = r['t_ff_std_Myr'] < t_avail
        print(f"  Standard collapse in time? {'YES' if can_form_std else 'NO'}")
        print(f"  Modified collapse in time? {'YES' if can_form else 'NO'}")
        n_collapses = t_avail / r['t_ff_mod_geom_Myr']
        print(f"  Number of collapse times available: {n_collapses:.1f}")
        print()

    # ---------------------------------------------------------
    # 3. Mass-redshift comparison
    # ---------------------------------------------------------
    print_header("3. MAXIMUM STELLAR MASS vs REDSHIFT")
    print(f"{'z':>4s}  {'t [Myr]':>8s}  {'LCDM max (SFE=10%)':>20s}  {'LCDM max (SFE=100%)':>21s}  {'LCDM nu=4':>10s}")
    print("-" * 75)

    z_range = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 20])
    for z in z_range:
        t = age_at_z(z) / Myr
        Mstar_10, Mhalo_10 = max_stellar_mass_standard(z, sfe=0.1)
        Mstar_100, Mhalo_100 = max_stellar_mass_standard(z, sfe=1.0)
        nu = peak_height(z)
        print(f"{z:4d}  {t:8.0f}  {np.log10(Mstar_10/Msun):20.1f}  {np.log10(Mstar_100/Msun):21.1f}  {nu:10.1f}")

    # ---------------------------------------------------------
    # 4. Key prediction: t_collapse(z) vs t_available(z)
    # ---------------------------------------------------------
    print_header("4. COLLAPSE TIME vs AVAILABLE TIME")
    print("For a 10^10 Msun baryonic cloud (-> 10^9 Msun galaxy at 10% SFE):")
    print()
    M_test = 1e10 * Msun
    print(f"{'z':>4s}  {'t_avail [Myr]':>13s}  {'t_ff,std [Myr]':>14s}  {'t_ff,mod [Myr]':>14s}  {'Ratio':>7s}  {'N_collapses':>11s}  {'Feasible?':>10s}")
    print("-" * 85)

    for z in [6, 8, 10, 12, 14, 17, 20]:
        r = collapse_timescale(M_test, z)
        t_avail = (age_at_z(z) - age_at_z(30)) / Myr
        ratio = r['t_ff_std_Myr'] / r['t_ff_mod_geom_Myr']
        n_coll = t_avail / r['t_ff_mod_geom_Myr']
        feasible = "YES" if n_coll >= 1.0 else "NO"
        print(f"{z:4d}  {t_avail:13.0f}  {r['t_ff_std_Myr']:14.0f}  {r['t_ff_mod_geom_Myr']:14.1f}  {ratio:7.0f}  {n_coll:11.1f}  {feasible:>10s}")

    # ---------------------------------------------------------
    # 5. Growth factor enhancement analysis
    # ---------------------------------------------------------
    print_header("5. GROWTH FACTOR / PEAK HEIGHT ANALYSIS")
    print("Standard LCDM peak heights for 10^11 Msun halo (sigma_0 ~ 2):")
    print()
    print(f"{'z':>4s}  {'D(z)/D(0)':>10s}  {'nu (std)':>9s}  {'Assessment':>30s}")
    print("-" * 60)
    for z in [2, 4, 6, 8, 10, 12, 14]:
        Dz = D_norm(z)
        nu = peak_height(z)
        if nu < 3:
            assess = "Common"
        elif nu < 5:
            assess = "Rare but expected"
        elif nu < 7:
            assess = "Very rare"
        elif nu < 10:
            assess = "Essentially impossible"
        else:
            assess = "IMPOSSIBLE (>10 sigma)"
        print(f"{z:4d}  {Dz:10.4f}  {nu:9.1f}  {assess:>30s}")

    print(f"\nRequired growth enhancement to bring nu(z=12) to target:")
    Dz12 = D_norm(12)
    for nu_target in [3.0, 4.0, 5.0]:
        D_needed = 1.686 / (2.0 * nu_target)
        enhancement = D_needed / Dz12
        print(f"  nu = {nu_target}: need D(z)/D(0) = {D_needed:.3f}, enhancement = {enhancement:.2f}x")

    # ---------------------------------------------------------
    # 6. Summary table for paper
    # ---------------------------------------------------------
    print_header("6. SUMMARY: CAN MODIFIED INERTIA EXPLAIN EACH JWST GALAXY?")
    print(f"{'Galaxy':>20s}  {'z':>5s}  {'logM*':>6s}  {'t_avail':>8s}  {'t_coll,mod':>10s}  {'N_coll':>7s}  {'Verdict':>10s}")
    print("-" * 78)

    for name, z, logM, r, t_avail, t_universe in results:
        t_mod = r['t_ff_mod_geom_Myr']
        n_coll = t_avail / t_mod
        if n_coll >= 3:
            verdict = "EASY"
        elif n_coll >= 1:
            verdict = "FEASIBLE"
        else:
            verdict = "TIGHT"
        print(f"{name:>20s}  {z:5.1f}  {logM:6.1f}  {t_avail:7.0f} My  {t_mod:8.1f} My  {n_coll:7.1f}  {verdict:>10s}")

    print("\nVerdicts: EASY = multiple collapses possible, FEASIBLE = at least one, TIGHT = marginal")

    return results


def make_figures(results):
    """Generate figures for the paper."""

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Modified Inertia and JWST Early Massive Galaxies", fontsize=14, fontweight='bold')

    # ---------------------------------------------------------
    # Fig 1: a_0(z) evolution
    # ---------------------------------------------------------
    ax = axes[0, 0]
    z_arr = np.linspace(0, 25, 200)
    a0_arr = np.array([a0(z) for z in z_arr])

    ax.semilogy(z_arr, a0_arr, 'b-', linewidth=2)
    ax.axhline(a0_now, color='gray', linestyle='--', alpha=0.5, label=r'$a_0(z=0) = cH_0$')
    ax.set_xlabel('Redshift $z$')
    ax.set_ylabel(r'$a_0(z) = cH(z)$ [m/s$^2$]')
    ax.set_title(r'Critical acceleration $a_0(z)$')

    # Mark JWST galaxy redshifts
    for name, z, logM, logM_err, ref, notes in jwst_galaxies:
        ax.axvline(z, color='red', alpha=0.3, linewidth=0.8)
    ax.legend(fontsize=9)

    # ---------------------------------------------------------
    # Fig 2: Collapse time vs available time
    # ---------------------------------------------------------
    ax = axes[0, 1]
    z_arr2 = np.linspace(5, 22, 100)

    M_cloud = 1e10 * Msun  # progenitor cloud mass
    t_avail_arr = np.array([(age_at_z(z) - age_at_z(30)) / Myr for z in z_arr2])
    t_std_arr = np.array([collapse_timescale(M_cloud, z)['t_ff_std_Myr'] for z in z_arr2])
    t_mod_arr = np.array([collapse_timescale(M_cloud, z)['t_ff_mod_geom_Myr'] for z in z_arr2])

    ax.semilogy(z_arr2, t_avail_arr, 'k-', linewidth=2, label='Available time (from $z=30$)')
    ax.semilogy(z_arr2, t_std_arr, 'r--', linewidth=2, label=r'Standard $t_{\rm ff}$')
    ax.semilogy(z_arr2, t_mod_arr, 'b-', linewidth=2, label=r'Modified $t_{\rm ff}$')

    ax.fill_between(z_arr2, t_mod_arr, t_avail_arr,
                     where=t_mod_arr < t_avail_arr, alpha=0.15, color='blue',
                     label='Formation window')

    ax.set_xlabel('Redshift $z$')
    ax.set_ylabel('Timescale [Myr]')
    ax.set_title(r'Collapse time vs available time ($10^{10}\,M_\odot$ cloud)')
    ax.legend(fontsize=8, loc='upper right')
    ax.set_ylim(1, 5000)

    # ---------------------------------------------------------
    # Fig 3: JWST galaxies on mass-redshift plane
    # ---------------------------------------------------------
    ax = axes[1, 0]

    # Plot JWST data
    for name, z, logM, logM_err, ref, notes in jwst_galaxies:
        ax.errorbar(z, logM, yerr=logM_err, fmt='ro', markersize=8,
                     capsize=3, zorder=5)
        ax.annotate(name, (z, logM), fontsize=6, ha='left',
                     xytext=(5, 5), textcoords='offset points')

    # LCDM maximum (SFE=100%, nu=4)
    z_theory = np.linspace(5, 18, 50)
    lcdm_max = np.array([np.log10(max_stellar_mass_standard(z, sfe=1.0)[0] / Msun)
                          for z in z_theory])
    lcdm_10 = np.array([np.log10(max_stellar_mass_standard(z, sfe=0.1)[0] / Msun)
                          for z in z_theory])

    ax.plot(z_theory, lcdm_max, 'r--', linewidth=1.5,
            label=r'$\Lambda$CDM max (SFE=100%, $\nu$=4)')
    ax.plot(z_theory, lcdm_10, 'r:', linewidth=1.5,
            label=r'$\Lambda$CDM max (SFE=10%, $\nu$=4)')

    # Shade the "impossible" region
    ax.fill_between(z_theory, lcdm_max, 12, alpha=0.1, color='red',
                     label=r'Impossible in $\Lambda$CDM')

    ax.set_xlabel('Redshift $z$')
    ax.set_ylabel(r'$\log_{10}(M_\star / M_\odot)$')
    ax.set_title('JWST galaxies vs $\\Lambda$CDM limits')
    ax.legend(fontsize=7, loc='upper right')
    ax.set_xlim(5, 18)
    ax.set_ylim(6, 12)

    # ---------------------------------------------------------
    # Fig 4: Enhancement factor and regime
    # ---------------------------------------------------------
    ax = axes[1, 1]

    # g/a_0 for different cloud masses at each z
    z_arr3 = np.linspace(5, 20, 100)
    for logM_cloud, color, label in [(9, 'green', r'$10^9\,M_\odot$'),
                                      (10, 'blue', r'$10^{10}\,M_\odot$'),
                                      (11, 'red', r'$10^{11}\,M_\odot$')]:
        M = 10**logM_cloud * Msun
        ratios = []
        for z in z_arr3:
            r = collapse_timescale(M, z, overdensity=5.0)
            ratios.append(r['g_over_a0'])
        ax.semilogy(z_arr3, ratios, color=color, linewidth=2, label=label)

    ax.axhline(1.0, color='black', linestyle='--', alpha=0.5,
               label=r'$g = a_0(z)$ (QI boundary)')
    ax.fill_between(z_arr3, 0, 1, alpha=0.1, color='blue')
    ax.text(12, 0.3, 'Deep QI regime\n(modified inertia dominant)', fontsize=9,
            ha='center', style='italic', color='blue')

    ax.set_xlabel('Redshift $z$')
    ax.set_ylabel(r'$g_{\rm cloud} / a_0(z)$')
    ax.set_title('Protogalactic clouds: QI regime check')
    ax.legend(fontsize=8, loc='upper right')
    ax.set_ylim(1e-5, 10)

    plt.tight_layout()
    plt.savefig('/mnt/public/Vault/Resources/Physics/Projects/MassiveGalaxies/fig_jwst_analysis.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("\nFigure saved: fig_jwst_analysis.png")


# =============================================================
# RUN
# =============================================================
if __name__ == '__main__':
    results = run_analysis()
    make_figures(results)
