from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("telecom_docs")

docs = [
    "High churn observed in 5G premium plans in metro regions.",
    "ARPU increased by 12% after bundled OTT offerings.",
    "Network congestion in Mumbai due to spectrum constraints."
]

embeddings = [model.encode(doc).tolist() for doc in docs]

collection.add(
    documents=docs,
    embeddings=embeddings,
    ids=["1","2","3"]
)

print("Vector DB Loaded")
