import streamlit as st
import os

def configure_page():
    """Sets up the page configuration and removes sidebar"""
    st.set_page_config(
        page_title="Beat the AI - Level 2",
        page_icon="🤖",
        layout="wide"
    )
    # Hide sidebar using CSS injection
    st.markdown("""
        <style>
            [data-testid="stSidebar"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

def apply_custom_styles():
    """Defines and applies all custom CSS styles"""
    styles = """
    <style>
        body {
            background-color: #1e1e1e;
            color: #f0f0f0;
        }
        .edgy-header {
            font-family: 'Montserrat', sans-serif;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #ff4d4d;
            margin-top: 50px;
            margin-bottom: 20px;
        }
        .edgy-subheader {
            font-family: 'Roboto', sans-serif;
            font-size: 1.5em;
            text-align: center;
            color: #e0e0e0;
            margin-bottom: 50px;
        }
        .edgy-button {
            background-color: #ff4d4d;
            border: none;
            color: #1e1e1e;
            padding: 10px 24px;
            text-align: center;
            font-size: 1.2em;
            margin: 4px 2px;
            border-radius: 8px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .edgy-button:hover {
            background-color: #e60000;
            transform: scale(1.05);
        }
    </style>
    """
    st.markdown(styles, unsafe_allow_html=True)

def display_header():
    """Renders the main header and subheader"""
    st.markdown(
        '<div class="edgy-header">Beat the AI - Level 2</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="edgy-subheader">Show your skills and outsmart the machines!</div>',
        unsafe_allow_html=True
    )

def main_content():
    """Displays the core content and interaction logic"""
    st.write("Welcome to the ultimate showdown against AI. Prepare for battle in our competition!")
    
    if st.button("Join the Challenge", key="join", help="Click to join the event"):
        if os.path.exists('history.txt'): os.remove('history.txt')
        if os.path.exists('attempts.txt'): os.remove('attempts.txt')
        with open('history.txt', 'w') as fp: pass
        with open('attempts.txt', 'w') as fp: fp.write(str(0))
        st.switch_page("pages/LLM_Interface.py")

def main():
    """Main application orchestration"""
    configure_page()
    apply_custom_styles()
    display_header()
    main_content()

if __name__ == "__main__":
    main()
