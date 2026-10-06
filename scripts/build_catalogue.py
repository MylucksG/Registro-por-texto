#!/usr/bin/env python3
"""Cruza el catalogo de familias de openai/math con su catalogo de formalizaciones Lean.

Uso: python3 -I scripts/build_catalogue.py RUTA_AL_CLON_DE_openai_math
Genera data/catalogue.json y CONTENTS.md.
"""
import json, re, sys
from collections import OrderedDict
from pathlib import Path

root = Path(sys.argv[1])
out = Path(__file__).resolve().parent.parent
tex = (root / "overview.tex").read_text(encoding="utf-8")
yml = (root / "lean" / "formalization.yaml").read_text(encoding="utf-8")


def group(s, i):
    """Devuelve (contenido, indice_siguiente) del grupo {...} que empieza en s[i]."""
    assert s[i] == "{", s[i:i + 40]
    depth, j = 0, i
    while True:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1


def clean(t):
    t = re.sub(r"\\href\{[^}]*\}\{([^}]*)\}", r"\1", t)
    t = t.replace("\\enspace\\textperiodcentered\\enspace", " · ")
    t = t.replace("--", "–").replace("\\&", "&").replace("\\'", "").replace('\\"', "")
    t = re.sub(r"\\H\{o\}", "o", t)
    t = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


# 1. Familias, con su disciplina (orden de aparicion en el overview)
families, discipline = [], None
for line in tex.splitlines():
    m = re.match(r"\\cataloguesection\{([^}]*)\}", line)
    if m:
        discipline = clean(m.group(1))
        continue
    if line.startswith("\\resultentry{"):
        pos = len("\\resultentry")
        args = []
        for _ in range(4):
            a, pos = group(line, pos)
            args.append(a)
        fid, title, summary, links = args
        dirs = re.findall(r"/preprints/([^/]+)/", links)
        families.append(OrderedDict(
            id=fid, discipline=discipline, title=clean(title), summary=clean(summary),
            papers=[clean(x) for x in re.findall(r"\\href\{[^}]*\}\{([^}]*)\}", links)],
            preprint_dirs=dirs))

# 2. Preprints con resultado principal formalizado (seccion `sources` del yaml)
src_block = yml.split("\nsources:")[1].split("\nrelated_formalizations:")[0]
formalized = set(re.findall(r"id: \.\./preprints/([^/]+)/", src_block))

for f in families:
    n = len(f["preprint_dirs"])
    k = sum(d in formalized for d in f["preprint_dirs"])
    f["n_papers"], f["n_lean"] = n, k
    f["lean"] = "completo" if n and k == n else "parcial" if k else "no visible"

(out / "data").mkdir(exist_ok=True)
(out / "data" / "catalogue.json").write_text(
    json.dumps(families, ensure_ascii=False, indent=1), encoding="utf-8")

# 3. CONTENTS.md
badge = {"completo": "✅ completo", "parcial": "🟡 parcial", "no visible": "⚪ no visible"}
tot = len(families)
cnt = {k: sum(f["lean"] == k for f in families) for k in badge}
lines = [
    "# Mapa de contenidos",
    "",
    f"**{tot} familias de resultados** del repositorio [openai/math](https://github.com/openai/math), "
    f"con el estado de verificación en Lean de cada una. Generado por `scripts/build_catalogue.py`.",
    "",
    f"- ✅ Todos los manuscritos de la familia tienen su resultado principal formalizado: **{cnt['completo']}**",
    f"- 🟡 Solo algunos manuscritos: **{cnt['parcial']}**",
    f"- ⚪ No aparece en `lean/formalization.yaml`: **{cnt['no visible']}**",
    "",
    "> \"No visible\" no significa que no exista una formalización. Significa que el título del manuscrito "
    "no está en el catálogo `sources` del yaml. Que una prueba compile tampoco garantiza que el enunciado "
    "formal diga lo mismo que el paper.",
    "",
]
by = OrderedDict()
for f in families:
    by.setdefault(f["discipline"], []).append(f)
for d, fs in by.items():
    n_ok = sum(x["lean"] != "no visible" for x in fs)
    lines += [f"## {d}", "", f"{len(fs)} familias, {n_ok} con alguna formalización.", "",
              "| ID | Familia | Manuscritos | Lean |", "|---|---|---|---|"]
    for x in fs:
        t = x["title"].replace("|", "\\|")
        lines.append(f"| {x['id']} | {t} | {x['n_papers']} | {badge[x['lean']]} |")
    lines.append("")
(out / "CONTENTS.md").write_text("\n".join(lines), encoding="utf-8")

print(tot, "familias;", cnt, "; preprints formalizados en yaml:", len(formalized))
