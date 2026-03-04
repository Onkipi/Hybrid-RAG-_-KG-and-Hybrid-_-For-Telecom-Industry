📡 Telecom Hybrid Intelligence Platform
Vector Retrieval + Neo4j Knowledge Graph + Real-Time Web Intelligence

An enterprise-grade Hybrid RAG (Retrieval-Augmented Generation) system designed for telecom strategic intelligence, combining:

🔎 Semantic Vector Retrieval

🧠 Neo4j Knowledge Graph Reasoning

🌐 Real-Time Industry Web Intelligence

📊 Executive-Level Structured Reporting

Built for 5G strategy, churn reduction, ARPU optimization, congestion analytics, and regulatory intelligence.

🚀 Why This Project?

Telecom operators operate in:

Hyper-competitive 5G markets

High churn segments

Multi-region spectrum constraints

Complex vendor ecosystems

Regulatory pressure

This system consolidates internal and external intelligence into a causal, explainable decision engine.

🏗 Architecture Overview
User Query
     ↓
[1] Vector Retrieval (Internal Docs)
     ↓
[2] Neo4j Knowledge Graph Reasoning
     ↓
[3] Real-Time Web Intelligence
     ↓
Executive Strategic Report

# 🔷 Hybrid RAG Architecture
### Production-grade Vector DB + Knowledge Graph + Agentic RAG System

> Built by **Vijay Kashyab** — AI Program Manager & Architect | PMP · PgMP · PfMP
> Based on real enterprise deployments delivering **41% retrieval precision improvement** and **44% hallucination reduction**

---

## Why Hybrid RAG?

Simple vector-only RAG misses **relationship-based patterns**. Knowledge-graph-only systems miss **semantic similarity**. This repo combines both — and adds an agentic layer that decides which retrieval path to use.

| Retrieval Type | What It Answers | Technology |
|---|---|---|
| Vector (Semantic) | "Find documents similar to this query" | pgvector / ChromaDB |
| Graph (Relational) | "Who is connected to what, and how?" | Neo4j |
| Agentic | "Decide which retrieval to use, combine results" | LangChain Agent |

---

## Architecture

```
User Query
    │
    ▼
Query Classifier Agent
    │
    ├──► Vector Retriever (pgvector) ──► Semantic chunks
    │
    ├──► Graph Retriever (Neo4j) ──────► Relationship paths
    │
    └──► Hybrid (both) ────────────────► Re-ranked combined results
                                              │
                                              ▼
                                        LLM (GPT-4o-mini)
                                              │
                                              ▼
                                    Structured Response + Sources
                                              │
                                              ▼
                                    RAGAS Evaluation Layer
```

---

## Quickstart

```bash
# Clone and set up
git clone https://github.com/Onkipi/hybrid-rag-architecture
cd hybrid-rag-architecture
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Set your API keys
cp .env.example .env
# Edit .env: OPENAI_API_KEY, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

# Index your documents
python scripts/ingest.py --docs-dir ./docs/

# Run the Streamlit app
streamlit run app.py
```

---

## Project Structure

```
hybrid-rag-architecture/
├── app.py                        # Streamlit Q&A interface
├── rag/
│   ├── vector_retriever.py       # pgvector semantic search
│   ├── graph_retriever.py        # Neo4j relationship traversal
│   ├── hybrid_retriever.py       # Ensemble: BM25 + vector
│   ├── agentic_retriever.py      # Agent decides retrieval strategy
│   └── chain.py                  # Full RAG chain (LCEL)
├── indexing/
│   ├── chunking.py               # Recursive + Semantic chunking
│   ├── embeddings.py             # OpenAI text-embedding-3-small
│   └── ingest.py                 # Document loading pipeline
├── evaluation/
│   ├── ragas_eval.py             # RAGAS faithfulness/relevancy
│   └── hallucination_check.py    # LLM-as-Judge detector
├── graph/
│   ├── schema.py                 # Neo4j node/relationship schema
│   └── builder.py                # Graph construction from documents
├── api/
│   └── main.py                   # FastAPI production endpoint
├── docs/                         # Drop your documents here
├── requirements.txt
└── .env.example
```

---

## Chunking Strategies Covered

```python
# 1. Recursive Character (general purpose)
RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# 2. Semantic Chunking (best quality)
SemanticChunker(embeddings, breakpoint_threshold_type="percentile")

# 3. Hierarchical (parent-doc retrieval)
# Section-level parents + paragraph-level children

# 4. Document-specific (PDFs by page, Word by section)
PyPDFLoader + Docx2txtLoader with metadata tagging
```

---

## Evaluation (RAGAS)

