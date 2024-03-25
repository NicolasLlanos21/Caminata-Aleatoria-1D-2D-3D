import random

# Parámetros del generador lineal congruencial
a = 1664525                         #Pendiente  = {a E Z | 1 <= a < m}
c = 1013904223                      #Intersección = {c E Z | 0 <= C < m} 
m = 2**32                           #Conjunto = {m E Z | m > 0} 
ri = []                             #Numeros Ri
ni = []                             #Numeros Ni

# FUNCIÓN PARA GENERAR RI CON CONGRUENCIA LINEAL
def generar_ri(semilla,total):   
    ri.clear()
    if semilla is None:
        semilla = random.randint(0, m - 1)  #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m} se utiliza RANDOND unicamente para generar una semilla si no se especifica una

    for _ in range(total):
        semilla = (a * semilla + c) % m
        ri.append(semilla / (m - 1))                  
        
#FUNCIÓN PARA GENERAR NI CON DISTRIBUCION UNIFORME
#Intervalo superior (maxI)
#Intervalo Inferior (minI)
def generarIntDistrUniforme(maxIntervalo,minIntervalo, total,semilla):
    global ni
    ni = []   
    generar_ri(semilla, total)
    ni += [round(minIntervalo + (maxIntervalo - minIntervalo) * N, 5) for N in ri]    
    return ni    

def generarDistrUniforme(maxIntervalo,minIntervalo,semilla,total):
    global ni
    ni = []   
    generar_ri(semilla,total)
    ni += [(minIntervalo + (maxIntervalo - minIntervalo) * N) for N in ri]    
    return ni      
