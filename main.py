import csv
import os
import json

from pathlib import Path

full_base_path = Path(__file__).resolve().parent

input_filename = full_base_path / "test_scores.csv"
output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)

average_final = 0.0
unique_students = 0

with open(input_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

        # TODO: compute average final score
        # TODO: unique student count
        if row['exam_name']=='final':
            average_final=average_final+float(row['score'])
            unique_students=unique_students+1

average_final=round(average_final/unique_students, 1)

if os.path.exists(output_filename):
    os.remove(output_filename)

result = {
    "average_final": average_final,
    "unique_students": unique_students,
}

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

