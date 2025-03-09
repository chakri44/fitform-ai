import os
import pandas as pd
import random

# Paths
DATA_PATH = "data/frames"
LABELS_PATH = "data/labels.csv"

# List all frames
frames = sorted([f for f in os.listdir(DATA_PATH) if f.endswith('.jpg')])

# Generate random labels (example: 'correct_posture' or 'incorrect_posture')
labels = [random.choice(['correct_posture', 'incorrect_posture']) for _ in frames]

# Create DataFrame
labels_df = pd.DataFrame({
    'frame_name': frames,
    'label': labels
})

# Save to CSV
labels_df.to_csv(LABELS_PATH, index=False)

print(f"✅ Labels file created with {len(frames)} entries.")
