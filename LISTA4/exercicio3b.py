# (b) Para termos uma solução mais eficiente basta
# usar a divisão e conquista e a cada recursão pegar metade
# do número de listas (k\2) e ordená-la, fazendo a ordenação
# log(k) vezes. Assim basta resolver a fórmula de recorrência
# T((k/2)n) = T((3(k/2)n)/2) + 1 e a complexidade  é igual a 
# O(log(k)*n*log(log(k)*n)).

class Exercicio3b (object):

	def mergeSort(lista):
		if len(lista) > 1:
			meio = len(lista)/2
			p = lista[:meio]
			q = lista[meio:]
			mergeSort(p)
		 	mergeSort(q)
		 	i = 0
		    	j = 0
		    	k = 0
		    	while i < len(p) and j < len(q):
		        	if p[i] < q[j]:
		            		lista[k] = p[i]
		            		i += 1
		        	else:
		            		lista[k] = q[j]
		            		j += 1
		        		k += 1
		    	while i < len(p):
		        	lista[k] = p[i]
		        	i += 1
		       		k += 1
		    	while j < len(q):
		        	lista[k] = q[j]
		        	j += 1
		        	k += 1

	def div_conquist(k):
		p = 0
    		q = len(k) - 1
		if (q >= p):
			r = (p + q) / 2
			x1 = div_conquist_aux(k, p, r)
			x2 = div_conquist_aux(k, r + 1, q)
			mergeSort(x1 + x2)

	def div_conquist_aux(k, p, q):
		if (q >= p):
			r = (p + q) / 2
			x1 = div_conquist_aux(k, p, r)
			x2 = div_conquist_aux(k, r + 1, q)
			mergeSort(x1 + x2)

