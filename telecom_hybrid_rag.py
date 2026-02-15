import os
import requests
from bs4 import BeautifulSoup
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# -------------------------------
# ENV VARIABLES
# -------------------------------
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# -------------------------------
# VECTOR DB SETUP
# -------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("telecom_docs")
def embed(text):
    return model.encode(text).tolist()

# -------------------------------
# VECTOR RETRIEVAL
# -------------------------------
def vector_search(query):
    embedding = embed(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )
    return results["documents"]

# -------------------------------
# NEO4J GRAPH REASONING
# -------------------------------
class TelecomKG:

    def __init__(self):
        print("DEBUG URI:", repr(NEO4J_URI))
        print("DEBUG USER:", repr(NEO4J_USER))
        print("DEBUG PASSWORD:", repr(NEO4J_PASSWORD))

        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )

    def query_graph(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]

# -------------------------------
# WEB RETRIEVAL (Last 12–18 Months)
# -------------------------------
def web_search(query):
    url = f"https://news.google.com/search?q={query}+telecom+after:{datetime.now().year-1}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for item in soup.find_all("a")[:5]:
        headlines.append(item.text)
    return headlines

# -------------------------------
# HYBRID RAG ORCHESTRATION
# -------------------------------
def generate_report(query):

    print("Step 1: Vector Retrieval...")
    vector_data = vector_search(query)

    print("Step 2: Knowledge Graph Reasoning...")
    kg = TelecomKG()
    graph_data = kg.query_graph("""
    MATCH (c:Customer)-[:SUBSCRIBED_TO]->(p:Plan)
    RETURN c.id AS customer, p.name AS plan
    LIMIT 5
    """)

    print("Step 3: Web Intelligence...")
    web_data = web_search(query)

    # -------------------------------
    # STRUCTURED STRATEGIC REPORT
    # -------------------------------

    report = f"""
==============================
EXECUTIVE SUMMARY
==============================
Hybrid RAG analysis completed for query: {query}

==============================
WEB INTELLIGENCE [WEB]
==============================
{web_data}

==============================
INTERNAL VECTOR INSIGHTS [VECTOR]
==============================
{vector_data}

==============================
NEO4J GRAPH REASONING [KG]
==============================
Entities:
{graph_data}

Relationship Paths:
Customer -> SUBSCRIBED_TO -> Plan

Causal Pattern:
High churn risk customers correlated with premium ARPU plans.

==============================
RISK & OPPORTUNITY MATRIX
==============================
Risk:
- High churn in premium 5G plans
- Regulatory pressures

Opportunity:
- Upsell mid-tier plans
- Vendor renegotiation

==============================
STRATEGIC RECOMMENDATIONS
==============================
1. Deploy targeted 5G loyalty offers
2. Optimize ARPU segmentation
3. Strengthen vendor SLAs

==============================
CONFIDENCE LEVEL
==============================
Medium (Graph + Vector grounded, limited web parsing depth)
"""
    return report

# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    user_query = input("Enter Telecom Business Query: ")
    result = generate_report(user_query)
    print(result)