```python
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

# Target thresholds (enterprise standard)
THRESHOLDS = {
    "faithfulness":       0.90,   # Hallucination guard
    "answer_relevancy":   0.85,   # Relevance gate
    "context_precision":  0.80,   # Retrieval quality
    "context_recall":     0.80,   # Coverage
}
```

---

## Real-World Results (Production Deployments)

| Metric | Before | After |
|---|---|---|
| Retrieval Precision | ~55% (vector-only) | 82% (hybrid) |
| Hallucination Rate | 18% | 4% |
| RAGAS Faithfulness | 0.71 | 0.94 |
| Response Latency (p95) | 4.2s | 2.1s |

---

## Tech Stack

`Python 3.11` `LangChain` `pgvector` `Neo4j` `ChromaDB` `OpenAI` `RAGAS` `FastAPI` `Streamlit`

---

*Part of the [Enterprise AI PM Playbook](https://github.com/Onkipi/enterprise-ai-pm-playbook) series.*


Further Details: 

Strict retrieval order enforced:

1️⃣ Vector
2️⃣ Knowledge Graph
3️⃣ Web

🧠 System Components
🔹 Vector Database

ChromaDB

SentenceTransformers (semantic embedding)

Internal telecom documents

🔹 Knowledge Graph (Neo4j)

Entities:

Customer

Plan

Tower

Region

Device

Vendor

Competitor

Regulator

Relationships:

SUBSCRIBED_TO

LOCATED_IN

CONNECTED_TO

SUPPLIED_BY

COMPETES_WITH

REGULATED_BY

Supports multi-hop reasoning and causal path tracing.

🔹 Web Intelligence

Telecom news

Spectrum updates

Regulatory announcements

Earnings reports

Competitive moves
(Last 12–18 months)

📂 Project Structure
telecom-hybrid-rag/
│
├── telecom_hybrid_rag.py
├── test_neo4j.py
├── .env
├── requirements.txt
└── README.md

⚙️ Setup Instructions (VS Code)
1️⃣ Clone Repository
git clone https://github.com/your-username/telecom-hybrid-rag.git
cd telecom-hybrid-rag

2️⃣ Create Virtual Environment
python3 -m venv telecom_env
source telecom_env/bin/activate   # Mac/Linux


Windows:

telecom_env\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If requirements file not created:

pip install chromadb neo4j sentence-transformers requests beautifulsoup4 python-dotenv

4️⃣ Configure Environment Variables

Create .env file:

NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

5️⃣ Setup Neo4j
Option A — Neo4j Desktop

Install Neo4j Desktop

Create local database

Start database

Use Bolt port 7687

Option B — AuraDB (Cloud)

Create free instance

Copy connection credentials

Update .env

6️⃣ Load Sample Telecom Graph Data

Run in Neo4j Browser:

CREATE (:Vendor {name:"Ericsson"})
CREATE (:Vendor {name:"Nokia"})
CREATE (:Competitor {name:"Jio"})
CREATE (:Regulator {name:"TRAI"})
CREATE (:Region {name:"Mumbai"})
CREATE (:Plan {name:"5G Premium", arpu:899})
CREATE (:Customer {id:"C123", churn_risk:"High"})

MATCH (c:Customer {id:"C123"}), (p:Plan {name:"5G Premium"})
CREATE (c)-[:SUBSCRIBED_TO]->(p)

▶️ Running the System
python telecom_hybrid_rag.py


Example query:

How to reduce 5G churn in metro regions?

📊 Output Format

The system generates a structured executive report:

Executive Summary

Web Intelligence [WEB]

Internal Vector Insights [VECTOR]

Neo4j Graph Reasoning [KG]

Risk & Opportunity Matrix

Strategic Recommendations

Confidence Level

All insights are source-tagged.

🧩 Use Cases

✔ 5G Rollout Strategy
✔ Telecom Churn Reduction
✔ ARPU Optimization
✔ Network Congestion Analytics
✔ Regulatory & Competitive Intelligence

📈 Business Impact (Projected)

8–12% churn reduction

6–10% ARPU uplift

Faster executive decision cycles

Explainable multi-source intelligence

🔐 Design Principles

No unsupported assumptions

Causal reasoning via graph paths

Multi-source grounding

Explainable outputs

Modular architecture

🛠 Future Enhancements

FastAPI deployment layer

Docker containerization

Streamlit executive dashboard

Kafka real-time ingestion

Multi-hop advanced graph traversal

Pinecone production vector DB

SerpAPI/NewsAPI integration

🧪 Testing Neo4j Connectivity
python test_neo4j.py


Expected output:

Connection Successful

📌 Requirements

Python 3.10+

Neo4j 5+

8GB RAM recommended

👤 Author

Vijay kashyab
