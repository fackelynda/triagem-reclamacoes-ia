# Testes com o ChatGPT

Todos os dados são fictícios. Usei o prompt v1 (`prompt_v1.txt`) e enviei uma frase por mensagem. A tabela mostra só a **categoria**, que é o que contei como acerto. Urgência e resposta sugerida não entraram na conta, porque não defini um gabarito para elas.

Resultado: **15 de 15** nas frases iniciais e **10 de 10** nas frases difíceis.

## Rodada 1: 15 frases iniciais

| # | Reclamação | Categoria | Urgência |
|---|---|---|---|
| 1 | Meu pedido chegou frio e muito atrasado | entrega | 2 |
| 2 | Cobraram duas vezes no meu cartão | pagamento | 3 |
| 3 | Veio faltando um item no pedido | pedido incorreto | 1 |
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

## Rodada 2: 10 frases difíceis

| # | Reclamação | Categoria | Urgência |
|---|---|---|---|
| 16 | pedi pizza e veio hamburguer | pedido incorreto | 1 |
| 17 | cade meu pedido??? ja faz 2h | entrega | 3 |
| 18 | me cobraram taxa de entrega mas era frete gratis | pagamento | 3 |
| 19 | O app fica fechando sozinho toda hora | outros | 2 |
| 20 | Parabéns, só 3 horas de espera, muito rápido (ironia) | entrega | 2 |
| 21 | Chegou tudo certo, mas o entregador foi grosseiro | entrega | 2 |
| 22 | cobraram o pedido e cancelaram sem avisar | pagamento | 3 |
| 23 | Vem sem talher toda vez | pedido incorreto | 1 |
| 24 | Qual o horário de funcionamento do restaurante? (não é reclamação) | outros | 1 |
| 25 | Entregaram no endereço errado | entrega | 2 |

## Observações

- Na frase 24, o ChatGPT acertou a categoria ("outros"), mas respondeu com uma pergunta ("Você poderia informar o nome do restaurante?"). O prompt v2 passou a proibir perguntas por causa disso e do erro do Gemini.
- A frase 20 é irônica. O ChatGPT entendeu que era uma reclamação de atraso.
- A urgência variou entre os modelos (veja `testes-gemini.md`), o que mostra que ela é mais subjetiva que a categoria.
