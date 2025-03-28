import os
import pandas as pd
import shutil
from sklearn.model_selection import train_test_split

# Paths
DATA_PATH = "data/frames"
LABELS_PATH = "data/labels.csv" 

# Output directories
TRAIN_PATH = "data/train"
VAL_PATH = "data/val"
TEST_PATH = "data/test"

# Create folders if they don't exist
for path in [TRAIN_PATH, VAL_PATH, TEST_PATH]:
    os.makedirs(path, exist_ok=True)

# Generate labels.csv if it doesn't exist
if not os.path.exists(LABELS_PATH):
    print("⚠️ 'labels.csv' not found — generating new labels...")

    # Generate labels (Example: alternating 'correct' and 'incorrect' postures)
    frames = sorted(os.listdir(DATA_PATH))
    labels = ["correct_posture" if i % 2 == 0 else "incorrect_posture" for i in range(len(frames))]

    # Create and save labels.csv
    labels_df = pd.DataFrame({"frame_name": frames, "label": labels})
    labels_df.to_csv(LABELS_PATH, index=False)
    print(f"✅ Labels.csv created successfully with {len(labels)} entries.")
else:
    labels_df = pd.read_csv(LABELS_PATH)

# Split data
train_data, test_data = train_test_split(labels_df, test_size=0.2, random_state=42)
train_data, val_data = train_test_split(train_data, test_size=0.1, random_state=42)

# Function to move files
def move_files(data, target_folder):
    for _, row in data.iterrows():
        src = os.path.join(DATA_PATH, row['frame_name'])
        dst = os.path.join(target_folder, row['frame_name'])
        if os.path.exists(src):
            shutil.copy(src, dst)

# Organize data
move_files(train_data, TRAIN_PATH)
move_files(val_data, VAL_PATH)
move_files(test_data, TEST_PATH)

print(f"✅ Data split complete: {len(train_data)} train, {len(val_data)} val, {len(test_data)} test samples.")
