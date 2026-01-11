"""Pipeline de RAG (Retrieval-Augmented Generation)."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class RetrievedChunk:
    source_id: str
    content: str
    score: float


def retrieve_context(query: str, max_items: int) -> List[RetrievedChunk]:
    """Retorna trechos de contexto relevantes para a consulta."""
    if not query:
        return []
    return [
        RetrievedChunk(
            source_id="jurisprudencia/exemplo_001",
            content="Trecho de exemplo para consulta jurídica.",
            score=0.42,
        )
    ][:max_items]


def build_prompt(query: str, context: List[RetrievedChunk]) -> str:
    """Combina a consulta com o contexto recuperado."""
    context_block = "\n\n".join(
        f"[{item.source_id}] {item.content}" for item in context
    )
    return (
        "Você é um assistente jurídico embarcado. "
        "Responda apenas com base nas fontes fornecidas.\n\n"
        f"Contexto:\n{context_block}\n\n"
        f"Pergunta: {query}\n"
        "Resposta:"
    )
