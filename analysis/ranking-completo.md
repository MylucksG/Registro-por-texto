# Ranking completo

Las **372 familias de resultados** de [openai/math](https://github.com/openai/math), ordenadas de mayor a menor impacto. Solo el orden: sin explicaciones.

**¿Quieres saber qué resuelve cada uno?** Los 50 primeros tienen ficha, con una versión sencilla y ejemplos, en el [ranking explicado](ranking.md). Del 51 al 100 hay explicaciones cortas en [ranking-51-100.md](ranking-51-100.md). Para el resto, el resumen original en inglés está en [`CONTENTS.md`](../CONTENTS.md) y en `data/catalogue.json`.

**Cómo se ordena.** Los 50 primeros están fijados a mano y coinciden con el ranking explicado. Del 51 en adelante, el orden sale de una puntuación reproducible (`scripts/build_ranking.py`) que combina: si el problema tiene nombre propio reconocible, si está comprobado con Lean, el área (más peso en las que tienen efecto fuera de las matemáticas), si cierra una conjetura y si es algorítmico. Es una opinión del análisis, no de OpenAI. Dos puestos seguidos pueden ser intercambiables.

**Lean:** ✅ toda la familia comprobada por máquina · 🟡 solo una parte · ⚪ no visible en el catálogo. 127 de 372 tienen alguna comprobación.

| # | Descubrimiento | ID | Área | Lean |
|---:|---|:---:|---|:---:|
| 1 | **[Multiplicación de matrices con exponente como máximo 9/4](ranking.md#r1)** | 107 | Informática teórica | ✅ |
| 2 | **[La Conjetura de Unique Games y los umbrales óptimos de aproximación](ranking.md#r2)** | 102 | Informática teórica | 🟡 |
| 3 | **[La hipótesis de quasi-Riemann](ranking.md#r3)** | 003 | Teoría de números | 🟡 |
| 4 | **[La fórmula completa de Birch–Swinnerton-Dyer con corango de Selmer cero y uno](ranking.md#r4)** | 002 | Teoría de números | ⚪ |
| 5 | **[Subset Sum en tiempo O(2^{0,49n})](ranking.md#r5)** | 138 | Informática teórica | ⚪ |
| 6 | **[Multiplicación de enteros por debajo de n log n](ranking.md#r6)** | 109 | Informática teórica | ⚪ |
| 7 | **[Suavidad global para Vlasov–Maxwell relativista](ranking.md#r7)** | 362 | Ecuaciones en derivadas parciales | ✅ |
| 8 | **[La conjetura de la suma de recíprocos de Erdős y cotas cuasipolinómicas de Szemerédi](ranking.md#r8)** | 159 | Combinatoria | ⚪ |
| 9 | **[Emparejamiento exacto en grafos generales en tiempo casi lineal](ranking.md#r9)** | 120 | Informática teórica | ⚪ |
| 10 | **[Kakeya en dimensiones tres y cuatro](ranking.md#r10)** | 074 | Análisis real y complejo | ⚪ |
| 11 | **[El exponente de irracionalidad de π es 2](ranking.md#r11)** | 017 | Teoría de números | ⚪ |
| 12 | **[Factorización polinómica determinista sobre cuerpos primos](ranking.md#r12)** | 142 | Informática teórica | ⚪ |
| 13 | **[Grupos no sofic y contraejemplos en anillos de grupo](ranking.md#r13)** | 197 | Álgebra | 🟡 |
| 14 | **[El plano euclídeo no se puede colorear con cinco colores](ranking.md#r14)** | 158 | Combinatoria | ✅ |
| 15 | **[Cotas uniformes de ciclos límite en el decimosexto problema de Hilbert](ranking.md#r15)** | 143 | Sistemas dinámicos y teoría ergódica | 🟡 |
| 16 | **[El grupo F de Thompson no es promediable](ranking.md#r16)** | 248 | Teoría de grupos | ✅ |
| 17 | **[La conjetura de Cannon](ranking.md#r17)** | 246 | Teoría de grupos | ⚪ |
| 18 | **[La conjetura de distancias de Falconer](ranking.md#r18)** | 073 | Análisis real y complejo | ✅ |
| 19 | **[Todos los factores de grupo libre no abelianos son isomorfos](ranking.md#r19)** | 287 | Álgebras de operadores | ⚪ |
| 20 | **[Computación universal en flujos de Navier–Stokes forzados](ranking.md#r20)** | 376 | Ecuaciones en derivadas parciales | ⚪ |
| 21 | **[El décimo problema de Hilbert sobre ℚ](ranking.md#r21)** | 004 | Teoría de números | ⚪ |
| 22 | **[La conjetura racional de Hodge para variedades abelianas CM y productos de superficies K3](ranking.md#r22)** | 032 | Geometría algebraica y compleja | ⚪ |
| 23 | **[Desaleatorización del espacio logarítmico: L=RL=BPL](ranking.md#r23)** | 103 | Informática teórica | ⚪ |
| 24 | **[Embeddings L₁ de distorsión acotada para grafos planares y de anchura arbórea acotada](ranking.md#r24)** | 089 | Geometría convexa y métrica | ✅ |
| 25 | **[Construcción determinista de árboles delgados fuertes](ranking.md#r25)** | 174 | Combinatoria | 🟡 |
| 26 | **[Desigualdades de profeta para matroides con una muestra frente a un adversario todopoderoso](ranking.md#r26)** | 111 | Informática teórica | ⚪ |
| 27 | **[Algoritmos cuasipolinómicos para juegos de pago medio, estocásticos y de paridad](ranking.md#r27)** | 104 | Informática teórica | 🟡 |
| 28 | **[Dureza de colorear grafos tricoloreables](ranking.md#r28)** | 106 | Informática teórica | ✅ |
| 29 | **[Umbrales de Random-SAT, varianza exacta y computabilidad](ranking.md#r29)** | 235 | Probabilidad y mecánica estadística | ⚪ |
| 30 | **[Conjetura de las raíces primitivas de Artin: infinitud para toda base](ranking.md#r30)** | 029 | Teoría de números | ⚪ |
| 31 | **[Irracionalidad de la constante de Catalan](ranking.md#r31)** | 005 | Teoría de números | ⚪ |
| 32 | **[Las conjeturas de Mahler y el ancho simpléctico](ranking.md#r32)** | 087 | Geometría convexa y métrica | 🟡 |
| 33 | **[La conjetura logarítmica de Brunn–Minkowski](ranking.md#r33)** | 091 | Geometría convexa y métrica | ✅ |
| 34 | **[Optimalidad universal de la red triangular](ranking.md#r34)** | 090 | Geometría convexa y métrica | ⚪ |
| 35 | **[La conjetura de Borsuk falla en dimensión nueve](ranking.md#r35)** | 156 | Combinatoria | ✅ |
| 36 | **[Contraejemplos a las conjeturas de Hadwiger y de Colin de Verdière](ranking.md#r36)** | 157 | Combinatoria | ⚪ |
| 37 | **[La conjetura de Ramsey del hipercubo](ranking.md#r37)** | 171 | Combinatoria | ⚪ |
| 38 | **[La conjetura del segundo vecindario de Seymour](ranking.md#r38)** | 173 | Combinatoria | ✅ |
| 39 | **[La conjetura del ciclo hamiltoniano de Barnette](ranking.md#r39)** | 180 | Combinatoria | ⚪ |
| 40 | **[La ley de Bloch y el orden ferromagnético espontáneo](ranking.md#r40)** | 271 | Física matemática | ⚪ |
| 41 | **[La brecha de Haldane de espín uno](ranking.md#r41)** | 268 | Física matemática | ⚪ |
| 42 | **[Las conjeturas de ionización y de ionización generalizada](ranking.md#r42)** | 263 | Física matemática | 🟡 |
| 43 | **[La fórmula de Mézard–Parisi para vidrios de espín diluidos](ranking.md#r43)** | 221 | Probabilidad y mecánica estadística | ⚪ |
| 44 | **[La conjetura de los puntos calientes para dominios planos simplemente conexos](ranking.md#r44)** | 369 | Ecuaciones en derivadas parciales | ⚪ |
| 45 | **[La conjetura de De Giorgi en dimensión ocho](ranking.md#r45)** | 375 | Ecuaciones en derivadas parciales | ⚪ |
| 46 | **[La conjetura de Birkhoff cerca del borde](ranking.md#r46)** | 147 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 47 | **[Medida de Hausdorff exacta para SLE](ranking.md#r47)** | 230 | Probabilidad y mecánica estadística | ⚪ |
| 48 | **[La conjetura de Hilbert–Smith en toda dimensión](ranking.md#r48)** | 304 | Topología | ⚪ |
| 49 | **[La conjetura de uniformización de Yau](ranking.md#r49)** | 338 | Geometría diferencial | ⚪ |
| 50 | **[La hipótesis de homotopía de Grothendieck](ranking.md#r50)** | 312 | Topología | ✅ |
| | *Del 51 en adelante: orden por puntuación. Del 51 al 100, explicación corta al pulsar el título.* | | | |
| 51 | [Brechas no acotadas en empaquetado y la conjetura de redondeo entero modificada](ranking-51-100.md#r51) | 118 | Informática teórica | ✅ |
| 52 | [La conjetura de los juegos 2 a 1 con completitud perfecta](ranking-51-100.md#r52) | 105 | Informática teórica | ✅ |
| 53 | [Un contraejemplo a la conjetura de sensibilidad cuadrática](ranking-51-100.md#r53) | 132 | Informática teórica | ✅ |
| 54 | [La conjetura de Brennan y un contraejemplo a la predicción de Kraetzer](ranking-51-100.md#r54) | 072 | Análisis real y complejo | ✅ |
| 55 | [La conjetura del foso gaussiano](ranking-51-100.md#r55) | 028 | Teoría de números | ✅ |
| 56 | [Un contraejemplo al teselado periódico en dimensión tres](ranking-51-100.md#r56) | 155 | Combinatoria | ✅ |
| 57 | [Números de van der Waerden superexponenciales](ranking-51-100.md#r57) | 160 | Combinatoria | ✅ |
| 58 | [La conjetura de descomposición en ciclos de Erdős–Gallai](ranking-51-100.md#r58) | 181 | Combinatoria | ✅ |
| 59 | [Corte más disperso uniforme: dureza y brechas semidefinidas](ranking-51-100.md#r59) | 117 | Informática teórica | 🟡 |
| 60 | [El umbral de aproximación para k-medianas métricas](ranking-51-100.md#r60) | 125 | Informática teórica | 🟡 |
| 61 | [Transformadas de Fourier por debajo de n log n](ranking-51-100.md#r61) | 130 | Informática teórica | 🟡 |
| 62 | [Números de cruce exactos de grafos completos y bipartitos completos](ranking-51-100.md#r62) | 165 | Combinatoria | ✅ |
| 63 | [La conjetura de Crouzeix completa](ranking-51-100.md#r63) | 325 | Análisis funcional | ✅ |
| 64 | [La segunda conjetura de Kahn–Kalai](ranking-51-100.md#r64) | 176 | Combinatoria | ✅ |
| 65 | [La conjetura de Hadamard circulante](ranking-51-100.md#r65) | 179 | Combinatoria | ✅ |
| 66 | [Un contraejemplo a la conjetura de divisores de cero de Kaplansky](ranking-51-100.md#r66) | 196 | Álgebra | ✅ |
| 67 | [Repetición de umbral para juegos entrelazados](ranking-51-100.md#r67) | 277 | Física matemática | ✅ |
| 68 | [Un contraejemplo a la conjetura de cuasitrazas de Kaplansky](ranking-51-100.md#r68) | 294 | Álgebras de operadores | ✅ |
| 69 | [Las conjeturas subcríticas de Lane–Emden y Hénon–Lane–Emden](ranking-51-100.md#r69) | 370 | Ecuaciones en derivadas parciales | ✅ |
| 70 | [Contraejemplos a las conjeturas de recubrimiento de Ryser y de recubrimiento por árboles de Gyárfás](ranking-51-100.md#r70) | 162 | Combinatoria | 🟡 |
| 71 | [Un contraejemplo al problema del subespacio hiperinvariante](ranking-51-100.md#r71) | 293 | Álgebras de operadores | 🟡 |
| 72 | [Cotas inferiores superpolinómicas y reconstrucción cuasipolinómica a partir de trazas de borrado](ranking-51-100.md#r72) | 122 | Informática teórica | ⚪ |
| 73 | [La conjetura de convexidad de Villani y el transporte óptimo regular](ranking-51-100.md#r73) | 360 | Geometría diferencial | ✅ |
| 74 | [Las conjeturas de Talagrand y descomposiciones de grafos en umbrales de esperanza](ranking-51-100.md#r74) | 175 | Combinatoria | 🟡 |
| 75 | [Desigualdades exactas de Lieb–Thirring unidimensionales](ranking-51-100.md#r75) | 262 | Física matemática | 🟡 |
| 76 | [Densidad inferior positiva de grandes huecos entre primos](ranking-51-100.md#r76) | 026 | Teoría de números | ⚪ |
| 77 | [Rigidez de los grados de Turing](ranking-51-100.md#r77) | 241 | Lógica matemática | ✅ |
| 78 | [Un grupo hiperbólico sin torsión que no es residualmente finito](ranking-51-100.md#r78) | 252 | Teoría de grupos | ✅ |
| 79 | [Un grupo simple, infinito, finitamente presentado y promediable](ranking-51-100.md#r79) | 253 | Teoría de grupos | ✅ |
| 80 | [Un grupo hiperbólico sin acción CAT(0) geométrica](ranking-51-100.md#r80) | 257 | Teoría de grupos | ✅ |
| 81 | [El problema de la isometría de esferas de Tingley](ranking-51-100.md#r81) | 322 | Análisis funcional | ✅ |
| 82 | [La conjetura de Donaldson de dominado a compatible](ranking-51-100.md#r82) | 342 | Geometría diferencial | ✅ |
| 83 | [Zilber–Pink en variedades abelianas y la variedad tridimensional de Siegel](ranking-51-100.md#r83) | 016 | Teoría de números | ⚪ |
| 84 | [Sin clústeres críticos infinitos en grafos cuasi-transitivos](ranking-51-100.md#r84) | 213 | Probabilidad y mecánica estadística | 🟡 |
| 85 | [La brecha de Laughlin y la estabilidad bajo desorden escalar](ranking-51-100.md#r85) | 269 | Física matemática | 🟡 |
| 86 | [La conjetura fuerte de Kadison–Kastler](ranking-51-100.md#r86) | 289 | Álgebras de operadores | ⚪ |
| 87 | [La conjetura de Nagata y las constantes de Seshadri máximas](ranking-51-100.md#r87) | 039 | Geometría algebraica y compleja | 🟡 |
| 88 | [Toms–Winter y la estabilidad equivariante de Jiang–Su](ranking-51-100.md#r88) | 291 | Álgebras de operadores | 🟡 |
| 89 | [Conjetura de Goldfeld](ranking-51-100.md#r89) | 006 | Teoría de números | ⚪ |
| 90 | [k-server aleatorizado de orden óptimo en métricas arbitrarias](ranking-51-100.md#r90) | 110 | Informática teórica | ⚪ |
| 91 | [Correcciones logarítmicas críticas y escalado BKT para el modelo XY plano](ranking-51-100.md#r91) | 216 | Probabilidad y mecánica estadística | ⚪ |
| 92 | [Desigualdades de Penrose espaciotemporales y rigidez](ranking-51-100.md#r92) | 260 | Física matemática | ⚪ |
| 93 | [Condensación de Bose–Einstein a temperatura positiva y depleción cuántica](ranking-51-100.md#r93) | 267 | Física matemática | ⚪ |
| 94 | [La conjetura de Boone–Higman y la finitud superior](ranking-51-100.md#r94) | 250 | Teoría de grupos | 🟡 |
| 95 | [Chowla de dos puntos y la conjetura de Elliott binaria corregida](ranking-51-100.md#r95) | 007 | Teoría de números | ⚪ |
| 96 | [La conjetura inversa de Goldbach de Ostmann](ranking-51-100.md#r96) | 013 | Teoría de números | ⚪ |
| 97 | [La conjetura débil inhomogénea de Duffin–Schaeffer](ranking-51-100.md#r97) | 022 | Teoría de números | ⚪ |
| 98 | [La conjetura de las fracciones egipcias cortas de Erdős](ranking-51-100.md#r98) | 025 | Teoría de números | ✅ |
| 99 | [La conjetura de Stein para transformadas de Hilbert a lo largo de direcciones lipschitzianas](ranking-51-100.md#r99) | 083 | Análisis real y complejo | ⚪ |
| 100 | [Una cota inferior cúbica permanente–determinante](ranking-51-100.md#r100) | 108 | Informática teórica | ⚪ |
| 101 | Aproximación de la distancia de edición en tiempo esperado casi lineal | 121 | Informática teórica | ⚪ |
| 102 | Una aproximación de factor dos para la supercadena común más corta | 128 | Informática teórica | ✅ |
| 103 | La conjetura cuasilineal de PCP para PPAD | 136 | Informática teórica | ⚪ |
| 104 | La teoría existencial de los reales y las sentencias existenciales–universales en la jerarquía de conteo | 141 | Informática teórica | ⚪ |
| 105 | Contraejemplos a la conjetura de Sidorenko y a la conjetura de forzamiento | 161 | Combinatoria | ⚪ |
| 106 | La conjetura de distancias distintas de Erdős en dimensiones superiores | 166 | Combinatoria | ⚪ |
| 107 | Grafos de Ramanujan no bipartitos deterministas en todo grado fijo | 178 | Combinatoria | ⚪ |
| 108 | Una mejora potencial en el problema del triángulo de Heilbronn | 191 | Combinatoria | ⚪ |
| 109 | Entrelazamiento sin clave secreta y la conjetura PPT-cuadrado | 272 | Física matemática | ⚪ |
| 110 | El exponente de consultas aleatorizado–cuántico óptimo | 284 | Física matemática | ⚪ |
| 111 | La conjetura del recubrimiento universal de Kollár–Pardon | 058 | Geometría algebraica y compleja | 🟡 |
| 112 | La conjetura de categoricidad eventual de Shelah | 240 | Lógica matemática | 🟡 |
| 113 | La conjetura del bicentralizador de Connes y bicentralizadores relativos | 290 | Álgebras de operadores | 🟡 |
| 114 | La distorsión exacta de la distancia de edición en ℓ₁ | 099 | Geometría convexa y métrica | ⚪ |
| 115 | Umbrales exactos de reconstrucción de tres y cuatro estados | 229 | Probabilidad y mecánica estadística | ⚪ |
| 116 | Censura cósmica fuerte cerca de datos de Kerr de dos extremos | 264 | Física matemática | ⚪ |
| 117 | Contraejemplos a Baum–Connes y a Kadison–Kaplansky | 285 | Álgebras de operadores | ⚪ |
| 118 | La conjetura de dominios circulares de Koebe y la rigidez de dominios circulares | 071 | Análisis real y complejo | ⚪ |
| 119 | Restricción de Fourier para superficies de curvatura positiva | 077 | Análisis real y complejo | ⚪ |
| 120 | El extremo de Sobolev en el problema de convergencia de Schrödinger de Carleson | 080 | Análisis real y complejo | ⚪ |
| 121 | La conjetura de proyección-volumen de Petty y contraejemplos simpliciales | 088 | Geometría convexa y métrica | ✅ |
| 122 | Costes de estados exponenciales para autómatas bidireccionales | 129 | Informática teórica | ✅ |
| 123 | Exponentes logarítmicos exactos para números de Ramsey fuera de la diagonal | 170 | Combinatoria | ⚪ |
| 124 | La ley de fluctuaciones a baja temperatura de Sherrington–Kirkpatrick | 217 | Probabilidad y mecánica estadística | ⚪ |
| 125 | Universalidad GOE para grafos regulares aleatorios con desorden débil | 219 | Probabilidad y mecánica estadística | ⚪ |
| 126 | Localización y deslocalización en el modelo de Anderson | 261 | Física matemática | ⚪ |
| 127 | La ley del área con brecha en dos dimensiones | 265 | Física matemática | ⚪ |
| 128 | Exactamente tres bases mutuamente insesgadas en dimensión seis | 266 | Física matemática | ⚪ |
| 129 | Optimalidad de QAOA para el modelo SK | 281 | Física matemática | ⚪ |
| 130 | No unicidad de Boltzmann con conservación local exacta | 363 | Ecuaciones en derivadas parciales | ⚪ |
| 131 | El problema de aproximación de Ball–Evans tridimensional | 368 | Ecuaciones en derivadas parciales | ⚪ |
| 132 | Terminación de los programas de modelo mínimo en dimensión cuatro | 056 | Geometría algebraica y compleja | ⚪ |
| 133 | La conjetura de Deligne–Drinfeld | 008 | Teoría de números | ✅ |
| 134 | Cuárticas libres de cuadrados y valores de polinomios libres de potencias | 020 | Teoría de números | ✅ |
| 135 | Una cota cuadrática para la función de Jacobsthal | 021 | Teoría de números | ✅ |
| 136 | La conjetura de Bochner–Riesz tridimensional | 078 | Análisis real y complejo | ⚪ |
| 137 | La conjetura de suavizado local de Sogge en dimensión tres | 079 | Análisis real y complejo | ⚪ |
| 138 | Desigualdad logarítmica de Sobolev libre de dimensión para medidas log-cóncavas subgaussianas | 093 | Geometría convexa y métrica | ⚪ |
| 139 | La conjetura de la hélice gaussiana | 096 | Geometría convexa y métrica | ✅ |
| 140 | La conjetura del símplex exacta para constantes isótropas | 101 | Geometría convexa y métrica | ⚪ |
| 141 | Más allá del exponente de raíz cuadrada para circuitos de profundidad tres | 112 | Informática teórica | ✅ |
| 142 | La conjetura asintótica de Gotsman–Linial | 127 | Informática teórica | ✅ |
| 143 | Consultas subpolinómicas para muestreo log-cóncavo | 139 | Informática teórica | ✅ |
| 144 | La conjetura de sumas y productos finitos de Hindman | 164 | Combinatoria | ⚪ |
| 145 | Invariancia combinatoria de los polinomios de Kazhdan–Lusztig | 168 | Combinatoria | ⚪ |
| 146 | Clasificación de las configuraciones finitas de Ramsey euclidianas | 172 | Combinatoria | ✅ |
| 147 | La conjetura de multiplicidad de Lech | 194 | Álgebra | ⚪ |
| 148 | Un contraejemplo al problema de los anillos de división de Kurosh | 201 | Álgebra | ⚪ |
| 149 | La conjetura de no unicidad de Benjamini–Schramm | 214 | Probabilidad y mecánica estadística | ⚪ |
| 150 | La conjetura CLE₄ del doble dímero en el semiplano | 226 | Probabilidad y mecánica estadística | ⚪ |
| 151 | La conjetura de similitud de Kadison | 288 | Álgebras de operadores | ⚪ |
| 152 | Un contraejemplo al problema de inmersión de ultrapotencia de norma de Kirchberg | 292 | Álgebras de operadores | ⚪ |
| 153 | Un contraejemplo en ZFC al problema de Naimark | 297 | Álgebras de operadores | ⚪ |
| 154 | Un contraejemplo a la conjetura de igualdad de entropía libre de Voiculescu | 298 | Álgebras de operadores | ⚪ |
| 155 | Un contraejemplo cuatridimensional a la rigidez de Borel | 320 | Topología | ⚪ |
| 156 | Un contraejemplo a la conjetura D(2) finita de Wall | 321 | Topología | ⚪ |
| 157 | Independencia relativa del problema del cociente separable | 323 | Análisis funcional | ⚪ |
| 158 | Un contraejemplo a la conjetura lagrangiana cercana | 340 | Geometría diferencial | ⚪ |
| 159 | Singularidad en tiempo finito del flujo de Calabi | 352 | Geometría diferencial | ⚪ |
| 160 | La conjetura de regularidad de Mumford–Shah plana | 366 | Ecuaciones en derivadas parciales | ⚪ |
| 161 | Explosión estable para una ecuación de Schrödinger desenfocante | 371 | Ecuaciones en derivadas parciales | ⚪ |
| 162 | Regularidad interior C^{1,α} para funciones infinito-armónicas | 377 | Ecuaciones en derivadas parciales | ⚪ |
| 163 | Contraejemplos a las conjeturas de Auslander–Reiten, Tachikawa y Nakayama | 199 | Álgebra | ✅ |
| 164 | La conjetura de Donovan sobre cuerpos y anillos de valoración discreta | 203 | Álgebra | ⚪ |
| 165 | Transiciones de fase continuas para potenciales radiales de pares | 228 | Probabilidad y mecánica estadística | ✅ |
| 166 | La conjetura de Howie sobre ecuaciones sobre grupos | 256 | Teoría de grupos | ⚪ |
| 167 | La conjetura de Gersten para grupos de una relación | 258 | Teoría de grupos | ⚪ |
| 168 | La conjetura de paridad de Moore para QAC⁰ | 274 | Física matemática | ✅ |
| 169 | La desigualdad integral de curvatura escalar de Gromov | 335 | Geometría diferencial | ⚪ |
| 170 | Polinomios de Littlewood reales ultraplanos | 076 | Análisis real y complejo | 🟡 |
| 171 | Cotas maximales y variacionales para la transformada de Hilbert triangular | 082 | Análisis real y complejo | 🟡 |
| 172 | Conos de hiperbolicidad sin levantamientos semidefinidos | 095 | Geometría convexa y métrica | 🟡 |
| 173 | Prueba de identidad uniforme para fórmulas no conmutativas | 116 | Informática teórica | 🟡 |
| 174 | La conjetura de libertad de Fujita | 038 | Geometría algebraica y compleja | ⚪ |
| 175 | La conjetura de Bloch para superficies complejas | 040 | Geometría algebraica y compleja | ⚪ |
| 176 | P=W para espacios de moduli de determinante fijo | 043 | Geometría algebraica y compleja | ⚪ |
| 177 | Un contraejemplo a la conjetura de positividad de Griffiths | 050 | Geometría algebraica y compleja | ✅ |
| 178 | El problema de la transformada de Riesz de David–Semmes en codimensión mayor | 081 | Análisis real y complejo | ✅ |
| 179 | Regularidad en el extremo de la función maximal centrada plana | 085 | Análisis real y complejo | ✅ |
| 180 | Reducción de dimensión subpolinómica en L_p | 094 | Geometría convexa y métrica | ✅ |
| 181 | La conjetura euclídea de Steinitz–Bergström | 097 | Geometría convexa y métrica | ✅ |
| 182 | La conjetura de entropía positiva de Sinai para la aplicación estándar | 146 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 183 | Clasificación aritmética de las convoluciones de Bernoulli | 153 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 184 | La conjetura de multiplicidad de intersección de Serre | 193 | Álgebra | ⚪ |
| 185 | La conjetura de peso de Alperin por bloques | 202 | Álgebra | ⚪ |
| 186 | Un grupo sin precio fijo | 259 | Teoría de grupos | ⚪ |
| 187 | La capacidad clásica de la amortiguación de amplitud generalizada | 276 | Física matemática | ✅ |
| 188 | La conjetura de cirugía puramente cosmética para nudos en S³ | 306 | Topología | ⚪ |
| 189 | El problema del invariante de Kervaire en el primo tres | 309 | Topología | ⚪ |
| 190 | La conjetura de Singer en dimensión cuatro | 315 | Topología | ⚪ |
| 191 | La conjetura de rigidez de entropía de Katok | 339 | Geometría diferencial | ⚪ |
| 192 | La conjetura de deformación hipersimpléctica de Donaldson | 341 | Geometría diferencial | ⚪ |
| 193 | La conjetura métrica de Blaschke | 344 | Geometría diferencial | ⚪ |
| 194 | Infinitas geodésicas cerradas en esferas y variedades de dimensión tres | 345 | Geometría diferencial | ⚪ |
| 195 | Conteo aproximado y la conjetura de entropía de emparejamientos perfectos | 113 | Informática teórica | 🟡 |
| 196 | Conteo aproximado de bases comunes de polimatroides enteros | 114 | Informática teórica | 🟡 |
| 197 | Las conjeturas de Courtade–Kumar y de Hellinger | 119 | Informática teórica | 🟡 |
| 198 | Distancias ancladas y una mejora potencial para las distancias unitarias planas | 167 | Combinatoria | 🟡 |
| 199 | Coloración e independencia en grafos con subgrafos prohibidos | 184 | Combinatoria | 🟡 |
| 200 | Límites continuos masivos y asintótica exacta de la masa para modelos O(n) planos | 215 | Probabilidad y mecánica estadística | 🟡 |
| 201 | La transición de fase dinámica en el modelo de Sherrington–Kirkpatrick | 227 | Probabilidad y mecánica estadística | 🟡 |
| 202 | Mezcla logarítmica óptima de la barajada de Thorp | 238 | Probabilidad y mecánica estadística | 🟡 |
| 203 | Equivalencia lipschitziana sin isomorfismo lineal | 324 | Análisis funcional | ✅ |
| 204 | Langlands geométrico restringido, Ramanujan genérico y parámetros de Arthur | 014 | Teoría de números | ⚪ |
| 205 | Leyes cero–uno direccionales y balisticidad en entornos aleatorios | 220 | Probabilidad y mecánica estadística | 🟡 |
| 206 | Mayores factores primos independientes de enteros consecutivos | 012 | Teoría de números | ⚪ |
| 207 | Una fórmula asintótica para el número de totientes | 024 | Teoría de números | ⚪ |
| 208 | Una respuesta negativa al problema de Lang–Plaut | 098 | Geometría convexa y métrica | ✅ |
| 209 | Planificación en tiempo polinómico en tres máquinas idénticas | 124 | Informática teórica | ⚪ |
| 210 | La fórmula de dimensión para medidas autosimilares en la recta | 148 | Sistemas dinámicos y teoría ergódica | ✅ |
| 211 | Contraejemplos a la intersección de matroides infinitos y al empaquetado/recubrimiento | 185 | Combinatoria | ✅ |
| 212 | La eliminación polinómica falla para matrices binarias ordenadas | 190 | Combinatoria | ✅ |
| 213 | El principio de partición no implica elección | 244 | Lógica matemática | ✅ |
| 214 | El problema del generador para factores finitos | 296 | Álgebras de operadores | ✅ |
| 215 | El tipo de Markov caracteriza la superreflexividad | 327 | Análisis funcional | ✅ |
| 216 | Puntos fijos de aplicaciones no expansivas en espacios de Banach reflexivos | 328 | Análisis funcional | ✅ |
| 217 | La complejidad del refinamiento de Weisfeiler–Leman | 133 | Informática teórica | ⚪ |
| 218 | El orden óptimo de la densidad de recubrimiento por cuerpos convexos | 092 | Geometría convexa y métrica | 🟡 |
| 219 | Sin bigeodésicas y formas límite suaves en la percolación de primer paso plana | 212 | Probabilidad y mecánica estadística | 🟡 |
| 220 | El conteo sin elección no captura el tiempo polinómico | 243 | Lógica matemática | 🟡 |
| 221 | Promediabilidad, unitarizabilidad y estabilidad de Ulam | 251 | Teoría de grupos | 🟡 |
| 222 | Cotas inferiores de memoria–muestras para regresión gaussiana sin ruido | 140 | Informática teórica | 🟡 |
| 223 | Bogomolov–Pop y reconstrucción K-teórica de Milnor | 009 | Teoría de números | ⚪ |
| 224 | Modularidad de Fontaine–Mazur en el primo 2 y pro-modularidad 2-ádica | 010 | Teoría de números | ⚪ |
| 225 | La conjetura de Ford–Konyagin–Luca sobre predecesores primos | 011 | Teoría de números | ⚪ |
| 226 | Equidistribución de paquetes de toros en grados primo, cuártico y séxtico | 015 | Teoría de números | ⚪ |
| 227 | La conjetura de Margulis–Platonov sobre cuerpos globales | 018 | Teoría de números | ⚪ |
| 228 | La conjetura de la sección p-ádica | 019 | Teoría de números | ⚪ |
| 229 | El caso geométrico de la conjetura de similitud de Erdős | 084 | Análisis real y complejo | ⚪ |
| 230 | Muestreo y conteo de tablas de contingencia con márgenes arbitrarios | 115 | Informática teórica | ⚪ |
| 231 | QMA-dureza de la energía de Coulomb en el continuo | 275 | Física matemática | ⚪ |
| 232 | Geometría, difusión y espectros de mapas planos aleatorios | 211 | Probabilidad y mecánica estadística | ⚪ |
| 233 | Universalidad conforme para modelos de Ising débilmente interactuantes y desordenados | 218 | Probabilidad y mecánica estadística | ⚪ |
| 234 | Límites conformes de interfaces de clúster aleatorio en la red cuadrada | 223 | Probabilidad y mecánica estadística | ⚪ |
| 235 | Convexidad uniforme de punto medio asintótica sin renormamiento asintóticamente uniformemente convexo | 331 | Análisis funcional | ✅ |
| 236 | Conjetura de racionalidad de Milne | 001 | Teoría de números | ⚪ |
| 237 | El primer momento de Patterson para sumas de Gauss cúbicas | 023 | Teoría de números | ⚪ |
| 238 | Densidad entera en variedades de caracteres de curvas | 027 | Teoría de números | ⚪ |
| 239 | Modularidad sobre cuerpos cuadráticos imaginarios | 030 | Teoría de números | ⚪ |
| 240 | La conjetura de Uchida para homomorfismos de Galois abiertos | 031 | Teoría de números | ⚪ |
| 241 | Contraejemplos complejos a la cancelación y a las fibraciones afines | 047 | Geometría algebraica y compleja | ✅ |
| 242 | Una cota L³ para la transformada de Hilbert trilineal | 086 | Análisis real y complejo | ⚪ |
| 243 | Complejidad semidefinida exponencial del emparejamiento perfecto | 126 | Informática teórica | ⚪ |
| 244 | Simulación de tiempo de una cinta en espacio de potencia dos quintos | 137 | Informática teórica | ⚪ |
| 245 | Números de Ramsey exactos ciclo–clique | 189 | Combinatoria | ⚪ |
| 246 | Un contraejemplo a la conjetura de la pequeña dimensión finitística | 198 | Álgebra | ✅ |
| 247 | El umbral de factor de IID para estados libres de Ising en árboles | 236 | Probabilidad y mecánica estadística | ✅ |
| 248 | Factorización cuántica exacta sobre un conjunto finito fijo de puertas | 279 | Física matemática | ⚪ |
| 249 | Síntesis unitaria de error constante en tiempo polinómico a partir de un oráculo booleano | 283 | Física matemática | ⚪ |
| 250 | Un contraejemplo a la conjetura de dualidad de entropía métrica de Pietsch | 329 | Análisis funcional | ✅ |
| 251 | Energías libres del perceptrón y atasco microscópico | 222 | Probabilidad y mecánica estadística | ⚪ |
| 252 | Escisiones del fibrado tangente y recubrimientos universales | 052 | Geometría algebraica y compleja | 🟡 |
| 253 | La conjetura de Saxl y los cuadrados tensoriales universales | 205 | Álgebra | 🟡 |
| 254 | Las conjeturas ℓ¹-Bass y de traza de Bass compleja | 207 | Álgebra | 🟡 |
| 255 | Contraejemplos a formas fuertes de la conjetura del punto fijo de Arnold | 347 | Geometría diferencial | 🟡 |
| 256 | Mejoras potenciales para conjuntos sin diferencias polinómicas | 182 | Combinatoria | ⚪ |
| 257 | Universalidad crítica y casi crítica para la percolación de Voronoi | 224 | Probabilidad y mecánica estadística | ⚪ |
| 258 | Contraejemplos al encaje de discos y a la conjetura de variedades de Wall | 305 | Topología | ⚪ |
| 259 | La curvatura escalar detecta singularidades del flujo de Ricci en dimensión cuatro | 351 | Geometría diferencial | ⚪ |
| 260 | Las conjeturas de umbral de grafos e hipergrafos de Friedgut–Kalai | 186 | Combinatoria | ⚪ |
| 261 | Estados ligados de umbral y de energía positiva del modelo BFSS | 270 | Física matemática | ⚪ |
| 262 | Límites cinéticos y fluctuaciones durante la vida útil de Boltzmann | 364 | Ecuaciones en derivadas parciales | ⚪ |
| 263 | La conjetura de Iitaka orbifold de Campana y la subaditividad logarítmica | 033 | Geometría algebraica y compleja | ⚪ |
| 264 | Log abundancia y fibraciones de Iitaka efectivas | 034 | Geometría algebraica y compleja | ⚪ |
| 265 | Recuperación conjunta de la métrica y la conexión a partir de un parche de frontera | 365 | Ecuaciones en derivadas parciales | 🟡 |
| 266 | La conjetura nodal de Yau: superficies y contraejemplos | 350 | Geometría diferencial | 🟡 |
| 267 | La conjetura de convergencia de Fourier L log L | 075 | Análisis real y complejo | ⚪ |
| 268 | Mezcla polinómica de intercambios de grafos con grados prescritos | 131 | Informática teórica | ⚪ |
| 269 | La conjetura de e-positividad de Shareshian–Wachs | 169 | Combinatoria | ⚪ |
| 270 | Expansores de cofrontera de grado acotado en toda dimensión | 177 | Combinatoria | ⚪ |
| 271 | Mejoras potenciales para rectas bisectoras planas y k-conjuntos | 183 | Combinatoria | ⚪ |
| 272 | La constante exacta en la eliminación aleatoria de triángulos | 188 | Combinatoria | ⚪ |
| 273 | Un contraejemplo a la conjetura del módulo de Cohen–Macaulay pequeño | 195 | Álgebra | ⚪ |
| 274 | El bosque aleatorio libre generador es un factor de IID | 231 | Probabilidad y mecánica estadística | ⚪ |
| 275 | El límite de escala crítico conjunto de Ashkin–Teller | 233 | Probabilidad y mecánica estadística | ⚪ |
| 276 | Presión a toda temperatura para vidrios de espín de Ising ortogonalmente invariantes | 234 | Probabilidad y mecánica estadística | ⚪ |
| 277 | Representaciones diofánticas de un solo pliegue | 242 | Lógica matemática | ✅ |
| 278 | Un contraejemplo finitamente generado a Eilenberg–Ganea | 249 | Teoría de grupos | ⚪ |
| 279 | La desigualdad de entropía del número de fotones | 273 | Física matemática | ⚪ |
| 280 | El criterio de caracteres de Kirchberg–Rørdam | 299 | Álgebras de operadores | ✅ |
| 281 | La conjetura cotipo–cotipo bajo la propiedad de aproximación | 326 | Análisis funcional | ✅ |
| 282 | Una métrica de superficie suave sin inmersión local en ℝ³ | 334 | Geometría diferencial | ✅ |
| 283 | Una 3-variedad sin puntos conjugados y sin métrica de curvatura no positiva | 358 | Geometría diferencial | ✅ |
| 284 | Semiamplitud numérica y modelos mínimos generalizados | 036 | Geometría algebraica y compleja | ⚪ |
| 285 | Un contraejemplo a la cota de Bang para el recubrimiento con cilindros | 100 | Geometría convexa y métrica | ⚪ |
| 286 | Un contraejemplo de coordenadas estables en cuatro variables | 049 | Geometría algebraica y compleja | 🟡 |
| 287 | Curvatura de Kähler negativa sin coordenadas holomorfas acotadas | 359 | Geometría diferencial | 🟡 |
| 288 | Contraejemplos a la cota de dimensión armónica de Yau | 361 | Geometría diferencial | 🟡 |
| 289 | La conjetura de abelianidad de Campana y las variedades especiales | 057 | Geometría algebraica y compleja | ⚪ |
| 290 | Altura de estrella generalizada como máximo tres | 134 | Informática teórica | ⚪ |
| 291 | Variedades de Einstein de dimensión cuatro de curvatura no negativa y una brecha topológica | 348 | Geometría diferencial | ⚪ |
| 292 | Log abundancia de variedades de dimensión tres con dimensión numérica uno en característica p>3 | 035 | Geometría algebraica y compleja | ⚪ |
| 293 | La brecha de volumen exacta de puntos dobles ordinarios | 037 | Geometría algebraica y compleja | ⚪ |
| 294 | SYZ hiperkähler y bases de espacio proyectivo | 041 | Geometría algebraica y compleja | ⚪ |
| 295 | La conjetura de Gepner de Toda y la estabilidad de volumen grande | 055 | Geometría algebraica y compleja | ⚪ |
| 296 | Restricciones de Virasoro para intersecciones completas y fibrados proyectivos | 065 | Geometría algebraica y compleja | ⚪ |
| 297 | Complementos klt acotados para contracciones de Fano | 066 | Geometría algebraica y compleja | ⚪ |
| 298 | Mezcla débil de billares triangulares irracionales | 150 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 299 | Representación de retículos finitos: contraejemplos e indecidibilidad | 206 | Álgebra | ⚪ |
| 300 | Rigidez aritmética de las álgebras de von Neumann de retículos | 286 | Álgebras de operadores | ⚪ |
| 301 | La conjetura de paving fuerte-operador cuadrático de Popa–Vaes | 300 | Álgebras de operadores | ⚪ |
| 302 | Isoperimetría de Cartan–Hadamard y rellenos CAT(0) | 337 | Geometría diferencial | ⚪ |
| 303 | El exponente de diámetro de tres cuartos para caminatas en panal | 237 | Probabilidad y mecánica estadística | ⚪ |
| 304 | División cromática: contraejemplos y filtraciones | 318 | Topología | ⚪ |
| 305 | Espacios clasificantes y obstrucciones geométricas para grupos de Artin | 254 | Teoría de grupos | 🟡 |
| 306 | Clasificación de Oka para superficies K3 y otras superficies complejas compactas | 042 | Geometría algebraica y compleja | ⚪ |
| 307 | La conjetura de Hikita cohomológica equivariante para carcajs | 044 | Geometría algebraica y compleja | ⚪ |
| 308 | La conjetura de amplitud canónica de Kobayashi | 051 | Geometría algebraica y compleja | ⚪ |
| 309 | La conjetura de la Cáscara Esférica Global | 060 | Geometría algebraica y compleja | ⚪ |
| 310 | La conjetura de LeBrun–Salamon y la clasificación proyectiva de contacto | 062 | Geometría algebraica y compleja | ⚪ |
| 311 | La conjetura de Mukai generalizada | 063 | Geometría algebraica y compleja | ⚪ |
| 312 | La conjetura de Campana–Peternell en dimensión seis | 067 | Geometría algebraica y compleja | ⚪ |
| 313 | Langlands geométrico cuántico a nivel irracional | 069 | Geometría algebraica y compleja | ⚪ |
| 314 | El problema del espectro de Lebesgue simple de Banach | 144 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 315 | El problema de mezcla múltiple de Rokhlin | 145 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 316 | Rigidez cuasi-isométrica de grupos virtualmente policíclicos | 255 | Teoría de grupos | ⚪ |
| 317 | La conjetura de cohomología de Kadison–Ringrose | 295 | Álgebras de operadores | ⚪ |
| 318 | La conjetura de Quillen en homología racional | 310 | Topología | ⚪ |
| 319 | La conjetura de volumen mínimo de Solomon–Yau | 349 | Geometría diferencial | ⚪ |
| 320 | Complejidad homogénea exacta de profundidad cinco de productos de matrices | 135 | Informática teórica | ⚪ |
| 321 | Un contraejemplo a la conjetura de Gopalan–Servedio | 192 | Combinatoria | ⚪ |
| 322 | Fallo de la representación de conjunto de Kohn–Sham | 278 | Física matemática | ⚪ |
| 323 | Estabilidad exacta de un tercio de los mapas de transporte óptimo | 374 | Ecuaciones en derivadas parciales | ⚪ |
| 324 | La conjetura de Foulkes para sextas potencias y la estabilización cuadrática | 210 | Álgebra | 🟡 |
| 325 | La caracterización de Gigli de la curvatura de Alexandrov | 356 | Geometría diferencial | 🟡 |
| 326 | Campos gaussianos e interfaces SLE para alturas lipschitzianas | 232 | Probabilidad y mecánica estadística | ⚪ |
| 327 | Contraejemplos a la convexidad holomorfa de Shafarevich | 046 | Geometría algebraica y compleja | ⚪ |
| 328 | Contraejemplos a la conjetura de multiplicidad de Zariski | 059 | Geometría algebraica y compleja | ⚪ |
| 329 | Eisenbud–Green–Harris y lex-plus-potencias en característica cero | 200 | Álgebra | ⚪ |
| 330 | Contraejemplos enteros a la conjetura de Gersten | 209 | Álgebra | ⚪ |
| 331 | Tasas de singularidad exactas para matrices de signos simétricas | 239 | Probabilidad y mecánica estadística | ⚪ |
| 332 | Fallo de la inyectividad racional del ensamblaje grueso máximo | 307 | Topología | ⚪ |
| 333 | No anulación anticanónica bajo semipositividad suave | 068 | Geometría algebraica y compleja | ⚪ |
| 334 | Un contraejemplo en característica cero a Lipman–Zariski | 048 | Geometría algebraica y compleja | ⚪ |
| 335 | Un contraejemplo a la conjetura de completitud original de Pixton | 053 | Geometría algebraica y compleja | ⚪ |
| 336 | Contraejemplos a la conjetura de racionalidad de Kuznetsov | 054 | Geometría algebraica y compleja | ⚪ |
| 337 | Un contraejemplo C¹ a la conjetura de entropía de Shub | 151 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 338 | Contraejemplos a la conjetura de Hahn–Wilson en altura dos | 319 | Topología | ⚪ |
| 339 | Cotipo de Markov métrico dos para ℓ₁ | 332 | Análisis funcional | ⚪ |
| 340 | Snaky en 21 jugadas de Maker | 187 | Combinatoria | ⚪ |
| 341 | Límites del campo libre gaussiano para el modelo de seis vértices balanceado | 225 | Probabilidad y mecánica estadística | ⚪ |
| 342 | Localidad fuerte para álgebras de operadores de vértice unitarias fuertemente racionales | 280 | Física matemática | ⚪ |
| 343 | Mejora de escala a conforme en teoría cuántica de campos de cuatro dimensiones | 282 | Física matemática | ⚪ |
| 344 | La dimensión crítica del problema de Bernoulli de una fase | 367 | Ecuaciones en derivadas parciales | ⚪ |
| 345 | Unicidad global en elasticidad isótropa suave | 372 | Ecuaciones en derivadas parciales | ⚪ |
| 346 | No alcance en el transporte de Coulomb de tres marginales | 373 | Ecuaciones en derivadas parciales | ⚪ |
| 347 | Promedios ergódicos múltiples puntuales para transformaciones mezclantes | 154 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 348 | Curvatura escalar espectral y anchura de codimensión dos | 336 | Geometría diferencial | ⚪ |
| 349 | Permanencia para redes de reacción débilmente reversibles | 149 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 350 | Un 2-grupo infinito, finitamente presentado y residualmente finito | 247 | Teoría de grupos | ⚪ |
| 351 | La fórmula de Phillips–Toms para acciones enteras mínimas | 302 | Álgebras de operadores | ⚪ |
| 352 | Complejos de Smith–Toda a toda altura con primos variables | 308 | Topología | ⚪ |
| 353 | Cotas exactas del conjunto singular para varifolds enteros estacionarios | 346 | Geometría diferencial | ⚪ |
| 354 | El umbral de dimensión exacto para la rigidez afín de Bernstein | 353 | Geometría diferencial | ⚪ |
| 355 | El problema de la constante μ para singularidades de superficies | 064 | Geometría algebraica y compleja | ⚪ |
| 356 | Entropía cero no garantiza un modelo suave de volumen positivo | 152 | Sistemas dinámicos y teoría ergódica | ⚪ |
| 357 | Saturación tensorial para grupos spin pares | 204 | Álgebra | ⚪ |
| 358 | La conjetura finita de Benson–Etingof–Ostrik | 208 | Álgebra | ⚪ |
| 359 | La conjetura β de Barendregt–Geuvers–Klop | 245 | Lógica matemática | ⚪ |
| 360 | Clasificación por conos de traza tras la estabilización de Razak–Jacelon | 301 | Álgebras de operadores | ⚪ |
| 361 | De la pura infinitud ordinaria a la fuerte | 303 | Álgebras de operadores | ⚪ |
| 362 | La conjetura del ideal invariante de Chai | 311 | Topología | ⚪ |
| 363 | Generación finita para la esfera K(n)-local | 313 | Topología | ⚪ |
| 364 | El problema cromático del punto fijo de Smith para p-grupos finitos | 314 | Topología | ⚪ |
| 365 | La conjetura de Curtis | 316 | Topología | ⚪ |
| 366 | Estructuras de modelo de Thomason en toda dimensión superior estricta | 317 | Topología | ⚪ |
| 367 | Una respuesta negativa a la pregunta de aproximación Lipschitz-libre de Kalton | 330 | Análisis funcional | ⚪ |
| 368 | Inmersiones isométricas suaves de superficies en ℝ⁴ | 333 | Geometría diferencial | ⚪ |
| 369 | Criterios exactos de empaquetado de bolas simplécticas en dimensiones superiores | 343 | Geometría diferencial | ⚪ |
| 370 | Regiones isoperimétricas en el 3-toro cúbico | 354 | Geometría diferencial | ⚪ |
| 371 | Flujos tangentes únicos en la primera singularidad de superficie | 355 | Geometría diferencial | ⚪ |
| 372 | Coordenadas bi-Lipschitz en todo punto regular RCD | 357 | Geometría diferencial | ⚪ |

---

Generado por `scripts/build_ranking.py` a partir de `data/catalogue.json`. El ID es el número de familia en `openai/math`.
