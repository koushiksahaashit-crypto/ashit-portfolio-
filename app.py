import streamlit as st

st.set_page_config(page_title="আশিত সাহা", layout="wide", initial_sidebar_state="expanded")

# থিম: ব্ল্যাক + লাইট গ্রিন গ্লো
st.markdown("""
    <style>
    .main { background-color: #000000; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; }
    h1, h2, h3 { 
        color: #90ee90; 
        text-shadow: 0 0 15px #90ee90, 0 0 30px #90ee90; 
        animation: glow 2s infinite alternate; 
    }
    @keyframes glow { from { text-shadow: 0 0 10px #90ee90; } to { text-shadow: 0 0 30px #90ee90; } }
    
    .fade-in { 
        animation: fadeInUp 1.8s ease-out forwards; 
        opacity: 0; 
    }
    @keyframes fadeInUp { 
        from { opacity: 0; transform: translateY(40px); } 
        to { opacity: 1; transform: translateY(0); } 
    }
    
    .stButton>button { 
        background-color: #90ee90; 
        color: black; 
        border: none; 
        border-radius: 12px; 
        padding: 12px 24px; 
        transition: all 0.3s ease; 
        box-shadow: 0 0 10px #90ee90; 
    }
    .stButton>button:hover { 
        transform: scale(1.1); 
        box-shadow: 0 0 25px #90ee90; 
    }
    
    /* পার্টিকল ব্যাকগ্রাউন্ড (হালকা গ্রিন স্পার্কল) */
    body::before { 
        content: ''; 
        position: fixed; 
        top: 0; left: 0; right: 0; bottom: 0; 
        background: radial-gradient(circle, rgba(144,238,144,0.05) 0%, transparent 70%); 
        pointer-events: none; 
        z-index: -1; 
        animation: sparkle 8s infinite; 
    }
    @keyframes sparkle { 0% { opacity: 0.3; } 50% { opacity: 0.8; } 100% { opacity: 0.3; } }
    </style>
""", unsafe_allow_html=True)

# সাইডবার অটো থাকবে (pages থেকে আসবে)
st.title("আশিত সাহা")
st.markdown("**AI Builder | Software Engineer | Bluebull Rider**")