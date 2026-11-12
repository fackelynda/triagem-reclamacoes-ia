# Testes com o Gemini

Todos os dados são fictícios. Usei o prompt v1 (`prompt_v1.txt`) e enviei uma frase por mensagem. A tabela mostra só a **categoria**, que é o que contei como acerto. Urgência e resposta sugerida não entraram na conta.

Resultado com o prompt v1: **15 de 15** nas frases iniciais e **9 de 10** nas frases difíceis.

## Rodada 1: 15 frases iniciais (prompt v1)

| # | Reclamação | Categoria | Urgência |
|---|---|---|---|
| 1 | Meu pedido chegou frio e muito atrasado | entrega | 2 |
| 2 | Cobraram duas vezes no meu cartão | pagamento | 3 |
| 3 | Veio faltando um item no pedido | pedido incorreto | 2 |
| 4 | O entregador foi muito educado, parabéns | elogio | 1 |
| 5 | Esperei mais de uma hora e ninguém avisou | entrega | 2 |
| 6 | A comida estava fria | entrega | 2 |
| 7 | Fui cobrado a mais e quero reembolso | pagamento | 3 |
| 8 | Não veio o refrigerante que pedi | pedido incorreto | 1 |
| 9 | Adorei o atendimento, obrigado! | elogio | 1 |
| 10 | O aplicativo travou na hora de pagar | outros | 2 |
| 11 | O entregador atrasou, mas foi muito educado | entrega | 2 |
| 12 | Paguei no cartão e o pedido nunca chegou | entrega | 3 |
| 13 | Recebi o pedido de outra pessoa | pedido incorreto | 2 |
| 14 | Entrega rápida e comida ótima, parabéns | elogio | 1 |
| 15 | Demorou muito, mas chegou tudo certo | entrega | 2 |

## Rodada 2: 10 frases difíceis (prompt v1)

| # | Reclamação | Categoria | Urgência |
|---|---|---|---|
| 16 | pedi pizza e veio hamburguer | pedido incorreto | 2 |
| 17 | cade meu pedido??? ja faz 2h | entrega | 3 |
| 18 | me cobraram taxa de entrega mas era frete gratis | pagamento | 3 |
| 19 | O app fica fechando sozinho toda hora | outros | 2 |
| 20 | Parabéns, só 3 horas de espera, muito rápido (ironia) | entrega | 3 |
| 21 | Chegou tudo certo, mas o entregador foi grosseiro | entrega | 2 |
| 22 | cobraram o pedido e cancelaram sem avisar | pagamento | 3 |
| 23 | Vem sem talher toda vez | pedido incorreto | 1 |
| 24 | Qual o horário de funcionamento do restaurante? (não é reclamação) | **errou** | sem JSON |
| 25 | Entregaram no endereço errado | entrega | 3 |

## O erro da frase 24

Em vez de classificar, o Gemini fez uma pergunta ("Para qual restaurante você deseja saber o horário?") e respondeu com uma lista de estabelecimentos. Ele não seguiu o formato JSON, e isso quebraria a automação, porque o Make espera um JSON.

## Correção: prompt v2

Acrescentei ao prompt (`prompt_v2.txt`):

- Se o texto não for uma reclamação, classificar como "outros".
- Nunca fazer perguntas.
- Responder sempre em JSON, mesmo para dúvidas.

Com o v2, quatro mensagens que não eram reclamações (uma mensagem de configuração, "Vocês aceitam pagamento em dinheiro?", "Quanto custa a taxa de entrega?" e "Oi! Vcs fazem encomendas?") foram classificadas como "outros", sempre em JSON.

## Diferenças de urgência entre ChatGPT e Gemini

| Frase | ChatGPT | Gemini |
|---|---|---|
| Veio faltando um item no pedido | 1 | 2 |
| pedi pizza e veio hamburguer | 1 | 2 |
| Parabéns, só 3 horas de espera | 2 | 3 |
| Entregaram no endereço errado | 2 | 3 |

A categoria coincidiu em todas as frases, exceto na 24 (erro do Gemini com o v1). A urgência é mais subjetiva, e por isso não entrou no cálculo de acertos.
