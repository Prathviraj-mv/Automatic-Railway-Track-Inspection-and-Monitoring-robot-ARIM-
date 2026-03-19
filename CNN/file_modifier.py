import pandas as pd
import os
import shutil

csv_file = "V1/test/_classes.csv"
image_dir = "V1/test"
output_dir = "test_sorted"

df = pd.read_csv(csv_file)

# all class columns (skip filename)
classes = df.columns[1:]

for _, row in df.iterrows():

    img = row["filename"]

    for c in classes:
        if row[c] == 1:

            class_folder = os.path.join(output_dir, c)
            os.makedirs(class_folder, exist_ok=True)

            src = os.path.join(image_dir, img)
            dst = os.path.join(class_folder, img)

            if os.path.exists(src):
                shutil.copy(src, dst)

print("Dataset converted to ImageFolder format")