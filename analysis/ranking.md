# Ranking de los descubrimientos

Los 50 resultados más importantes de `openai/math`, ordenados por su impacto si se confirman. Los 20 primeros pueden tener efecto fuera de las matemáticas; del 21 al 50 son importantes para los matemáticos, pero con poco impacto fuera por ahora. Para cada uno: cuál era el problema, qué resuelve y cuánto está comprobado.

**Cómo se hizo el ranking.** Se puntúa cada resultado por tres cosas: cuánto tiempo llevaba abierto el problema, cuánta gente fuera de su área se ve afectada, y si está comprobado con Lean (✅ todo, 🟡 una parte, ⚪ no visible). El orden es nuestra opinión, no la de OpenAI. Las descripciones salen de los resúmenes publicados en `openai/math`, no de leer los artículos completos. Ningún resultado ha pasado todavía por la revisión de otros matemáticos.

Cada ficha tiene dos niveles: primero un recuadro **en palabras sencillas**, con un ejemplo de lo que pasaba antes y de lo que puede pasar ahora, y después la explicación más técnica. Los ejemplos son ilustrativos. Si una palabra no te suena, mira el [glosario](../docs/glosario.md).

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

> **En palabras sencillas.** Multiplicar dos tablas grandes de números es lo que hace un ordenador millones de veces por segundo cuando entrena una IA o dibuja un videojuego. Este resultado demuestra que, en teoría, se puede hacer con bastantes menos operaciones de las que se creía posibles.
>
> **Antes:** Si una tabla tenía 1.000 filas, el mejor método teórico necesitaba unas 10 millones de operaciones. Nadie había bajado de ese nivel en medio siglo.
>
> **Ahora:** Sobre el papel, bastarían unos 5 millones. Pero el método solo compensa con tablas de un tamaño que no cabe en ningún ordenador, así que tu móvil y tu tarjeta gráfica seguirán igual. Lo que cambia es que ahora los investigadores saben que la operación es más barata de lo que pensaban, y buscarán métodos que sí se puedan usar.

**El problema.** Multiplicar dos tablas de números de n filas y n columnas, de la forma obvia, cuesta n³ operaciones. En 1969 Strassen demostró que se puede hacer con menos, y desde entonces se busca el mínimo exponente posible, llamado ω. El récord humano estaba en 2,371. Se cree que el verdadero valor es 2, pero nadie ha bajado de 2,37 en cincuenta años de intentos.

**Qué resuelve.** Demuestra que ω es como máximo 2,25. Es la mayor bajada desde los años 80.

**Por qué el puesto 1.** Multiplicar matrices es la operación central de la IA, los gráficos y la simulación científica, y está comprobado al completo con Lean. Pero no hará más rápido ningún programa: estos métodos solo ganan con matrices de un tamaño que nadie usa. Su valor es saber que la operación es más barata de lo que se creía.

## 2. La Conjetura de Unique Games (102) 🟡

> **En palabras sencillas.** Hay problemas, como repartir tareas o cortar una red en dos partes, que un ordenador no puede resolver a la perfección en un tiempo razonable. Se usan métodos que dan una respuesta "bastante buena". Este resultado demuestra que esos métodos ya son los mejores posibles: nadie encontrará uno rápido que lo haga mejor.
>
> **Antes:** Una empresa de logística pagaba a un equipo para buscar un algoritmo que repartiera rutas un 5 % mejor que el método estándar. Nadie sabía si existía.
>
> **Ahora:** Ese equipo puede dejar de buscar: está demostrado que no existe un método rápido que garantice mejores resultados en todos los casos. El esfuerzo se puede dedicar a trucos que funcionen bien en sus datos concretos.

**El problema.** Muchos problemas de reparto y de redes no se pueden resolver de forma exacta en un tiempo razonable, así que se usan algoritmos que dan una solución "bastante buena". En 2002 Khot conjeturó que, para muchos de esos problemas, los algoritmos conocidos ya eran los mejores posibles. Era una de las preguntas abiertas más importantes de la informática teórica.

**Qué resuelve.** Demuestra la conjetura. Como consecuencia, para Max-Cut, Vertex Cover y otros problemas, ningún algoritmo rápido puede garantizar una solución mejor que las actuales.

**Por qué este puesto.** Cierra una pregunta de dos décadas y dice a los ingenieros dónde dejar de buscar. Está en Lean el artículo principal, pero no todos los de la familia.

## 3. Los primos son más ordenados de lo que se sabía (003) 🟡

> **En palabras sencillas.** Los números primos (2, 3, 5, 7, 11...) parecen aparecer al azar, pero siguen un patrón escondido. Una famosa hipótesis de 1859 describe ese patrón al detalle, y nadie la ha demostrado. Este resultado demuestra una parte grande de ella: los primos son más ordenados de lo que se podía asegurar.
>
> **Antes:** Si querías saber cuántos primos hay hasta un billón, las fórmulas conocidas tenían un margen de error grande, porque no se podía descartar que los primos hicieran algo raro.
>
> **Ahora:** Ese margen de error se reduce mucho. Las fórmulas que cuentan primos son más precisas, lo que afecta a quienes estudian la criptografía y la teoría de números. Para el usuario normal no cambia nada: internet sigue igual de seguro.

**El problema.** La Hipótesis de Riemann, de 1859, dice dónde pueden estar los "ceros" de una función que controla cómo se reparten los números primos. Es el problema abierto más famoso de las matemáticas. Hasta ahora solo se sabía que no hay ceros en una franja muy estrecha del borde.

**Qué resuelve.** Amplía mucho la zona sin ceros: no hay ninguno con parte real mayor que 7/8. Sigue sin ser la hipótesis completa, que pide llegar a 1/2.

**Por qué este puesto.** Es el mayor avance en esta dirección en más de un siglo, y mejora las fórmulas que cuentan primos. El artículo principal está en Lean.

## 4. Birch–Swinnerton-Dyer en muchos casos (002) ⚪

> **En palabras sencillas.** Las curvas elípticas son unas ecuaciones que protegen tus mensajes de WhatsApp y tus pagos con tarjeta. Una conjetura de 1965 dice cómo contar sus soluciones. Es uno de los siete problemas por los que se ofrece un millón de dólares. Este resultado la demuestra para una gran parte de las curvas.
>
> **Antes:** Para saber cuántas soluciones tenía una curva, había que calcular a mano o confiar en que la conjetura fuera cierta sin demostración.
>
> **Ahora:** Para muchas curvas, la fórmula está demostrada y se puede usar con seguridad. Si otros matemáticos confirman el resultado, sería el mayor avance en ese problema del Milenio. Ojo: no está comprobado con Lean, así que todavía puede tener errores.

**El problema.** Las curvas elípticas son ecuaciones que están detrás de la criptografía moderna. En 1965 dos matemáticos conjeturaron una fórmula que relaciona sus soluciones con una función analítica. Es uno de los siete Problemas del Milenio, con un millón de dólares de premio.

**Qué resuelve.** Demuestra la fórmula completa para una gran familia de curvas, y con otro resultado de la colección la extiende a "casi todas" las variantes de cualquier curva.

**Por qué este puesto.** Sería un paso enorme hacia un Problema del Milenio, pero no tiene comprobación en Lean visible. Es el resultado que más necesita revisión humana.

## 5. Subset Sum más rápido (138) ⚪

> **En palabras sencillas.** Tienes una lista de números y quieres saber si algunos de ellos suman exactamente una cantidad, por ejemplo, qué compras de un ticket suman 100 euros. Con pocos números es fácil, pero con cientos el tiempo se dispara. Este resultado acelera el mejor método conocido por primera vez desde 1974.
>
> **Antes:** Con 100 números, el mejor método necesitaba del orden de mil billones de pasos (2 elevado a 50). Inabordable.
>
> **Ahora:** El exponente baja a 49. Sigue siendo inabordable, pero es la primera vez en 50 años que alguien lo mueve, y abre la puerta a que se pueda seguir bajando.

**El problema.** Dados unos números, ¿hay un grupo que sume exactamente un valor dado? Es uno de los problemas "difíciles" clásicos. En 1974 se encontró un método que tarda unos 2^(n/2) pasos, y durante cincuenta años nadie consiguió bajar ese exponente.

