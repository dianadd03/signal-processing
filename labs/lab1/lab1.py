import numpy as np
import matplotlib.pyplot as plt

## EXERCITIUL 1

# A)

t = np.arange(0, 0.03, 0.0005)

# B)

x = np.cos(520 * np.pi * t + np.pi/3)
y = np.cos(280 * np.pi * t - np.pi/3)
z = np.cos(120 * np.pi * t + np.pi/3)

fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].plot(t, x)
axs[0].grid()
axs[1].plot(t, y)
axs[1].grid()
axs[2].plot(t, z)
axs[2].grid()
fig.savefig("ex1b.pdf")
plt.show()

#C)

fs = 200
n = np.arange(int(0.3 * 200))
ts = n / fs

xn = np.cos(520 * np.pi * ts + np.pi/3)
yn = np.cos(280 * np.pi * ts - np.pi/3)
zn = np.cos(120 * np.pi * ts + np.pi/3)

fign, axsn = plt.subplots(3, 1, sharex=True)

axsn[0].plot(t, x, color="red")
axsn[0].stem(ts, xn)
axsn[0].grid()

axsn[1].plot(t, y, color="red")
axsn[1].stem(ts, yn)
axsn[1].grid()

axsn[2].plot(t, z, color="red")
axsn[2].stem(ts, zn)
axsn[2].grid()

axsn[2].set_xlim(0, 0.03)
axsn[2].set_xlabel("Timp [s]")
fign.savefig("ex1c.pdf")
plt.show()


##EXERCITIUL 2

#A)

fs = 10000
n = np.arange(1600)
t = n / fs
x = np.sin(2 * np.pi * 400 * t)

fig, ax = plt.subplots(figsize=(12, 6))
ax.stem(t, x)
ax.set_xlim(0, 0.03)
ax.grid()
ax.set_title("sin 400hz 1600 esantioane")
plt.tight_layout()
fig.savefig("ex2a.pdf")
plt.show()


#B)
fs = 10000
n = np.arange(3 * fs)
t = n / fs
x = np.sin(2 * np.pi * 800 * t)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, x)
ax.set_xlim(0, 0.03)
ax.set_title("sin 800hz")
ax.grid()
plt.tight_layout()
fig.savefig("ex2b.pdf")
plt.show()

#C)

fs = 40000
n = np.arange(fs)
t = n / fs
x = 2 * np.mod(240 * t, 1) - 1

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlim(0, 0.03)
ax.grid()
ax.set_title("sawtooth")
plt.tight_layout()
fig.savefig("ex2c.pdf")
plt.show()



#D)


fs = 10000
n = np.arange(fs)
t = n / fs
x = np.sign(np.sin(2 * np.pi * 300 * t))
#
fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlim(0, 0.03)
ax.set_title("square")
ax.grid()
plt.tight_layout()
fig.savefig("ex2d.pdf")
plt.show()


## E)

I = np.random.rand(128, 128)

fig, ax = plt.subplots()
ax.imshow(I)
ax.set_title("2D random")
fig.savefig("ex2e.pdf")
plt.show()

## F)
I = np.zeros((128, 128))
I[3, 3] = 0.75
I[96:128, 96:128] = 0.5
I[:, ::16] = 1
I[::16, :] = 0.65
I[32:48, 32:48] = np.linspace(0, 1, 16)

fig, ax = plt.subplots()
ax.imshow(I)
ax.set_title("2D custom")
fig.savefig("ex2f.pdf")
plt.show()

## Exericiul 3
#a)  1/2000
#b)
esantioane_per_ora = 2000 * 60 * 60
biti = 2000 * 60 * 60 * 4
bytes_total = biti / 8
