# Constitutional AI · CAI · lineage data

**Anthropic's Constitutional AI**, folded into **UD0 · Universe David 0** as **lineage data** — the documented ancestry of the machine, *cited and linked, never claimed, never re-shipped*.

Constitutional AI (Bai et al., Anthropic, December 2022) trains a harmless assistant using a **written constitution** as the only human oversight: the model **critiques and revises** its own answers against the principles (**SL-CAI**), then learns from **AI feedback** via a preference model built from its own constitutional choices (**RL-CAI / RLAIF**). Harmless, but **non-evasive**.

The lineage runs to the present: the 2022 promise — *put the values in a document you can read* — became, in **January 2026**, the published **Claude constitution** (CC0).

## Lineage data (sources, attributed)
| artifact | source | license |
|---|---|---|
| the paper | [arXiv:2212.08073](https://arxiv.org/abs/2212.08073) | — |
| supplementary repo (prompts/evals/samples) | [anthropics/ConstitutionalHarmlessnessPaper](https://github.com/anthropics/ConstitutionalHarmlessnessPaper) | **none** |
| the 2026 published constitution | [anthropics/claude-constitution](https://github.com/anthropics/claude-constitution) | **CC0-1.0** |
| political neutrality eval | [anthropics/political-neutrality-eval](https://github.com/anthropics/political-neutrality-eval) | **CC-BY-4.0** |

**No data files ship with this repo** (`.gitignore` excludes `*.jsonl`/`*.csv`): the critique-revision principles are shown only as short functional structure, evals/samples are counted and linked, and the harmful **red-team** prompts are deliberately **excluded** at the source. The ROOT0 contribution is the framing and the `.dlw` cataloguing; the underlying corpus remains its owners'.

Domain: **Artificial Intelligence** — the values/governance cluster, kin to `alignment`, `ai-governance`, and `the-language-of-the-machine`.

Built by `build.py` (self-contained). Catalogued by David Lee Wise (ROOT0); instance AVAN (locked).
