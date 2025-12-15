import numpy as np
import matplotlib.pyplot as plt

# Time parameters
fs = 100000          # Sampling frequency (Hz)
t = np.arange(0, 0.02, 1/fs)

# Message signal
fm = 400             # Message frequency (Hz)
Am = 1               # Message amplitude
message = Am * np.sin(2 * np.pi * fm * t)

# Carrier signal parameters
fc = 5000            # Carrier frequency (Hz)
Ac = 1               # Carrier amplitude

# FM parameters
beta = 5             # Frequency modulation index

# Frequency Modulation (FM)
fm_signal = Ac * np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, Ac * np.cos(2 * np.pi * fc * t))
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, fm_signal)
plt.title("FM Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
