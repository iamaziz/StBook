import streamlit as st

from code_runner import code_runner

st.set_page_config(layout="wide")
st.title("Streamlit Notebook")


def copilot():
    from stbook.code_completion import auto_complete
    auto_complete()


def app():
    c1, c2 = st.columns([1, 10])
    with c1: theme = st.radio("cell theme", ["light", "dark"], horizontal=True)
    with c2: num_cells = st.number_input("add new cell", min_value=1, max_value=200, value=1)

    for i in range(1, num_cells+1):
        c1, c2 = st.columns([1, 10])
        with c1: st.write(f"> `In [{i}]`")
        with c2: result = code_runner("", key=f"{i}", theme=theme)
        if result:
            c1, c2 = st.columns([1, 10])
            with c1: st.write(f"> `Out [{i}]`")
            with c2: st.write(result)


if __name__ == "__main__":
    app()
    # if st.toggle(f"Copilot"): copilot() # optional copilot, requires Ollama

