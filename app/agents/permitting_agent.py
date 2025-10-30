from langchain_core.tools import tool
import random

@tool("permitting_agent", return_direct=True)
def permitting_agent(location: str) -> str:
    """Provide solar permitting and regulation overview for the location."""
    cost = random.choice([350, 450, 500])
    days = random.choice([30, 45, 60])
    return (
        f"Permitting requirements for {location}: Permit required, "
        f"average cost ${cost}, estimated approval time {days} days."
    )
