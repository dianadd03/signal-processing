import numpy as np
import matplotlib.pyplot as plt
import scipy
import sounddevice


# # EXERCITIUL 1

## a)

fs = 40000
n = np.arange(fs)
t = n / fs
x = np.sin(2 * np.pi * 200 * t)
y = np.cos(2 * np.pi * 200 * t - np.pi/2)

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot(t, x, color="red", label="sin")
axs[0].grid()
axs[0].legend()

axs[1].plot(t, y, color="blue", label="cos")
axs[1].grid()
axs[1].legend()

axs[1].set_xlim(0, 0.03)
axs[1].set_xlabel("Timp [s]")
fig.savefig("ex1.pdf")
plt.show()


## EXERCITIUL 2


fs = 10000
n = np.arange(fs)
t = n / fs

fig, axs = plt.subplots(1, 1, sharex=True)

for i in range(4):
    x = np.sin(2 * np.pi * 50 * t + i * np.pi/2)
    axs.plot(t, x, label=f"Faza {i} * pi/2")
    axs.grid()
    axs.legend()


axs.set_xlim(0, 0.03)
axs.set_xlabel("Timp [s]")
fig.savefig("ex2.pdf")
plt.show()

## SNR

fs = 10000
n = np.arange(fs)
t = n / fs
x = np.sin(2 * np.pi * 50 * t)

z = np.random.normal(loc=0, scale=1, size=len(x))
snr = [0.1, 1, 10, 100]

fig, axs = plt.subplots(4, 1, figsize=(8, 8), sharex=True)

for i in range(4):
    gamma = np.linalg.norm(x) / (np.sqrt(snr[i]) * np.linalg.norm(z))
    y = x + gamma * z

    axs[i].plot(t, y)
    axs[i].plot(t, x, color="black")
    axs[i].grid()

axs[3].set_xlim(0, 0.03)
axs[3].set_xlabel("Timp [s]")
fig.savefig("ex2_snr.pdf")
plt.show()


## EXERCITIUL 3

fs = 44100
durata = 1
n = np.arange(int(durata * fs))
t = n / fs
x = np.sin(2 * np.pi * 400 * t)
scipy.io.wavfile.write("lab1_2a.wav", fs, x)
sounddevice.play(x, fs)
sounddevice.wait()

rate, semnal = scipy.io.wavfile.read("lab1_2a.wav")
sounddevice.play(semnal, rate)
sounddevice.wait()

fs = 44100
durata = 1
n = np.arange(int(durata * fs))
t = n / fs
x = np.sin(2 * np.pi * 800 * t)
scipy.io.wavfile.write("lab1_2b.wav", fs, x)
sounddevice.play(x, fs)
sounddevice.wait()

fs = 44100
durata = 1
n = np.arange(int(durata * fs))
t = n / fs
x = 2 * np.mod(240 * t, 1) - 1
scipy.io.wavfile.write("lab1_2c.wav", fs, x)
sounddevice.play(x, fs)
sounddevice.wait()

fs = 44100
durata = 1
n = np.arange(int(durata * fs))
t = n / fs
x = np.sign(np.sin(2 * np.pi * 300 * t))
scipy.io.wavfile.write("lab1_2d.wav", fs, x)
sounddevice.play(x, fs)
sounddevice.wait()

#EXERCITIUL 4

fs = 44100
durata = 1
n = np.arange(int(durata * fs))
t = n / fs
sin = np.sin(2 * np.pi * 100 * t)
sawt = 2 * np.mod(240 * t, 1) - 1
summ = sin + sawt

fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].plot(t, sin, label="sin")
axs[0].grid()
axs[0].legend()

axs[1].plot(t, sawt, label="sawtooth")
axs[1].grid()
axs[1].legend()

axs[2].plot(t, summ, label="sum")
axs[2].grid()
axs[2].legend()

axs[2].set_xlim(0, 0.03)
axs[2].set_xlabel("Timp [s]")
fig.savefig("ex4.pdf")
plt.show()

sounddevice.play(sin, fs)
sounddevice.wait()
sounddevice.play(sawt, fs)
sounddevice.wait()
sounddevice.play(summ, fs)
sounddevice.wait()

## EXERCITIUL 5
fs = 44100
durata = 2
n = np.arange(int(durata * fs))
t = n / fs
sig = np.concatenate((np.sin(2 * np.pi * 100 * t), np.sin(2 * np.pi * 600 * t)))

## Prima data se aude un sunet de 100hz si apoi unul mai inalt de 600hz, unul dupa altul
sounddevice.play(sig, fs)
sounddevice.wait()

## EXERCITIUL 6
fs = 44100
n = np.arange(fs)
t = n / fs
s1 = np.sin(2 * np.pi * fs/2 * t)
s2 = np.sin(2 * np.pi * fs/4 * t)
s3 = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].plot(t, s1, label="fs/2")
axs[0].grid()
axs[0].legend()

#Se produc valori foarte mici in loc de 0 exact din cauza preciziei numerice

axs[1].plot(t, s2, label="fs/4")
axs[1].grid()
axs[1].legend()

axs[2].plot(t, s3, label= "f=0")
axs[2].grid()
axs[2].legend()

axs[2].set_xlim(0.05, 0.058)
axs[2].set_xlabel("Timp [s]")
fig.savefig("ex6.pdf")
plt.show()

# EXERCITIUL 7

fs = 1000
n = np.arange(fs)
t = n / fs
x = np.sin(2 * np.pi * 50 * t)

y = x[::4]
z = x[1::4]

fig, axs = plt.subplots(3, 1, sharex=True)

axs[0].plot(t, x)
axs[0].set_title("Semnal initial")
axs[0].grid()


axs[1].plot(t[::4], y)
axs[1].set_title("Decimare de la primul element")
axs[1].grid()

axs[2].plot(t[1::4], z)
axs[2].set_title("Decimare de la al doilea element")
axs[2].grid()

axs[2].set_xlim(0, 0.06)
axs[2].set_xlabel("Timp [s]")
fig.savefig("ex7.pdf")
plt.show()

## Frecventa de esantionare este de 4 ori mai mica, deci "graficul are colturi" fiindca se evalueaza in mai putine puncte.
## Daca pornim de la al doilea element, se selecteaza alta puncte pentru esantionare, deplasate fata de graficul anterior cu 1/1000.

## EXERCITIUL 8
alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)
x = np.sin(alpha)
y = alpha
z = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)

err_taylor = np.abs(x - y)
err_pade = np.abs(x - z)

fig, axs = plt.subplots(3, 1, sharex=True)

axs[0].plot(alpha, x, label="sin(alpha)")
axs[0].plot(alpha, y, label="Taylor")
axs[0].plot(alpha, z, label="Pade")
axs[0].legend()
axs[0].grid()

axs[1].plot(alpha, err_taylor, label="Eroare Taylor")
axs[1].plot(alpha, err_pade, label="Eroare Pade")
axs[1].legend()
axs[1].grid()

axs[2].plot(alpha, err_taylor, label="Eroare Taylor")
axs[2].plot(alpha, err_pade, label="Eroare Pade")
axs[2].set_yscale("log")
axs[2].legend()
axs[2].grid()

axs[2].set_xlim(-np.pi / 2, np.pi / 2)
axs[2].set_xlabel("alpha [rad]")
plt.tight_layout()
fig.savefig("ex8.pdf")
plt.show()