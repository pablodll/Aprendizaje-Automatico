import time
import numpy as np
import matplotlib.pyplot as plt

def valor_maximo(fun, a, b):
    """Busca el valor maximo de una funcion en cierto intervalo"""
    m = 0
    for i in np.arange(a,b+1):
        if(fun(i) > fun(m)):
            m = i
    return fun(m)

def valor_minimo(fun, a, b):
    """Busca el valor minimo de una funcion en cierto intervalo"""
    m = 0
    for i in np.arange(a,b+1):
        if(fun(i) < fun(m)):
            m = i
    return fun(m)

def f(x):
    return (-(x**2)+(10*x))

def integra_mc_bucle(fun, a, b, num_puntos=10000):
    """Calcula la integral definida de una funcion mediante 
    el metodo MonteCarlo haciendo uso de un bucle"""
    Nunder = 0
    M = valor_maximo(fun, a, b)
    m = valor_minimo(fun, a, b)

    for i in range(num_puntos):
        x = np.random.uniform(a,b)
        y = np.random.uniform(m,M)
        if y < fun(x):
            Nunder += 1

    I = ((Nunder / num_puntos) * (b-a) * M)
    return I

def integra_mc_vector(fun, a, b, num_puntos=10000):
    """Calcula la integral definida de una funcion mediante 
    el metodo MonteCarlo haciendo uso de operaciones con vectores"""
    Nunder = 0
    M = valor_maximo(fun, a, b)
    m = valor_minimo(fun, a, b)
    
    x = np.random.uniform(a,b,num_puntos)
    y = np.random.uniform(m,M,num_puntos)
    Nunder= np.count_nonzero((y < fun(x)))

    
    I = ((Nunder / num_puntos) * (b-a) * M)
    return I

def compara_tiempos(f,a,b):
    """Genera grafica de tiempos """
    sizes = np.linspace(100, 10000000, 20)
    times_bucle = []
    times_vector = []
    for size in sizes:
        tic = time.process_time()
        integra_mc_bucle(f, a, b, int(size))
        toc = time.process_time()
        times_bucle += [1000*(toc-tic)]
        
        tic = time.process_time()
        integra_mc_vector(f, a, b, int(size))
        toc = time.process_time()
        times_vector += [1000*(toc-tic)]

    plt.figure()
    plt.xlabel('Nº de puntos')
    plt.ylabel('Tiempo (ms)')
    plt.scatter(sizes, times_bucle, c='red', label='bucle')
    plt.scatter(sizes, times_vector, c='blue', label='vector')
    plt.legend()
    plt.savefig('graph2.png')
    plt.show()
