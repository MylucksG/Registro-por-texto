# Panorama

## Cobertura de Lean por disciplina

Cuántas familias tienen al menos un manuscrito con su resultado principal formalizado. Datos calculados en `data/catalogue.json`.

| Disciplina | Familias | Con Lean | % |
|---|---:|---:|---:|
| Mathematical logic | 6 | 5 | 83% |
| Functional analysis | 11 | 8 | 73% |
| Convex and metric geometry | 15 | 10 | 67% |
| Theoretical computer science | 40 | 20 | 50% |
| Group theory | 14 | 7 | 50% |
| Combinatorics | 37 | 17 | 46% |
| Algebra | 18 | 7 | 39% |
| Differential geometry | 29 | 9 | 31% |
| Operator algebras | 19 | 6 | 32% |
| Probability and statistical mechanics | 29 | 8 | 28% |
| Mathematical physics | 25 | 6 | 24% |
| Real and complex analysis | 16 | 6 | 38% |
| Dynamical systems and ergodic theory | 12 | 2 | 17% |
| Partial differential equations | 16 | 3 | 19% |
| Algebraic and complex geometry | 36 | 6 | 17% |
| Number theory | 31 | 6 | 19% |
| Topology | 18 | 1 | 6% |
| **Total** | **372** | **127** | **34%** |

Total de 127 familias: 74 completas y 53 parciales (ver `CONTENTS.md`).

## Qué dice la tabla

- La formalización se concentra donde las definiciones ya existen en Lean y Mathlib: lógica, análisis funcional, geometría convexa, informática teórica y combinatoria.
- Se queda atrás donde falta infraestructura: topología, geometría algebraica, teoría de números y ecuaciones en derivadas parciales. Ahí la comunidad tendrá que confiar más en la revisión humana.
- Dos de cada tres familias no tienen formalización visible. Para esas, la fiabilidad depende de que alguien las lea.

## Resultados que más importan

Elegidos por impacto potencial, dentro o fuera de las matemáticas. El estado de Lean es el de la familia en `CONTENTS.md`.

| ID | Resultado | Por qué importa | Lean |
|---|---|---|---|
| 102 | Unique Games Conjecture y umbrales de aproximación | Fija el límite de lo que se puede aproximar en optimización | 🟡 parcial (3 de 5; incluye el paper principal; faltan Min-UnCut y feedback vertex set) |
| 003 | Quasi-Riemann: ceros de zeta ausentes en Re(s) > 7/8 | Mejora el conteo de primos | 🟡 parcial (2 de 3; incluye el paper del semiplano 7/8, no la prueba alternativa 11/12) |
| 002 | Birch–Swinnerton-Dyer con Selmer de corango 0 o 1 | Problema del Milenio, en casos concretos | ⚪ no visible |
| 197 | Contraejemplos a Kaplansky, Gottschalk y Determinante | Cierra conjeturas de décadas | 🟡 parcial (3 de 4; el contraejemplo sin torsión no está formalizado, sí las versiones en característica 2 y impar y el de Determinante) |
| 362 | Vlasov–Maxwell relativista 3D | Buen planteamiento de ecuaciones de plasmas | ✅ completo |
| 087 | Conjeturas de Mahler | Resuelve un problema clásico de geometría convexa | 🟡 parcial (2 de 3; formalizada la simétrica, no la general) |
| 089 | Embeddings L1 de grafos planares | Algoritmos de grafos | ✅ completo |
| 174 | Árboles de expansión delgados, determinista | Diseño de redes | 🟡 parcial (1 de 2; formalizada la conjetura, no la construcción en tiempo polinomial) |
| 111 | Prophet inequalities con una muestra | Decisión online | ⚪ no visible |
| 017 | Exponente de irracionalidad de π igual a 2 | Resultado clásico de aproximación diofántica | ⚪ no visible |
| 287 | Isomorfismo de los factores de grupo libre | Problema abierto de álgebras de operadores | ⚪ no visible |

## Lo que el repositorio no contiene

- Ningún ataque a RSA ni a la criptografía de curvas elípticas, ni resultados sobre P vs NP o factorización.
- Ni la Hipótesis de Riemann completa, ni Navier–Stokes, ni la conjetura de Hodge general. El README solo menciona Hodge para variedades abelianas CM.
- Nada sobre cómo se entrena o se mejora el modelo.