**Qué resuelve.** Un algoritmo que tarda 2^(0,49n). El número parece pequeño, pero es la primera mejora en medio siglo.

**Por qué este puesto.** Rompe una barrera histórica, aunque el problema sigue siendo muy lento en la práctica y no afecta a la criptografía.

## 6. Multiplicar enteros más rápido (109) ⚪

> **En palabras sencillas.** Multiplicar dos números muy largos, de millones de cifras, se usa para calcular decimales de π o en criptografía. Desde 1971 se pensaba que ya teníamos el método más rápido posible. Este resultado demuestra que no era así.
>
> **Antes:** Multiplicar dos números de mil millones de cifras tardaba un tiempo proporcional a n·log n, y se creía que era imposible bajar de ahí.
>
> **Ahora:** Se puede bajar, aunque tan poco que en la práctica no se nota. Lo que cambia es la idea: ese límite que parecía definitivo no lo era.

**El problema.** Multiplicar dos números de n cifras parece sencillo, pero encontrar el método más rápido es un problema abierto desde 1971. Schönhage y Strassen conjeturaron que n·log n era el mínimo posible.

**Qué resuelve.** Un método ligeramente más rápido que n·log n, lo que refuta esa conjetura.

**Por qué este puesto.** Derriba una conjetura de cincuenta años sobre una operación básica. La mejora es tan pequeña que no tiene uso práctico.

## 7. Las ecuaciones de los plasmas no explotan (362) ✅

> **En palabras sencillas.** Un plasma es un gas de partículas cargadas: el Sol, los rayos, el interior de un reactor de fusión. Las ecuaciones que lo describen se usan desde hace décadas, pero no se sabía si en algún momento podían "romperse" y dar resultados sin sentido. Este resultado demuestra que no.
>
> **Antes:** Un ingeniero que simulaba un reactor de fusión no podía estar seguro de si un resultado raro era un fallo de su programa o un fallo de las ecuaciones.
>
> **Ahora:** Ahora sabe que las ecuaciones no fallan: si algo sale raro, es cosa del programa o de los datos. Es un cimiento más firme para diseñar reactores y estudiar el espacio.

**El problema.** Un plasma es un gas de partículas cargadas, como el del Sol o el de un reactor de fusión. Las ecuaciones que lo describen (Vlasov–Maxwell) se usan desde hace décadas, pero no se sabía si sus soluciones podían "explotar" en un tiempo finito y dejar de tener sentido.

**Qué resuelve.** Demuestra que, en tres dimensiones y con datos iniciales razonables, la solución existe y sigue siendo suave para siempre.

**Por qué este puesto.** Da base sólida a los modelos de fusión y astrofísica, y está comprobado al completo con Lean.

## 8. Conjetura de Erdős sobre progresiones (159) ⚪

> **En palabras sencillas.** Si eliges un montón de números y el montón es "grande" (en un sentido matemático preciso), ¿siempre habrá dentro cadenas como 3, 7, 11, 15, donde cada número se separa del anterior lo mismo? Erdős apostó que sí hace 50 años. Este resultado le da la razón.
>
> **Antes:** Se sabía para cadenas de 3 números (demostrado en 2020). Para cadenas de 4, 5 o más, nadie lo sabía.
>
> **Ahora:** Vale para cadenas de cualquier longitud. Es matemática pura: no tiene aplicación directa, pero resuelve uno de los problemas con premio más famosos de Erdős.

**El problema.** Erdős preguntó en los años 70 si cualquier conjunto de números "suficientemente denso" (técnicamente, cuya suma de inversos diverge) contiene progresiones aritméticas de cualquier longitud, como 3, 7, 11, 15. Ofreció un premio por la respuesta. En 2020 se resolvió para progresiones de 3 términos; el caso general seguía abierto.

**Qué resuelve.** Demuestra la conjetura para progresiones de cualquier longitud.

**Por qué este puesto.** Es uno de los problemas con premio de Erdős más conocidos. Sin Lean visible.

## 9. Emparejamiento en tiempo casi lineal (120) ⚪

> **En palabras sencillas.** Tienes personas y tareas, y cada persona puede hacer solo algunas tareas. Quieres emparejar al máximo número posible. Se sabe resolver desde 1965, pero el método se vuelve lento con redes grandes. Este resultado lo hace casi tan rápido como leer la lista.
>
> **Antes:** Emparejar a un millón de conductores con un millón de pedidos podía tardar horas con el método clásico.
>
> **Ahora:** En teoría, tardaría casi lo que tarda el ordenador en leer los datos. Si alguien lo programa y funciona bien en la práctica, las apps de reparto, los hospitales que asignan órganos y los mercados laborales podrían usarlo.

**El problema.** Dada una red de personas o tareas, formar el máximo número de parejas compatibles. Se resuelve desde 1965 con el algoritmo de Edmonds, pero su tiempo crece más rápido que el tamaño de la red.

**Qué resuelve.** Un algoritmo que tarda casi lo mismo que leer la red.

**Por qué este puesto.** Es el resultado con más opciones de llegar a programas reales: asignación de recursos, rutas y mercados. Sin Lean visible.

## 10. Kakeya en 3 y 4 dimensiones (074) ⚪

> **En palabras sencillas.** Imagina una aguja que debe girar 180 grados. ¿Cuánto espacio mínimo necesita? En el plano, sorprendentemente casi nada. La pregunta es qué pasa en tres o más dimensiones. Esta conjetura de 1971 dice que el espacio nunca puede ser "pequeño". Este resultado la demuestra en más casos.
>
> **Antes:** El caso en tres dimensiones se resolvió en 2025, en una de sus versiones, tras décadas de intentos. Otras versiones seguían abiertas.
>
> **Ahora:** Se resuelven dos versiones más, en tres y cuatro dimensiones. Suena abstracto, pero este problema está conectado con cómo se procesan señales y ondas, y los avances aquí suelen acabar en herramientas de análisis.

**El problema.** ¿Cuánto espacio necesita una aguja para girar 180 grados? En el plano, sorprendentemente poco. La conjetura de Kakeya, de 1971, dice que en cualquier dimensión el conjunto que contiene una aguja en todas las direcciones no puede ser "pequeño". En 2025 se resolvió el caso tridimensional en una de sus formas; otras seguían abiertas.

**Qué resuelve.** La versión "maximal" en tres dimensiones y la de dimensión en cuatro.

**Por qué este puesto.** Kakeya está conectado con el análisis de Fourier y con las ecuaciones de ondas. Sin Lean visible.

## 11. π no se aproxima demasiado bien (017) ⚪

> **En palabras sencillas.** Las fracciones 22/7 y 355/113 se parecen mucho a π. ¿Hasta qué punto se puede acercar una fracción a π? Este resultado demuestra que π no es "especialmente fácil" de aproximar: se comporta como un número típico.
>
> **Antes:** Solo se sabía que π no se aproxima "demasiado bien", con un límite muy holgado (7,1). El valor exacto era desconocido.
>
> **Ahora:** El valor es 2, el mínimo posible. También responde a una pregunta curiosa que llevaba décadas abierta: si una suma infinita con senos (la serie de Flint Hills) da un número finito. Es matemática pura, sin uso práctico.

**El problema.** 22/7 y 355/113 son buenas aproximaciones de π. La pregunta es cuánto de bien se puede aproximar π con fracciones. El "exponente de irracionalidad" mide eso; para casi todos los números es 2, pero para π solo se sabía que era menor que 7,1.

**Qué resuelve.** Demuestra que es exactamente 2. De paso, responde a la pregunta de si la serie de Flint Hills converge.

**Por qué este puesto.** Es una pregunta clásica sobre el número más famoso. Sin Lean visible.

## 12. Factorizar polinomios sin azar (142) ⚪

