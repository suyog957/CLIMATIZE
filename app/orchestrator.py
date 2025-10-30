"""
CLIMATIZE – Groq-Powered Multi-Agent Solar Feasibility System
--------------------------------------------------------------
Sequentially runs all LangChain Tools (Agents), displays intermediate outputs,
and generates a final feasibility summary using Groq LLM.
"""

import os

from dotenv import load_dotenv
load_dotenv()

import pkgutil
import importlib
import inspect
from langchain_core.tools import BaseTool
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


def load_all_agent_tools():
    """Dynamically import all @tool-decorated functions from app/agents."""
    tools = []
    package = "app.agents"
    package_path = os.path.join(os.getcwd(), "app", "agents")

    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        mod = importlib.import_module(f"{package}.{module_name}")
        for name, obj in inspect.getmembers(mod):
            if isinstance(obj, BaseTool):
                tools.append(obj)
    print(f"✅ Loaded {len(tools)} tools: {[t.name for t in tools]}")
    return tools


def main():
    print("\n🌞 CLIMATIZE – Groq-Powered Multi-Agent Solar Feasibility System\n")

    agent_folder = os.path.join(os.getcwd(), "app", "agents")
    print(f"📂 Agent folder path: {agent_folder}")

    location = input("Enter site address (e.g., 'Buffalo, NY'): ").strip()

    # Load all dynamically discovered tools
    tools = load_all_agent_tools()

    # Groq LLM setup
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

    # Prepare to collect outputs
    all_outputs = {}

    print("\n🧠 Running agents sequentially...\n")

    for tool in tools:
        try:
            if "research" in tool.name.lower():
                print(f"🔍 Running {tool.name}...")
            elif "design" in tool.name.lower():
                print(f"⚙️ Running {tool.name}...")
            elif "permit" in tool.name.lower():
                print(f"🏛️ Running {tool.name}...")
            else:
                print(f"🤖 Running {tool.name}...")

            result = tool.run(location)
            print(f"✅ Output from {tool.name}:\n{result}\n")
            all_outputs[tool.name] = result

        except Exception as e:
            print(f"❌ Error in {tool.name}: {str(e)}\n")
            all_outputs[tool.name] = f"Error: {str(e)}"

    # Combine results for summary
    context = "\n\n".join([f"{k}: {v}" for k, v in all_outputs.items()])

    # Prompt template for final Groq summary
    prompt = ChatPromptTemplate.from_template("""
You are a solar feasibility expert. Based on the following agent outputs, generate a structured JSON report.

Context:
{context}

Your JSON output should contain:
- address
- summary
- verdict (Go / Moderate / Feasible with caution / Not recommended)
- recommendations (list of actionable items)
""")

    print("🧠 Generating final feasibility summary using Groq...\n")

    chain = prompt | llm
    response = chain.invoke({"context": context})
    print("📊 Final Report:\n")
    print(response.content)


if __name__ == "__main__":
    main()
