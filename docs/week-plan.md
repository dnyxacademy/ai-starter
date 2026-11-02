# The four weeks

Monday 2 November to Saturday 28 November 2026. Monday to Saturday, Sunday off. Plan on three to
four hours a day.

This is a guided tour, and we say so on day one. Core machine learning gets one week and deep
learning gets one, so you will train models and understand the ideas without deriving the maths.
Each week ends with a "go deeper" list.

The ticket for each day, with its due date, is in your Dnyx Learn lesson. The full brief for each
assignment is in [AI-Assignments](https://github.com/dnyxacademy/AI-Assignments).

## The rhythm

| Day | What happens |
|---|---|
| Mon | The week's tickets are released. Lesson, then build |
| Tue | Lesson and build. Written stand-up in the batch chat before 10 am, every day |
| Wed | Hands-on workshop with a trainer |
| Thu | Lesson and build. Draft pull request for early feedback |
| Fri | Build. Demo, five minutes each, in small groups. Fun Friday |
| Sat | Weekly quiz. Submission by noon. Placement Spotlight session. Mentor feedback in the evening |
| Sun | Off |

## Week 1 (2-7 Nov) - Python, data and first models

How AI, machine learning, deep learning and generative AI relate. Python from scratch. Colab, Git
and the pull request flow. NumPy and pandas. Cleaning and exploring data, Matplotlib, data ethics
and bias. Machine learning basics: features and labels, train and test split, overfitting,
regression and classification. Evaluation: accuracy, precision, recall, F1, the confusion matrix,
cross-validation, scikit-learn pipelines.

**By Saturday:** your analysis and a baseline model, with an evaluation table.
**By Wednesday:** your first pull request, however small.

## Week 2 (9-14 Nov) - Neural networks and deep learning

The neuron, layers, activation, loss, gradient descent, backpropagation - intuition first, then a
tiny network in NumPy by hand. PyTorch: tensors, autograd, training loops, optimisers, GPU on
Colab. Convolutional networks and transfer learning. Sequences and attention in outline, embeddings,
and why transformers replaced RNNs. Regularisation and tracking experiments.

**By Saturday:** a deep-learning model compared honestly against your Week 1 baseline, with
training curves.

## Week 3 (16-21 Nov) - Generative AI and retrieval

How large language models work: tokens, the context window, pre-training, instruction tuning,
sampling, hallucination. Calling an LLM API from Python. Prompt engineering: roles, examples,
chain-of-thought, structured JSON output, versioning and testing prompts. Embeddings and vector
search. RAG: chunking, retrieval, grounding, citations, then its quality - hybrid search,
re-ranking, evaluation. Fine-tuning versus RAG versus prompting. Safety: prompt injection, privacy,
copyright.

**By Saturday:** a Streamlit assistant that answers from your documents with citations, plus an
evaluation table of fifteen test questions.

## Week 4 (23-28 Nov) - Agents, MCP, ship, demo

From chatbot to agent: think, act, observe. Tool calling, and when a plain workflow beats an agent.
Patterns: ReAct, planning, reflection, routing, memory. Build one yourself before reaching for a
framework. Multi-agent and human-in-the-loop, guardrails, cost, tracing and evaluating agents.
**MCP (Model Context Protocol):** hosts, clients and servers; tools, resources and prompts; using
existing servers and writing a small one in Python. Deploying: a FastAPI service, secrets, rate
limits, logging, Hugging Face Spaces or Railway.

**Demo Day is Friday 27 November.** Final submission Saturday 28 November by noon.

### The final project has to have

- A clearly defined user and problem
- Your Week 1 to 3 work still visible in the repository
- An agent with at least three tools, one of them through MCP
- Logged traces
- At least ten test cases with results, and an honest failure analysis
- A deployed demo
- A README with limitations
- A two-minute demo video
- A short "How I used AI" note

## Going further (not marked)

Reinforcement learning basics, time-series forecasting, reading one paper a week, a Kaggle
competition, MLOps (versioning and monitoring), quantisation and running models on-device.
