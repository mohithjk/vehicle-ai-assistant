import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
df = pd.read_csv("cars.csv")

# Convert dataset to sentences
data = []

for _, row in df.iterrows():
    sentence = f"{row['name']} is a car with mileage of {row['mpg']} mpg, {row['cylinders']} cylinders engine, horsepower of {row['horsepower']}, weight {row['weight']} kg and was made in {row['model_year']}."
    data.append(sentence)

# Create embeddings
embeddings = model.encode(data)

print("🚗 Car AI Assistant Ready (type 'exit' to quit)\n")

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode(query)

    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    index = np.argmax(similarities)
    score = similarities[index]

    if score < 0.3:
        print("❌ Not enough data to answer.\n")
    else:
        print(f"✅ Answer: {data[index]}")
        print(f"🔎 Confidence: {round(score,2)}\n")