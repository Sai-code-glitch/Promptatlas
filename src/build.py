"""Render prompt data to prompts.json and inline it into index.html.

Usage: python3 build.py   (run from this folder)
"""
import json, re, pathlib
import prompts_a
import prompts_b  # noqa: F401  (registers its prompts on import)

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def render(p):
    lines = [f"# Role\nYou are {p['r']}.", f"\n# Goal\n{p['goal']}"]
    lines.append("\n# Inputs")
    for name, desc in p["i"]:
        lines.append(f"- {name.replace('_', ' ').capitalize()}: {{{{{name}}}}}")
    lines.append("\n# Instructions")
    lines += [f"{n}. {s}" for n, s in enumerate(p["s"], 1)]
    lines.append("\n# Constraints")
    lines += [f"- {k}" for k in p["k"]]
    lines += ["- Be complete: no placeholders, no 'etc.', no skipped sections.",
              "- If something is uncertain, say so instead of guessing."]
    lines.append(f"\n# Output format\n{p['o']}")
    lines.append("\n# Before you answer\nIf a required input above is missing or ambiguous, ask up to 3 focused "
                 "clarifying questions first. Otherwise, proceed, then check your answer against every "
                 "instruction and constraint above and fix any gaps before responding.")
    return "\n".join(lines)

def main():
    seen, out = set(), []
    for p in prompts_a.P:
        pid = slug(p["t"])
        assert pid not in seen, pid
        seen.add(pid)
        out.append({"id": pid, "title": p["t"], "category": p["c"], "tags": p["g"],
                    "description": p["d"], "variables": [{"name": n, "hint": h} for n, h in p["i"]],
                    "prompt": render(p)})
    # Variables referenced in role/steps but not declared become inputs too.
    for o in out:
        declared = {v["name"] for v in o["variables"]}
        for name in dict.fromkeys(re.findall(r"\{\{(\w+)\}\}", o["prompt"])):
            if name not in declared:
                o["variables"].append({"name": name, "hint": ""})
    data = json.dumps(out, ensure_ascii=False, indent=1)
    (OUT / "prompts.json").write_text(data)
    tpl = (HERE / "template.html").read_text()
    safe = json.dumps(out, ensure_ascii=False).replace("</", "<\\/")
    (OUT / "index.html").write_text(tpl.replace("/*__PROMPTS__*/[]", safe))
    cats = {}
    for o in out:
        cats[o["category"]] = cats.get(o["category"], 0) + 1
    print(len(out), "prompts in", len(cats), "categories")
    for c, n in cats.items():
        print(f"  {n:3d}  {c}")

if __name__ == "__main__":
    main()
