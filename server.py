# server.py
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI

mcp = FastMCP("demo-wxo-mcp")

@mcp.tool()
def soma(a: int, b: int) -> int:
    """Soma dois números"""
    return a + b

# 1) Gere a app ASGI do MCP (endpoint /mcp)
mcp_app = mcp.http_app(path="/mcp")

# 2) Envolva com FastAPI repassando o lifespan do MCP
app = FastAPI(lifespan=mcp_app.lifespan)
app.mount("/", mcp_app)
