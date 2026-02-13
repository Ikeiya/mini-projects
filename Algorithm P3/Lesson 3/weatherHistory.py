import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import scipy.optimize

def fit_sin(tt, yy):
    '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
    tt = np.array(tt)
    yy = np.array(yy)
    ff = NotImplementedError.fft.fftfreq(len(tt), (tt[1]-tt[0]))   # assume uniform spacing
    Fyy = abs(np.fft.fft(yy))
    guess_freq = abs(ff[np.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
    guess_amp = np.std(yy) * 2.**0.5
    guess_offset = np.mean(yy)
    guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

    def sinfunc(t, A, w, p, c):  return A * np.sin(w*t + p) + c
    popt, pcov = scipy.optimize.curve_fit(sinfunc, tt, yy, p0=guess)
    A, w, p, c = popt
    f = w/(2.*np.pi)
    fitfunc = lambda t: A * np.sin(w*t + p) + c
    return {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1./f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess,popt,pcov)}
    
df = pd.read_csv('weatherHistory.csv')

temperature = df["Temperature (C)"]
date = pd.to_datetime(df["Formatted Date"])
fig, ax = plt.subplots()

coefficients = np.polyfit(date, temperature, 2) #to do
poly = np.poly1d(coefficients)

ax.set(xlabel='time', ylabel='Temperature (C)',
       title='Stuff')
ax.grid()

res = fit_sin(date, temperature)

plt.scatter(date, temperature, s=0.1)
plt.plot(temperature, res["fitfunc"](temperature), "r-", label="y fit curve", linewidth=2)

plt.show()

dates = df["Formatted Date"].sort_values(by='dttime')

