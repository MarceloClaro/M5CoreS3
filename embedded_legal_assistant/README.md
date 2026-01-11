# Embedded Legal Assistant (RAG + CAG)

Assistente jurídico embarcado com suporte a **RAG** (Retrieval-Augmented Generation)
 e **CAG** (Context-Augmented Generation). Este esqueleto define a arquitetura
 mínima para ingestão de documentos, recuperação de contexto e geração de
 respostas com controle de segurança.

## Objetivos
- Operar em dispositivo embarcado com memória limitada.
- Oferecer respostas com base em documentos legais locais.
- Registrar fontes e contexto utilizados.

## Estrutura
- `main.py`: ponto de entrada do assistente.
- `rag.py`: recuperação de contexto e pipeline de busca.
- `cag.py`: regras de contexto e guarda de segurança.
- `config.py`: parâmetros de execução.

## Próximos passos
- Conectar o modelo LLM local.
- Integrar armazenamento vetorial leve.
- Adicionar ingestão de documentos e atualização incremental.

## Projeto M5F2
- `assistant.m5f2`: layout e blocos do projeto CoreS3 no formato M5F2.
