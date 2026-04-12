# Laboratorio Robotica

## Descripcion del laboratorio
Este laboratorio implementa un controlador en Webots para un robot diferencial tipo e-puck, con el objetivo de comparar trayectorias ideales y trayectorias perturbadas por ruido en actuadores.

El archivo [main.py](main.py) define:

- Un conjunto de 4 experimentos cinemativos, seleccionados con la variable EXPERIMENTO.
- Un modo con o sin perturbacion de actuadores, controlado por la variable SIMULAR_RUIDO.
- El uso de encoders de rueda para estimar distancia lineal por rueda con la relacion:

  distancia = radio * angulo

Los escenarios evaluados son:

1. Recta: v_izq = v_der.
2. Curva suave: v_izq > v_der.
3. Curva cerrada: v_izq >> v_der.
4. Giro en el lugar: v_izq = -v_der.

## Como ejecutar la simulacion en Webots
1. Abrir el proyecto en Webots y verificar que el robot e-puck use este controlador Python.
2. Confirmar que existen los dispositivos con estos nombres:
   left wheel motor, right wheel motor, left wheel sensor, right wheel sensor.
3. Editar [main.py](main.py) y configurar:
   EXPERIMENTO = 1, 2, 3 o 4.
   SIMULAR_RUIDO = False o True.
4. Ejecutar la simulacion y revisar la consola del controlador.
5. Repetir para cada experimento, primero sin ruido y luego con ruido.

## Resultados obtenidos
### Sin ruido en actuadores

| Experimento | Velocidades (v_izq, v_der) | Comportamiento observado |
|---|---|---|
| 1 | (3.0, 3.0) | Avance rectilineo, simetrico |
| 2 | (4.0, 3.5) |  Curva suave (rueda izq recorre mas) |
| 3 | (4.0, 2.0) |  Curva cerrada (trayectoria circular) |
| 4 | (3.0, -3.0) |  Rotacion sobre su eje |

### Con ruido en actuadores

| Experimento | Condicion | Observacion |
|---|---|---|
| 1 | Ruido uniforme en [-2.5, 2.5] rad/s | Trayectoria cercana a recta, con dispersion |
| 2 | Ruido uniforme en [-2.5, 2.5] rad/s |  Curva con mayor variabilidad y avance acumulado |
| 3 | Ruido uniforme en [-2.5, 2.5] rad/s | Curvatura inestable, diferencias grandes entre ruedas |
| 4 | Ruido uniforme en [-2.5, 2.5] rad/s | Giro en el lugar con perturbaciones |

*Ultimo dato completo visible en la salida compartida.

Interpretacion general:

- Sin ruido, los resultados coinciden con el modelo de traccion diferencial esperado.
- Con ruido, aumenta la dispersion de velocidades y se altera la forma de la trayectoria.
- Se observaron advertencias de saturacion de velocidad (maxVelocity = 6.28 rad/s), especialmente en experimentos 2 y 3 con ruido.

Esto confirma que las perturbaciones de actuador impactan de forma directa la repetibilidad del movimiento y justifican el uso de limites, filtrado o control en lazo cerrado para mejorar robustez.

## Preguntas de analisis
1. Que ocurre cuando ambas ruedas tienen la misma velocidad?
2. Como cambia la trayectoria cuando las velocidades son diferentes?
3. Que ocurre cuando una rueda gira en sentido opuesto a la otra?
4. Que tipo de movimiento permite dibujar un circulo?

## Respuestas 
1. Cuando ambas ruedas tienen la misma velocidad, el robot avanza en linea recta. Con ruido, el comportamiento medio se conserva, pero aparecen pequenas desviaciones por diferencias instantaneas entre ruedas.
2. Cuando las velocidades son diferentes, la trayectoria se vuelve curva. Si la diferencia es constante, la curvatura es aproximadamente constante; si la diferencia varia por ruido, la curvatura cambia y la trayectoria presenta desviaciones.
3. Cuando una rueda gira en sentido opuesto a la otra, el robot rota. Si los modulos son similares, gira sobre su propio eje, si no, combina giro con un leve desplazamiento.
4. Un movimiento circular se obtiene cuando ambas ruedas giran en el mismo sentido con velocidades constantes y distintas; la rueda mas rapida queda en el radio exterior de la curva.