import numpy as np
import matplotlib.pyplot as plt
import time

from scipy.io import wavfile


#EXERCITIUL 1

def fft_manual(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    if N == 1:
        return x

    evenn = fft_manual(x[::2])
    oddd= fft_manual(x[1::2])

    k = np.arange(N // 2)
    W = np.exp(-2j * np.pi * k / N)

    half1 = evenn + W * oddd
    half2 = evenn - W * oddd

    return np.concatenate((half1, half2))

def dft_manual(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

### test
x_test = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x_manual = fft_manual(x_test)
x_numpy= np.fft.fft(x_test)

eps  = 1e-10
eroare = np.max(np.abs(x_manual - x_numpy))
print("Eroarea maxima:", eroare, eroare < eps)
###

dimen = [128, 256, 512, 1024, 2048, 4096, 8192]

t_dft = []
t_fft = []
t_numpy = []

for N in dimen:
    x = np.random.rand(N)

    start = time.perf_counter()
    dft_manual(x)
    t_dft.append(time.perf_counter() - start)

    start = time.perf_counter()
    fft_manual(x)
    t_fft.append(time.perf_counter() - start)

    start = time.perf_counter()
    np.fft.fft(x)
    t_numpy.append(time.perf_counter() - start)

    print(f"N = {N}: DFT = {t_dft[-1]:.6f}s, FFT = {t_fft[-1]:.6f}s, NumPy = {t_numpy[-1]:.6f}s")

plt.figure(figsize=(10, 5))

plt.plot(dimen, t_dft, label="DFT manual")
plt.plot(dimen, t_fft, label="FFT manual")
plt.plot(dimen, t_numpy, label="FFT NumPy")

plt.yscale("log")
plt.xlabel("N")
plt.ylabel("Timp")
plt.title("Timpi DFT si FFT")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("ex1.pdf")
plt.show()


## EXERCIIUL 2

fs = 6
durata = 1
frecv = [5, 17, 29]
t = np.linspace(0, durata, 5000)

n = np.arange(int(durata * fs) + 1)
t_esantioane = n / fs

fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True, sharey=True)

for i, f in enumerate(frecv):
    x = np.sin(2 * np.pi * f * t)
    x_esantioane = np.sin(2 * np.pi * f * t_esantioane)

    axs[i].plot(t, x)
    axs[i].scatter(t_esantioane, x_esantioane, color="red")

    axs[i].set_ylabel("Amplitudine")
    axs[i].set_title(f"f = {f} Hz")
    axs[i].grid()

axs[-1].set_xlabel("Timp")
fig.suptitle("Aliere")
plt.tight_layout()
plt.savefig("ex2.pdf")
plt.show()

## EXERCITIUL 3


fs = 60
durata = 1
frecv = [5, 17, 29]
t = np.linspace(0, durata, 5000)

n = np.arange(int(durata * fs) + 1)
t_esantioane = n / fs

fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True, sharey=True)

for i, f in enumerate(frecv):
    x = np.sin(2 * np.pi * f * t)
    x_esantioane = np.sin(2 * np.pi * f * t_esantioane)

    axs[i].plot(t, x)
    axs[i].scatter(t_esantioane, x_esantioane, color="red")

    axs[i].set_ylabel("Amplitudine")
    axs[i].set_title(f"f = {f} Hz")
    axs[i].grid()

axs[-1].set_xlabel("Timp")
fig.suptitle("Fara Aliere")
plt.tight_layout()
plt.savefig("ex3.pdf")
plt.show()

## EXERCITIUL 4
f_max = 200
prag = 2 * f_max

print(f"Frecventa de esantionare trebuie sa fie > {prag} Hz, de exp 500HZ")

## EXERCITIUL 6

fs, x = wavfile.read("vocale.wav")

x = x.astype(float)
N = len(x)

dim_grup = int(0.01 * N)
dim_grup -= dim_grup % 2
pas = dim_grup // 2

spectru = []
timpi = []

for start in range(0, N - dim_grup + 1, pas):
    grup = x[start:start + dim_grup]
    X = np.fft.fft(grup)

    spectru.append(np.abs(X[:dim_grup // 2 + 1]))
    timpi.append((start + dim_grup / 2) / fs)

spectru = np.array(spectru).T
timpi = np.array(timpi)
frecvente = np.arange(dim_grup // 2 + 1) * fs / dim_grup

plt.figure(figsize=(12, 6))

plt.pcolormesh(timpi, frecvente, spectru, cmap="magma")

plt.xlabel("Timp")
plt.ylabel("Frecv")
plt.title("Spectrograma vocalelor")
plt.ylim(0, min(5000, fs / 2))
plt.tight_layout()
plt.savefig("ex6_spectrograma.pdf")
plt.show()

## EXERCITIUL 7

SNR_db = 80
P_semnal_db = 90
SNR = 10 ** (SNR_db / 10)
P_semnal = 10 ** (P_semnal_db / 10)

P_zgomot = P_semnal / SNR
P_zgomot_db = 10 * np.log10(P_zgomot)
print("Puterea zgomotului, in dB:", P_zgomot_db)

# In dB, impartirea devine scadere prin proprietarile log:
# P_zgomot_db = P_semnal_db - SNR_db = 90 - 80 = 10 dB