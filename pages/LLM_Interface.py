from ai_model import AIModel, ChatSession
import streamlit as st

def configure_page():
    """Configures Streamlit page settings"""
    st.set_page_config(
        page_title="LLM Interface",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def display_header():
    """Displays the header and subheader"""
    st.markdown(
        '<div style="font-family: Montserrat, sans-serif; font-size: 2.5em; color: #ff4d4d; '
        'text-align: center;">LLM Interface</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-family: Roboto, sans-serif; font-size: 1.2em; color: #e0e0e0; '
        'text-align: center; margin-bottom: 40px;">Enter your prompt and see the magic happen!</div>',
        unsafe_allow_html=True
    )

def handle_input_column():
    """Creates and manages the input column"""
    with st.container():
        st.markdown("### Input")
        return st.text_area("Type your prompt here:", height=300, key="user_input")

def display_output_column(user_input):
    """Creates and manages the output column with response generation"""
    with st.container():
        st.markdown("### Output")
        
        if st.button("Generate Response", key="generate_btn"):
            response = generate_response(user_input)
            st.text_area("LLM Response", value=response, height=300, key="response_output")
        else:
            st.text_area("LLM Response", value="The LLM response will appear here.", 
                        height=300, key="placeholder_output")

def generate_response(user_input):
    """Generates mock LLM response (Replace with actual model integration)"""
    return f"Simulated response based on your input: {user_input}"

def main():
    """Main function to orchestrate the app layout and functionality"""
    configure_page()
    display_header()
    
    col1, col2 = st.columns(2)
    with col1:
        user_input = handle_input_column()
    with col2:
        display_output_column(user_input)

if __name__ == "__main__":
    main()
