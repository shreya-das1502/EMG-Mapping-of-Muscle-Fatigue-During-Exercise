# EMG-Mapping-of-Muscle-Fatigue-During-Exercise

## Overview

This project investigates muscle fatigue, motor unit recruitment, fiber type dominance, neuromuscular coordination, and training-related adaptations using surface Electromyography (EMG).

A custom EMG acquisition system based on Arduino and surface electrodes was used to record muscle activity during standardized exercises. Signal processing and analysis were performed in Python to extract physiological metrics including RMS amplitude, Median Frequency (MDF), Mean Frequency (MNF), Integrated EMG (iEMG), Central Fatigue Index (CFI), and Motor Unit Activity (MUA).

The study compares trained and untrained participants across multiple exercise modalities to quantify the effects of training on neuromuscular performance and fatigue resistance.

---

## Research Objectives

- Quantify muscle fatigue using EMG-derived metrics
- Assess muscle fiber type dominance through frequency-domain analysis
- Analyze motor unit recruitment and firing patterns
- Evaluate muscle synergy and inter-muscle coordination
- Measure neuromuscular activation timing characteristics
- Compare fatigue responses across exercises and demographic groups

---

## Experimental Setup

### Hardware

- Arduino Uno
- Single-channel Surface EMG Sensor
- Disposable Surface Electrodes
- Personal Computer

### Software

- Arduino IDE
- Python
- NumPy
- SciPy
- Pandas
- Matplotlib

### Signal Processing

- Sampling Rate: 1000 Hz
- Fourth-order Butterworth Bandpass Filter
- Noise and Motion Artifact Removal
- Feature Extraction Pipeline

---

## Exercises Performed

Participants performed five standardized exercises:

1. Stress Ball Squeeze
2. Bicep Curls
3. Seated Knee Lifts
4. Overhead Press
5. Calf Raises

Each exercise was performed for 40 seconds with 30-second recovery intervals.

---

## Participant Groups

The study involved healthy adults aged 18–30 years.

### Trained Group
- Gym-going males
- Gym-going females

### Untrained Group
- Non-gym males
- Non-gym females

Participants were categorized based on exercise history and resistance training experience.

---

## EMG Parameters Extracted

### Amplitude-Based Metrics

- RMS (Root Mean Square)
- Integrated EMG (iEMG)
- Signal Amplitude

### Frequency-Based Metrics

- Median Frequency (MDF)
- Mean Frequency (MNF)

### Fatigue Metrics

- Central Fatigue Index (CFI)
- Fatigue Decrement Ratio (FDR)

### Motor Unit Metrics

- Motor Unit Activity (MUA)
- Recruitment Strength
- Firing Frequency

### Temporal Metrics

- Activation Onset Time
- Activation Duration
- Neuromuscular Response Timing

---

## Methodology

1. Surface electrodes were placed over target muscle groups.
2. EMG signals were acquired using an Arduino-based recording setup.
3. Raw signals were filtered using a Butterworth bandpass filter.
4. Processed signals underwent feature extraction.
5. Statistical analysis was performed across demographic groups.
6. Fatigue, coordination, and recruitment metrics were compared between trained and untrained participants.

---

## Project Workflow

```text
EMG Signal Acquisition
           ↓
Signal Conditioning
           ↓
Digital Filtering
           ↓
Feature Extraction
           ↓
Statistical Analysis
           ↓
Fatigue & Coordination Assessment
```

---

## Results

### Muscle Fatigue

- Trained participants demonstrated higher RMS, iEMG, and CFI values.
- Fatigue progression was slower in trained individuals.
- Gym-going participants maintained more stable muscle activation across tasks.

### Fiber Type Dominance

- Trained participants exhibited MDF values predominantly above 100 Hz.
- Results suggest greater fast-twitch fiber recruitment.
- Untrained participants showed characteristics associated with slow-twitch dominance.

### Motor Unit Recruitment

- Higher amplitude and MUA values were observed in trained subjects.
- Stronger recruitment and firing efficiency were associated with resistance training.

### Muscle Synergy and Coordination

- Trained groups showed more stable RMS and iEMG profiles.
- Improved inter-muscle coordination was observed across exercises.

### Neuromuscular Activation

- Faster activation onset times were observed in trained participants.
- Enhanced neural efficiency and motor control were demonstrated.

---

## Key Findings

| Metric | Observation |
|----------|------------|
| Fatigue Resistance | Higher in trained individuals |
| RMS | Greater muscle activation in trained groups |
| MDF/MNF | Increased fast-twitch recruitment |
| MUA | Improved motor unit recruitment |
| Coordination | Enhanced muscle synergy |
| Response Time | Faster neuromuscular activation |

---

## Key Analyses Performed

- EMG-based muscle fatigue quantification
- Motor unit recruitment and firing pattern analysis
- Fast-twitch vs. slow-twitch fiber dominance assessment
- Neuromuscular coordination and activation timing evaluation
- Exercise-wise fatigue comparison across demographic groups
- Statistical analysis of training-related neuromuscular adaptations

---

## Applications

- Sports Performance Analysis
- Rehabilitation Engineering
- Physiotherapy Assessment
- Neuromuscular Disorder Monitoring
- Human Performance Optimization
- Wearable Biosignal Systems
- Personalized Training Programs

---

## Limitations

- Limited participant sample size
- Single-channel EMG acquisition
- Surface EMG cannot assess deep muscle activity
- Electrode placement variability
- Cross-sectional study design

---

## Future Work

- Multi-channel EMG acquisition
- Real-time fatigue monitoring dashboard
- Machine learning-based fatigue prediction
- Wearable EMG system development
- Larger participant cohorts
- Clinical rehabilitation studies

---

## Author

**Shreya Das**  
Electronics and Communication Engineering (Biomedical Engineering)  
Vellore Institute of Technology


---

## License

This project was conducted for academic and research purposes.
