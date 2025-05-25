from mcp.server.fastmcp import FastMCP

# Create an MCP servrer
mcp=FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a specified location.
    
    Args:
        location (str): The name of the location to get the weather for.
        
    Returns:
        str: A string describing the current weather in the specified location.
    """
    # Simulate a weather response
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource"""
    return f"Weather data for {location}: Sunny, 25°C"

@mcp.prompt()
def weather_report(location: str) -> str:
    """ create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""

# Run the Server
if __name__ == "__main__":
    mcp.run()
