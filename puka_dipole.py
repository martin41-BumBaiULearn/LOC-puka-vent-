# LOC Prediction #7: Puka Vent Dipole Model
# Author: Martin Kaipo Kalani Kanakaole [ORCID: 0009-0002-0033-7140]
# Falsifiable with DESI Y3 2027. NO ACK UP. For Joey.

D0 = 1.2e-3  # Secrest+2022 quasar dipole at z=0

def dipole(z):
    """
    Predicts quasar dipole amplitude D(z) from void infall.
    LOC: D(z) = D0 * (1 + z)
    LCDM: D(z) ≈ D0 (flat)
    """
    return D0 * (1 + z)

if __name__ == "__main__":
    z_test = 1.5
    D_loc = dipole(z_test)
    D_lcdm = D0
    
    print(f"LOC Prediction #7:")
    print(f"D(z={z_test}) = {D_loc:.1e}")
    print(f"LCDM expects:   {D_lcdm:.1e}")
    print(f"Ratio:          {D_loc/D_lcdm:.1f}x")
    print("\nDESI Y3 2027 decides. To the principle of least resistance.")
