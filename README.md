# Registro-por-texto

Descubrimientos de la IA.

---

# Descubrimientos de la IA

Este repositorio reúne descubrimientos hechos por sistemas de inteligencia artificial, con un análisis independiente de cada uno: qué afirman, cuánto se puede confiar en ellos, qué se puede aplicar y hacia dónde apunta.

- ¿Primera vez que oyes hablar de Lean? Empieza por [¿Qué es Lean?](docs/que-es-lean.md), una explicación sencilla para quien no sabe del tema.
- Para añadir un nuevo descubrimiento, mira [`discoveries/`](discoveries/README.md).

## Análisis disponibles

| Descubrimiento | Resumen |
|---|---|
| [openai/math](#análisis-de-openaimath) | 722 manuscritos de matemáticas producidos por un modelo de OpenAI, cruzados con su verificación en Lean |

---

# Análisis de `openai/math`

Este repositorio también contiene un análisis independiente de [openai/math](https://github.com/openai/math), una colección de manuscritos matemáticos y pruebas formales producidos por un modelo interno de OpenAI. Sigue la misma estructura que el repositorio original, para que se pueda leer en paralelo.

## Cómo navegar

- [`docs/que-es-lean.md`](docs/que-es-lean.md): qué es Lean, explicado sin tecnicismos.
- [`CONTENTS.md`](CONTENTS.md): las 372 familias de resultados, con su disciplina y su estado de verificación en Lean.
- [`analysis/overview.md`](analysis/overview.md): panorama por disciplina y qué resultados importan más.
- [`analysis/applications.md`](analysis/applications.md): qué se puede aplicar, cómo y en qué plazo.
- [`analysis/future.md`](analysis/future.md): hacia dónde apunta, qué lo impulsa y qué lo frena.
- [`data/catalogue.json`](data/catalogue.json): el catálogo completo en formato máquina.
- [`scripts/build_catalogue.py`](scripts/build_catalogue.py): regenera `CONTENTS.md` y `data/catalogue.json` desde un clon de `openai/math`.

## Qué es el material analizado

Según el README de `openai/math`, el catálogo tiene 722 manuscritos en 372 familias. Se obtuvieron con un modelo interno no publicado, con unas 3 horas de razonamiento por resultado, sobre unos 4.000 problemas planteados. Los resultados están en distintas etapas de verificación y los que no están formalizados en Lean podrían tener errores.

## Cómo se hizo este análisis

1. Se clonó `openai/math` (commit `adc7f12`, 6 de octubre de 2026).
2. Se leyeron el README, `overview.tex` y `lean/formalization.yaml`.
3. Se cruzó cada manuscrito de cada familia con la lista de papers cuyo resultado principal está formalizado. Eso da la columna "Lean" de `CONTENTS.md`.
4. La parte de aplicaciones y futuro es interpretación mía sobre esos datos.

## Límites

- No se verificó ninguna demostración, ni se compiló nada de Lean.
- "No visible" en `CONTENTS.md` significa que el título no aparece en el catálogo `sources` del yaml. Puede haber formalizaciones que ese catálogo no recoja.
- El cruce es por título de manuscrito. Que una prueba compile no garantiza que el enunciado formal coincida con el del paper.
- Las secciones de aplicaciones y de futuro son estimaciones, no hechos del repositorio original. No se leyeron los papers completos.

## Regenerar los datos

```
git clone --depth 1 https://github.com/openai/math /ruta/a/openai-math
python3 -I scripts/build_catalogue.py /ruta/a/openai-math
```
