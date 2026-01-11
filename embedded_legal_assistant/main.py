"""Ponto de entrada do assistente jurídico embarcado."""

from config import AssistantConfig
from rag import build_prompt, retrieve_context
from cag import apply_guardrails, default_rules


def generate_answer(prompt: str) -> str:
    """Simula a geração de resposta do LLM."""
    return (
        "Resposta simulada baseada no contexto fornecido. "
        "Substitua por integração real com o LLM."
    )


def run_assistant(query: str) -> str:
    config = AssistantConfig()
    context = retrieve_context(query, config.max_context_items)
    prompt = build_prompt(query, context)
    answer = generate_answer(prompt)
    if config.enable_cag_guardrails:
        answer = apply_guardrails(answer, default_rules())
    return answer


def main() -> None:
    query = "Quais são os requisitos para um contrato válido?"
    answer = run_assistant(query)
    print(answer)


if __name__ == "__main__":
    main()
