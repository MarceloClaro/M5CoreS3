"""Camada de CAG (Context-Augmented Generation) e guarda de segurança."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SafetyRule:
    rule_id: str
    description: str


def default_rules() -> List[SafetyRule]:
    return [
        SafetyRule(
            rule_id="legal_scope",
            description=(
                "O assistente não substitui aconselhamento jurídico formal."
            ),
        )
    ]


def apply_guardrails(answer: str, rules: List[SafetyRule]) -> str:
    if not rules:
        return answer
    disclaimer = "\n\n".join(rule.description for rule in rules)
    return f"{answer}\n\nAviso: {disclaimer}"
