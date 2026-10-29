import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# EXERCITIUL 1

N = 8
eps = 1e-8
F = np.zeros((N, N), dtype=complex)

for k in range(N):
    for n in range(N):
        F[k, n] = np.exp(-2j * np.pi * k * n / N)
        print(F[k, n].real, F[k, n].imag, end=" | ")
    print()

fig, axs = plt.subplots(N, 2, figsize=(14, 16), sharex=True, sharey=True)
fig.suptitle("Mat Fourier N = 8")

for k in range(N):
    axs[k, 0].plot(np.arange(N), F[k].real)
    axs[k, 0].set_ylabel(f"Row {k}")
    axs[k, 1].plot(np.arange(N), F[k].imag)

axs[0, 0].set_title("Real")
axs[0, 1].set_title("Imaginar")

fig.tight_layout()
fig.savefig("ex1.pdf")
plt.show()

FH = F.conj().T
G = FH @ F
diff = np.abs(G - N * np.eye(N))

print("FH F=N I", np.all(diff < eps))


# EXERCITIUL 2

fs = 1000
freq = 3
n = np.arange(fs)
t = n / fs
x = np.sin(2 * np.pi * freq * t)

plt.figure(figsize=(12, 4))
plt.plot(t, x)
plt.title(f"Sin {freq} Hz")
plt.xlabel("Timp (s)")
plt.ylabel("x(t)")
plt.grid()
plt.tight_layout()
plt.savefig("ex2_sig.pdf")
plt.show()

omega = [1, 2, 3, 8]

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for i in range(len(omega)):
    o = omega[i]
    z = x * np.exp(-2j * np.pi * o * t)

    ax = axs[i // 2, i % 2]
    r = np.abs(z)

    ax.scatter(z.real, z.imag, c=r, cmap="BuPu")
    ax.set_title(f"Infasuratoare {o} Hz")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imag")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.grid()

fig.tight_layout()
fig.savefig("ex2.pdf")
plt.show()


# ANIMATION

anim_fig = plt.figure(figsize=(12, 12))
gs = anim_fig.add_gridspec(3, 2)

sig_ax = anim_fig.add_subplot(gs[0, :])
sig_ax.plot(t, x)

sig_pt, = sig_ax.plot([], [], "ro", markersize=6)

sig_ax.set_title(f"Sin {freq} Hz")
sig_ax.grid()

zs = []
scats = []
pts = []

for i in range(len(omega)):
    o = omega[i]
    z = x * np.exp(-2j * np.pi * o * t)
    zs.append(z)

    ax = anim_fig.add_subplot(gs[1 + i // 2, i % 2])

    sc = ax.scatter([], [], c=[], cmap="BuPu", vmin=0, vmax=1)
    scats.append(sc)

    pt, = ax.plot([], [], "ro", markersize=6)
    pts.append(pt)

    ax.set_title(f"Infasuratoare {o} Hz")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imag")
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.grid()

anim_fig.tight_layout()


def update(k):
    sig_pt.set_data([t[k]], [x[k]])

    for i in range(len(omega)):
        z = zs[i]

        coords = np.column_stack((z.real[:k + 1], z.imag[:k + 1]))
        scats[i].set_offsets(coords)
        scats[i].set_array(np.abs(z[:k + 1]))

        pts[i].set_data([z.real[k]], [z.imag[k]])


frames = list(range(0, len(t), 5))

if frames[-1] != len(t) - 1:
    frames.append(len(t) - 1)

anim = FuncAnimation(anim_fig, update, frames=frames, interval=10, repeat=False)

update(len(t) - 1)
anim_fig.savefig("ex2_anim_final.pdf")

update(0)
plt.show()


# EXERCITIUL 3

fs = 1000
n = np.arange(fs)
t = n / fs

x1 = np.sin(2 * np.pi * 5 * t)
x2 = 2 * np.sin(2 * np.pi * 2 * t)
x3 = 0.5 * np.sin(2 * np.pi * 30 * t)

x = x1 + x2 + x3

plt.figure(figsize=(12, 4))
plt.plot(t, x)
plt.title("Frecv 5, 2, 30 Hz")
plt.xlabel("Timp (s)")
plt.ylabel("x(t)")
plt.grid()
plt.tight_layout()
plt.savefig("ex3_semnal.pdf")
plt.show()

N = len(x)
X = np.zeros(N, dtype=complex)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

freqs = np.arange(N) * fs / N

plt.figure(figsize=(12, 4))
plt.stem(freqs[:101], np.abs(X[:101]))
plt.grid()
plt.tight_layout()
plt.savefig("ex3.pdf")
plt.show()