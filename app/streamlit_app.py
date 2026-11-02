"""Your demo, from Week 3 onwards.

    streamlit run app/streamlit_app.py

Week 3 this answers questions from your documents, with citations.
Week 4 it calls your agent, and the FastAPI service in app/api.py does the work.
"""

import streamlit as st

st.set_page_config(page_title="My AI project", page_icon="*")

st.title("My AI project")
st.caption("Replace this with what your project does, and who it is for.")

question = st.text_input("Ask a question")

if question:
    # TODO Week 3: retrieve from your documents, then answer with citations.
    st.info("Not built yet. This is where retrieval and the answer go.")
    with st.expander("Sources"):
        st.write("Show which chunks you retrieved. An answer with no citation is a guess.")

st.divider()
st.caption(
    "Limitations: say plainly what this cannot do and where it has been wrong. "
    "That honesty carries marks."
)
