from controller import Robot
import random

# 1. configuración inicial
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# inicialización de motores
motor_izq = robot.getDevice('left wheel motor')
motor_der = robot.getDevice('right wheel motor')

# los motores deben estar en modo velocidad 
motor_izq.setPosition(float('inf'))
motor_der.setPosition(float('inf'))

# inicialización de Encoders (sensores de posición)
izq_sensor = robot.getDevice('left wheel sensor')
der_sensor = robot.getDevice('right wheel sensor')
izq_sensor.enable(timestep)
der_sensor.enable(timestep)



# experimentos y desafios:
# 1: línea Recta (vr = vl)
# 2: trayectoria curva (vr != vl)
# 3: círculo (vexterior > vinteriorconstante)
# 4: rotación en el lugar (vr = -vl)
EXPERIMENTO = 1

# simular perturbaciones en los actuadores (True o False)
SIMULAR_RUIDO = True
# =================================================================

# datos del robot e-puck
radio = 0.0205  # 20.5 mm en metros

print("=========================================")
print(f"--- Iniciando Experimento {EXPERIMENTO} ---")
print(f"Simulando ruido en actuadores: {SIMULAR_RUIDO}")
print("=========================================")

# 2. bucle principal de simulación
while robot.step(timestep) != -1:
    
    #a) movimiento de cada experimento

    if EXPERIMENTO == 1:
        vl_ideal = 3.0
        vr_ideal = 3.0
    elif EXPERIMENTO == 2:
        vl_ideal = 4.0
        vr_ideal = 3.5
    elif EXPERIMENTO == 3:
        vl_ideal = 4.0
        vr_ideal = 2.0 
    elif EXPERIMENTO == 4:
        vl_ideal = 3.0
        vr_ideal = -3.0
    else:
        vl_ideal = 0.0
        vr_ideal = 0.0
        
    #b) pertubacion en actuadores
    if SIMULAR_RUIDO:
        ruido_izq = random.uniform(-2.5, 2.5)
        ruido_der = random.uniform(-2.5, 2.5)
        
        vl_actual = vl_ideal + ruido_izq
        vr_actual = vr_ideal + ruido_der
    else:
        vl_actual = vl_ideal
        vr_actual = vr_ideal

    # se envían las velocidades reales (con o sin ruido) a los motores
    motor_izq.setVelocity(vl_actual)
    motor_der.setVelocity(vr_actual)
    

    # leemos la posición angular en radianes
    left_value = izq_sensor.getValue()
    right_value = der_sensor.getValue()
    
    # convertimos el giro a distancia en metros 
    izq_distance = radio * left_value
    der_distance = radio * right_value
    
    # imprimimo la información 
    print(f"Dist Izq: {izq_distance:.4f}m | Dist Der: {der_distance:.4f}m | v_izq: {vl_actual:.2f} | v_der: {vr_actual:.2f}")