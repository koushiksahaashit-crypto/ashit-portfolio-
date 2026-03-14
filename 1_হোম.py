import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.header("হোম")
st.write("আমি আশিত—AI-এর ম্যাজিক দিয়ে বাংলা বানাই।")
st.markdown('<span style="animation: pulse 2s infinite;">✨</span> এই সাইটটা দেখে মনে হচ্ছে ম্যাজিক, তাই না?', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# পালস ইফেক্ট (যাদুর স্পার্কল)
st.markdown("""
    <style>
    @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.2); } 100% { transform: scale(1); } }
    </style>
""", unsafe_allow_html=True)