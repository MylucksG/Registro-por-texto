# Ranking de los descubrimientos

Los 20 resultados más importantes de `openai/math`, ordenados por su impacto si se confirman. Para cada uno: cuál era el problema, qué resuelve y cuánto está comprobado.

**Cómo se hizo el ranking.** Se puntúa cada resultado por tres cosas: cuánto tiempo llevaba abierto el problema, cuánta gente fuera de su área se ve afectada, y si está comprobado con Lean (✅ todo, 🟡 una parte, ⚪ no visible). El orden es nuestra opinión, no la de OpenAI. Las descripciones salen de los resúmenes publicados en `openai/math`, no de leer los artículos completos. Ningún resultado ha pasado todavía por la revisión de otros matemáticos.

Si una palabra no te suena, mira el [glosario](../docs/glosario.md).

## Resumen

| # | Descubrimiento | Problema abierto desde | Lean |
|---|---|---|---|
| 1 | Multiplicar matrices más barato (107) | 1969 | ✅ |
| 2 | La Conjetura de Unique Games (102) | 2002 | 🟡 |
| 3 | Los primos son más ordenados de lo que se sabía (003) | 1859 | 🟡 |
| 4 | Birch–Swinnerton-Dyer en muchos casos (002) | 1965 | ⚪ |
| 5 | Subset Sum más rápido (138) | 1974 | ⚪ |
| 6 | Multiplicar enteros más rápido (109) | 1971 | ⚪ |
| 7 | Las ecuaciones de los plasmas no explotan (362) | años 80 | ✅ |
| 8 | Conjetura de Erdős sobre progresiones (159) | años 70 | ⚪ |
| 9 | Emparejamiento en tiempo casi lineal (120) | 1965 | ⚪ |
| 10 | Kakeya en 3 y 4 dimensiones (074) | 1971 | ⚪ |
| 11 | π no se aproxima demasiado bien (017) | 1953 | ⚪ |
| 12 | Factorizar polinomios sin azar (142) | años 70 | ⚪ |
| 13 | Contraejemplos a Kaplansky (197) | 1950 | 🟡 |
| 14 | Colorear el plano: cinco colores no bastan (158) | 1950 | ✅ |
| 15 | El decimosexto problema de Hilbert, parte uniforme (143) | 1900 | 🟡 |
| 16 | El grupo F de Thompson no es promediable (248) | años 60 | ✅ |
| 17 | La conjetura de Cannon (246) | 1991 | ⚪ |
| 18 | La conjetura de distancias de Falconer (073) | 1985 | ✅ |
| 19 | Los factores de grupo libre son todos iguales (287) | años 60 | ⚪ |
| 20 | Un fluido puede ser un ordenador (376) | 2000s | ⚪ |

---

## 1. Multiplicar matrices más barato (107) ✅

**El problema.** Multiplicar dos tablas de números de n filas y n columnas, de la forma obvia, cuesta n³ operaciones. En 1969 Strassen demostró que se puede hacer con menos, y desde entonces se busca el mínimo exponente posible, llamado ω. El récord humano estaba en 2,371. Se cree que el verdadero valor es 2, pero nadie ha bajado de 2,37 en cincuenta años de intentos.

**Qué resuelve.** Demuestra que ω es como máximo 2,25. Es la mayor bajada desde los años 80.

**Por qué el puesto 1.** Multiplicar matrices es la operación central de la IA, los gráficos y la simulación científica, y está comprobado al completo con Lean. Pero no hará más rápido ningún programa: estos métodos solo ganan con matrices de un tamaño que nadie usa. Su valor es saber que la operación es más barata de lo que se creía.

## 2. La Conjetura de Unique Games (102) 🟡

**El problema.** Muchos problemas de reparto y de redes no se pueden resolver de forma exacta en un tiempo razonable, así que se usan algoritmos que dan una solución "bastante buena". En 2002 Khot conjeturó que, para muchos de esos problemas, los algoritmos conocidos ya eran los mejores posibles. Era una de las preguntas abiertas más importantes de la informática teórica.

**Qué resuelve.** Demuestra la conjetura. Como consecuencia, para Max-Cut, Vertex Cover y otros problemas, ningún algoritmo rápido puede garantizar una solución mejor que las actuales.

**Por qué este puesto.** Cierra una pregunta de dos décadas y dice a los ingenieros dónde dejar de buscar. Está en Lean el artículo principal, pero no todos los de la familia.

## 3. Los primos son más ordenados de lo que se sabía (003) 🟡

**El problema.** La Hipótesis de Riemann, de 1859, dice dónde pueden estar los "ceros" de una función que controla cómo se reparten los números primos. Es el problema abierto más famoso de las matemáticas. Hasta ahora solo se sabía que no hay ceros en una franja muy estrecha del borde.

**Qué resuelve.** Amplía mucho la zona sin ceros: no hay ninguno con parte real mayor que 7/8. Sigue sin ser la hipótesis completa, que pide llegar a 1/2.

**Por qué este puesto.** Es el mayor avance en esta dirección en más de un siglo, y mejora las fórmulas que cuentan primos. El artículo principal está en Lean.

