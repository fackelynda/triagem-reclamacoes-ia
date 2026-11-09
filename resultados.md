## Resumo
| Método | Acertos |
| --- | --- |
| Script com palavras-chave (15 frases) | 10 de 15 (66,7%) |
| ChatGPT, 15 frases iniciais | 15 de 15 |
| Gemini, 15 frases iniciais | 15 de 15 |
| ChatGPT, 10 frases difíceis | 10 de 10 |
| Gemini, 10 frases difíceis | 9 de 10 (90%) |

## Onde a IA errou
- Frase: "Qual o horário de funcionamento do restaurante?"
- O que o Gemini respondeu: pediu o nome do restaurante, em texto livre, sem JSON.
- Causa: o prompt não dizia o que fazer com mensagens que não são reclamação.
- O que mudei no prompt: acrescentei regras para dúvidas e proibi perguntas (prompt_v2).