import csv
import os
import json

from pathlib import Path

full_base_path = Path(__file__).resolve().parent

input_filename = full_base_path / "test_scores.csv"
output_filename = "output.json"

if os.path.exists(output_filename):
    os.remove(output_filename)


def finalavg(input_filename):
    average_final = 0.0
    count=0
    with open(input_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['exam_name'] == 'final':
                average_final = average_final + float(row['score'])
                count=count+1

    return average_final/count

def uniquestudents(input_filename):
    list1=[]
    with open(input_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            list1.append(row['student_id'])
    return len(set(list1))


if os.path.exists(output_filename):
    os.remove(output_filename)

result = {
    "average_final": finalavg(input_filename),
    "unique_students": uniquestudents(input_filename),
}

with open(output_filename, "w") as out:
    json.dump(result, out, indent=2)

