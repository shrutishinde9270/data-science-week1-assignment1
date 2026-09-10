import kagglehub
import pandas as pd
import numpy as np
import os

path = kagglehub.dataset_download(
    "spscientist/students-performance-in-exams"
)

print("Path to dataset files:", path)


print("\nFiles in dataset folder:")
print(os.listdir(path))


file_path = os.path.join(path, "StudentsPerformance.csv")

df = pd.read_csv(file_path)

print("\nFirst 5 rows of dataset:")
print(df.head())


print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df["math score"] = df["math score"].fillna(
    df["math score"].mean()
)

df["reading score"] = df["reading score"].fillna(
    df["reading score"].mean()
)

df["writing score"] = df["writing score"].fillna(
    df["writing score"].mean()
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


print("\n--- Average Scores ---")

print("Average Math Score:",
      df["math score"].mean())

print("Average Reading Score:",
      df["reading score"].mean())

print("Average Writing Score:",
      df["writing score"].mean())


print("\n--- Maximum Scores ---")

print("Maximum Math Score:",
      df["math score"].max())

print("Maximum Reading Score:",
      df["reading score"].max())

print("Maximum Writing Score:",
      df["writing score"].max())


print("\n--- Minimum Scores ---")

print("Minimum Math Score:",
      df["math score"].min())

print("Minimum Reading Score:",
      df["reading score"].min())

print("Minimum Writing Score:",
      df["writing score"].min())



result = df[
    ["math score", "reading score", "writing score"]
].agg(["mean", "max", "min"])

print("\n--- Student Marks Analysis ---")
print(result)


math = df["math score"].to_numpy()
reading = df["reading score"].to_numpy()
writing = df["writing score"].to_numpy()

print("\n--- Using NumPy ---")

print("Math Average:", np.mean(math))
print("Math Maximum:", np.max(math))
print("Math Minimum:", np.min(math))

print("Reading Average:", np.mean(reading))
print("Reading Maximum:", np.max(reading))
print("Reading Minimum:", np.min(reading))

print("Writing Average:", np.mean(writing))
print("Writing Maximum:", np.max(writing))
print("Writing Minimum:", np.min(writing))