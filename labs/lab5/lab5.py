import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

eps = 1e-10

date = np.genfromtxt("Train.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")

x = np.asarray(date["Count"], dtype=float)
N = len(x)

##  EXERCITIUL 1
#a)

Ts = 3600
fs = 1 / Ts
print("Frecv de esantionare:", fs, "Hz")

#b)
nr_ore = N
nr_zile = N / 24
print(f"Nr de ore: {N}")
print(f"Nr de zile: {nr_zile}")

#c)
f_max = fs / 2
print(f"Lim Nyquist: {f_max}")

#d)
X = np.fft.fft(x)
modul = np.abs(X[:N//2]) / N
frecv = np.arange(N//2) * fs / N
per_zile = 1 / frecv[1:] / (3600*24)

fig, axs = plt.subplots(2, 1, figsize=(12, 8))
axs[0].plot(frecv, modul)
axs[0].set_title("Modulul transf Fourier")
axs[0].set_xlabel("Frecv")
axs[0].set_ylabel("|X| / N")
axs[0].grid()

axs[1].plot(per_zile, modul[1:])
axs[1].set_title("Spectru in functie de per")
axs[1].set_xlabel("Perioada")
axs[1].set_ylabel("|X| / N")
axs[1].set_xscale("log")
axs[1].grid()

plt.tight_layout()
plt.savefig("ex1_d.pdf")
plt.show()

#e)
media = np.mean(x)
print(media)
print(f"Componenta continua: {abs(media) > eps}")

x_centrat = x - media
print("Media dupa centrare:", np.mean(x_centrat))

X_centrat = np.fft.fft(x_centrat)
XC_modul = np.abs(X_centrat[:N//2]) / N

plt.figure(figsize=(12, 5))
plt.plot(frecv, XC_modul)
plt.title("Spectrul fara componenta continua")
plt.xlabel("Frecventa")
plt.ylabel("|X_centrat| / N")
plt.grid()
plt.tight_layout()
plt.savefig("ex1_e.pdf")
plt.show()


#f)
indx = np.argsort(XC_modul[1:])[-4:]
indx = indx[::-1] + 1

for i in indx:
    per_ore = 1 / frecv[i] / 3600
    per_zile = per_ore / 24
    print(f"Modul: {XC_modul[i]:.4f}, frecv: {frecv[i]:.10f} Hz, per: {per_ore:.2f} ore = {per_zile:.2f} zile")

#g
dates = np.array([datetime.strptime(t, "%d-%m-%Y %H:%M") for t in date["Datetime"]])
start = 1001

while dates[start].weekday() != 0 or dates[start].hour != 0:
    start += 1

stop = start + 30 * 24

print("Start:", start)
print("Data de inceput:", dates[start])
print("Ultimul mom:", dates[stop - 1])

plt.figure(figsize=(12, 5))
plt.plot(dates[start:stop], x[start:stop])
plt.title("Trafic pentru 30 de zile")
plt.xlabel("Data")
plt.ylabel("Nr masini")
plt.grid()
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig("ex1_g.pdf")
plt.show()

#h)
# As analiza semnalul pe intervale de aprox 3 luni cautand variatii sezoniere, scaderi de trafic in perioada sarbatorilor
# si cresteri asociate inceperii anului scolar
# As verifica daca tiparele se repeta dupa un an, apoi as numara inapoi esantioanele orare pentru a estima data de inceput
# Metoda este aprox, deoarece traficul depinde si de vreme, localitate si evenimente neprevazute. Data exacta nu poate fi determinata sigur doar din semnal.

#i)
f_prag = 1 / (8 * 3600)
X = np.fft.fft(x)
frecvente = np.fft.fftfreq(N, d=Ts)

X_filtrat = X.copy()
X_filtrat[np.abs(frecvente) > f_prag] = 0
x_filtrat = np.fft.ifft(X_filtrat).real

fig, axs = plt.subplots(2, 1, figsize=(12, 7), sharex=True, sharey=True)

axs[0].plot(dates[start:stop], x[start:stop])
axs[0].set_title("Semnal original")
axs[0].set_ylabel("Nr masini")
axs[0].grid()

axs[1].plot(dates[start:stop], x_filtrat[start:stop])
axs[1].set_title("Semnal filtrat - prag de 8 ore")
axs[1].set_xlabel("Data")
axs[1].set_ylabel("Nr masini")
axs[1].grid()

fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("ex1_i.pdf")
plt.show()