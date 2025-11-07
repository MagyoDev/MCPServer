# server.py
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo-wxo-mcp")

@mcp.tool()
def soma(a: int, b: int) -> int:
    """Soma dois números"""
    return a + b

@mcp.tool()
def saudacao(nome: str) -> str:
    """Saúda um usuário pelo nome"""
    return f"Olá, {nome}!"

if __name__ == "__main__":
    mcp.run()