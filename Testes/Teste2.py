# Teste Bubble Sort

def bubble_sort(v):
    elementos = len(v)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if v[i] > v[i+1]:
                v[i], v[i+1] = v[i+1],v[i]
                ordenado = False        
                print(v)
    print ('\n','O resultado final é...')
    print (v)

v = [5, 3, 2, 4, 7, 1, 0, 6]
bubble_sort(v)