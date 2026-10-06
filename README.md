# Registro-por-texto

**Descubrimientos de la IA, explicados en español para quien no es experto.**

Aquí analizamos descubrimientos hechos por sistemas de inteligencia artificial: qué afirman, cuánto se puede confiar en ellos, si sirven para algo y hacia dónde apuntan.

## Empieza aquí

1. **¿Qué es Lean?** Es la herramienta que comprueba si una demostración es correcta. Léelo primero: [¿Qué es Lean?](docs/que-es-lean.md)
2. **¿Alguna palabra no te suena?** Mira el [glosario](docs/glosario.md).
3. **Elige un descubrimiento** de la lista de abajo.

## Descubrimientos analizados

| Descubrimiento | De qué trata | Estado |
|---|---|---|
| [openai/math](#openaimath-matemáticas-hechas-por-una-ia) | 722 artículos de matemáticas escritos por un modelo de IA de OpenAI | 1 de cada 3 familias de resultados tiene alguna parte comprobada por máquina |

---

# openai/math: matemáticas hechas por una IA

## En un minuto

- **Qué es.** OpenAI puso a un modelo de IA, que no ha publicado, a trabajar en unos 4.000 problemas de matemáticas sin resolver. Publicó 722 artículos con los resultados, agrupados en 372 familias.
- **Cuánto fiarse.** El propio OpenAI avisa que algunos pueden tener errores. Una de cada tres familias tiene al menos una parte comprobada con Lean, que es la señal más fiable. Ninguno ha pasado todavía por la revisión de otros expertos.
- **Lo más llamativo.** Una forma más barata, en teoría, de multiplicar matrices, comprobada por completo con Lean. También avances sobre los números primos y sobre problemas clásicos de algoritmos.
- **Si sirve para algo.** Casi nada se puede usar mañana. Son avances teóricos. Algunos algoritmos podrían llegar a programas reales en uno o dos años.
- **Lo que no hace.** No rompe la criptografía que protege internet ni resuelve los grandes problemas del Milenio.

## Para leer más

| Quiero saber... | Lee |
|---|---|
| Qué resultados importan y por qué, en sencillo | [Panorama](analysis/overview.md) |
| Si algo se puede aplicar, cómo y cuándo | [Aplicaciones](analysis/applications.md) |
| Hacia dónde va todo esto | [El futuro](analysis/future.md) |
| La lista completa de los 372 resultados | [Mapa de contenidos](CONTENTS.md) |

## Cómo hicimos este análisis

1. Descargamos `openai/math` tal como estaba el 6 de octubre de 2026 (versión `adc7f12`).
2. Leímos su presentación, su resumen de resultados y su catálogo de pruebas en Lean.
3. Cruzamos cada artículo con ese catálogo para saber cuáles están comprobados por máquina.
4. Las partes de aplicaciones y de futuro son nuestra interpretación de esos datos.

## Lo que este análisis no hace

- No comprobamos ninguna demostración ni ejecutamos Lean.
- "No visible" significa que un artículo no aparece en el catálogo de Lean de OpenAI. Puede existir una comprobación que ese catálogo no recoja.
- Que Lean acepte una prueba no garantiza que demuestre exactamente lo que dice el artículo.
- No leímos los artículos completos. Los plazos y los usos son estimaciones.

## Para desarrolladores

- [`data/catalogue.json`](data/catalogue.json): el catálogo completo. Los resúmenes (`summary`) están en inglés, como los publicó OpenAI. Los títulos tienen versión en español (`title_es`).
- [`data/titulos_es.txt`](data/titulos_es.txt): los 372 títulos traducidos. Si una traducción es mejorable, corrígela ahí y vuelve a ejecutar el script.
- [`scripts/build_catalogue.py`](scripts/build_catalogue.py): regenera `CONTENTS.md` y `data/catalogue.json`.
- Para añadir otro descubrimiento, usa la plantilla de [`discoveries/`](discoveries/README.md).

```
git clone --depth 1 https://github.com/openai/math /ruta/a/openai-math
python3 -I scripts/build_catalogue.py /ruta/a/openai-math
```

---

## Proyecto relacionado: CaminoASI

[**CaminoASI**](https://caminoasi.com/) es una plataforma en español que sigue el avance de la inteligencia artificial en el mundo. Este repositorio complementa esa actividad: aquí se analizan a fondo descubrimientos concretos de la IA, y allí se puede seguir el panorama general.

Según su página principal, ofrece:

- Noticias de IA de distintas fuentes, traducidas automáticamente al español.
- Herramientas, investigaciones y robótica.
- Un ranking de modelos y un ranking de países por capacidad y adopción de IA.
- Un índice de influencia de la IA por sectores.
- Una sección de centros de datos.

Esa descripción es un resumen de su portada, hecho el 6 de octubre de 2026. El sitio puede haber cambiado desde entonces. Para ver el detalle completo, visita [caminoasi.com](https://caminoasi.com/).
