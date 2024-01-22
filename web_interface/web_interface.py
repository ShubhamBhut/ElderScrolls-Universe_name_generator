import streamlit as st
from eso_names.raw_model import RNN
from eso_names.main import names_generator, names_recommendor

st.set_page_config(
    page_title="ESO Names Generator",
    page_icon=":crystal_ball:",
    layout="centered",
)

# App Header
st.title("ESO Names Generator and Recommender")

# Function to Generate Names
def generate_character_names():
    st.subheader("Character Name Generation")
    gender = st.selectbox("Select Gender", ["male", "female"])
    category = st.selectbox("Select Race/Category", ["Argonian", "Nord", "Khajiit", "Other"])
    start_letter = st.text_input("Starting Letter (Optional)")
    quantity = st.slider("Number of Names", 1, 10, 5)

    if st.button("Generate Names"):
        generated_names = names_generator(gender=gender, category=category, start_letter=start_letter, quantity=quantity)
        st.success(f"Generated Names: {', '.join(generated_names)}")

# Function to Recommend Names
def recommend_character_names():
    st.subheader("Character Name Recommendation")
    gender = st.selectbox("Select Gender", ["male", "female"])
    category = st.selectbox("Select Race/Category", ["Argonian", "Nord", "Khajiit", "Other"])
    start_letter = st.text_input("Starting Letter (Optional)")
    quantity = st.slider("Number of Names", 1, 10, 5)
    similarity_threshold = st.slider("Similarity Threshold", 1, 10, 5)
    similar_to = st.text_input("Similar To (Optional)")

    if st.button("Recommend Names"):
        recommended_names = names_recommendor(gender=gender, category=category, start_letter=start_letter, quantity=quantity, similarity_threshold=similarity_threshold, similar_to=similar_to)
        st.success(f"Recommended Names: {', '.join(recommended_names)}")

# Sidebar Navigation
menu_option = st.sidebar.radio("Select Option", ["Generate Names", "Recommend Names"])

# Main Content
if menu_option == "Generate Names":
    generate_character_names()
elif menu_option == "Recommend Names":
    recommend_character_names()