> **En palabras sencillas.** Descomponer un polinomio en factores, como 6 = 2 × 3 pero con expresiones algebraicas, es una operación básica en los programas de matemáticas y en los códigos que corrigen errores en los CD, los satélites y los QR. Los métodos rápidos conocidos usan el azar. Este resultado da uno que no lo necesita.
>
> **Antes:** Un programa de cálculo simbólico factorizaba polinomios con un método aleatorio: casi siempre funcionaba, pero no había garantía absoluta.
>
> **Ahora:** Hay un método con garantía total que sigue siendo rápido. Si se implementa, los programas de matemáticas y los códigos correctores podrían usarlo. No tiene que ver con factorizar números grandes, que es lo que protege las contraseñas.

**El problema.** Descomponer un polinomio en factores es básico en el cálculo simbólico y en los códigos correctores de errores. Los métodos rápidos conocidos usan el azar; se buscaba uno que no lo necesite y sea igual de rápido.

**Qué resuelve.** Un algoritmo determinista y eficiente, sin suposiciones no demostradas.

**Por qué este puesto.** Resuelve un problema abierto de décadas en computación algebraica. No tiene nada que ver con factorizar números, que es lo que protege a RSA.

## 13. Contraejemplos a Kaplansky (197) 🟡

> **En palabras sencillas.** En 1950 un matemático planteó varias "apuestas" sobre unas estructuras algebraicas. Durante 70 años todo el mundo encontró que se cumplían. Este resultado construye ejemplos concretos en los que fallan.
>
> **Antes:** Los matemáticos asumían que las conjeturas de Kaplansky eran ciertas y construían teoría encima.
>
> **Ahora:** Se sabe que son falsas en general. Parte de esa teoría hay que revisarla, y los ejemplos nuevos abren una línea de investigación. Tres de los cuatro artículos están comprobados con Lean.

**El problema.** En 1950 Kaplansky planteó varias conjeturas sobre anillos de grupo, una estructura del álgebra. Durante setenta años se demostraron en muchos casos y nadie encontró un fallo.

**Qué resuelve.** Construye ejemplos concretos que las tumban, y de paso refuta otras dos conjeturas relacionadas (Gottschalk y la del determinante).

**Por qué este puesto.** Un contraejemplo cierra una pregunta para siempre. Tres de los cuatro artículos están en Lean; falta el del ejemplo sin torsión.

## 14. Colorear el plano: cinco colores no bastan (158) ✅

> **En palabras sencillas.** Pinta todos los puntos de una hoja infinita con colores, con una regla: dos puntos a exactamente 1 cm no pueden tener el mismo color. ¿Cuántos colores hacen falta? Desde 1950 se sabe que entre 4 y 7. Este resultado descarta el 5.
>
> **Antes:** En 2018 se demostró que con 4 colores no se puede. Quedaban 5, 6 y 7 como posibles respuestas.
>
> **Ahora:** Con 5 tampoco se puede. Solo quedan 6 o 7. Es un rompecabezas que cualquiera entiende y que llevaba 70 años atascado. Comprobado con Lean.

**El problema.** ¿Cuántos colores hacen falta para pintar todos los puntos del plano de modo que dos puntos a distancia exactamente 1 nunca tengan el mismo color? Desde 1950 se sabía que la respuesta está entre 4 y 7. En 2018 se demostró que 4 no bastan.

**Qué resuelve.** Que 5 tampoco bastan. Solo quedan 6 o 7.

**Por qué este puesto.** Es un problema que cualquiera entiende y que llevaba setenta años atascado. Comprobado al completo con Lean.

## 15. El decimosexto problema de Hilbert, parte uniforme (143) 🟡

> **En palabras sencillas.** En 1900 Hilbert publicó una lista de 23 problemas para el siglo. El número 16 pregunta cuántas "órbitas cerradas" puede tener un sistema de ecuaciones sencillas en el plano, como las que describen un péndulo o una población de animales. Este resultado demuestra que hay un máximo que solo depende de lo complicadas que sean las ecuaciones.
>
> **Antes:** Para cada sistema concreto se sabía que las órbitas eran finitas, pero nadie podía dar un número máximo de antemano.
>
> **Ahora:** Hay un tope garantizado según el grado de las ecuaciones. Para un tipo concreto de sistemas (Liénard de grado 5), el máximo es exactamente 2. Es relevante para quien modela sistemas que oscilan: circuitos, poblaciones, reacciones químicas.

**El problema.** En 1900 Hilbert publicó 23 problemas para el siglo XX. El decimosexto pregunta cuántas órbitas cerradas ("ciclos límite") puede tener un sistema de ecuaciones polinómicas en el plano. Se sabía que son finitas para cada sistema, pero no si hay un máximo que dependa solo del grado.

**Qué resuelve.** Demuestra que sí: hay una cota que depende solo del grado del polinomio.

**Por qué este puesto.** Es uno de los pocos problemas de Hilbert que seguían abiertos. Está en Lean uno de los dos artículos.

## 16. El grupo F de Thompson no es promediable (248) ✅

> **En palabras sencillas.** Hay un objeto matemático llamado grupo F de Thompson que se comporta de forma extraña. Desde los años 60 se discute si tiene una propiedad llamada "promediabilidad". Ha habido varias demostraciones en los dos sentidos, todas con errores. Este resultado zanja la cuestión.
>
> **Antes:** Un matemático que necesitaba saber si F es promediable tenía que elegir en qué demostración fallida confiar.
>
> **Ahora:** Está demostrado que no lo es, y la prueba está comprobada con Lean, lo que importa especialmente en un problema con tantos intentos fallidos. Es matemática pura.

**El problema.** El grupo F de Thompson es un objeto del álgebra con propiedades raras. Desde los años 60 se discute si es "promediable", una propiedad que decide cómo se comporta en muchas situaciones. Ha habido demostraciones en los dos sentidos, todas con errores.

**Qué resuelve.** Que no lo es.

**Por qué este puesto.** Es el problema más famoso de la teoría geométrica de grupos. Comprobado con Lean, lo que importa en un problema con tantas demostraciones fallidas.

## 17. La conjetura de Cannon (246) ⚪

> **En palabras sencillas.** Hay grupos abstractos cuyo "borde" se parece a una esfera. En 1991 Cannon conjeturó que todos ellos son en realidad las simetrías de un espacio tridimensional curvado. Este resultado lo demuestra.
>
> **Antes:** Se conocían muchos ejemplos que lo cumplían, pero no había forma de asegurar que no existiera una excepción.
>
> **Ahora:** No hay excepciones. Era el gran problema pendiente de la geometría tridimensional tras la conjetura de Poincaré. Sin Lean visible.

**El problema.** Cannon conjeturó en 1991 que ciertos grupos abstractos, cuyo "borde" se parece a una esfera, son en realidad los grupos de simetría de un espacio tridimensional curvado.

**Qué resuelve.** Demuestra la conjetura.

**Por qué este puesto.** Conecta dos áreas, grupos y geometría tridimensional, y era el gran problema pendiente tras la conjetura de Poincaré. Sin Lean visible.

## 18. La conjetura de distancias de Falconer (073) ✅

> **En palabras sencillas.** Si tienes un conjunto de puntos "suficientemente grande", ¿las distancias entre ellos forman también un conjunto grande? Falconer lo conjeturó en 1985. Este resultado lo demuestra en todas las dimensiones.
>
> **Antes:** Solo se sabía en casos parciales, con condiciones más exigentes que las de la conjetura.
>
> **Ahora:** Se cumple siempre. Es un pilar del análisis geométrico, conectado con el problema de Kakeya. Comprobado con Lean.

**El problema.** Si un conjunto de puntos es "suficientemente grande" (dimensión mayor que la mitad del espacio), ¿el conjunto de distancias entre sus puntos es también grande? Falconer lo conjeturó en 1985. Se sabía en casos parciales.

**Qué resuelve.** Lo demuestra en todas las dimensiones.

**Por qué este puesto.** Problema central del análisis geométrico, comprobado al completo con Lean.

## 19. Los factores de grupo libre son todos iguales (287) ⚪

