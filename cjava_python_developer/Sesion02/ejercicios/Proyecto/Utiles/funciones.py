from clases import Estudiante

def proms(A, q):
    pred = sum(i.edad for i in A)/q
    pria = sum(i.indice for i in A)/q

    S = [pred, pria]
    return S

