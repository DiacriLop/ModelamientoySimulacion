from random import expovariate
from statistics import mean
from math import inf as Infinity

# Parámetros
lamda = 1.3
mu = 2.0
Num_Pkts = 1000000
count = 0
clock = 0
N = 0

Arr_Time = expovariate(lamda)
Dep_Time = Infinity
Prev_Event_Time = 0.0  # Tiempo del último evento
Area = 0.0  # Variable para acumular el área

while count < Num_Pkts:
    if Arr_Time < Dep_Time:
        # Evento de llegada
        clock = Arr_Time
        Area += (clock - Prev_Event_Time) * N
        Prev_Event_Time = clock
        N += 1
        Arr_Time = clock + expovariate(lamda)
        if N == 1:
            Dep_Time = clock + expovariate(mu)
    else:
        # Evento de salida
        clock = Dep_Time
        Area += (clock - Prev_Event_Time) * N
        Prev_Event_Time = clock
        N -= 1
        count += 1
        if N > 0:
            Dep_Time = clock + expovariate(mu)
        else:
            Dep_Time = Infinity

print("E[N(t)] =", round(Area / clock, 4))