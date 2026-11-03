# AI starter

The starting point for your project on the Dnyx Academy **AI** training-cum-internship — machine
learning, deep learning, generative AI, agents and MCP. One domain, one dataset, four weeks, layer
on layer.

> **Use this template** (green button, top right) → name it after your domain, like
> `crop-advisor` → keep it **public** so your mentor can read your pull requests → clone it, or open
> the notebooks straight in Colab.

Then replace this README with your own. [docs/README-template.md](docs/README-template.md) is the
shape we expect by Week 4.

## First, today

Nothing to install if you use [Google Colab](https://colab.research.google.com/) — open
`notebooks/week-1-explore-your-dataset.ipynb` from GitHub and start. Colab gives you a free GPU,
which you will want in Week 2.

Locally, if you prefer:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then branch, change the project name in this README, commit, push and open a pull request. That is
your **first pull request, due Wednesday of Week 1** — it is meant to be tiny.

```bash
git switch -c week-1/first-pull-request
git add -A
git commit -m "Set the project name and domain"
git push -u origin week-1/first-pull-request
```

## What is here

```
notebooks/      one notebook per week — this is where most of Week 1 and 2 happens
src/            code you reuse across notebooks (loading, cleaning, helpers)
app/            your Streamlit demo (Week 3) and FastAPI service (Week 4)
data/           small sample data only — never the full dataset
.env.example    copy to .env for API keys (never commit .env)
docs/           how to submit, the week plan, the README shape we expect
```

**Commit the notebook with its output cleared** unless a chart is the point. A notebook full of
output is unreadable in a pull request.

## Pick your domain in Week 1

Education, health, agriculture, finance, retail — or your own idea, approved by a mentor. You work
with **one dataset and one set of documents for the whole programme**. Each week adds a layer:

| Week | Dates | What you add |
|---|---|---|
| 1 | 2–7 Nov | Python, the data, and a first model that works |
| 2 | 9–14 Nov | A neural network, compared honestly against Week 1 |
| 3 | 16–21 Nov | An assistant that answers from your documents, with citations |
| 4 | 23–28 Nov | An agent with tools, one through MCP, deployed |

The day-by-day plan is in [docs/week-plan.md](docs/week-plan.md). Your tickets and due dates are in
Dnyx Learn; the full assignment briefs are in
[AI-Assignments](https://github.com/dnyxacademy/AI-Assignments).

**Not chosen a domain yet?** Five worked-through domains — education, agriculture, insurance,
retail and health — are in [project-ideas](https://github.com/dnyxacademy/project-ideas), each
naming a prediction task, the documents to pair with it, and three agent tools. Read
[ai/README.md](https://github.com/dnyxacademy/project-ideas/blob/main/ai/README.md) first: you need
**a dataset and a document set**, and finding only one of the two is how Week 3 goes wrong.

## Free tiers only

Nothing in this programme needs a paid account.

| Need | Use |
|---|---|
| Notebooks and GPU | Google Colab |
| LLM access | Any provider's free tier, or [Ollama](https://ollama.com/) for local open models |
| Vectors | Chroma locally, pgvector on Neon for the deployed version |
| Demo and API | Streamlit, then FastAPI |
| Hosting | Hugging Face Spaces, Railway or Render free tier |

If you hit a rate limit, say so in your stand-up — trainers hold a spare key, and Ollama runs
offline.

## Rules worth repeating

- Never commit `.env` or an API key. `.gitignore` covers it — do not fight it.
- Never commit the full dataset, model weights, or anyone's personal data. A small sample in
  `data/` is fine; link to the source for the rest.
- AI assistants are allowed and taught. Disclose what you used in your weekly note, and do not ship
  a line you cannot explain in review.

Full version: [CONTRIBUTING.md](https://github.com/dnyxacademy/.github/blob/main/.github/CONTRIBUTING.md).

## Getting help

Lesson Q&A in Dnyx Learn, your batch chat, mentor office hours (two hours a day), or a support
ticket. Stuck for more than an hour on the same thing: ask.

---

MIT licensed ([LICENSE](LICENSE)) — your project is yours.
