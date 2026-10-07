# Panorama

## En pocas palabras

- La colección tiene 372 familias de resultados matemáticos producidos por un modelo de IA de OpenAI.
- Una de cada tres tiene al menos una parte comprobada por máquina con Lean. Las otras dos dependen de que algún experto las revise.
- Hay resultados llamativos en algoritmos y en teoría de números, pero nada que cambie la tecnología que usas hoy.

Si alguna palabra no te suena, mira el [glosario](../docs/glosario.md).

## Los resultados más llamativos, en palabras sencillas

Para ver cuál era el problema y qué resuelve cada uno, mira el [ranking](ranking.md).

Elegidos por su posible impacto, dentro o fuera de las matemáticas. "Lean" indica si está comprobado por máquina (✅ todo, 🟡 una parte, ⚪ no visible).

### Algoritmos e informática

| ID | Qué afirma, en sencillo | Por qué importa | Lean |
|---|---|---|---|
| 107 | Multiplicar matrices grandes cuesta menos pasos de lo que se sabía: el exponente baja de 2,371 a 2,25 | Multiplicar matrices es la operación básica de la IA, los gráficos y las simulaciones. Pero estos métodos suelen ser [galácticos](../docs/glosario.md): no aceleran tu ordenador | ✅ completo |
| 102 | Para ciertos problemas de reparto y de cortar redes, ningún algoritmo rápido puede garantizar una solución mejor que las actuales (la Conjetura de Unique Games) | Dice a los ingenieros dónde dejar de buscar mejores garantías | 🟡 parcial, incluye el paper principal |
| 138 | Decidir si unos números contienen un grupo que suma un valor exacto (Subset Sum) se puede hacer más rápido que el récord de 1974 | Rompe una barrera de 50 años, aunque sigue siendo un problema lento | ⚪ no visible |
| 120 | Formar el máximo número de parejas en una red cualquiera (emparejamiento) en un tiempo casi proporcional a su tamaño | Asignar tareas, rutas o recursos más rápido, en teoría | ⚪ no visible |
| 142 | Descomponer polinomios en factores sin usar azar, de forma eficiente | Era un problema abierto en cálculo simbólico. No es la factorización de números que protege a RSA | ⚪ no visible |
| 279 | Una versión del algoritmo cuántico de Shor que factoriza números con probabilidad 1 | Necesita un ordenador cuántico grande, que no existe. No cambia la seguridad de hoy | ⚪ no visible |

### Matemáticas puras

| ID | Qué afirma, en sencillo | Por qué importa | Lean |
|---|---|---|---|
| 003 | Los números primos están repartidos de forma más ordenada de lo que se podía demostrar. Es un paso hacia la Hipótesis de Riemann, no la hipótesis completa | Mejora las fórmulas que cuentan primos | 🟡 parcial, incluye el paper principal |
| 002 | Una fórmula famosa sobre curvas elípticas (Birch–Swinnerton-Dyer) es cierta en una gran parte de los casos | Es uno de los siete Problemas del Milenio, aquí en casos concretos | ⚪ no visible |
| 017 | π no se deja aproximar "demasiado bien" por fracciones | Responde una pregunta clásica sobre π | ⚪ no visible |
| 197 | Ejemplos concretos que tumban conjeturas de álgebra de los años 50 (Kaplansky y otras) | Cierra preguntas de décadas | 🟡 parcial; falta el ejemplo sin torsión |
| 087 | Qué formas geométricas minimizan cierta medida de volumen (conjeturas de Mahler) | Problema clásico de geometría | 🟡 parcial; está la versión simétrica, no la general |
| 287 | Ciertos objetos del álgebra de operadores que parecían distintos son en realidad el mismo | Problema abierto desde hace décadas | ⚪ no visible |

### Física y aplicaciones lejanas

| ID | Qué afirma, en sencillo | Por qué importa | Lean |
|---|---|---|---|
| 362 | Las ecuaciones que describen un plasma (gas cargado, como en la fusión nuclear) no "explotan": su solución sigue siendo suave para siempre | Da confianza en los modelos de plasmas | ✅ completo |
| 089 | Las distancias de un mapa plano se pueden representar de forma más simple sin deformarlas demasiado | Útil para algoritmos de redes y rutas | ✅ completo |
| 174 | Toda red bien conectada tiene un "esqueleto" que usa pocas conexiones de cada zona | Diseño de redes. La parte del algoritmo no está en Lean | 🟡 parcial |

## Cuánto está comprobado por máquina, por área

Cuántas familias tienen al menos un manuscrito comprobado con Lean. Ordenado de más a menos.

| Área | Familias | Con Lean | % |
|---|---:|---:|---:|
| Lógica matemática | 6 | 5 | 83% |
| Análisis funcional | 11 | 8 | 73% |
| Geometría convexa y métrica | 15 | 10 | 67% |
| Informática teórica | 40 | 20 | 50% |
| Teoría de grupos | 14 | 7 | 50% |
| Combinatoria | 37 | 17 | 46% |
| Álgebra | 18 | 7 | 39% |
| Análisis real y complejo | 16 | 6 | 38% |
| Álgebras de operadores | 19 | 6 | 32% |
| Geometría diferencial | 29 | 9 | 31% |
| Probabilidad y mecánica estadística | 29 | 8 | 28% |
| Física matemática | 25 | 6 | 24% |
| Teoría de números | 31 | 6 | 19% |
| Ecuaciones en derivadas parciales | 16 | 3 | 19% |
| Sistemas dinámicos y teoría ergódica | 12 | 2 | 17% |
| Geometría algebraica y compleja | 36 | 6 | 17% |
| Topología | 18 | 1 | 6% |
| **Total** | **372** | **127** | **34%** |

De esas 127 familias, 74 están comprobadas por completo y 53 en parte. El detalle está en [`CONTENTS.md`](../CONTENTS.md).

**Qué dice la tabla.** Lean ya tiene mucha matemática escrita en áreas como lógica, geometría o informática, y ahí es más fácil comprobar resultados nuevos. En topología, geometría algebraica o teoría de números falta esa base, así que esos resultados dependen más de la revisión humana.

## Lo que la colección no contiene

- Nada que rompa RSA ni la criptografía actual. El único resultado sobre factorizar números (279) necesita un ordenador cuántico que no existe.
- No resuelve P vs NP, ni la Hipótesis de Riemann completa, ni el problema del Milenio de Navier–Stokes. La familia 376 trata de Navier–Stokes, pero sobre otra pregunta: que un fluido puede simular un ordenador.
- No resuelve la conjetura de Hodge en general, solo casos particulares (familia 032).
- No explica cómo se entrenó o se mejora el modelo.
