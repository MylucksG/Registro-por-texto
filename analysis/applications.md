# Qué se puede aplicar y cómo

**En pocas palabras:** casi nada se puede usar mañana. Son descubrimientos teóricos. Algunos algoritmos podrían llegar a programas reales en uno o dos años, si alguien los implementa y resultan rápidos en la práctica.

Ninguno de estos resultados es un producto. Son teoremas. El camino a un uso real es leer el paper, implementar y medir. Los plazos son estimaciones mías, basadas en lo que suele tardar un teorema en llegar a una aplicación. No se leyeron los papers completos, así que el uso descrito es el típico de cada tipo de resultado.

## Resumen

| Aplicación | Familia | Plazo | Primer paso concreto |
|---|---|---|---|
| Flujo "IA propone, Lean verifica" | carpeta `lean/` | Corto | Replicar el flujo de Comparator con un resultado propio y pequeño |
| Saber dónde dejar de optimizar | 102 | Corto | Revisar qué problemas de optimización propios tienen garantía óptima |
| Emparejamiento casi lineal | 120 | 1 a 2 años | Implementarlo y compararlo con los algoritmos de asignación actuales |
| Factorizar polinomios sin azar | 142 | 1 a 2 años | Compararlo con lo que usan los programas de cálculo simbólico |
| Multiplicar matrices | 107 | Probablemente nunca en la práctica | Ninguno: es un resultado teórico, ver abajo |
| Árboles delgados deterministas | 174 | 1 a 2 años | Implementar en Python con `networkx` y comparar con heurísticas actuales |
| Decisiones online con una muestra | 111 | 1 a 2 años | Implementar la regla de umbral y simularla con datos históricos |
| Inmersiones L1 de grafos planares | 089 | 1 a 2 años | Probar la inmersión sobre una red vial y medir la distorsión |
| Cotas de primos | 003 | 5 años o más | Dejar que lo integren los especialistas en teoría de números |
| Curvas elípticas | 002 | 5 años o más | Esperar la revisión externa antes de apoyarse en el resultado |
| Plasmas y fusión | 362 | 5 años o más | Dejar que lo integren los grupos de simulación |

## 1. Flujo de verificación (corto plazo)

**Qué es.** La carpeta `lean/` del repo original es una biblioteca de pruebas formales con un catálogo (`formalization.yaml`) y retos de verificación (`ComparatorChallenges/`).

**Cómo se aplica.**
1. Leer `lean/README.md` y las instrucciones de `lean/ComparatorChallenges/README.md`.
2. Elegir un resultado propio acotado, por ejemplo una propiedad de un algoritmo.
3. Formalizarlo y comprobarlo con el mismo flujo.

**Dónde sirve.** En cualquier equipo que reciba pruebas o código crítico generado por un modelo. El valor es poder comprobarlo sin confiar en quien lo escribió.

## 2. Unique Games: dónde dejar de optimizar (corto plazo)

**Qué cambia.** Si el resultado se sostiene, los algoritmos de aproximación estándar para Max-Cut, Vertex Cover y problemas parecidos ya son los mejores posibles en el peor caso.

**Cómo se aplica.** Un equipo con un problema de este tipo puede dejar de buscar una garantía teórica mejor y dedicar el esfuerzo a heurísticas para sus instancias reales. Es una decisión de ingeniería, no código nuevo.

**Dónde sirve.** Logística, diseño de redes, diseño de chips.

## 3. Algoritmos concretos (1 a 2 años)

Los tres comparten el mismo camino:
1. Leer el algoritmo en el paper de la familia.
2. Implementarlo con datos reales de tu dominio.
3. Medirlo contra lo que se usa hoy y decidir si compensa.

- **174, árboles delgados.** Sirve para diseño de redes y aproximaciones del viajante asimétrico. La parte algorítmica (el paper de construcción en tiempo polinomial) no tiene Lean visible, solo la conjetura de existencia, así que conviene verificar el algoritmo con tests propios.
- **111, desigualdades de profeta con una muestra.** Sirve para subastas y asignación cuando se decide sin conocer el futuro.
- **089, inmersiones L1.** Sirve para aproximar distancias en mapas y redes.

El riesgo en los tres es que una cota teórica buena no siempre se traduce en mejor rendimiento práctico.

## 4. Multiplicar matrices (107): importante, pero no acelera nada

Es de los resultados más sólidos de la colección, porque está comprobado al completo con Lean. Baja el exponente de la multiplicación de matrices de 2,371 a 2,25.

Aun así, no hará más rápidas las tarjetas gráficas ni la IA. Desde el método de Strassen de 1969, que sí se usa, los récords de este tipo han sido algoritmos galácticos: solo ganan con matrices de un tamaño que nunca se usa. Su valor es teórico, porque muestra que la operación es más barata de lo que se creía.

## 5. Efecto indirecto (5 años o más)

- **003, zeta.** Cotas mejores para el conteo de primos. Lo usan matemáticos.
- **002, Birch–Swinnerton-Dyer.** Sin Lean visible, así que antes de apoyarse en él hay que esperar revisión externa.
- **362, Vlasov–Maxwell.** Da confianza de que las ecuaciones de plasmas están bien planteadas. Lo usan grupos de simulación.

## Lo que no hay que esperar

- No rompen RSA. El resultado sobre factorizar números (279) necesita un ordenador cuántico que no existe, y el de factorizar polinomios (142) es otro problema distinto.
- No resuelven P vs NP. Subset Sum (138) se resuelve más rápido, pero sigue necesitando un tiempo que crece de forma exponencial.
- No mejoran directamente los modelos de IA, ni siquiera el resultado sobre matrices (107), por lo explicado arriba.
