"""Loading and cleaning your dataset.

Why a module and not just the notebook: by Week 3 you will want the same cleaning in
the notebook, in the Streamlit app and in the FastAPI service. Write it once here and
import it, rather than copying cells between notebooks.

    from src.load_data import load_raw, clean

In Colab you may need to tell Python where the repository is first:

    import sys; sys.path.append('..')
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_raw(filename: str = "sample.csv") -> pd.DataFrame:
    """Read a file from data/ into a DataFrame.

    Keep the full dataset out of git. Point this at a local path or a download URL, and
    keep a small sample_*.csv committed so the notebooks and CI still run.
    """
    path = DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing. Put a sample file in data/, or change the filename. "
            "See data/README.md."
        )
    return pd.read_csv(path)


def clean(frame: pd.DataFrame) -> pd.DataFrame:
    """Your cleaning steps, in one place.

    Write down every decision you make here in your weekly note: what you dropped, what
    you filled in, and why. A mentor will ask.
    """
    out = frame.copy()
    out = out.drop_duplicates()
    out.columns = [str(column).strip().lower().replace(" ", "_") for column in out.columns]
    # TODO: handle missing values, types and outliers for YOUR dataset.
    return out
