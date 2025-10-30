from langchain_core.tools import tool
import random

@tool("design_agent", return_direct=True)
def design_agent(location: str) -> str:
    """Estimate a solar design for the given location."""
    kwh = round(random.uniform(7000, 9500), 2)
    capacity = random.choice([5.5, 6.2, 7.0, 8.0])
    efficiency = round(random.uniform(17, 21), 1)
    return (
        f"Estimated solar design for {location}: {capacity} kW system, "
        f"~{kwh} kWh/year production at {efficiency}% efficiency."
    )
