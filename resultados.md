# Resultados dos testes

Todos os dados são fictícios. O gabarito (a resposta certa de cada frase) foi definido por mim, e algumas frases são ambíguas.

## Acertos por método

| Método | Acertos |
|---|---|
| Script com palavras-chave (15 frases) | 10 de 15 (66,7%) |
| ChatGPT, 15 frases iniciais | 15 de 15 |
| Gemini, 15 frases iniciais | 15 de 15 |
| ChatGPT, 10 frases difíceis | 10 de 10 |
| Gemini, 10 frases difíceis (prompt v1) | 9 de 10 |
| Automação no Make (Gemini, prompt v2), 15 frases | 15 de 15 |

## O que o teste mostrou

- O script erra quando a frase mistura assuntos, por exemplo "Paguei no cartão e o pedido nunca chegou" (ele marca pagamento, o certo é entrega).
- O Gemini com o prompt v1 errou 1 das 10 frases difíceis (uma frase que não era reclamação, sobre horário de funcionamento).
- O prompt v2 acrescentou regras: texto que não é reclamação vira "outros", a IA nunca faz perguntas e sempre responde em JSON. Com ele, a automação acertou 15 de 15.

## Tempo

- À mão: 20 minutos para 20 reclamações, cerca de 1 minuto cada.
- Automação: 101 segundos para 15 reclamações, cerca de 7 segundos cada.
- Cerca de 9 vezes mais rápido no processamento. O tempo de montar o fluxo não está incluído.

## Limitações

- Poucas frases (15 e 10), então os percentuais não provam que funciona em grande escala.
- O plano gratuito do Gemini limita as chamadas (5 por minuto e 20 por dia), por isso rodei em lotes de 3 a 4 linhas.
