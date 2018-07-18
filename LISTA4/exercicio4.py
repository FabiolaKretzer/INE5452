class Exercicio4(object):

	i = 0

	def cartao(lista):
		p = 0
    		q = len(k) - 1
		if (q >= p):
			r = (p + q) / 2
			cartao_aux(l, p, r)
			cartao_aux(l, r + 1, q)
			
	def cartao_aux(k, p, q):
		if (q >= p):
			r = (p + q) / 2
			x1 = div_conquist_aux(k, p, r)
			x2 = div_conquist_aux(k, r + 1, q)
			equivalente(x1, x2)
	
	def equivalente(x1, x2):
		if x1 in x2:
			i++
		return