## 4. Birch–Swinnerton-Dyer en muchos casos (002) ⚪

**El problema.** Las curvas elípticas son ecuaciones que están detrás de la criptografía moderna. En 1965 dos matemáticos conjeturaron una fórmula que relaciona sus soluciones con una función analítica. Es uno de los siete Problemas del Milenio, con un millón de dólares de premio.

**Qué resuelve.** Demuestra la fórmula completa para una gran familia de curvas, y con otro resultado de la colección la extiende a "casi todas" las variantes de cualquier curva.

**Por qué este puesto.** Sería un paso enorme hacia un Problema del Milenio, pero no tiene comprobación en Lean visible. Es el resultado que más necesita revisión humana.

## 5. Subset Sum más rápido (138) ⚪

**El problema.** Dados unos números, ¿hay un grupo que sume exactamente un valor dado? Es uno de los problemas "difíciles" clásicos. En 1974 se encontró un método que tarda unos 2^(n/2) pasos, y durante cincuenta años nadie consiguió bajar ese exponente.

**Qué resuelve.** Un algoritmo que tarda 2^(0,49n). El número parece pequeño, pero es la primera mejora en medio siglo.

**Por qué este puesto.** Rompe una barrera histórica, aunque el problema sigue siendo muy lento en la práctica y no afecta a la criptografía.

## 6. Multiplicar enteros más rápido (109) ⚪

**El problema.** Multiplicar dos números de n cifras parece sencillo, pero encontrar el método más rápido es un problema abierto desde 1971. Schönhage y Strassen conjeturaron que n·log n era el mínimo posible.

**Qué resuelve.** Un método ligeramente más rápido que n·log n, lo que refuta esa conjetura.

**Por qué este puesto.** Derriba una conjetura de cincuenta años sobre una operación básica. La mejora es tan pequeña que no tiene uso práctico.

## 7. Las ecuaciones de los plasmas no explotan (362) ✅

**El problema.** Un plasma es un gas de partículas cargadas, como el del Sol o el de un reactor de fusión. Las ecuaciones que lo describen (Vlasov–Maxwell) se usan desde hace décadas, pero no se sabía si sus soluciones podían "explotar" en un tiempo finito y dejar de tener sentido.

**Qué resuelve.** Demuestra que, en tres dimensiones y con datos iniciales razonables, la solución existe y sigue siendo suave para siempre.

**Por qué este puesto.** Da base sólida a los modelos de fusión y astrofísica, y está comprobado al completo con Lean.

## 8. Conjetura de Erdős sobre progresiones (159) ⚪

**El problema.** Erdős preguntó en los años 70 si cualquier conjunto de números "suficientemente denso" (técnicamente, cuya suma de inversos diverge) contiene progresiones aritméticas de cualquier longitud, como 3, 7, 11, 15. Ofreció un premio por la respuesta. En 2020 se resolvió para progresiones de 3 términos; el caso general seguía abierto.

**Qué resuelve.** Demuestra la conjetura para progresiones de cualquier longitud.

**Por qué este puesto.** Es uno de los problemas con premio de Erdős más conocidos. Sin Lean visible.

## 9. Emparejamiento en tiempo casi lineal (120) ⚪

**El problema.** Dada una red de personas o tareas, formar el máximo número de parejas compatibles. Se resuelve desde 1965 con el algoritmo de Edmonds, pero su tiempo crece más rápido que el tamaño de la red.

**Qué resuelve.** Un algoritmo que tarda casi lo mismo que leer la red.

**Por qué este puesto.** Es el resultado con más opciones de llegar a programas reales: asignación de recursos, rutas y mercados. Sin Lean visible.

## 10. Kakeya en 3 y 4 dimensiones (074) ⚪

**El problema.** ¿Cuánto espacio necesita una aguja para girar 180 grados? En el plano, sorprendentemente poco. La conjetura de Kakeya, de 1971, dice que en cualquier dimensión el conjunto que contiene una aguja en todas las direcciones no puede ser "pequeño". En 2025 se resolvió el caso tridimensional en una de sus formas; otras seguían abiertas.

**Qué resuelve.** La versión "maximal" en tres dimensiones y la de dimensión en cuatro.

**Por qué este puesto.** Kakeya está conectado con el análisis de Fourier y con las ecuaciones de ondas. Sin Lean visible.

## 11. π no se aproxima demasiado bien (017) ⚪

**El problema.** 22/7 y 355/113 son buenas aproximaciones de π. La pregunta es cuánto de bien se puede aproximar π con fracciones. El "exponente de irracionalidad" mide eso; para casi todos los números es 2, pero para π solo se sabía que era menor que 7,1.

**Qué resuelve.** Demuestra que es exactamente 2. De paso, responde a la pregunta de si la serie de Flint Hills converge.

**Por qué este puesto.** Es una pregunta clásica sobre el número más famoso. Sin Lean visible.

## 12. Factorizar polinomios sin azar (142) ⚪

**El problema.** Descomponer un polinomio en factores es básico en el cálculo simbólico y en los códigos correctores de errores. Los métodos rápidos conocidos usan el azar; se buscaba uno que no lo necesite y sea igual de rápido.

