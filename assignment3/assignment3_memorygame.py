import streamlit as st
import random

# Function to create a shuffled deck of cards
def create_deck():
    cards = list(range(1, 7))  # 6 unique cards
    random.shuffle(cards)
    return cards

# Streamlit app layout
st.title("Memory Sequence Game")
st.header("Try to remember the sequence of numbers!")

# Game state initialization
if "deck" not in st.session_state:
    st.session_state.deck = create_deck()
    st.session_state.show_cards = True
    st.session_state.attempted = False

# Display the game board
if st.session_state.show_cards:
    cols = st.columns(6)  # Create 6 columns for the cards
    for idx, card in enumerate(st.session_state.deck):
        cols[idx].markdown(f"<h1 style='text-align: center;'>{card}</h1>", unsafe_allow_html=True)
    
    # Button to hide cards and start the test
    if st.button("Start to Test Your Memory"):
        st.session_state.show_cards = False  # Hide cards immediately

# Input for the user's guessed sequence
if not st.session_state.show_cards:
    # Display prompt only after cards are hidden
    st.markdown("The numbers are hidden! Now enter the sequence you remember below:")
    user_input = st.text_input("Enter your sequence (separate numbers with commas):", "")
    
    if st.button("Submit"):
        st.session_state.attempted = True
        # Process the user's input
        user_sequence = [int(num.strip()) for num in user_input.split(",") if num.strip().isdigit()]

        if user_sequence == st.session_state.deck:
            st.success("Correct! 🎉 You remembered the sequence!")
        else:
            st.error("Incorrect! 😢 The correct sequence was: " + ", ".join(map(str, st.session_state.deck)))

# Restart button
if st.button("Restart Game"):
    st.session_state.deck = create_deck()
    st.session_state.show_cards = True
    st.session_state.attempted = False