> **En palabras sencillas.** En un área del álgebra hay unos objetos, los factores de grupo libre, construidos a partir de 2, 3, 4... piezas. Desde los años 60 nadie sabía si el de 2 piezas y el de 3 son el mismo objeto o distintos. Este resultado dice que son el mismo.
>
> **Antes:** La pregunta era tan difícil que para atacarla se creó toda una teoría nueva, la probabilidad libre, que hoy se usa en estadística de matrices grandes.
>
> **Ahora:** Si se confirma, se cierra la pregunta que dio origen a esa teoría. No está en Lean y es un campo donde los errores sutiles son frecuentes, así que hay que esperar a la revisión.

**El problema.** En álgebras de operadores hay unos objetos, los factores de grupo libre, de los que no se sabía si el de dos generadores y el de tres son el mismo o distintos. La pregunta lleva abierta desde los años 60 y ha motivado toda una teoría (la probabilidad libre de Voiculescu).

**Qué resuelve.** Que son todos el mismo objeto.

**Por qué este puesto.** Es el problema más conocido de su área, pero sin Lean visible y en un campo donde los errores sutiles son frecuentes.

## 20. Un fluido puede ser un ordenador (376) ⚪

> **En palabras sencillas.** Las ecuaciones de Navier–Stokes describen el agua, el aire y la sangre. Este resultado demuestra que un fluido, empujado de la forma adecuada, puede ejecutar cualquier programa de ordenador.
>
> **Antes:** Se sospechaba que los fluidos podían "calcular", pero solo se había demostrado en modelos simplificados.
>
> **Ahora:** Está demostrado en el modelo real en tres dimensiones. Significa que predecir un fluido puede ser tan difícil como predecir si un programa termina, algo que se sabe imposible en general. No es el Problema del Milenio de Navier–Stokes, que pregunta otra cosa.

**El problema.** Las ecuaciones de Navier–Stokes describen cómo se mueven los fluidos. Se sospechaba que un fluido podía, en principio, simular cualquier cálculo, lo que tendría consecuencias sobre si sus soluciones se pueden predecir.

**Qué resuelve.** Construye flujos en tres dimensiones que, con una fuerza externa adecuada, ejecutan cualquier programa.

**Por qué este puesto.** Es llamativo, pero no es el Problema del Milenio de Navier–Stokes, que pregunta otra cosa (si las soluciones existen y son suaves). Ninguno de sus nueve artículos está en Lean.

---

## Del 21 al 50: importantes, pero con poco impacto hoy

Los 30 siguientes son resultados que los matemáticos consideran importantes y que en muchos casos llevaban décadas abiertos. Están fuera del top 20 por una razón: afectan a poca gente fuera de su área. Resuelven una pregunta, confirman una predicción o cierran una conjetura, pero no cambian ninguna herramienta ni tecnología a corto plazo. En cada ficha, la parte **Por qué este puesto** explica ese límite.

| # | Descubrimiento | Problema abierto desde | Lean |
|---|---|---|---|
| 21 | El décimo problema de Hilbert para fracciones (004) | 1900 | ⚪ |
| 22 | La conjetura de Hodge en un caso importante (032) | 1950 | ⚪ |
| 23 | El azar no ayuda a los programas con poca memoria (103) | 1979 | ⚪ |
| 24 | Mapas que se pueden aplanar sin deformar (089) | 2004 | ✅ |
| 25 | Esqueletos de redes que no sobrecargan ningún tramo (174) | 2004 | 🟡 |
| 26 | Decidir sin conocer el futuro con una sola pista (111) | 2012 | ⚪ |
| 27 | Juegos de estrategia que se resuelven rápido (104) | 1979 | 🟡 |
| 28 | Colorear mapas de tres colores es difícil incluso con muchos (106) | 1976 | ✅ |
| 29 | Dónde está el límite de los problemas aleatorios (235) | 1990s | ⚪ |
| 30 | Las raíces primitivas de Artin (029) | 1927 | ⚪ |
| 31 | La constante de Catalan es irracional (005) | 1865 | ⚪ |
| 32 | La forma más "pequeña" posible (conjeturas de Mahler) (087) | 1939 | 🟡 |
| 33 | Una desigualdad sobre mezclar formas (Brunn–Minkowski logarítmica) (091) | 2012 | ✅ |
| 34 | Por qué los panales son hexagonales (090) | 1960s | ⚪ |
| 35 | La conjetura de Borsuk falla antes de lo que se creía (156) | 1933 | ✅ |
| 36 | Dos conjeturas sobre colorear redes son falsas (157) | 1943 | ⚪ |
| 37 | Cuántos amigos hacen falta para garantizar un cubo (171) | 1983 | ⚪ |
| 38 | La conjetura del segundo vecindario de Seymour (173) | 1990 | ✅ |
| 39 | La conjetura de Barnette sobre recorridos (180) | 1969 | ⚪ |
| 40 | Por qué los imanes pierden fuerza al calentarse (ley de Bloch) (271) | 1930 | ⚪ |
| 41 | La brecha de Haldane (268) | 1983 | ⚪ |
| 42 | Cuántos electrones puede sujetar un átomo (263) | 1980s | 🟡 |
| 43 | La fórmula de los vidrios de espín diluidos (221) | 1987 | ⚪ |
| 44 | Dónde está el punto más caliente de una placa (369) | 1974 | ⚪ |
| 45 | La conjetura de De Giorgi en su última dimensión (375) | 1978 | ⚪ |
| 46 | La conjetura de Birkhoff sobre mesas de billar (147) | 1920s | ⚪ |
| 47 | Cuánto "mide" una curva aleatoria (SLE) (230) | 2000 | ⚪ |
| 48 | La conjetura de Hilbert–Smith (304) | 1941 | ⚪ |
| 49 | La conjetura de uniformización de Yau (338) | 1974 | ⚪ |
| 50 | La hipótesis de homotopía de Grothendieck (312) | 1983 | ✅ |

---

## 21. El décimo problema de Hilbert para fracciones (004) ⚪

> **En palabras sencillas.** Hilbert pidió en 1900 un método automático que diga si una ecuación con números enteros tiene solución. En 1970 se demostró que ese método no existe para soluciones enteras. Quedaba la pregunta para soluciones con fracciones, que llevaba 50 años abierta.
>
> **Antes:** Un programa podía intentar resolver una ecuación con fracciones, pero nadie sabía si existía un método que funcionara siempre.
>
> **Ahora:** Está demostrado que no existe: ningún programa, por listo que sea, puede decidirlo en todos los casos. Es un límite definitivo del conocimiento, no una herramienta nueva.

**El problema.** El décimo problema de Hilbert pide un algoritmo que decida si un polinomio con coeficientes enteros tiene raíces. Matiyasevich demostró en 1970 que no existe para raíces enteras. La versión sobre los racionales era uno de los grandes problemas abiertos de la lógica.

**Qué resuelve.** Demuestra que tampoco existe tal algoritmo para raíces racionales.

**Por qué este puesto.** Es un resultado histórico en lógica, pero solo dice que algo es imposible. No da ninguna herramienta nueva, y las ecuaciones que importan en la práctica ya se atacan caso por caso.

## 22. La conjetura de Hodge en un caso importante (032) ⚪

> **En palabras sencillas.** La conjetura de Hodge es otro de los siete problemas del Milenio. Pregunta si ciertas formas abstractas dentro de un espacio geométrico vienen siempre de piezas "reales" (ecuaciones). Este resultado lo demuestra para una familia concreta de espacios.
>
> **Antes:** Se sabía en pocos casos, y el problema general lleva 75 años sin avances importantes.
>
> **Ahora:** Se demuestra para las variedades abelianas de tipo CM, en todas las dimensiones. No es el problema del Milenio completo, y ninguno de sus 8 artículos está en Lean. Es matemática muy abstracta, sin aplicación.

**El problema.** La conjetura de Hodge, de 1950, afirma que las clases de Hodge racionales de una variedad proyectiva compleja son combinaciones de clases de subvariedades algebraicas. Es uno de los Problemas del Milenio.

**Qué resuelve.** La demuestra para toda variedad abeliana compleja con multiplicación compleja, en cualquier dimensión y codimensión, y de rebote obtiene las conjeturas de Tate y estándar de Hodge para variedades abelianas sobre cuerpos finitos.

**Por qué este puesto.** Un paso real hacia un Problema del Milenio, pero en un caso particular y sin verificación formal. Afecta a un área pequeña de la geometría algebraica.

