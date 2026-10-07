# Registro-por-texto

**Descubrimientos de la IA, explicados en español para quien no es experto.**

Aquí analizamos descubrimientos hechos por sistemas de inteligencia artificial: qué afirman, cuánto se puede confiar en ellos, si sirven para algo y hacia dónde apuntan.

## Empieza aquí

1. **¿Qué es Lean?** Es la herramienta que comprueba si una demostración es correcta. Léelo primero: [¿Qué es Lean?](docs/que-es-lean.md)
2. **¿Alguna palabra no te suena?** Mira el [glosario](docs/glosario.md).
3. **Elige un descubrimiento** de la lista de abajo, o ve directo al [ranking de los 20 más importantes](analysis/ranking.md).
4. **¿Quieres el panorama completo de la IA?** Este repositorio es parte de [CaminoASI](#caminoasi-el-proyecto-del-que-forma-parte-este-repositorio).

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
| Los 20 descubrimientos más importantes: cuál era el problema y qué resuelve | [Ranking](analysis/ranking.md) |
| Qué resultados importan y por qué, en sencillo | [Panorama](analysis/overview.md) |
| Si algo se puede aplicar, cómo y cuándo | [Aplicaciones](analysis/applications.md) |
| Hacia dónde va todo esto | [El futuro](analysis/future.md) |
| La lista completa de los 372 resultados | [Mapa de contenidos](CONTENTS.md) |

## Cómo hicimos este análisis

1. Descargamos `openai/math` tal como estaba el 6 de octubre de 2026 (versión `adc7f12`).
2. Leímos su presentación, su resumen de resultados y su catálogo de pruebas en Lean.
3. Cruzamos cada artículo con ese catálogo para saber cuáles están comprobados por máquina.
4. Las partes de aplicaciones y de futuro son nuestra interpretación de esos datos.
5. El análisis y la traducción de los 372 títulos se redactaron con ayuda de IA (Claude). Si ves un error, avísanos.

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

## CaminoASI: el proyecto del que forma parte este repositorio

[**CaminoASI**](https://caminoasi.com/) es un portal en español sobre todo lo que la inteligencia artificial está cambiando. Su objetivo es que cualquier hispanohablante entienda hacia dónde va la IA: qué ya hace de verdad, qué es solo un anuncio y qué falta todavía.

El nombre viene de **ASI**, siglas en inglés de *superinteligencia artificial*: el portal sigue el camino que recorre la IA hacia ella. Es un proyecto independiente, hecho por una sola persona, que no depende de ningún laboratorio ni empresa de IA.

### Qué encontrarás

| Sección | Para qué sirve |
|---|---|
| [Noticias](https://caminoasi.com/noticias) | Lo que pasa en la IA cada día, de fuentes reales. Las noticias se filtran y clasifican por sector con [Jev](https://typesafe.ai/), un modelo de TypeSafe AI |
| [Investigaciones](https://caminoasi.com/investigaciones) | Los artículos científicos y anuncios de los laboratorios más relevantes |
| [Herramientas](https://caminoasi.com/herramientas) y [Robótica](https://caminoasi.com/robotica) | Herramientas de IA y robots, revisados antes de publicarse |
| [Ranking de modelos](https://caminoasi.com/ranking) | Qué modelos de IA rinden mejor |
| [Países](https://caminoasi.com/paises) y [Centros de datos](https://caminoasi.com/centros-de-datos) | Quién lidera la IA y dónde se construye su infraestructura |
| [Calendario ASI](https://caminoasi.com/calendario) | La historia de la humanidad contada desde la invención de la escritura, comparando los hitos del pasado con lo que pasa hoy en la IA |
| [Ética](https://caminoasi.com/etica) | Una propuesta de principios para la IA y la superinteligencia |
| [Glosario](https://caminoasi.com/glosario) | Los términos de la IA explicados |

En la portada hay además un **índice de influencia de la IA** de 0 a 10 para 15 sectores, como salud, energía o política. Parte de una estimación anual por sector y la ajusta con las noticias del último mes, sin moverla más de 2 puntos. La fórmula está publicada en el propio portal.

### Cómo encaja este repositorio

CaminoASI muestra el panorama: noticias, rankings y tendencias. Este repositorio baja al detalle: toma un descubrimiento concreto, como `openai/math`, y lo analiza a fondo.

Los dos siguen los mismos criterios:

- Citar siempre la fuente, con fecha y enlace.
- Separar lo que está comprobado de lo que es estimación.
- Avisar cuando algo está traducido o redactado con ayuda de IA.

¿Quieres seguir el día a día de la IA en español? Visita **[caminoasi.com](https://caminoasi.com/)**.
