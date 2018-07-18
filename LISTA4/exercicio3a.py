# (a) Considerando que o merge sort é um algoritmo que é
# no melhor, médio e pior caso O(n*log(n))
# (fonte:https://pt.wikipedia.org/wiki/Merge_sort).
# Uma possível estratégia usando algoritmo mege sort 
# em k vias de n lementos. Para descobbrir a nova
# complexidade do novo algoritmo  basta resolver a 
# fórmula de recorrência T(kn) = T(3kn/2) + 1
# é igual a O(k*n*log(k*n)).

class Exercicio3a (object):

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

#k = lista de listas
	def linear_kn (k):
		aux = k[0]
		x = 1
		for x in len(k) - 1:
			aux = aux + x
			mergeSort(aux)


