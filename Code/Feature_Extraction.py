import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt, welch

# ==========================
# Load EMG Data
# ==========================

data = pd.read_csv("emg_data.csv")

emg = data["EMG"].values

# ==========================
# Parameters
# ==========================

fs = 1000  # Sampling Frequency (Hz)

# ==========================
# Butterworth Bandpass Filter
# ==========================

lowcut = 20
highcut = 450
order = 4

nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist

b, a = butter(order, [low, high], btype='band')

filtered_emg = filtfilt(b, a, emg)

# ==========================
# RMS
# ==========================

rms = np.sqrt(np.mean(filtered_emg**2))

# ==========================
# Integrated EMG (iEMG)
# ==========================

iemg = np.sum(np.abs(filtered_emg))

# ==========================
# Mean Amplitude
# ==========================

mean_amplitude = np.mean(np.abs(filtered_emg))

# ==========================
# Frequency Analysis
# ==========================

freqs, psd = welch(filtered_emg, fs)

# Mean Frequency (MNF)
mnf = np.sum(freqs * psd) / np.sum(psd)

# Median Frequency (MDF)
cumulative_power = np.cumsum(psd)
mdf = freqs[np.where(cumulative_power >= cumulative_power[-1]/2)[0][0]]

# ==========================
# Activation Timing
# ==========================

threshold = 0.1 * np.max(np.abs(filtered_emg))

active_samples = np.where(np.abs(filtered_emg) > threshold)[0]

if len(active_samples) > 0:
    onset_time = active_samples[0] / fs
    activation_duration = (
        active_samples[-1] - active_samples[0]
    ) / fs
else:
    onset_time = 0
    activation_duration = 0

# ==========================
# Results
# ==========================

print("----- EMG Features -----")
print(f"RMS: {rms:.4f}")
print(f"iEMG: {iemg:.4f}")
print(f"Mean Amplitude: {mean_amplitude:.4f}")
print(f"Mean Frequency: {mnf:.2f} Hz")
print(f"Median Frequency: {mdf:.2f} Hz")
print(f"Activation Onset: {onset_time:.3f} s")
print(f"Activation Duration: {activation_duration:.3f} s")