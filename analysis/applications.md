# Qué se puede aplicar y cómo

Ninguno de estos resultados es un producto. Son teoremas. El camino a un uso real es leer el paper, implementar y medir. Los plazos son estimaciones mías, basadas en lo que suele tardar un teorema en llegar a una aplicación. No se leyeron los papers completos, así que el uso descrito es el típico de cada tipo de resultado.

## Resumen

| Aplicación | Familia | Plazo | Primer paso concreto |
|---|---|---|---|
| Flujo "IA propone, Lean verifica" | carpeta `lean/` | Corto | Replicar el flujo de Comparator con un resultado propio y pequeño |
| Saber dónde dejar de optimizar | 102 | Corto | Revisar qué problemas de optimización propios tienen garantía óptima |
| Árboles delgados deterministas | 174 | 1 a 2 años | Implementar en Python con `networkx` y comparar con heurísticas actuales |
| Decisiones online con una muestra | 111 | 1 a 2 años | Implementar la regla de umbral y simularla con datos históricos |
| Embeddings L1 de grafos planares | 089 | 1 a 2 años | Probar el embedding sobre una red vial y medir la distorsión |
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
- **111, prophet inequalities con una muestra.** Sirve para subastas y asignación cuando se decide sin conocer el futuro.
- **089, embeddings L1.** Sirve para aproximar distancias en mapas y redes.

El riesgo en los tres es que una cota teórica buena no siempre se traduce en mejor rendimiento práctico.

## 4. Efecto indirecto (5 años o más)

- **003, zeta.** Cotas mejores para el conteo de primos. Lo usan matemáticos.
- **002, Birch–Swinnerton-Dyer.** Sin Lean visible, así que antes de apoyarse en él hay que esperar revisión externa.
- **362, Vlasov–Maxwell.** Da confianza de que las ecuaciones de plasmas están bien planteadas. Lo usan grupos de simulación.

## Lo que no hay que esperar

Estos resultados no rompen RSA, no resuelven P vs NP y no aportan nada directo a la mejora de modelos de lenguaje.
