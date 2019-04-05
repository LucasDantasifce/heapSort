from random import randint, shuffle
import matplotlib as mpl
import timeit


Dlista = [10000, 20000, 30000, 40000, 50000]


def geraLista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,tam))
    shuffle(lista)

    return lista


def heapsort(aList):
    # convert aList to heap
    length = len(aList) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        moveDown(aList, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if aList[0] > aList[i]:
            swap(aList, 0, i)
            moveDown(aList, 0, i - 1)


def moveDown(aList, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap(aList, largest, first)
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return  # force exit


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp



mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Pior Tempo")
    ax.plot(x,ym, label = "Melhor Tempo")
    ax.plot(x,yp, label = "Medio Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('Graficoheapsort.png')

MelhorCaso = []
PiorCaso = []
MedioCaso = []

for i in Dlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(melhor, reverse=True)

    MelhorCaso.append(timeit.timeit("aux={}\naux = heapsort(aux)".format(melhor.copy()),setup="from __main__ import heapsort",number=1))
    PiorCaso.append(timeit.timeit("aux={}\naux = heapsort(aux)".format(pior.copy()),setup="from __main__ import heapsort",number=1))
    MedioCaso.append(timeit.timeit("aux={}\naux = heapsort(aux)".format(medio.copy()),setup="from __main__ import heapsort",number=1))
    print("Ordenado um i em Dlista!")


desenhaGrafico(Dlista,MedioCaso,MelhorCaso,PiorCaso)

import itertools as it
tamlista = list(it.permutations(list(range(6))))
tempoIteracao = []
listaOrig = []
for lista in tamlista:
    tempoIteracao.append(timeit.timeit("heapsort({})".format(list(lista).copy()),setup="from __main__ import heapsort",number=1))
    listaOrig.append(list(lista))

print("O tempo minimo foi de {}".format(min(tempoIteracao)))
print("lista que teve tempo minimo foi:{}".format(listaOrig[tempoIteracao.index(min(tempoIteracao))]))
print("O tempo maximo foi de {}".format(max(tempoIteracao)))
print("lista que teve tempo maximo foi:{}".format(listaOrig[tempoIteracao.index(max(tempoIteracao))]))


