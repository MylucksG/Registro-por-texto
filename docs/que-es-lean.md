# ¿Qué es Lean? Una explicación sencilla

## En una frase

Lean es un programa que comprueba demostraciones matemáticas paso a paso, sin que nadie tenga que fiarse de quien las escribió.

## La idea con una analogía

Un corrector ortográfico marca las palabras mal escritas. Lean hace algo parecido con los razonamientos: si un paso no se sigue del anterior, lo rechaza. Y si todos los pasos son válidos, lo acepta.

Una demostración escrita en papel puede tener cientos de páginas, y un error escondido en la página 87 puede pasar años sin que nadie lo vea. En Lean, esa página no compila.

```
Demostración en papel          Demostración en Lean
────────────────────           ────────────────────
La revisa una persona    →     La revisa un programa
Puede tardar años              Tarda segundos o minutos
Puede pasar un error           Un paso inválido no compila
```

## Cómo se ve

Esto es Lean de verdad. Afirma que 2 + 2 es 4 y lo demuestra:

```lean
example : 2 + 2 = 4 := by norm_num
```

Si cambias el 4 por un 5, Lean se niega a aceptarlo. Una demostración real es más larga, pero funciona igual: cada paso se comprueba.

## Quién lo hizo y qué hay a su alrededor

- Lean nació como un proyecto de Leonardo de Moura, primero en Microsoft Research. Hoy lo mantiene la comunidad y una organización sin ánimo de lucro dedicada a él.
- **Mathlib** es la gran biblioteca comunitaria de matemáticas ya formalizadas en Lean. Es la base sobre la que se construyen resultados nuevos.
- El repositorio `openai/math` usa Lean y Mathlib para formalizar parte de sus resultados.

## Por qué importa con la inteligencia artificial

Una IA puede escribir una demostración que parece correcta y no serlo. Con Lean eso se puede comprobar de forma automática:

| Sin Lean | Con Lean |
|---|---|
| Hay que confiar en la IA o revisar a mano | La máquina dice si compila o no |
| Un error sutil puede pasar desapercibido | Un paso inválido bloquea la prueba |
| Revisar 722 manuscritos lleva años | Se comprueba lo formalizado en minutos |

Por eso, en este repositorio, "tiene Lean" es la señal más fuerte de fiabilidad.

## Lo que Lean no garantiza

Que una prueba compile no significa que el problema esté bien planteado. Hay tres cosas que siguen necesitando a una persona:

1. **Que el enunciado sea el correcto.** Si se formaliza una afirmación distinta de la que dice el paper, Lean puede aceptar una prueba perfectamente válida de otra cosa.
2. **Que las definiciones sean las que se pretendían.** Lean comprueba la lógica, no la intención.
3. **Entender qué se ha demostrado.** Que la máquina lo acepte no explica por qué es verdad.

## Cómo leer la columna "Lean" de `CONTENTS.md`

| Símbolo | Significado |
|---|---|
| ✅ completo | Todos los manuscritos de la familia tienen su resultado principal formalizado |
| 🟡 parcial | Solo algunos manuscritos lo tienen |
| ⚪ no visible | No aparece en el catálogo de formalizaciones. No prueba que sea falso ni que no exista |

## Para saber más

- Sitio oficial de Lean: https://lean-lang.org
- Mathlib: https://github.com/leanprover-community/mathlib4
- La carpeta `lean/` de [openai/math](https://github.com/openai/math)
