# 🌞 CLIMATIZE – Groq-Powered Multi-Agent Solar Feasibility System

## 🚀 Overview
CLIMATIZE is a **multi-agent AI system** built using **LangChain + Groq**, designed to assess the solar energy feasibility of any U.S. location.  
It orchestrates multiple specialized agents (design, permitting, and research) and generates a structured JSON report.

---

## 🧠 Agents Implemented

| Agent | Purpose | Example Output |
|--------|----------|----------------|
| **Design Agent** | Estimates system size, yearly kWh generation, and efficiency based on city-level irradiance | “7 kW system → ~9300 kWh/year” |
| **Permitting Agent** | Fetches typical permit costs and approval timelines | “$350 / 45 days average approval” |
| **Research Agent** | Pulls live renewable-energy headlines via RSS to contextualize policy or incentive risk | “Ohio manufacturing impacted by energy cuts” |

Each agent runs sequentially, feeding its output into the final summarizer powered by **Groq’s Llama 3.3 70B model**.

---

## 🧰 How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/suyog957/climatize.git
   cd climatize
