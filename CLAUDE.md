# CLAUDE.md

Instructions for Claude Code working in this repository. You will fill this in properly in
Week 4, when instruction files are taught — but start it in Week 1 and add a line whenever an
assistant gets something wrong.

Claude Code reads this file; most other tools read `AGENTS.md`. Keep them saying the same thing.

## The project

<!-- One paragraph: what this is, who it is for. -->

## Stack

<!-- Keep this current. It changes every week. -->

- Week 1: Python, pandas, scikit-learn, in Colab notebooks

## How to run it

<!-- The exact commands. -->

## Rules

- Do not add a dependency without saying why in the pull request.
- Do not put secrets in code. Read them from environment variables; document them in `.env.example`.
- Match the existing style. Do not reformat files you were not asked to change.
- Small changes, explained. If a change touches more than a few files, say so first.
- I have to explain this code in a review, so leave it understandable to a beginner.
- Never put a dataset, an API key or personal data in a notebook cell.
- Prefer a function in `src/` over a long notebook cell I will later copy twice.
