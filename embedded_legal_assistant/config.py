"""Configurações do assistente jurídico embarcado."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AssistantConfig:
    device_name: str = "M5CoreS3"
    language: str = "pt-BR"
    max_context_items: int = 5
    max_answer_tokens: int = 256
    enable_cag_guardrails: bool = True