## 23. El azar no ayuda a los programas con poca memoria (103) ⚪

> **En palabras sencillas.** Algunos programas usan tirar una moneda para resolver problemas más rápido. La pregunta era si un programa con muy poca memoria gana algo con esa moneda. Este resultado dice que no: todo lo que se hace con azar y poca memoria se puede hacer sin azar con la misma memoria.
>
> **Antes:** Para comprobar si dos puntos de un laberinto están conectados usando poca memoria, el método con moneda era conocido desde 1979; sin moneda, solo desde 2005 y para laberintos sin dirección.
>
> **Ahora:** Cualquier problema de ese tipo se puede resolver sin moneda. Es un hito de la teoría de la computación, pero los programas reales tienen memoria de sobra y no notarán nada.

**El problema.** Se sabía que L ⊆ RL ⊆ BPL, las clases de problemas decidibles en espacio logarítmico sin azar, con azar de un lado y con azar de dos lados. Si coinciden era una pregunta abierta desde los años 80, considerada el caso más accesible de la desaleatorización.

**Qué resuelve.** Demuestra L = RL = BPL con un compilador explícito que elimina el azar.

**Por qué este puesto.** Es uno de los grandes problemas de la complejidad computacional, pero sus consecuencias son teóricas. No está en Lean.

## 24. Mapas que se pueden aplanar sin deformar (089) ✅

> **En palabras sencillas.** Un mapa de carreteras tiene distancias complicadas. Sería útil representarlas con coordenadas sencillas, como una cuadrícula, sin que las distancias se deformen mucho. Este resultado demuestra que para mapas "planos" siempre se puede, con una deformación limitada.
>
> **Antes:** Se sabía para mapas muy simples. Para mapas planos en general, nadie sabía si la deformación podía crecer sin límite.
>
> **Ahora:** La deformación tiene un tope fijo, igual para todos los mapas planos. Si alguien lo convierte en código, podría mejorar los algoritmos de rutas y de división de redes. Comprobado con Lean.

**El problema.** La conjetura de Gupta–Newman–Rabinovich–Sinclair (2004) afirma que las métricas de grafos que excluyen un menor fijo se sumergen en L₁ con distorsión acotada. El caso planar era el más buscado.

**Qué resuelve.** Lo demuestra para grafos planares, con distorsión universal, y para grafos de anchura arbórea acotada.

**Por qué este puesto.** Tiene uso potencial en algoritmos de grafos y está comprobado al completo con Lean, pero es una pieza teórica que todavía nadie ha llevado a código.

## 25. Esqueletos de redes que no sobrecargan ningún tramo (174) 🟡

> **En palabras sencillas.** Imagina una red eléctrica muy conectada. Quieres quedarte con un "esqueleto" mínimo que llegue a todos los puntos sin cargar demasiado ninguna zona. Este resultado demuestra que ese esqueleto siempre existe y da una receta para encontrarlo.
>
> **Antes:** Se sabía que el esqueleto existía "casi siempre" si se elegía al azar, pero no había un método seguro.
>
> **Ahora:** Hay un método determinista. Si se implementa, podría mejorar las aproximaciones del problema del viajante con sentido único, que se usa en reparto. La receta no está en Lean, solo la existencia.

**El problema.** La conjetura del árbol delgado fuerte, ligada a Goddyn (2004), afirma que todo grafo k-arista-conexo tiene un árbol generador que usa a lo sumo una fracción C/k de las aristas de cada corte. Es la vía conocida hacia una aproximación constante del viajante asimétrico.

**Qué resuelve.** Demuestra la conjetura y da un algoritmo determinista en tiempo polinomial.

**Por qué este puesto.** Es útil en teoría de redes, pero el camino hasta un programa real es largo y la parte algorítmica no está verificada.

## 26. Decidir sin conocer el futuro con una sola pista (111) ⚪

> **En palabras sencillas.** Vendes algo y los compradores llegan uno a uno; cada vez debes aceptar o rechazar sin saber qué vendrá después. Este resultado da una regla que, con una sola muestra previa de cada comprador, consigue una fracción fija de lo que ganaría alguien que viera el futuro.
>
> **Antes:** Las reglas conocidas necesitaban saber bien cómo se comportan los compradores o varias muestras de cada uno.
>
> **Ahora:** Basta una muestra por comprador y la garantía vale incluso contra un adversario que elija el orden. Podría usarse en subastas y asignación de recursos, pero sin Lean y aún sin implementaciones.

**El problema.** Las desigualdades de profeta comparan una regla online con el óptimo offline. Para matroides generales, se buscaba una regla que no dependa de la distribución y use una sola muestra por elemento.

**Qué resuelve.** Da esa regla, con garantía constante frente a un adversario todopoderoso.

**Por qué este puesto.** Es relevante para la teoría de mercados y subastas, pero su efecto depende de que alguien lo implemente y mida.

## 27. Juegos de estrategia que se resuelven rápido (104) 🟡

> **En palabras sencillas.** Hay juegos abstractos de dos jugadores que se usan para comprobar que un programa de control (un semáforo, un avión) hace siempre lo correcto. Resolverlos era lento. Este resultado da un método casi rápido.
>
> **Antes:** Un verificador de software podía tardar un tiempo exponencial en decidir quién gana el juego, lo que limitaba el tamaño de los sistemas que se podían verificar.
>
> **Ahora:** El tiempo es "cuasipolinómico", mucho menor. Podría permitir verificar sistemas más grandes, si se lleva a las herramientas. Uno de los cuatro artículos está en Lean.

**El problema.** Los juegos de paridad y de pago medio son el núcleo de la verificación de modelos. Se sabía que están en NP ∩ coNP, pero no si tienen algoritmos polinómicos. En 2017 se logró un algoritmo cuasipolinómico para paridad.

**Qué resuelve.** Da algoritmos cuasipolinómicos deterministas para juegos de pago medio y dos extensiones estocásticas, calculando valores y estrategias exactas.

**Por qué este puesto.** Útil en verificación formal, pero es un avance incremental sobre un resultado de 2017 y el salto a las herramientas industriales no es inmediato.

## 28. Colorear mapas de tres colores es difícil incluso con muchos (106) ✅

> **En palabras sencillas.** Hay redes que se pueden pintar con tres colores sin que dos vecinos coincidan, pero encontrar esa pintura es difícil. ¿Y si te permiten usar 10 colores? ¿O 100? Este resultado demuestra que sigue siendo igual de difícil con cualquier número fijo de colores.
>
> **Antes:** Se sabía que con 4 colores seguía siendo difícil (2000). Para 5 o más, nadie lo había demostrado sin suposiciones extra.
>
> **Ahora:** Está demostrado para cualquier número fijo de colores, y comprobado con Lean. Es un resultado de imposibilidad: dice qué no esperar de los algoritmos de asignación de frecuencias o de horarios.

**El problema.** Colorear un grafo 3-coloreable con c colores era NP-difícil solo para c = 4 (Khanna–Linial–Safra, Guruswami–Khanna) y, bajo hipótesis, para c = 5. El caso general era una pregunta clásica.

**Qué resuelve.** Demuestra NP-dureza para todo c ≥ 3 fijo, con una reducción determinista desde 3SAT.

**Por qué este puesto.** Pulcro y verificado, pero solo cierra una pregunta de dureza. No cambia ningún algoritmo que se use hoy.

## 29. Dónde está el límite de los problemas aleatorios (235) ⚪

> **En palabras sencillas.** Si generas al azar un rompecabezas lógico con muchas piezas, hay un punto exacto en el que pasa de tener solución a no tenerla. Los físicos lo predijeron hace 25 años, pero no se había demostrado que ese punto exista para todos los tamaños.
>
> **Antes:** Para rompecabezas con cláusulas de 3 piezas (3-SAT), el umbral se observaba en los experimentos, pero no se sabía si existía como límite matemático.
>
> **Ahora:** El umbral existe para cualquier tamaño de cláusula, y para 3-SAT es un número que se puede calcular. Interesa a la física estadística y a quien diseña resolvedores SAT; no cambia los resolvedores actuales.

