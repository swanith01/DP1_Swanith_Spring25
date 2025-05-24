import os
# ✅ Limit CPU threads for safety
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from classy import Class

try:
    cosmo = Class()
    cosmo.set({
        'output': 'mTk',
        'l_max_scalars': 10,              # very low for safety
        'P_k_max_1/Mpc': 0.5,
        'k_output_values': '0.1',
        'omega_b': 0.02237,
        'omega_cdm': 0.1200,
        'h': 0.674,
        'A_s': 2.1e-9,
        'n_s': 0.965,
        'tau_reio': 0.054,
    })
    cosmo.compute()

    transfers = cosmo.get_transfer(z=1100)
    print("✅ CLASS transfer keys:", list(transfers.keys()))
    print("ℓ values:", transfers['q'][:5])
    print("T0 sample:", transfers['t0'][:5])

    cosmo.struct_cleanup()
    cosmo.empty()

except Exception as e:
    print("❌ Something went wrong:", e)

