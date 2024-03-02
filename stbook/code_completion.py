import streamlit as st

from code_editor import code_editor

def complete(code):
    import ollama
    sys_message = 'You are an AI code completion system. Generate code to complete the given Python code.'
    ret = ollama.generate(model='deepseek-coder:6.7b', prompt=code, system=sys_message)['response']
    st.session_state.in_code = f'{code}{ret}'
    st.code(st.session_state.in_code)


def auto_complete():
    if 'in_code' not in st.session_state: st.session_state.in_code = 'Type to complete...'
    res = code_editor(st.session_state.in_code)
    if len(res['id']) != 0 and (res['type'] == 'submit' or res['type'] == 'selection'):
        complete(res['text'])
    else: st.session_state.in_code = 'Type to complete...'