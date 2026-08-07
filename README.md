# LOC-Dipole Prediction #7: Bulk Flow Anisotropy

### The Test
DESI Y3 2027 should measure `D(z=1.5) = 3.6 × 10⁻³`

### The Comparison  
**ΛCDM**: Predicts `D(1.5) ≈ 1.2 × 10⁻³` (flat)

**Falsification**: If DESI sees bulk flow, LOC is rejected. NO ACK UP.

### Run it
```python
# puka_dipole.py
def D(z): return 1.2e-3 * (1 + z)
print(f"D(z=1.5) = {D(1.5):.1e}")
'''
'''bash
python puka_dipole.py
'''
