import numpy as np

# Parámetros
lam = 0.4  # Tasa de llegada (lambda)
mu = 0.8  # Tasa de servicio (mu)
Tmax = 100000# Tiempo máximo de simulación



# Listas para registrar tiempos de llegada y salida
arrival_times = []
departure_times = []

# Variables auxiliares
t = 0.0  # Reloj de simulación (tiempo actual)
last_departure = 0.0  # Último tiempo en que el servidor terminó de atender

# 1) Generar llegadas mientras no superen Tmax
while t < Tmax:
    # Agregar la llegada del cliente i al sistema
    arrival_times.append(t)

    # El tiempo de servicio inicia cuando el servidor queda libre
    # o en el momento de la llegada, el que sea mayor.
    service_start = max(t, last_departure)

    # Dibujar un tiempo de servicio exponencial(1/mu)
    service_time = np.random.exponential(1 / mu)

    # Momento de salida de este cliente
    dep_time = service_start + service_time
    departure_times.append(dep_time)

    # Actualizar último tiempo de salida del servidor
    last_departure = dep_time

    # Generar el siguiente arribo y actualizar t
    next_interarrival = np.random.exponential(1 / lam)
    t += next_interarrival

# 2) Calcular el tiempo promedio de espera en el sistema
#    Solo consideraremos los clientes que llegaron antes de Tmax
#    (aunque puedan salir después de Tmax, eso es normal)
arrival_times = np.array(arrival_times)
departure_times = np.array(departure_times)

# Cantidad de clientes que realmente llegaron antes de Tmax
num_clients = len(arrival_times)

# Tiempos de permanencia en el sistema (hasta su salida)
waiting_times = departure_times - arrival_times

# Tiempo promedio de espera en el sistema
W_sim = np.mean(waiting_times)

print(f"Número de clientes simulados: {num_clients}")
print(f"Tiempo promedio de espera en el sistema (W_sim): {W_sim:.4f} (unidades de tiempo)")
