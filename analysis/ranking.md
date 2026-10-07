# Ranking de los descubrimientos

Los 20 resultados más importantes de `openai/math`, ordenados por su impacto si se confirman. Para cada uno: cuál era el problema, qué resuelve y cuánto está comprobado.

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

## Lo que queda fuera del ranking

Hay otras 352 familias. Muchas son importantes en su área pero tienen poco efecto fuera de ella, o afectan a tan pocas personas que no entran aquí. La lista completa está en [`CONTENTS.md`](../CONTENTS.md).
