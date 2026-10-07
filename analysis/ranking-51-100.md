# Ranking explicado: del 51 al 100

Explicaciones cortas de los puestos 51 a 100 del [ranking completo](ranking-completo.md). Son más breves y menos trabajadas que las [fichas de los 50 primeros](ranking.md): tres frases por resultado, pensadas para saber de qué va en medio minuto.

Estos resultados son importantes para los matemáticos, pero tienen poco efecto fuera de su área por ahora. La última frase de cada uno lo dice.

Si una palabra no te suena, mira el [glosario](../docs/glosario.md). Las descripciones salen de los resúmenes publicados en `openai/math`, no de leer los artículos completos.

---

<a id="r51"></a>
### 51. Meter cajas en el menor número de contenedores (118) ✅

**El problema.** Tienes objetos de distintos tamaños y quieres usar los menos contenedores posibles. Como el problema exacto es lento, se usa una versión "relajada" que da un número aproximado, y desde 2004 se conjeturaba que ese número nunca se quedaba corto en más de 1 contenedor.

**Qué resuelve.** Demuestra que sí puede quedarse corto, y por cualquier cantidad. La aproximación habitual no es tan buena como se pensaba.

**Fuera de su área.** Afecta a quien diseña algoritmos de logística y corte de materiales, pero los programas reales ya usan otros trucos. Comprobado con Lean.

<a id="r52"></a>
### 52. Los juegos 2 a 1, un primo de Unique Games (105) ✅

**El problema.** Es una variante de la Conjetura de Unique Games (puesto 2). En 2018 se demostró en una versión débil; faltaba la fuerte, con "completitud perfecta".

**Qué resuelve.** Demuestra la versión fuerte. Con ella, varios problemas de aproximación quedan clasificados como difíciles sin suposiciones extra.

**Fuera de su área.** Solo interesa a la teoría de la complejidad. Comprobado con Lean.

<a id="r53"></a>
### 53. La sensibilidad de las funciones booleanas (132) ✅

**El problema.** En 2019 se demostró un resultado famoso: la "sensibilidad" de una función de bits (cuánto cambia al tocar un bit) controla otras medidas de complejidad, con una relación a lo sumo cuadrática. Se conjeturaba que una versión más fuerte también valía.

**Qué resuelve.** Construye funciones que incumplen la versión fuerte. La relación cuadrática original sigue en pie, pero no se puede mejorar como se esperaba.

**Fuera de su área.** Es un detalle fino de la teoría de la computación, sin efecto práctico. Comprobado con Lean.

<a id="r54"></a>
### 54. Cómo se deforma el plano al aplanarlo (Brennan) (072) ✅

**El problema.** Cualquier forma plana sin agujeros se puede transformar en un círculo de manera "conforme" (sin deformar ángulos). Brennan conjeturó en 1978 hasta qué punto puede estirarse esa transformación. Se sabía en parte.

**Qué resuelve.** Demuestra la conjetura completa y de paso refuta una predicción numérica relacionada.

**Fuera de su área.** Es análisis complejo puro. Comprobado con Lean.

<a id="r55"></a>
### 55. ¿Se puede caminar hasta el infinito saltando entre primos gaussianos? (028) ✅

**El problema.** Los primos gaussianos son los "primos" de los números complejos. La pregunta, de 1962: ¿puedes alejarte hasta el infinito dando saltos de tamaño limitado de un primo gaussiano a otro, o siempre te topas con un "foso"?

**Qué resuelve.** Demuestra que siempre hay un foso: con saltos de cualquier tamaño fijo, te quedas atrapado en una zona finita.

**Fuera de su área.** Es una curiosidad clásica de la teoría de números, sin aplicación. Comprobado con Lean.

<a id="r56"></a>
### 56. Una pieza que llena el espacio pero nunca de forma ordenada (155) ✅

**El problema.** ¿Toda pieza que llena el espacio sin huecos lo puede hacer también de forma periódica, repitiéndose como un papel pintado? En el plano, sí. En 2022 se encontró una pieza que lo incumple, pero en una dimensión enorme. ¿Y en dimensión 3?

**Qué resuelve.** Construye una pieza en tres dimensiones que llena el espacio pero nunca de forma periódica. Es la dimensión más baja posible.

**Fuera de su área.** Conecta con los cuasicristales de la física, pero no tiene uso directo. Comprobado con Lean.

<a id="r57"></a>
### 57. Cuánto crecen los números de van der Waerden (160) ✅

