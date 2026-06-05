import pandas as pd
import time
from datetime import datetime

# =========================
# Study Configuration
# =========================

EXERCISE_DURATION = 40   # seconds
REST_DURATION = 30       # seconds

exercises = [
    "Stress Ball Squeeze",
    "Bicep Curls",
    "Seated Knee Lifts",
    "Overhead Press",
    "Calf Raises"
]

# =========================
# Data Logging
# =========================

log = []

participant_id = input("Enter Participant ID: ")

print("\nEMG Data Collection Starting...")
print("Prepare participant.\n")

time.sleep(5)

# =========================
# Exercise Protocol
# =========================

for exercise in exercises:

    print("\n" + "="*50)
    print(f"START EXERCISE: {exercise}")
    print(f"Duration: {EXERCISE_DURATION} seconds")
    print("="*50)

    start_time = datetime.now()

    # Countdown during exercise
    for remaining in range(EXERCISE_DURATION, 0, -1):
        print(f"\r{exercise}: {remaining:02d}s remaining", end="")
        time.sleep(1)

    end_time = datetime.now()

    print("\nExercise Complete!")

    log.append({
        "Participant_ID": participant_id,
        "Exercise": exercise,
        "Start_Time": start_time,
        "End_Time": end_time,
        "Duration_sec": EXERCISE_DURATION
    })

    # Rest period except after final exercise
    if exercise != exercises[-1]:

        print("\nREST PERIOD")
        print(f"Rest for {REST_DURATION} seconds")

        for remaining in range(REST_DURATION, 0, -1):
            print(f"\rRest: {remaining:02d}s remaining", end="")
            time.sleep(1)

        print("\nRest Complete.")

# =========================
# Save Protocol Log
# =========================

df = pd.DataFrame(log)

filename = f"{participant_id}_exercise_log.csv"
df.to_csv(filename, index=False)

print("\n" + "="*50)
print("ALL EXERCISES COMPLETED")
print(f"Log saved as: {filename}")
print("="*50)