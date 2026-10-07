#!/usr/bin/env python3
"""Genera analysis/ranking-completo.md: las 372 familias de openai/math ordenadas.

Uso: python3 -I scripts/build_ranking.py

Los 50 primeros puestos vienen fijados a mano (son los que tienen ficha en
analysis/ranking.md). El resto se ordena con una puntuacion reproducible:

  tier       -> +4 si es un problema con nombre propio reconocible (lista TIER1),
                -2 si es un resultado tecnico de interes muy local (lista TIER3)
  lean       -> +3 si toda la familia esta formalizada, +1.5 si solo una parte
  area       -> peso por disciplina, mayor en las que tienen mas efecto fuera
  palabras   -> +1 si cierra una conjetura (contraejemplo o refutacion),
                +1 si es algoritmico, +1 si lleva el nombre de Hilbert o Erdos
  tamano     -> +0.3 por manuscrito de la familia, hasta 5

La puntuacion es una opinion del analisis, no de OpenAI. Cambia las listas y
vuelve a ejecutar el script para reordenar.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
catalogue = json.loads((ROOT / "data" / "catalogue.json").read_text(encoding="utf-8"))
by_id = {f["id"]: f for f in catalogue}

# Puestos 1-50, en orden. Coinciden con las fichas de analysis/ranking.md.
TOP50 = """107 102 003 002 138 109 362 159 120 074 017 142 197 158 143 248 246 073 287 376
004 032 103 089 174 111 104 106 235 029 005 087 091 090 156 157 171 173 180 271
268 263 221 369 375 147 230 304 338 312""".split()
assert len(TOP50) == 50 and len(set(TOP50)) == 50

# Problemas con nombre propio que un matematico de otra area reconoceria.
TIER1 = set("""006 007 013 016 022 026 028 038 039 040 043 056 058 071 072 077 078 079 080 083
093 099 101 105 108 110 117 118 121 122 125 130 132 136 141 146 153 155 160 161
162 164 165 166 168 170 175 176 178 179 181 191 193 194 196 201 202 203 213 214
216 217 219 226 229 240 241 250 252 253 256 257 258 259 260 261 262 264 265 266
267 269 272 277 281 284 285 288 289 290 291 292 293 294 297 298 306 309 315 320
321 322 323 325 335 339 340 341 342 344 345 352 360 363 366 368 370 371 377""".split())

# Resultados tecnicos cuyo interes queda dentro de una subarea.
TIER3 = set("""046 047 048 049 053 054 059 064 068 098 100 131 134 135 140 149 151 152 154 185
187 190 192 198 200 204 206 208 209 210 225 232 236 237 239 242 245 247 254 278
280 282 299 301 302 303 307 308 311 313 314 316 317 318 319 326 329 330 331 332
333 334 336 343 346 347 350 353 354 355 356 357 358 359 361 365 367 372 373 374""".split())

AREA = {
    "Theoretical computer science": 3.0, "Number theory": 3.0,
    "Combinatorics": 2.0, "Partial differential equations": 2.0,
    "Mathematical physics": 2.0, "Probability and statistical mechanics": 2.0,
    "Convex and metric geometry": 2.0, "Real and complex analysis": 2.0,
    "Algebra": 1.0, "Algebraic and complex geometry": 1.0, "Group theory": 1.0,
    "Operator algebras": 1.0, "Topology": 1.0, "Functional analysis": 1.0,
    "Differential geometry": 1.0, "Dynamical systems and ergodic theory": 1.0,
    "Mathematical logic": 1.0,
}
LEAN = {"completo": 3.0, "parcial": 1.5, "no visible": 0.0}


def score(f):
    s = AREA[f["discipline"]] + LEAN[f["lean"]] + 0.3 * min(f["n_papers"], 5)
    if f["id"] in TIER1:
        s += 4
    if f["id"] in TIER3:
        s -= 2
    text = (f["title"] + " " + f["summary"]).lower()
    if re.search(r"counterexample|disprov|refut", text):
        s += 1
    if re.search(r"algorithm|polynomial-time|np-hard|quasipolynomial", text):
        s += 1
    if re.search(r"hilbert|erd[oő]s", text):
        s += 1
    return s


rest = [f for f in catalogue if f["id"] not in TOP50]
rest.sort(key=lambda f: (-score(f), f["id"]))
ordered = [by_id[i] for i in TOP50] + rest
assert len(ordered) == 372

BADGE = {"completo": "✅", "parcial": "🟡", "no visible": "⚪"}
n_lean = sum(f["lean"] != "no visible" for f in ordered)

lines = [
    "# Ranking completo",
    "",
    f"Las **372 familias de resultados** de [openai/math](https://github.com/openai/math), ordenadas de mayor a menor impacto. Solo el orden: sin explicaciones.",
    "",
    "**¿Quieres saber qué resuelve cada uno?** Los 50 primeros tienen ficha, con una versión sencilla y ejemplos, en el [ranking explicado](ranking.md). Para el resto, el resumen original en inglés está en [`CONTENTS.md`](../CONTENTS.md) y en `data/catalogue.json`.",
    "",
    "**Cómo se ordena.** Los 50 primeros están fijados a mano y coinciden con el ranking explicado. Del 51 en adelante, el orden sale de una puntuación reproducible (`scripts/build_ranking.py`) que combina: si el problema tiene nombre propio reconocible, si está comprobado con Lean, el área (más peso en las que tienen efecto fuera de las matemáticas), si cierra una conjetura y si es algorítmico. Es una opinión del análisis, no de OpenAI. Dos puestos seguidos pueden ser intercambiables.",
    "",
    f"**Lean:** ✅ toda la familia comprobada por máquina · 🟡 solo una parte · ⚪ no visible en el catálogo. {n_lean} de 372 tienen alguna comprobación.",
    "",
    "| # | Descubrimiento | ID | Área | Lean |",
    "|---:|---|:---:|---|:---:|",
]
for n, f in enumerate(ordered, 1):
    title = f["title_es"].replace("|", "\\|")
    if n <= 50:
        title = f"**[{title}](ranking.md)**"
    lines.append(f"| {n} | {title} | {f['id']} | {f['discipline_es']} | {BADGE[f['lean']]} |")
    if n == 50:
        lines.append("| | *Del 51 en adelante: orden por puntuación. Sin ficha explicativa.* | | | |")

lines += ["", "---", "", "Generado por `scripts/build_ranking.py` a partir de `data/catalogue.json`. El ID es el número de familia en `openai/math`.", ""]
(ROOT / "analysis" / "ranking-completo.md").write_text("\n".join(lines), encoding="utf-8")
print("372 puestos;", n_lean, "con Lean; primeros tras el 50:", [f["id"] for f in rest[:8]])
