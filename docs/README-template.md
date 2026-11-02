# The README we expect by Week 4

Your README is the first thing an employer reads, and it carries marks in the final project. Replace
the root `README.md` with something shaped like this.

---

# Project name

One sentence: what it does and who it is for.

**Live demo:** https://...  |  **Demo video:** https://...

![A screenshot of the app](docs/screenshot.png)

## The problem

Who has this problem, what they do today, and why an AI approach helps. Two or three sentences.

## What it does

- What a user can ask or do
- What comes back
- What it will refuse or cannot answer

## The data

- **Source and licence:** where the dataset came from, and whether you are allowed to use it
- **Size and shape:** rows, columns, the period it covers
- **What I cleaned:** dropped, filled in, anonymised - and why
- **Who is missing from it:** and what that means for the results

## How it works

A short paragraph or diagram: data, model, retrieval, agent, tools. Which model or provider, and why.

## Results

| Stage | Approach | Metric | Score |
|---|---|---|---|
| Week 1 | Baseline (logistic regression) | F1 | |
| Week 2 | Neural network | F1 | |
| Week 3 | RAG assistant | Answers with a correct citation, out of 15 | |
| Week 4 | Agent | Test cases passed, out of 10 | |

Say which metric matters for your problem, and why.

## Where it fails

The honest section, and the one mentors read most closely. Which questions it gets wrong, what
makes it hallucinate, where the model is weakest, what you would need to fix it. This gains marks -
it does not lose them.

## Running it

    git clone https://github.com/<you>/<repo>.git
    cd <repo>
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env    # then fill in your key
    streamlit run app/streamlit_app.py

Notebooks: `notebooks/`, in order. They run top to bottom on a fresh kernel.

## Responsible use

What this should not be used for, what a human should check, and what you would tell a user about
its limits before they trusted it.

## How I used AI

Which tools, for what - exploring, debugging, drafting prompts, writing tests. Every line here is
something you can explain.

## Licence

MIT. Built on the Dnyx Academy training-cum-internship, November 2026.