**El problema.** La existencia de un umbral límite nítido para k-SAT aleatorio se demostró para k grande (Ding–Sly–Sun, 2015). Para k pequeño, incluido 3-SAT, seguía abierta.

**Qué resuelve.** Demuestra umbrales límite para todo k ≥ 3, la varianza exacta del tiempo de golpe y la computabilidad del umbral de 3-SAT. Reconoce la prioridad de Gaia Carenini en la existencia del umbral.

**Por qué este puesto.** Resultado central en la teoría de la satisfacibilidad aleatoria, pero su efecto en los resolvedores prácticos es nulo a corto plazo.

## 30. Las raíces primitivas de Artin (029) ⚪

> **En palabras sencillas.** Si tomas el número 2 y haces 2, 4, 8, 16... dividiendo entre un primo, ¿recorres todos los restos posibles? Cuando sí, 2 es una "raíz primitiva" de ese primo. Artin conjeturó en 1927 que para 2 (y casi cualquier base) hay infinitos primos así. Este resultado lo demuestra.
>
> **Antes:** Se sabía que era cierto para "casi todas" las bases, pero no se podía señalar ni una sola base concreta, ni siquiera el 2.
>
> **Ahora:** Está demostrado para cada base concreta que no sea -1 ni un cuadrado. Es matemática pura: interesa a la teoría de números y a los generadores de números pseudoaleatorios, pero sin efecto práctico.

**El problema.** La conjetura de Artin afirma que todo entero a que no sea -1 ni un cuadrado es raíz primitiva módulo infinitos primos. Hooley la demostró en 1967 bajo la hipótesis de Riemann generalizada; Heath-Brown mostró que falla para a lo sumo dos primos, sin poder decir cuáles.

**Qué resuelve.** Demuestra la infinitud incondicionalmente para toda base admisible, con una cota inferior cuantitativa.

**Por qué este puesto.** Un clásico de la teoría de números resuelto, pero sin Lean y sin consecuencias fuera de ella.

## 31. La constante de Catalan es irracional (005) ⚪

> **En palabras sencillas.** Hay un número, llamado constante de Catalan, que aparece en muchas fórmulas (vale 0,9159...). Desde hace 150 años se sospecha que no se puede escribir como fracción, pero nadie lo había demostrado.
>
> **Antes:** Se sabía que π es irracional desde 1761. De la constante de Catalan no se sabía nada parecido.
>
> **Ahora:** Queda demostrado que es irracional. Es un resultado de prestigio en teoría de números, sin ninguna aplicación.

**El problema.** La constante de Catalan G = 1 - 1/9 + 1/25 - ... es una de las constantes clásicas cuya irracionalidad estaba abierta, junto con la de ζ(5).

**Qué resuelve.** Demuestra que G es irracional.

**Por qué este puesto.** Pregunta famosa, respuesta sin consecuencias prácticas, y sin Lean.

## 32. La forma más "pequeña" posible (conjeturas de Mahler) (087) 🟡

> **En palabras sencillas.** Toma una figura convexa y su "figura dual". El producto de sus áreas tiene un mínimo. Mahler conjeturó en 1939 qué figuras lo alcanzan: en el plano, el cuadrado. En dimensiones altas nadie lo sabía.
>
> **Antes:** Estaba demostrado en el plano (1939) y en tres dimensiones (2020). En dimensiones mayores seguía abierto.
>
> **Ahora:** Está demostrado en todas las dimensiones, con las figuras ganadoras identificadas. La versión simétrica está en Lean. Interesa a la geometría y a la teoría de la información, sin uso directo.

**El problema.** Las conjeturas de Mahler identifican los minimizadores del volumen-producto de un cuerpo convexo y su polar: politopos de Hanner en el caso simétrico, símplices en el general. Resuelto en dimensión 3 por Iriyeh–Shibata.

**Qué resuelve.** Las demuestra en toda dimensión, clasifica los casos de igualdad y obtiene las desigualdades funcionales asociadas.

**Por qué este puesto.** Problema clásico de la geometría convexa cerrado, pero su impacto queda dentro de esa área.

## 33. Una desigualdad sobre mezclar formas (Brunn–Minkowski logarítmica) (091) ✅

> **En palabras sencillas.** Si mezclas dos figuras, el área de la mezcla cumple una desigualdad clásica. En 2012 se propuso una versión más fuerte para figuras simétricas. Este resultado la demuestra.
>
> **Antes:** Se sabía solo en el plano y en casos especiales.
>
> **Ahora:** Vale en cualquier dimensión y está comprobada con Lean. Es una herramienta para geómetras y probabilistas, no para ingenieros.

**El problema.** La conjetura logarítmica de Brunn–Minkowski (Böröczky–Lutwak–Yang–Zhang, 2012) refuerza la desigualdad clásica para cuerpos simétricos respecto al origen. Se conocía en dimensión 2 y para clases especiales.

**Qué resuelve.** La demuestra en toda dimensión, junto con la conjetura B para medidas log-cóncavas pares y las desigualdades L_p asociadas.

**Por qué este puesto.** Resultado limpio y verificado que ordena una parte de la geometría convexa, sin salir de ella.

## 34. Por qué los panales son hexagonales (090) ⚪

> **En palabras sencillas.** Si colocas partículas que se repelen en una mesa, ¿cómo se ordenan para gastar la menor energía? La intuición dice que en una red triangular, como un panal. Este resultado lo demuestra para una familia muy amplia de fuerzas.
>
> **Antes:** Se sabía para fuerzas concretas (Coulomb, algunas potencias). Para fuerzas generales era una conjetura.
>
> **Ahora:** La red triangular es la mejor para toda fuerza "completamente monótona". Explica por qué la naturaleza elige esa forma, pero no cambia cómo se fabrica nada.

**El problema.** La optimalidad universal de la red triangular en el plano, análoga a la de E8 y Leech en dimensiones 8 y 24 (Cohn–Kumar–Miller–Radchenko–Viazovska, 2019), estaba abierta.

**Qué resuelve.** La demuestra para todo potencial completamente monótono del cuadrado de la distancia, y para energías de Riesz y Coulomb.

**Por qué este puesto.** Resultado elegante de física matemática, sin Lean y con efecto solo dentro de su campo.

## 35. La conjetura de Borsuk falla antes de lo que se creía (156) ✅

> **En palabras sencillas.** Borsuk preguntó en 1933 si cualquier figura en n dimensiones se puede partir en n+1 trozos más pequeños. Es falso en dimensiones altas (se sabe desde 1993). La pregunta era desde qué dimensión falla.
>
> **Antes:** Se sabía que fallaba desde la dimensión 64 y que valía hasta la 3. Entre medias, nadie sabía.
>
> **Ahora:** Falla ya en dimensión 9. Es un ejemplo concreto comprobado con Lean. Curiosidad geométrica sin aplicación.

**El problema.** La conjetura de Borsuk se refutó en dimensión 1325 (Kahn–Kalai, 1993) y el récord bajó hasta 64 (Bondarenko, Jenrich–Brouwer). Las dimensiones 4 a 63 estaban abiertas.

**Qué resuelve.** Construye un contraejemplo en dimensión 9: un compacto que no se cubre con diez conjuntos de diámetro menor.

**Por qué este puesto.** Reduce mucho la dimensión mínima de fallo, pero sigue siendo un problema de geometría combinatoria pura.

## 36. Dos conjeturas sobre colorear redes son falsas (157) ⚪

> **En palabras sencillas.** La conjetura de Hadwiger, de 1943, es uno de los problemas más famosos sobre cómo colorear redes. Generaliza el teorema de los cuatro colores. Este resultado construye redes que la incumplen, incluso en una versión relajada.
>
> **Antes:** Se creía cierta: estaba demostrada para redes con pocos colores y nadie había encontrado un fallo en 80 años.
>
> **Ahora:** Es falsa en general. Hay que revisar lo que se construyó suponiéndola. No afecta a ningún algoritmo de coloreado que se use hoy. Sin Lean.

**El problema.** La conjetura de Hadwiger afirma que todo grafo sin K_t como menor es (t-1)-coloreable. Es uno de los problemas abiertos más profundos de la teoría de grafos.

