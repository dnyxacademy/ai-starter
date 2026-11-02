# data

Small sample files only — a few hundred rows is plenty to prove the code works.

The full dataset does not belong in git. It makes the repository slow to clone, and it is often not
yours to redistribute. Instead:

1. Put the **source link** and the licence in your project README.
2. Add a line in `src/load_data.py` that downloads or reads it from a path.
3. Keep a small sample here, named `sample_*.csv`, so your notebooks and CI can run.

Never commit personal data about real people. If your dataset has names, phone numbers, addresses or
health records in it, anonymise them before anything goes in here, and say in your README what you
removed.