**Qué resuelve.** Un algoritmo determinista y eficiente, sin suposiciones no demostradas.

**Por qué este puesto.** Resuelve un problema abierto de décadas en computación algebraica. No tiene nada que ver con factorizar números, que es lo que protege a RSA.

## 13. Contraejemplos a Kaplansky (197) 🟡

**El problema.** En 1950 Kaplansky planteó varias conjeturas sobre anillos de grupo, una estructura del álgebra. Durante setenta años se demostraron en muchos casos y nadie encontró un fallo.

**Qué resuelve.** Construye ejemplos concretos que las tumban, y de paso refuta otras dos conjeturas relacionadas (Gottschalk y la del determinante).

**Por qué este puesto.** Un contraejemplo cierra una pregunta para siempre. Tres de los cuatro artículos están en Lean; falta el del ejemplo sin torsión.

## 14. Colorear el plano: cinco colores no bastan (158) ✅

**El problema.** ¿Cuántos colores hacen falta para pintar todos los puntos del plano de modo que dos puntos a distancia exactamente 1 nunca tengan el mismo color? Desde 1950 se sabía que la respuesta está entre 4 y 7. En 2018 se demostró que 4 no bastan.

**Qué resuelve.** Que 5 tampoco bastan. Solo quedan 6 o 7.

**Por qué este puesto.** Es un problema que cualquiera entiende y que llevaba setenta años atascado. Comprobado al completo con Lean.

## 15. El decimosexto problema de Hilbert, parte uniforme (143) 🟡

**El problema.** En 1900 Hilbert publicó 23 problemas para el siglo XX. El decimosexto pregunta cuántas órbitas cerradas ("ciclos límite") puede tener un sistema de ecuaciones polinómicas en el plano. Se sabía que son finitas para cada sistema, pero no si hay un máximo que dependa solo del grado.

**Qué resuelve.** Demuestra que sí: hay una cota que depende solo del grado del polinomio.

**Por qué este puesto.** Es uno de los pocos problemas de Hilbert que seguían abiertos. Está en Lean uno de los dos artículos.

## 16. El grupo F de Thompson no es promediable (248) ✅

**El problema.** El grupo F de Thompson es un objeto del álgebra con propiedades raras. Desde los años 60 se discute si es "promediable", una propiedad que decide cómo se comporta en muchas situaciones. Ha habido demostraciones en los dos sentidos, todas con errores.

**Qué resuelve.** Que no lo es.

**Por qué este puesto.** Es el problema más famoso de la teoría geométrica de grupos. Comprobado con Lean, lo que importa en un problema con tantas demostraciones fallidas.

## 17. La conjetura de Cannon (246) ⚪

**El problema.** Cannon conjeturó en 1991 que ciertos grupos abstractos, cuyo "borde" se parece a una esfera, son en realidad los grupos de simetría de un espacio tridimensional curvado.

**Qué resuelve.** Demuestra la conjetura.

**Por qué este puesto.** Conecta dos áreas, grupos y geometría tridimensional, y era el gran problema pendiente tras la conjetura de Poincaré. Sin Lean visible.

## 18. La conjetura de distancias de Falconer (073) ✅

**El problema.** Si un conjunto de puntos es "suficientemente grande" (dimensión mayor que la mitad del espacio), ¿el conjunto de distancias entre sus puntos es también grande? Falconer lo conjeturó en 1985. Se sabía en casos parciales.

**Qué resuelve.** Lo demuestra en todas las dimensiones.

**Por qué este puesto.** Problema central del análisis geométrico, comprobado al completo con Lean.

## 19. Los factores de grupo libre son todos iguales (287) ⚪

**El problema.** En álgebras de operadores hay unos objetos, los factores de grupo libre, de los que no se sabía si el de dos generadores y el de tres son el mismo o distintos. La pregunta lleva abierta desde los años 60 y ha motivado toda una teoría (la probabilidad libre de Voiculescu).

**Qué resuelve.** Que son todos el mismo objeto.

**Por qué este puesto.** Es el problema más conocido de su área, pero sin Lean visible y en un campo donde los errores sutiles son frecuentes.

## 20. Un fluido puede ser un ordenador (376) ⚪

**El problema.** Las ecuaciones de Navier–Stokes describen cómo se mueven los fluidos. Se sospechaba que un fluido podía, en principio, simular cualquier cálculo, lo que tendría consecuencias sobre si sus soluciones se pueden predecir.

**Qué resuelve.** Construye flujos en tres dimensiones que, con una fuerza externa adecuada, ejecutan cualquier programa.

**Por qué este puesto.** Es llamativo, pero no es el Problema del Milenio de Navier–Stokes, que pregunta otra cosa (si las soluciones existen y son suaves). Ninguno de sus nueve artículos está en Lean.

---

## Lo que queda fuera del ranking

Hay otras 352 familias. Muchas son importantes en su área pero tienen poco efecto fuera de ella, o afectan a tan pocas personas que no entran aquí. La lista completa está en [`CONTENTS.md`](../CONTENTS.md).
