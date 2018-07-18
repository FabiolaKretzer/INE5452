class Exercicio1 (object):

    a = {3, 4, 2, 3}
    p = 0
    q = len(a)
    c = {1}

    def elemento_duplicado(a, p, q):
        if (q >= p):
            r = (p + q) / 2
            elemento_duplicado(a, p, r)
            elemento_duplicado(a, r + 1, q)
            duplicado(a, p, q, r)

    def duplicado(a, p, q, r):
      for a in range(r):
        c[r] = a[r]

    def retorno(c):
        for c in range(len(c)):
            print(i)
