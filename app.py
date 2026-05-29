import streamlit as st
from api_caliing_app import joke_generator


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Moriyom Daily Joke 💖",
    page_icon="😂",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* GOOGLE FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* BACKGROUND */
.stApp{
    background: linear-gradient(135deg,#ffe0ef,#f7d6ff);
}

/* REMOVE HEADER */
header{
    visibility:hidden;
}

/* MAIN TITLE */
.main-title{
    text-align:center;
    font-size:65px;
    font-weight:800;
    color:#ff2f7d;
    margin-top:20px;
    margin-bottom:10px;
}

/* SUBTITLE */
.subtitle{
    text-align:center;
    color:#6b2d5c;
    font-size:24px;
    margin-bottom:30px;
}

/* JOKE CARD */
.joke-card{
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(5px);
    border-radius:30px;
    padding:35px;
    box-shadow:0 10px 35px rgba(0,0,0,0.1);
    margin-top:25px;
}

/* JOKE TEXT */
.joke-text{
    font-size:36px;
    color:#8b1458;
    line-height:1.7;
    font-weight:600;
    text-align:center;
}

/* BUTTON */
.stButton>button{
    width:100%;
    height:70px;
    border:none;
    border-radius:20px;
    background: linear-gradient(90deg,#ff4b91,#ff6bcf);
    color:white;
    font-size:28px;
    font-weight:bold;
    margin-top:25px;
    transition:0.3s;
    box-shadow:0 8px 25px rgba(255,75,145,0.3);
}

.stButton>button:hover{
    transform:scale(1.02);
}

/* INFO BOX */
.info-box{
    background:#fbe7ff;
    padding:22px;
    border-radius:25px;
    margin-top:30px;
    color:#8d2f6f;
    font-size:20px;
    box-shadow:0 5px 15px rgba(0,0,0,0.05);
    text-align:center;
}

/* FOOTER */
.footer{
    text-align:center;
    color:#7d4263;
    margin-top:35px;
    font-size:18px;
}

/* FLOATING EMOJI */
.heart{
    position:fixed;
    font-size:30px;
    animation: float 5s infinite ease-in-out;
}

@keyframes float{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-20px);}
    100%{transform:translateY(0px);}
}

/* ---------------- MOBILE RESPONSIVE ---------------- */

@media (max-width:768px){

.main-title{
    font-size:38px;
    line-height:1.3;
}

.subtitle{
    font-size:18px;
    padding:0 10px;
}

.joke-card{
    padding:20px;
    border-radius:20px;
}

.joke-text{
    font-size:24px;
    line-height:1.5;
}

.stButton>button{
    height:58px;
    font-size:22px;
    border-radius:15px;
}

.info-box{
    font-size:17px;
    padding:18px;
}

.footer{
    font-size:15px;
}

.heart{
    font-size:22px;
}

}

</style>
""", unsafe_allow_html=True)

# ---------------- FLOATING EMOJI ----------------
st.markdown("""
<div class="heart" style="top:5%; left:5%;">💖</div>
<div class="heart" style="top:15%; right:8%;">✨</div>
<div class="heart" style="bottom:10%; left:10%;">💕</div>
""", unsafe_allow_html=True)



# ---------------- TITLE ----------------
st.markdown("""
<div class="main-title">
💖 Moriyom Daily Joke 😂
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Every click gives a new funny joke for my crush 💕
</div>
""", unsafe_allow_html=True)

# ---------------- IMAGE ----------------
st.image(
    "Couple chibi.jpeg",
    use_container_width=True
)

# ---------------- SESSION STATE ----------------
if "joke" not in st.session_state:
    st.session_state.joke = "🎉 Click the button to generate a joke 💖"

# ---------------- JOKE CARD ----------------
with st.container():
    st.markdown(f"""
    <div class="joke-card">
        <div class="joke-text">
        {st.session_state.joke}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- BUTTON ----------------
if st.button("🎉 Generate New Joke"):
    with st.spinner("Voot is writing new joke... 💖"):
        st.markdown("""
        <div style="text-align:center; font-size:22px; color:red; font-weight:700;">
        💖 Voot is writing new joke...
        </div>
    """, unsafe_allow_html=True)
        st.session_state.joke = joke_generator()
        st.rerun()

# ---------------- BUTTON ----------------
# button = st.button("🎉 Generate New Joke")
# with st.container(border=True):
#     if button:
#         with st.spinner("Voot is writing new joke"):
#             generate_joke = joke_generator()
#             st.markdown(generate_joke)

# ---------------- INFO BOX ----------------
st.markdown("""
<div class="info-box">
💡 <b>Did you know?</b><br><br>
A smile can make my whole day better 😄
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Made with 💖 for someone special (Moriyom) 🌸
</div>
""", unsafe_allow_html=True)