**El problema.** Si pintas los números 1, 2, 3... con r colores, antes o después aparece una progresión aritmética de un solo color. ¿Cuántos números hacen falta? Erdős preguntó si ese número crece más rápido que cualquier exponencial.

**Qué resuelve.** Demuestra que sí, con una fórmula explícita.

**Fuera de su área.** Teoría de Ramsey pura. Comprobado con Lean.

<a id="r58"></a>
### 58. Descomponer cualquier red en pocos ciclos (Erdős–Gallai) (181) ✅

**El problema.** Erdős y Gallai conjeturaron en 1966 que las conexiones de cualquier red con n nodos se pueden repartir en unos pocos ciclos y conexiones sueltas: a lo sumo un múltiplo de n.

**Qué resuelve.** Lo demuestra.

**Fuera de su área.** Resultado de teoría de grafos sin uso práctico. Comprobado con Lean.

<a id="r59"></a>
### 59. Dividir una red en dos partes poco conectadas (117) 🟡

**El problema.** El problema del "corte más disperso" busca partir una red en dos mitades con el mínimo de conexiones entre ellas. Se usa en diseño de chips y en análisis de redes. No se sabía si se podía aproximar bien con un algoritmo rápido.

**Qué resuelve.** Demuestra que no: aproximarlo dentro de cualquier factor fijo es tan difícil como los problemas más duros de la informática.

**Fuera de su área.** Dice a los ingenieros qué no esperar. Los algoritmos que se usan hoy siguen igual. Parte en Lean.

<a id="r60"></a>
### 60. Dónde poner k almacenes para estar cerca de todos (125) 🟡

**El problema.** Elige k lugares para almacenes de modo que la distancia media a los clientes sea mínima. Es un problema clásico de logística. Se conocía un algoritmo que se acerca al óptimo con un factor de 2,67, y se sospechaba que el mejor factor posible era 1,74.

**Qué resuelve.** Da un algoritmo que llega a 1,74 y demuestra que no se puede bajar más.

**Fuera de su área.** Si se implementa bien, podría mejorar herramientas de localización de instalaciones. Parte en Lean.

<a id="r61"></a>
### 61. La transformada de Fourier, un poco más rápida (130) 🟡

**El problema.** La transformada rápida de Fourier es el algoritmo que está detrás del audio digital, el JPEG y las telecomunicaciones. Desde 1965 se creía que su coste, n·log n, era imposible de mejorar.

**Qué resuelve.** Da un algoritmo ligeramente más rápido, con una mejora tan minúscula (un exponente de 10^-13) que no se nota.

**Fuera de su área.** No cambiará ningún aparato. Lo interesante es que el límite que parecía definitivo no lo era. Parte en Lean.

<a id="r62"></a>
### 62. Cuántos cruces tiene como mínimo un dibujo de una red (165) ✅

**El problema.** Si dibujas una red en la que todos están conectados con todos, ¿cuál es el menor número de cruces de líneas? Hay fórmulas conjeturadas desde los años 50 (Harary–Hill y el problema del ladrillar de Turán), comprobadas solo para redes pequeñas.

**Qué resuelve.** Demuestra que las fórmulas son exactas para cualquier tamaño.

**Fuera de su área.** Interesa al diseño de circuitos y a la visualización de redes, pero como teoría. Comprobado con Lean.

<a id="r63"></a>
### 63. La conjetura de Crouzeix (325) ✅

**El problema.** Para cualquier matriz, hay una forma de acotar lo que hace un polinomio aplicado a ella mirando solo una región del plano, su "rango numérico". Crouzeix conjeturó en 2004 que la constante de esa cota es 2. Se sabía que era como mucho 1+√2.

**Qué resuelve.** Demuestra que es exactamente 2, también para polinomios con valores matriciales.

**Fuera de su área.** Es útil en análisis numérico para estimar errores, pero de forma teórica. Comprobado con Lean.

<a id="r64"></a>
### 64. Cuándo aparece una estructura en una red aleatoria (Kahn–Kalai) (176) ✅

**El problema.** Si conectas nodos al azar con probabilidad p, ¿a partir de qué p aparece seguro una forma concreta, por ejemplo un triángulo o un cubo? Kahn y Kalai conjeturaron en 2006 que la respuesta está cerca de una cantidad fácil de calcular. La primera versión se demostró en 2022.

**Qué resuelve.** Demuestra la segunda versión, la específica para redes.

**Fuera de su área.** Teoría de redes aleatorias. Comprobado con Lean.

