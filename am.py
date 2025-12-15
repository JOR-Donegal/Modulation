import numpy as np
import matplotlib.pyplot as plt

# Time parameters
fs = 100000          # Sampling frequency (Hz)
t = np.arange(0, 0.02, 1/fs)

# Message signal (baseband)
fm = 200             # Message frequency (Hz)
Am = 1               # Message amplitude
message = Am * np.sin(2 * np.pi * fm * t)

# Carrier signal
fc = 5000            # Carrier frequency (Hz)
Ac = 1               # Carrier amplitude
carrier = Ac * np.cos(2 * np.pi * fc * t)

# Modulation index
ka = 0.8             # Must be <= 1 to avoid overmodulation

# Amplitude Modulation (AM)
am_signal = (1 + ka * message) * carrier

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title("AM Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
