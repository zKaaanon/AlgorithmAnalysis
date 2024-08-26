def votos(A, B):
    out = []

    if(len(A) == 1 & len(B) == 1):
        out.append(1, A) & out.append(1, B)
        return out
    else:
        if(len(A) != 0):
            x = A[len(A)/2]
            y = len(A)
            (L,D) = (A[:y] ,A[y+1:])
            
            izq = 0
            der = 0
            repetidos = 0
            cambiadorIzq = 0
            cambiadorDer = 0

            while izq < len(L):
                if(L[izq] == x):
                    L[cambiadorIzq] = L[izq]
                    cambiadorIzq+1
                    repetidos+1
                    izq+1
                else:
                    izq+1

            while der < len(D):
                if(D[der] == x):
                    D[cambiadorDer] = D[der]
                    cambiadorDer+1
                    repetidos+1
                    der+1
                else:
                    der+1

            L = L[:cambiadorIzq-1]
            D = D[:cambiadorDer-1]

            out.append(x, repetidos)

        else: 
            
            return []
        
        if(len(B) != 0):
            x = B[len(B)/2]
            y = len(B)
            (L,D) = (B[:y] ,B[y+1:])
            
            izq = 0
            der = 0
            repetidos = 0
            cambiadorIzq = 0
            cambiadorDer = 0

            while izq < len(L):
                if(L[izq] == x):
                    L[cambiadorIzq] = L[izq]
                    cambiadorIzq+1
                    repetidos+1
                    izq+1
                else:
                    izq+1

            while der < len(D):
                if(D[der] == x):
                    D[cambiadorDer] = D[der]
                    cambiadorDer+1
                    repetidos+1
                    der+1
                else:
                    der+1

            L = L[:cambiadorIzq-1]
            D = D[:cambiadorDer-1]

            out.append(x, repetidos)

        else: 
            
            return []

        return votos(L,D)
    

    print(votos(["perro", "gato", "perro", "zorro", "tlacuache"], []))
    
    