<a id="r65"></a>
### 65. No existen matrices de Hadamard circulantes grandes (179) ✅

**El problema.** Las matrices de Hadamard son tablas de +1 y -1 con propiedades que se usan en códigos y en comunicaciones. Desde los años 60 se conjeturaba que las de tipo "circulante" solo existen en tamaños 1 y 4.

**Qué resuelve.** Lo demuestra. De paso cierra la pregunta de las secuencias de Barker.

**Fuera de su área.** Cierra una búsqueda de décadas, pero los ingenieros ya trabajaban asumiendo que no existían. Comprobado con Lean.

<a id="r66"></a>
### 66. Otro contraejemplo a Kaplansky (196) ✅

**El problema.** Es una de las conjeturas de Kaplansky (ver puesto 13): que cierto tipo de álgebra no tiene "divisores de cero". En 2021 se refutó para un caso; quedaba la versión original.

**Qué resuelve.** Construye un contraejemplo a la versión original.

**Fuera de su área.** Álgebra pura. Comprobado con Lean.

<a id="r67"></a>
### 67. Repetir un juego cuántico muchas veces (277) ✅

**El problema.** En computación cuántica se estudian juegos en los que dos jugadores comparten partículas entrelazadas. Si ganan con probabilidad v una partida, ¿qué pasa al jugar muchas? Se esperaba que ganar más del v de las partidas sea exponencialmente raro, pero no estaba demostrado en general.

**Qué resuelve.** Lo demuestra para todo juego de dos jugadores y una ronda.

**Fuera de su área.** Es una herramienta para demostrar seguridad en protocolos cuánticos. Comprobado con Lean.

<a id="r68"></a>
### 68. Un tercer contraejemplo a Kaplansky (294) ✅

**El problema.** Otra conjetura de Kaplansky, esta sobre álgebras de operadores: que ciertas "cuasitrazas" son siempre sumables.

**Qué resuelve.** Construye un álgebra donde ninguna lo es.

**Fuera de su área.** Interés muy especializado. Comprobado con Lean.

<a id="r69"></a>
### 69. Cuándo no hay soluciones positivas en un sistema de ecuaciones (370) ✅

**El problema.** Un sistema de ecuaciones de Lane–Emden, que aparece en astrofísica y en difusión, tiene o no tiene soluciones positivas según los exponentes. Se conjeturaba desde los 90 cuál es la frontera exacta.

**Qué resuelve.** Demuestra la frontera exacta, también en la versión con pesos de Hénon.

**Fuera de su área.** Ecuaciones en derivadas parciales puras. Comprobado con Lean.

<a id="r70"></a>
### 70. Dos conjeturas de recubrimiento refutadas (Ryser) (162) 🟡

**El problema.** La conjetura de Ryser, de los años 70, dice cuántos elementos hacen falta para "tocar" todas las piezas de cierto tipo de estructura. Se sabía para los casos pequeños.

**Qué resuelve.** Construye ejemplos que la incumplen para infinitos tamaños, y refuta también una conjetura parecida de Gyárfás sobre árboles.

**Fuera de su área.** Combinatoria pura. Parte en Lean.

<a id="r71"></a>
### 71. Un operador que no deja ningún subespacio quieto (293) 🟡

**El problema.** En espacios de dimensión infinita, ¿todo operador deja quieto algún subespacio "razonable"? Para el caso más fuerte, los subespacios hiperinvariantes, la pregunta llevaba décadas abierta en los espacios de Hilbert.

**Qué resuelve.** Construye un operador que no deja quieto ninguno.

**Fuera de su área.** Análisis funcional puro. Parte en Lean.

<a id="r72"></a>
### 72. Reconstruir un mensaje a partir de copias con letras borradas (122) ⚪

**El problema.** Te llegan copias de un mensaje en las que cada letra se ha borrado al azar. ¿Cuántas copias necesitas para reconstruirlo? Se usa como modelo en secuenciación de ADN. Se sabía que bastaban exponencialmente muchas y que hacían falta al menos unas pocas; la brecha era enorme.

**Qué resuelve.** Demuestra que hacen falta más que cualquier polinomio de copias, y que con un número "cuasipolinómico" basta. Cierra casi toda la brecha.

**Fuera de su área.** Interesa a la bioinformática teórica. Sin Lean.

<a id="r73"></a>
### 73. Cuándo el transporte óptimo es suave (Villani) (360) ✅

**El problema.** El transporte óptimo estudia cómo mover una pila de arena a otra forma con el mínimo esfuerzo. Se usa en IA y en economía. Villani conjeturó en 2009 qué condición geométrica garantiza que la solución sea suave en una superficie curva.

