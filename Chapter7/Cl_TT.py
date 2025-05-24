
# import classy module
from classy import Class
import matplotlib.pyplot as plt
from math import pi


# create instance of the class "Class"
LambdaCDM = Class()
# pass input parameters
LambdaCDM.set({'omega_b':0.022032,'omega_cdm':0.12038,'h':0.67556,'A_s':2.215e-9,'n_s':0.9619,'tau_reio':0.0925})
LambdaCDM.set({'output':'tCl,pCl,lCl,mPk','lensing':'yes','P_k_max_1/Mpc':3.0})
# run class
LambdaCDM.compute()


# get all C_l output
cls = LambdaCDM.lensed_cl(2500)
# To check the format of cls
#print(cls.keys())

ll = cls['ell'][2:]
clTT = cls['tt'][2:]
clEE = cls['ee'][2:]
clPP = cls['pp'][2:]

# Compute spectrum in μK²
DlTT = clTT * ll * (ll + 1) / (2 * pi)*1e12

# Plot
plt.figure(figsize=(8,6))
plt.plot(ll, DlTT, label=r"$\ell(\ell+1)C_\ell^{TT}/2\pi$", color='darkred')
plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'Multipole $\ell$')
plt.ylabel(r'$[\mu K^2]$')
plt.title('CMB TT Power Spectrum (CLASS)')
plt.legend()
plt.tight_layout()
plt.savefig('warmup_cltt_fixed.png', dpi=300)
plt.show()



# optional: clear content of LambdaCDM (if you want to reuse it for another parameter set)
LambdaCDM.struct_cleanup()