**Qué resuelve.** La refuta incluso para coloración fraccionaria, con grafos de número de independencia 2, y refuta también la cota cromática fraccionaria de Colin de Verdière.

**Por qué este puesto.** Un terremoto en teoría de grafos, pero sin verificación formal y sin consecuencias prácticas.

## 37. Cuántos amigos hacen falta para garantizar un cubo (171) ⚪

> **En palabras sencillas.** En cualquier grupo grande de personas, si pintas cada amistad de rojo o azul, siempre aparece algún patrón de un solo color. Erdős y Burr preguntaron cuánta gente hace falta para garantizar un "cubo" de n dimensiones. Este resultado da la respuesta exacta en orden de magnitud.
>
> **Antes:** Se sabía que bastaba con un número exponencial en n², y se conjeturaba que bastaba con un múltiplo del tamaño del cubo. En 2021 se bajó a un exponente de 2n.
>
> **Ahora:** Basta con un múltiplo constante del tamaño del cubo, lo mejor posible. Teoría de Ramsey pura, sin Lean.

**El problema.** La conjetura de Burr–Erdős (1983) afirma que el número de Ramsey del hipercubo Q_n es O(2^n). Conlon, Fox y Sudakov habían llegado a O(2^{2n+o(n)}).

**Qué resuelve.** Demuestra r(Q_n) = Θ(2^n).

**Por qué este puesto.** Problema clásico resuelto, dentro de un área sin aplicaciones directas.

## 38. La conjetura del segundo vecindario de Seymour (173) ✅

> **En palabras sencillas.** En una red donde cada enlace tiene sentido único (como seguir a alguien en una red social), Seymour conjeturó que siempre hay alguien con al menos tantos "amigos de amigos" como amigos directos. Este resultado lo demuestra.
>
> **Antes:** Estaba demostrado para redes especiales (torneos) y en versiones aproximadas.
>
> **Ahora:** Vale para cualquier red orientada, y está comprobado con Lean. Es un resultado bonito sobre redes, sin ningún uso práctico conocido.

**El problema.** La conjetura del segundo vecindario (Seymour, ~1990) afirma que todo grafo orientado tiene un vértice cuyo segundo vecindario exterior es al menos tan grande como el primero. Se sabía para torneos (Fisher, 1996) y con constante 0,657.

**Qué resuelve.** La demuestra en general.

**Por qué este puesto.** Pregunta famosa y verificada, pero de teoría de grafos pura.

## 39. La conjetura de Barnette sobre recorridos (180) ⚪

> **En palabras sencillas.** Hay mapas con una estructura concreta (cada cruce une tres calles, se puede pintar con dos colores, y está bien conectado). Barnette conjeturó en 1969 que en todos ellos existe un recorrido que pasa por cada cruce una sola vez y vuelve al inicio.
>
> **Antes:** Estaba comprobado con ordenador hasta 86 cruces. Para mapas más grandes no se sabía.
>
> **Ahora:** Vale siempre. Es un problema de recorridos relacionado con el del viajante, pero para una clase tan concreta de mapas que no cambia nada práctico. Sin Lean.

**El problema.** La conjetura de Barnette afirma que todo grafo cúbico, bipartito, planar y 3-conexo es hamiltoniano. Verificada computacionalmente hasta 86 vértices.

**Qué resuelve.** La demuestra en general.

**Por qué este puesto.** Pregunta clásica de la teoría de grafos, sin verificación formal y sin aplicación.

## 40. Por qué los imanes pierden fuerza al calentarse (ley de Bloch) (271) ⚪

> **En palabras sencillas.** Un imán pierde magnetismo al calentarse, y Bloch predijo en 1930 exactamente cómo: proporcional a la temperatura elevada a 3/2. Los experimentos lo confirman desde hace décadas, pero no había demostración matemática a partir de las ecuaciones cuánticas.
>
> **Antes:** Se confiaba en la ley por los experimentos y por cálculos aproximados.
>
> **Ahora:** La ley queda demostrada con rigor desde el modelo cuántico, en tres dimensiones. No cambia cómo se fabrican imanes: confirma lo que ya se sabía. Sin Lean.

**El problema.** La ley T^{3/2} de Bloch y la magnetización espontánea en el modelo de Heisenberg cuántico ferromagnético eran resultados físicos sin prueba matemática. La existencia de orden a baja temperatura era un problema abierto desde Dyson–Lieb–Simon (1978) para el caso antiferromagnético.

**Qué resuelve.** Demuestra la ley de Bloch con su coeficiente exacto para todo espín en 3D, y la magnetización espontánea en toda dimensión d ≥ 3.

**Por qué este puesto.** Cierra un problema fundamental de la física matemática, pero sin efecto fuera de ella.

## 41. La brecha de Haldane (268) ⚪

> **En palabras sencillas.** Haldane predijo en 1983 que una cadena de imanes cuánticos de cierto tipo tiene un "salto de energía" que no desaparece por larga que sea la cadena. Le dieron el Nobel en 2016 en parte por eso. Faltaba la demostración matemática.
>
> **Antes:** Estaba demostrado para un modelo simplificado (AKLT, 1987) y confirmado numéricamente para el modelo real.
>
> **Ahora:** Queda demostrado para el modelo real en anillos de longitud par. Es la base matemática de las fases topológicas de la materia, que podrían servir para ordenadores cuánticos, pero eso está lejos. Sin Lean.

**El problema.** La conjetura de la brecha de Haldane para la cadena antiferromagnética de Heisenberg de espín 1 era uno de los problemas abiertos más conocidos de la física matemática.

**Qué resuelve.** Demuestra la brecha uniforme en anillos periódicos pares, y una brecha para cadenas abiertas impares con campo en los extremos.

**Por qué este puesto.** Confirma una predicción con Nobel, pero no abre ninguna tecnología nueva a corto plazo.

## 42. Cuántos electrones puede sujetar un átomo (263) 🟡

> **En palabras sencillas.** Un átomo con carga Z puede atrapar electrones de más y convertirse en un ion negativo. ¿Cuántos como máximo? Los experimentos dicen que uno o dos más que Z. La matemática solo podía demostrar que menos de 2Z. Este resultado acerca la teoría a la realidad.
>
> **Antes:** La mejor cota demostrada era 2Z+1 (Lieb, 1984), muy lejos de lo observado.
>
> **Ahora:** La cota pasa a Z más una constante. Confirma matemáticamente lo que la química sabe desde siempre. Uno de los tres artículos está en Lean.

**El problema.** La conjetura de ionización afirma que un átomo o molécula neutra liga a lo sumo Z + C electrones. La cota de Lieb era 2Z + M.

**Qué resuelve.** Demuestra la cota Z + CM para moléculas con M núcleos en el modelo de Coulomb no relativista con espín, y cotas universales para energías de ionización y radios atómicos.

**Por qué este puesto.** Importante en física matemática, pero la química ya operaba con el resultado correcto.

## 43. La fórmula de los vidrios de espín diluidos (221) ⚪

> **En palabras sencillas.** Los vidrios de espín son materiales magnéticos desordenados que sirven de modelo para redes neuronales y problemas de optimización. En 1987 dos físicos propusieron una fórmula para su energía. Este resultado la demuestra en una familia de modelos.
>
> **Antes:** La fórmula se usaba y encajaba con las simulaciones, pero sin demostración matemática, salvo en el modelo "denso" (Parisi, demostrado por Talagrand en 2006).
>
> **Ahora:** Queda demostrada para modelos diluidos con ciertas condiciones. Interesa a la física estadística y a la teoría de la optimización aleatoria; no cambia ningún algoritmo. Sin Lean.

**El problema.** La fórmula de cavidad jerárquica de Mézard–Parisi para modelos diluidos era el análogo abierto de la fórmula de Parisi para el modelo de Sherrington–Kirkpatrick.

**Qué resuelve.** La demuestra para modelos de Ising de aridad par diluidos por Poisson bajo las hipótesis de factorización y positividad de Panchenko–Talagrand.

**Por qué este puesto.** Avance notable en mecánica estadística rigurosa, con alcance limitado a esa comunidad.

