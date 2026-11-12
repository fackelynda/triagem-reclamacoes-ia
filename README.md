# Triagem de reclamações com IA

**Em uma frase:** uma automação que lê reclamações de clientes de um app de delivery fictício, classifica cada uma, define a urgência, escreve um resumo e sugere uma resposta educada, gravando tudo numa planilha.

Projeto de portfólio de Jaqueline, estudante de Análise e Desenvolvimento de Sistemas. Todos os dados são fictícios.

## O problema
Equipes de atendimento recebem muitas reclamações e precisam separar, priorizar e responder cada uma. Fazer isso à mão é lento e varia de pessoa para pessoa.

## Exemplo
| Entrada | Saída |
| --- | --- |
| "Meu pedido chegou frio e muito atrasado" | **Categoria:** entrega. **Urgência:** 2. **Resumo:** pedido entregue com atraso e comida fria. **Resposta sugerida:** "Lamentamos pelo atraso e por sua refeição ter chegado fria. Estamos repassando o ocorrido para a nossa equipe melhorar as próximas entregas." |

![Planilha preenchida](planilha-preenchida.png)

## Como funciona
1. As reclamações ficam numa planilha do Google Sheets.
2. O Make (ferramenta de automação) lê cada linha e a envia ao Gemini, junto com as instruções de [prompt_v2.txt](prompt_v2.txt).
3. O Gemini responde em JSON, com categoria, urgência, resumo e resposta sugerida.
4. O Make grava o resultado na mesma linha da planilha.

![Cenário no Make](cenario-make.png)

## Arquivos
- `triagem.py`: versão inicial em Python, que classifica por palavras-chave. Serve como ponto de comparação.
- `prompt_v1.txt` e `prompt_v2.txt`: as instruções dadas à IA, antes e depois da melhoria.
- `resultados.md`: os testes feitos, com os números.

## Resultados
Testei as mesmas frases com um script simples e com a IA.

| Método | Acertos |
| --- | --- |
| Script com palavras-chave (15 frases) | 10 de 15 (66,7%) |
| ChatGPT, 15 frases iniciais | 15 de 15 |
| Gemini, 15 frases iniciais | 15 de 15 |
| ChatGPT, 10 frases difíceis | 10 de 10 |
| Gemini, 10 frases difíceis (prompt v1) | 9 de 10 |
| Automação no Make (Gemini, prompt v2), 15 frases | 15 de 15 |

O gabarito foi definido por mim, e algumas frases são ambíguas.

### Três exemplos comparados
| Tipo | Frase | Esperado | Script | IA |
| --- | --- | --- | --- | --- |
| Fácil | Cobraram duas vezes no meu cartão | pagamento | pagamento | pagamento |
| Ambígua | Paguei no cartão e o pedido nunca chegou | entrega | pagamento (errou) | entrega |
| Difícil | Parabéns, só 3 horas de espera, muito rápido | entrega | elogio (errou) | entrega |

O script erra quando a frase tem uma palavra-chave que engana ("cartão", "parabéns"). A IA entende o contexto, inclusive o sarcasmo do terceiro exemplo.

## Tempo
Com a automação, 15 reclamações foram processadas em 101 segundos, em 3 execuções (cerca de 7 segundos cada).

## Problemas que encontrei e como resolvi
| Problema | Causa | O que fiz |
| --- | --- | --- |
| Erro 403 ao conectar o Google Sheets no Make | A conexão foi criada sem todas as permissões | Refiz a conexão marcando todas as permissões |
| O Gemini respondia com conselhos em vez de classificar | O prompt grande não chegava ao módulo | Troquei para o módulo com campo de instruções do sistema e conferi a entrada da execução |
| Erro 404: modelo indisponível | O modelo deixou de estar disponível para contas novas | Troquei para um modelo mais recente |
| Erro 503 | Alta demanda no Google | Esperei e rodei de novo |
| O Gemini não classificou a pergunta "Qual o horário de funcionamento do restaurante?" | O prompt não dizia o que fazer com mensagens que não são reclamação | Criei o prompt v2: dúvidas viram "outros", sem fazer perguntas e sempre em JSON |
| O JSON apareceu inteiro em todas as colunas numa linha | O Make não separou os campos naquela resposta | Ativei o Response Format como JSON Output |
| Erro 429 (5 pedidos por minuto e 20 por dia) | Limites do plano gratuito do Gemini | Processei em lotes de 3 a 4 linhas, esperando 1 minuto entre eles |

## Tempo
- **À mão:** 20 minutos para 20 reclamações (categoria), cerca de 1 minuto por reclamação.
- **Com a automação:** 101 segundos para 15 reclamações, em 3 execuções, cerca de 7 segundos por reclamação.
- A automação foi cerca de 9 vezes mais rápida no processamento. O tempo de montar o fluxo não está incluído.
- Com poucas reclamações, fazer à mão ainda compensa. O ganho aparece em grande volume.

## O que aprendi
- Medir antes de automatizar: comparar com um script simples mostrou o que a IA realmente melhora.
- Conferir o que chega ao modelo, e não só o que eu escrevi.
- Respostas de IA podem mudar de formato, então o fluxo precisa tratar isso.
- Planos gratuitos têm limites que afetam o plano de testes.

## Uso de IA no desenvolvimento
Usei ChatGPT e Gemini como apoio para escrever e revisar o prompt e o código. Eu defini as categorias e o gabarito, rodei os testes, medi os acertos e decidi os ajustes.

## O que ainda não funciona
- Poucos dados de teste (15 a 25 frases), fictícios, com gabarito definido por mim.
- O limite do plano gratuito obriga a processar em lotes.
- Não trata reclamações em outros idiomas nem textos muito longos.
- A resposta sugerida precisa de revisão humana antes de ser enviada a um cliente.

## Próximos passos
- Limitar as categorias com um esquema de resposta (Response Schema).
- Processar só as linhas novas e com intervalo automático entre as chamadas.
- Testar com mais frases e com um segundo avaliador para o gabarito.