**Qué resuelve.** Demuestra la conjetura.

**Fuera de su área.** Su uso en IA es a través de teoría, no de código. Comprobado con Lean.

<a id="r74"></a>
### 74. Cuándo aparece algo en un sistema aleatorio (Talagrand) (175) 🟡

**El problema.** Es la versión general del puesto 64: Talagrand conjeturó que dos formas de calcular el "umbral" de aparición de una estructura aleatoria dan casi lo mismo. En 2022 se demostró una parte.

**Qué resuelve.** Demuestra el resto, incluida una conjetura sobre descomponer redes.

**Fuera de su área.** Probabilidad y combinatoria. Parte en Lean.

<a id="r75"></a>
### 75. La mejor constante en una desigualdad de la mecánica cuántica (262) 🟡

**El problema.** Las desigualdades de Lieb–Thirring acotan la energía de un sistema cuántico y son clave para demostrar que la materia es estable. Desde 1976 se buscaba la constante óptima en una dimensión.

**Qué resuelve.** Da la constante exacta en un rango de casos, también para potenciales matriciales.

**Fuera de su área.** Física matemática. Parte en Lean.

<a id="r76"></a>
### 76. Muchos huecos grandes entre primos (026) ⚪

**El problema.** Entre dos primos consecutivos hay un hueco. En promedio mide log p. ¿Cuántos huecos son mucho más grandes que la media? Se sabía que existen; no se sabía si son una proporción positiva.

**Qué resuelve.** Demuestra que, para cualquier múltiplo de la media, una proporción positiva de huecos lo supera.

**Fuera de su área.** Teoría de números. Sin Lean.

<a id="r77"></a>
### 77. Los grados de Turing son rígidos (241) ✅

**El problema.** Los grados de Turing ordenan los problemas por lo difíciles que son de calcular. Desde los años 70 se preguntaba si ese orden tiene "simetrías": formas de reetiquetar los grados sin cambiar el orden.

**Qué resuelve.** Demuestra que no tiene ninguna, salvo la identidad.

**Fuera de su área.** Lógica matemática pura. Comprobado con Lean.

<a id="r78"></a>
### 78. Un grupo hiperbólico que no se ve con lentes finitas (252) ✅

**El problema.** Los grupos hiperbólicos son una familia central de la teoría de grupos. Desde los 80 se preguntaba si todos son "residualmente finitos", es decir, si se pueden estudiar por completo mirando sus versiones finitas.

**Qué resuelve.** Construye uno que no lo es, incluso sin torsión.

**Fuera de su área.** Teoría de grupos. Comprobado con Lean.

<a id="r79"></a>
### 79. Un grupo que reúne tres propiedades que parecían incompatibles (253) ✅

**El problema.** ¿Puede un grupo ser a la vez infinito, simple, descrito con un número finito de reglas, y "promediable"? Era una pregunta abierta desde hacía décadas.

**Qué resuelve.** Construye uno.

**Fuera de su área.** Teoría de grupos. Comprobado con Lean.

<a id="r80"></a>
### 80. Un grupo hiperbólico sin geometría CAT(0) (257) ✅

**El problema.** Se preguntaba si todo grupo hiperbólico actúa de forma natural sobre un espacio de curvatura no positiva (CAT(0)).

**Qué resuelve.** Construye uno que no.

**Fuera de su área.** Teoría de grupos. Comprobado con Lean.

<a id="r81"></a>
### 81. El problema de Tingley (322) ✅

**El problema.** Si una transformación conserva distancias entre los puntos de la superficie de una "bola" en un espacio abstracto, ¿se extiende a todo el espacio de forma lineal? Tingley lo preguntó en 1987 y se había demostrado para muchas familias de espacios.

**Qué resuelve.** Lo demuestra para todos los espacios de Banach reales.

**Fuera de su área.** Análisis funcional. Comprobado con Lean.

<a id="r82"></a>
### 82. Una conjetura de Donaldson en dimensión cuatro (342) ✅

**El problema.** En geometría de cuatro dimensiones hay dos nociones de compatibilidad entre una estructura compleja y una forma simpléctica. Donaldson conjeturó en 2006 que la débil implica la fuerte.

**Qué resuelve.** Lo demuestra.

**Fuera de su área.** Geometría diferencial. Comprobado con Lean.

<a id="r83"></a>
### 83. Zilber–Pink para variedades abelianas (016) ⚪

