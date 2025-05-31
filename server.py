from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
@mcp.tool()
def reverse_a_string(string: str) -> str:
    "enter a string you wanna reverse"
    n=len(string)
    rev=""
    for i in range(n-1,-1,-1):
        rev+=string[i]
    return f" the reverse of the string :",string ,"is ",rev


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"




