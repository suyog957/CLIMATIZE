# ☀️ CLIMATIZE – Groq-Powered Multi-Agent Solar Feasibility System

## 🧠 Overview
CLIMATIZE is a LangChain + Groq powered multi-agent system that evaluates the solar energy feasibility of any U.S. location.  
It uses three coordinated agents:
- **Research Agent** – Fetches real-time solar policy and renewable news headlines.
- **Design Agent** – Estimates solar capacity, energy output, and system efficiency.
- **Permitting Agent** – Simulates local permit requirements, costs, and approval times.

---

## 🐋 Run via Docker

### 1️⃣ Build the Docker image
```bash
docker build -t climatize .
