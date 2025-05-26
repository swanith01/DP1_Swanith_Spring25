import numpy as np
import matplotlib.pyplot as plt
import camb
import os

# Output directory
os.makedirs("TT_frames_tau_variation", exist_ok=True)

# Load Planck 2018 binned TT data
planck_data = np.loadtxt("Planck_TT_data.txt")
ell_planck = planck_data[:, 0]
Dl_planck = planck_data[:, 1]
Dl_err = planck_data[:, 2]

tau_values = np.linspace(0.0, 2.0, 20)
#ls = np.arange(2, 3001)
#factor = ls * (ls + 1) / (2 * np.pi)
#pars = camb.CAMBparams()
#results = camb.get_results(pars)
#totCL = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total']
#ls = np.arange(totCL.shape[0])

for i, tau in enumerate(tau_values):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, tau=tau)
    pars.InitPower.set_params(As=2e-9, ns=0.965)
    pars.set_for_lmax(3000, lens_potential_accuracy=1)
    pars.WantTensors = True
    results = camb.get_results(pars)
    totCL = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total']
    ls = np.arange(totCL.shape[0])

    
    Dl_tt = np.sqrt(totCL[2:, 0])# * factor[2:])
    #Dl_ee = np.sqrt(totCL[2:, 1] )#* factor[2:])
    #Dl_bb = np.sqrt(np.abs(totCL[2:, 2]))# * factor[2:]))
    #Dl_te = np.sign(totCL[2:, 3]) * np.sqrt(np.abs(totCL[2:, 3]))/(Dl_tt*Dl_ee)**0.5#* factor[2:]))

    plt.figure(figsize=(10, 6))
    plt.loglog(ls[2:], Dl_tt, label='TT', color='gold')

    # Planck data
    plt.errorbar(ell_planck, Dl_planck, yerr=Dl_err, fmt='o', color='black',
            ecolor='gray', elinewidth=1, capsize=2, label='Planck 2018 TT (binned)', markersize=3)

    #plt.loglog(ls[2:], Dl_ee, label='EE', color='deeppink')
    #plt.loglog(ls[2:], Dl_bb, label='BB', color='blue')
    #plt.plot(ls[2:], Dl_te, label='TE', color='limegreen')
    plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel(r'Multipole $\ell$')
    plt.ylabel(r'$\Delta T\ (\mu K)$')
    plt.title(f"CMB Spectra (τ = {tau:.3f})")
    #plt.ylim(0.1, 100)
    #plt.xlim(2, 3000)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"TT_frames_tau_variation/frame_{i:02d}.png")
    plt.close()

