# Resultados dos testes

Todos os dados são fictícios. O gabarito (a categoria certa de cada frase) foi definido por mim, e algumas frases são ambíguas. A tabela conta só a **categoria**. Urgência e resposta sugerida não entraram na conta, porque não defini um gabarito para elas.

## Acertos por método

| Método | Acertos (categoria) |
|---|---|
| Script com palavras-chave (15 frases) | 10 de 15 (66,7%) |
| ChatGPT, 15 frases iniciais | 15 de 15 |
| Gemini, 15 frases iniciais | 15 de 15 |
| ChatGPT, 10 frases difíceis | 10 de 10 |
| Gemini, 10 frases difíceis (prompt v1) | 9 de 10 |
| Automação no Make (Gemini, prompt v2), 15 frases | 15 de 15 |

As respostas de cada frase estão em [testes-chatgpt.md](testes-chatgpt.md) e [testes-gemini.md](testes-gemini.md).

## O que os testes mostraram

- O script de palavras-chave erra quando a frase mistura assuntos. Exemplo: "Paguei no cartão e o pedido nunca chegou" (ele marca pagamento, o certo é entrega) e "Parabéns, só 3 horas de espera" (ele marca elogio, mas é ironia).
- O Gemini com o prompt v1 errou 1 das 10 frases difíceis: "Qual o horário de funcionamento do restaurante?". Ele fez uma pergunta e respondeu fora do formato JSON, o que quebraria a automação.
- O ChatGPT acertou a categoria dessa mesma frase, mas também respondeu com uma pergunta.
- O prompt v2 acrescentou regras: texto que não é reclamação vira "outros", a IA nunca faz perguntas e sempre responde em JSON. Com ele, a automação no Make acertou as 15 frases da planilha.
- A urgência variou entre ChatGPT e Gemini em algumas frases, por ser mais subjetiva.

## Tempo

Comparei o tempo de tratar as mesmas 15 reclamações da planilha.

- **À mão:** cerca de 2 minutos e 30 segundos por reclamação (cronometrado, só categoria e urgência), o que dá cerca de 37 minutos e 30 segundos para as 15.
- **Com a automação:** 101 segundos para as 15, em 3 execuções (cerca de 7 segundos por reclamação), já incluindo também o resumo e a resposta sugerida.
- Isso dá cerca de 22 vezes mais rápido no processamento. A comparação favorece o trabalho à mão, porque a automação fez mais (resumo e resposta) no tempo medido.
- O tempo de montar o fluxo no Make (vários dias de testes e correções) não está incluído.
- Com poucas reclamações, fazer à mão ainda compensa. O ganho aparece em grande volume.

## Limitações

- Poucas frases (25 nos testes de chat e 15 na planilha), então os percentuais não provam que funciona em grande escala.
- O plano gratuito do Gemini limita as chamadas (5 por minuto e 20 por dia), por isso rodei em lotes de 3 a 4 linhas.
