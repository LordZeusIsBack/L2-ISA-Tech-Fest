import streamlit as st

st.set_page_config(page_title="LLM Interface", layout="wide")

st.markdown('<div style="font-family: Montserrat, sans-serif; font-size: 2.5em; color: #ff4d4d; text-align: center;">LLM Interface</div>', unsafe_allow_html=True)
st.markdown('<div style="font-family: Roboto, sans-serif; font-size: 1.2em; color: #e0e0e0; text-align: center; margin-bottom: 40px;">Enter your prompt and see the magic happen!</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Input")
    user_input = st.text_area("Type your prompt here:", height=300)

with col2:
    st.markdown("### Output")
    if st.button("Generate Response"):
        llm_response = f"Simulated response based on your input: {user_input}"
        st.text_area("LLM Response", value=llm_response, height=300)
    else:
        st.text_area("LLM Response", value="The LLM response will appear here.", height=300)