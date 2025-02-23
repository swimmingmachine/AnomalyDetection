import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)
# create simulated data
fs = 500
t = np.linspace(0,1,fs)
ecg_clean = np.sin(2*np.pi*5*t)
noise = np.random.normal(0,0.2,ecg_clean.shape)
ecg_noisy = ecg_clean + noise

filtered_ecg = bandpass_filter(ecg_noisy, 0.5, 40, fs)

plt.figure(figsize=(10, 4))
plt.plot(t, ecg_noisy, label='Noisy ECG', alpha=0.5)
plt.plot(t, filtered_ecg, label='Filtered ECG', linewidth=2, color='red')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('ECG Signal Before and After Filtering')
plt.show()