**El problema.** La conjetura de Zilber–Pink generaliza varios teoremas famosos sobre puntos especiales en geometría aritmética. Es uno de los problemas centrales del área.

**Qué resuelve.** La demuestra para variedades abelianas sobre los racionales y para curvas en el espacio de Siegel de dimensión tres.

**Fuera de su área.** Geometría aritmética muy avanzada. Sin Lean.

<a id="r84"></a>
### 84. En el punto crítico de la percolación no hay un clúster infinito (213) 🟡

**El problema.** La percolación modela cómo se filtra un líquido por un material poroso. Justo en el umbral crítico, ¿hay un camino infinito? Se sabía que no en la cuadrícula plana y en dimensiones altas; Benjamini y Schramm conjeturaron en 1996 que nunca lo hay en redes "simétricas".

**Qué resuelve.** Lo demuestra para toda red cuasi-transitiva.

**Fuera de su área.** Probabilidad y física estadística. Parte en Lean.

<a id="r85"></a>
### 85. La brecha de Laughlin (269) 🟡

**El problema.** El efecto Hall cuántico fraccionario, que dio un Nobel en 1998, se explica con el estado de Laughlin. Que ese estado tenga una "brecha de energía" estable es la base de la explicación, pero no estaba demostrado.

**Qué resuelve.** Lo demuestra en una esfera, y demuestra que la brecha sobrevive a pequeñas impurezas.

**Fuera de su área.** Física matemática. Parte en Lean.

<a id="r86"></a>
### 86. Álgebras cercanas son la misma álgebra (Kadison–Kastler) (289) ⚪

**El problema.** Kadison y Kastler conjeturaron en 1972 que dos álgebras de operadores "muy parecidas" son en realidad la misma, salvo un cambio de coordenadas pequeño.

**Qué resuelve.** Lo demuestra en su forma fuerte, con una tolerancia universal.

**Fuera de su área.** Álgebras de operadores. Sin Lean.

<a id="r87"></a>
### 87. La conjetura de Nagata (039) 🟡

**El problema.** Nagata preguntó en 1959 qué curvas pueden pasar por r puntos del plano con multiplicidades dadas. Lo demostró cuando r es un cuadrado perfecto; el resto seguía abierto.

**Qué resuelve.** La demuestra para todo r ≥ 10.

**Fuera de su área.** Geometría algebraica. Parte en Lean.

<a id="r88"></a>
### 88. Estabilidad de ciertas álgebras bajo simetrías (291) 🟡

**El problema.** En la clasificación de las C*-álgebras hay una propiedad clave, la estabilidad de Jiang–Su. Se preguntaba si se conserva al añadir una simetría de un grupo promediable.

**Qué resuelve.** Lo demuestra sin restricciones sobre las trazas.

**Fuera de su área.** Álgebras de operadores. Parte en Lean.

<a id="r89"></a>
### 89. La conjetura de Goldfeld (006) ⚪

**El problema.** Goldfeld conjeturó en 1979 que, si tomas una curva elíptica y la "retuerces" de todas las maneras posibles, la mitad de las variantes tienen rango 0 y la otra mitad rango 1. Es el análogo estadístico de Birch–Swinnerton-Dyer (puesto 4).

**Qué resuelve.** La demuestra para toda curva elíptica sobre los racionales.

**Fuera de su área.** Teoría de números. Sin Lean.

<a id="r90"></a>
### 90. El problema de los k servidores (110) ⚪

**El problema.** Tienes k técnicos y van llegando avisos en distintos puntos de una ciudad. Debes decidir a quién enviar sin saber los avisos futuros. Es un problema clásico de decisión online (1990). Se conocía una regla con un coste de log³ k veces el óptimo; se buscaba log² k.

**Qué resuelve.** Da una regla con coste log² k, que coincide con el mejor posible.

**Fuera de su área.** Es teoría de algoritmos online; podría inspirar sistemas de despacho. Sin Lean.

<a id="r91"></a>
### 91. El modelo XY y la transición de Kosterlitz–Thouless (216) ⚪

**El problema.** El modelo XY describe imanes planos y superfluidos. La transición de Kosterlitz–Thouless (Nobel 2016) predice un comportamiento muy concreto en el punto crítico, con correcciones logarítmicas que los físicos daban por buenas sin demostración.

**Qué resuelve.** Demuestra esas correcciones y la singularidad esencial de la transición.

**Fuera de su área.** Física matemática. Sin Lean.

<a id="r92"></a>
### 92. La desigualdad de Penrose (260) ⚪