## 44. Dónde está el punto más caliente de una placa (369) ⚪

> **En palabras sencillas.** Calienta una placa de metal de forma irregular y déjala enfriar. Con el tiempo, el punto más caliente y el más frío se desplazan hacia el borde. Rauch conjeturó en 1974 que siempre acaban en el borde. Es falso para placas con agujeros; este resultado demuestra que es cierto para placas sin agujeros.
>
> **Antes:** Se sabía para rectángulos, triángulos y algunas formas convexas. Para formas sin agujeros en general, no.
>
> **Ahora:** Vale para cualquier placa plana sin agujeros y de borde suave. Es un resultado de ecuaciones en derivadas parciales, con interés en la difusión del calor pero sin cambiar ninguna aplicación. Sin Lean.

**El problema.** La conjetura de los puntos calientes (Rauch, 1974) afirma que la segunda autofunción de Neumann alcanza sus extremos en la frontera. Burdzy–Werner la refutaron para dominios con agujeros; el caso simplemente conexo seguía abierto.

**Qué resuelve.** Demuestra una forma estricta para dominios planos simplemente conexos suaves: la autofunción no tiene puntos críticos interiores.

**Por qué este puesto.** Problema clásico resuelto dentro del análisis, sin repercusión fuera.

## 45. La conjetura de De Giorgi en su última dimensión (375) ⚪

> **En palabras sencillas.** Cuando dos materiales se separan (agua y aceite), la frontera entre ellos tiende a ser plana. De Giorgi conjeturó en 1978 que, en un modelo matemático de ese fenómeno, la frontera es plana en dimensiones hasta 8. Se demostró hasta la 7; faltaba la 8.
>
> **Antes:** Dimensiones 2 (1997), 3 (2000) y hasta 7 (2009, con una condición extra). La dimensión 8, el límite de la conjetura, seguía abierta.
>
> **Ahora:** Queda demostrada en dimensión 8, que es el caso límite. Es un hito del análisis de ecuaciones de transición de fase, sin aplicación directa. Sin Lean.

**El problema.** La conjetura de De Giorgi sobre soluciones monótonas de la ecuación de Allen–Cahn se demostró en dimensión 2 (Ghoussoub–Gui), 3 (Ambrosio–Cabré) y hasta 8 con hipótesis de límite (Savin). Del Pino–Kowalczyk–Wei construyeron contraejemplos en dimensión 9.

**Qué resuelve.** La demuestra en dimensión 8 sin hipótesis adicionales, y clasifica las soluciones estables en dimensión 7.

**Por qué este puesto.** Cierra un problema de 45 años, pero su efecto queda dentro del análisis.

## 46. La conjetura de Birkhoff sobre mesas de billar (147) ⚪

> **En palabras sencillas.** Imagina una mesa de billar ovalada. En una elipse perfecta, las bolas siguen trayectorias muy ordenadas. Birkhoff conjeturó que la elipse es la única forma con ese orden. Este resultado lo demuestra cuando el orden se da cerca del borde.
>
> **Antes:** Se sabía para mesas muy cercanas a un círculo (2018) y en versiones locales.
>
> **Ahora:** Vale para cualquier mesa convexa, siempre que el orden exista en una franja junto al borde. Es un problema de sistemas dinámicos, sin uso práctico. Sin Lean.

**El problema.** La conjetura de Birkhoff afirma que los billares integrables son elípticos. Kaloshin–Sorrentino la demostraron localmente cerca de elipses.

**Qué resuelve.** Demuestra la versión "cerca del borde": si un anillo completo junto al borde está foliado por curvas invariantes, el billar es una elipse.

**Por qué este puesto.** Resultado profundo en dinámica, de interés exclusivamente matemático.

## 47. Cuánto "mide" una curva aleatoria (SLE) (230) ⚪

> **En palabras sencillas.** Las curvas SLE describen fronteras aleatorias que aparecen en física: la orilla de una mancha que crece, la frontera entre dos fases. Schramm preguntó en 2000 cómo medir su longitud de forma natural. Este resultado da la respuesta exacta.
>
> **Antes:** Se conocía la dimensión fractal de la curva, pero no una medida de longitud bien definida que fuera finita y positiva.
>
> **Ahora:** Hay una medida explícita, con su corrección logarítmica exacta. Es una pieza de la teoría de la probabilidad moderna, sin aplicación directa. Sin Lean.

**El problema.** La pregunta de Schramm sobre la medida de Hausdorff del SLE_κ con la gauge correcta estaba abierta desde 2000.

**Qué resuelve.** Demuestra que la gauge r^d (log log 1/r)^{(2-d)/2}, con d = 1 + κ/8, da medida positiva y finita a cada segmento de la traza.

**Por qué este puesto.** Avance importante en probabilidad, dentro de un área muy especializada.

## 48. La conjetura de Hilbert–Smith (304) ⚪

> **En palabras sencillas.** El quinto problema de Hilbert preguntaba si ciertos grupos de simetrías son siempre "suaves". Se resolvió en 1952. Quedaba una versión más fuerte, sobre simetrías de espacios curvados: Hilbert–Smith. Este resultado la demuestra en todas las dimensiones.
>
> **Antes:** Estaba demostrada en dimensión 3 (Pardon, 2013). En dimensión 4 o más, no.
>
> **Ahora:** Vale en toda dimensión. Es un resultado fundamental de la topología, sin ninguna aplicación. Sin Lean.

**El problema.** La conjetura de Hilbert–Smith afirma que todo grupo localmente compacto que actúa fielmente sobre una variedad conexa es un grupo de Lie. Se reducía a excluir acciones de los enteros p-ádicos.

**Qué resuelve.** La demuestra para toda variedad topológica conexa de dimensión finita.

**Por qué este puesto.** Pieza central de la teoría de grupos de transformaciones, con interés puramente teórico.

## 49. La conjetura de uniformización de Yau (338) ⚪

> **En palabras sencillas.** En el plano hay un teorema famoso: cualquier superficie "simple" se puede aplanar. Yau conjeturó en 1974 una versión en muchas dimensiones: si un espacio es curvado positivamente de cierta forma y no se cierra sobre sí mismo, es en el fondo el espacio plano. Este resultado lo demuestra.
>
> **Antes:** Estaba demostrado con hipótesis extra sobre la curvatura (Liu, 2016; otros). El caso general seguía abierto.
>
> **Ahora:** Vale sin hipótesis adicionales. Es geometría compleja pura, sin aplicación. Sin Lean.

**El problema.** La conjetura de uniformización de Yau afirma que toda variedad de Kähler completa no compacta con curvatura biseccional holomorfa positiva es biholomorfa a C^n. Liu la demostró bajo crecimiento máximo de volumen.

**Qué resuelve.** La demuestra en general.

**Por qué este puesto.** Un problema clásico de geometría compleja, cerrado solo para esa comunidad.

## 50. La hipótesis de homotopía de Grothendieck (312) ✅

> **En palabras sencillas.** Grothendieck propuso en 1983 que ciertas estructuras algebraicas muy abstractas (los ∞-grupoides) capturan toda la información de las formas geométricas "hasta deformación". Es una idea central en la matemática moderna, y en una de sus versiones seguía sin demostración.
>
> **Antes:** Estaba demostrado para algunos modelos de ∞-grupoide, pero no para los que Grothendieck propuso originalmente.
>
> **Ahora:** Queda demostrado para los modelos originales, y comprobado con Lean. Es un resultado de fundamentos, sin ninguna aplicación.

**El problema.** La hipótesis de homotopía afirma que los ∞-grupoides de Grothendieck, definidos mediante coherators, modelan la teoría de homotopía de los espacios. Ara y Henry habían precisado el enunciado.

**Qué resuelve.** La demuestra para todo coherator de Grothendieck en la convención de Ara–Henry.

**Por qué este puesto.** Fundamental para la teoría de categorías superiores, verificado formalmente, y completamente ajeno a cualquier uso práctico.

---

## Lo que queda fuera

Hay otras 322 familias. Muchas son importantes en su área pero tienen aún menos efecto fuera de ella. La lista completa está en [`CONTENTS.md`](../CONTENTS.md).
