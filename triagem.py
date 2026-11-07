dados = [
	("Meu pedido chegou frio e muito atrasado", "entrega"),
	("Cobraram duas vezes no meu cartão", "pagamento"),
	("Veio faltando um item no pedido", "pedido incorreto"),
	("O entregador foi muito educado, parabéns", "elogio"),
	("Esperei mais de uma hora e ninguém avisou", "entrega"),
	("A comida estava fria", "entrega"),
	("Fui cobrado a mais e quero reembolso", "pagamento"),
	("Não veio o refrigerante que pedi", "pedido incorreto"),
	("Adorei o atendimento, obrigado!", "elogio"),
	("O aplicativo travou na hora de pagar", "outros"),
	("O entregador atrasou, mas foi muito educado", "entrega"),
	("Paguei no cartão e o pedido nunca chegou", "entrega"),
	("Recebi o pedido de outra pessoa", "pedido incorreto"),
	("Entrega rápida e comida ótima, parabéns", "elogio"),
	("Demorou muito, mas chegou tudo certo", "entrega"),
]


def classificar(texto):
	t = texto.lower()
	if "atras" in t or "frio" in t or "demor" in t:
		return "entrega"
	if "cobra" in t or "cartão" in t or "reembolso" in t:
		return "pagamento"
	if "faltando" in t or "faltou" in t or "item" in t:
		return "pedido incorreto"
	if "parabéns" in t or "adorei" in t or "obrigad" in t:
		return "elogio"
	return "outros"


acertos = 0
for texto, correta in dados:
	prevista = classificar(texto)
	ok = prevista == correta
	if ok:
		acertos += 1
	print(f"[{'OK' if ok else 'ERRO'}] previsto={prevista} | correto={correta} | {texto}")

print(f"\nAcertos: {acertos} de {len(dados)} ({acertos / len(dados):.1%})")