**El problema.** Penrose conjeturó en 1973 que la masa de un sistema con agujeros negros es al menos cierta función del área de sus horizontes. Se demostró en 2001 para el caso "estático". El caso general, con el espacio-tiempo en movimiento, seguía abierto.

**Qué resuelve.** Lo demuestra en toda dimensión bajo hipótesis razonables.

**Fuera de su área.** Relatividad general matemática. Sin Lean.

<a id="r93"></a>
### 93. Condensación de Bose–Einstein con temperatura (267) ⚪

**El problema.** La condensación de Bose–Einstein es un estado de la materia a temperaturas bajísimas, observado en 1995 (Nobel 2001). Que exista matemáticamente en un gas real a temperatura positiva no estaba demostrado.

**Qué resuelve.** Lo demuestra para el gas de esferas duras en tres dimensiones.

**Fuera de su área.** Física matemática. Sin Lean.

<a id="r94"></a>
### 94. Cuándo se puede decidir si dos palabras son iguales (Boone–Higman) (250) 🟡

**El problema.** En un grupo descrito por reglas, ¿se puede decidir con un algoritmo si dos expresiones representan lo mismo? Boone y Higman conjeturaron en 1974 que sí exactamente cuando el grupo "cabe" dentro de un grupo simple con descripción finita.

**Qué resuelve.** Lo demuestra.

**Fuera de su área.** Teoría de grupos y lógica. Parte en Lean.

<a id="r95"></a>
### 95. Correlaciones entre los signos de los números (Chowla) (007) ⚪

**El problema.** La función de Liouville asigna +1 o -1 a cada número según su número de factores primos. Chowla conjeturó en 1965 que esos signos no tienen correlación entre vecinos. En 2015 se demostró en promedio; el caso puntual de dos puntos seguía abierto.

**Qué resuelve.** Demuestra el caso de dos puntos con una cota explícita.

**Fuera de su área.** Teoría de números. Sin Lean.

<a id="r96"></a>
### 96. Los primos no son una suma de dos conjuntos (Ostmann) (013) ⚪

**El problema.** Ostmann conjeturó en 1956 que el conjunto de los primos no se puede escribir como "todas las sumas de un elemento de A y uno de B", ni siquiera cambiando un número finito de primos.

**Qué resuelve.** Lo demuestra.

**Fuera de su área.** Teoría de números. Sin Lean.

<a id="r97"></a>
### 97. Duffin–Schaeffer con desplazamiento (022) ⚪

**El problema.** El teorema de Duffin–Schaeffer, demostrado en 2019, dice con qué precisión se pueden aproximar casi todos los números con fracciones. Quedaba la versión "inhomogénea", con un desplazamiento.

**Qué resuelve.** La demuestra.

**Fuera de su área.** Teoría de números. Sin Lean.

<a id="r98"></a>
### 98. Fracciones egipcias cortas (Erdős) (025) ✅

**El problema.** Los egipcios escribían las fracciones como suma de fracciones con numerador 1: 2/3 = 1/2 + 1/6. ¿Cuántas hacen falta como mínimo para escribir a/b? Erdős conjeturó que muy pocas, del orden de log log b.

**Qué resuelve.** Lo demuestra, y demuestra que no se puede hacer mejor.

**Fuera de su área.** Teoría de números recreativa. Comprobado con Lean.

<a id="r99"></a>
### 99. La conjetura de Stein sobre transformadas de Hilbert (083) ⚪

**El problema.** La transformada de Hilbert es una operación básica del procesamiento de señales. Stein preguntó en los 90 si sigue siendo "controlable" cuando se aplica a lo largo de direcciones que cambian de forma suave.

**Qué resuelve.** Lo demuestra con una cota uniforme.

**Fuera de su área.** Análisis armónico. Sin Lean.

<a id="r100"></a>
### 100. Permanente contra determinante (108) ⚪

**El problema.** El permanente y el determinante son dos fórmulas parecidas para matrices, pero el primero es mucho más difícil de calcular. Una pregunta central de la complejidad algebraica es cuánto más grande tiene que ser una matriz para escribir el permanente como un determinante. Se sabía que al menos n²/2.

**Qué resuelve.** Sube la cota a n³, incluso en la versión "de frontera".

**Fuera de su área.** Es un paso hacia la versión algebraica de P vs NP, pero teórico. Sin Lean.

---

Siguiente tramo: cuando esté escrito, se enlazará desde el [ranking completo](ranking-completo.md).
