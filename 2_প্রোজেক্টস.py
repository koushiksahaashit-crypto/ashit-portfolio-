import streamlit as st

st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.header("প্রোজেক্টস")
with st.expander("Ashit AI Chat"):
    st.write("লোকাল AI চ্যাটবট — বাংলায় কথা বলে, ইন্টারনেট ছাড়া চলে।")
with st.expander("AarotVision"):
    st.write("কালাইয়া অ্যারাতদার অ্যাসোসিয়েশনের জন্য ইনভেন্টরি + ক্যাশ ট্র্যাকার।")
with st.expander("Uprokritoo"):
    st.write("ফার্মারদের জন্য অ্যাগ্রো-টেক অ্যাপ — প্ল্যানিং ফেজ।")
st.markdown('</div>', unsafe_allow_html=True)