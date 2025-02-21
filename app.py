import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

st.markdown(
    """
    <style>
        .stApp { background-color: #0A2540; color: white; }
        .container { 
            max-width: 700px;
            margin: auto;
            padding: 2rem;
            background: #1E3A5F;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        }
        h1, h2, h3 { color: #4DB3FF; text-align: center; }
        .stButton>button { background-color: #4DB3FF; color: #0A2540; font-size: 16px; border-radius: 8px; }
        .stButton>button:hover { background-color: #3A97D4; }
        .stTextInput>div>input, .stTextArea>div>textarea { background-color: #2B4865; color: white; border-radius: 8px; }
        .stSlider>div>div>div { background-color: #4DB3FF; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌱 Growth Mindset Challenge")
st.write("### Embrace challenges, persist through difficulties, and celebrate effort!")

st.header("What is a Growth Mindset?")
st.write(
    "A growth mindset is the belief that your abilities can improve through dedication and effort."
    " Popularized by Carol Dweck, it encourages resilience and lifelong learning."
)

st.header("Why Adopt a Growth Mindset?")
st.markdown("""
✅ **Embrace Challenges**: See obstacles as learning opportunities.  
✅ **Learn from Mistakes**: Use setbacks as stepping stones.  
✅ **Persist Through Difficulties**: Keep going even when it's hard.  
✅ **Celebrate Effort**: Recognize hard work, not just outcomes.  
✅ **Keep an Open Mind**: Adapt and stay curious.  
""")

st.header("📝 Reflect on Your Growth Mindset")
reflection = st.text_area("What challenges have you recently faced and how did you grow from them?")
if st.button("Submit Reflection"):
    st.success("Great job! Reflecting on growth helps strengthen your mindset.")

st.header("📊 Track Your Growth Mindset Progress")
st.write("Rate yourself on these mindset attributes (1 = Low, 5 = High):")
attributes = ["Embracing Challenges", "Learning from Mistakes", "Persisting Through Difficulties",
 "Celebrating Effort", "Keeping an Open Mind"]
rating = {attr: st.slider(attr, 1, 5, 3) for attr in attributes}

if st.button("Show Progress Chart"):
    df = pd.DataFrame([rating])
    fig, ax = plt.subplots(facecolor='#1E3A5F')
    ax.bar(df.columns, df.iloc[0], color='#4DB3FF')
    ax.set_ylim(1, 5)
    ax.set_ylabel("Self-Rating", color='white')
    ax.set_title("Growth Mindset Progress", color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    st.pyplot(fig)

# Daily Encouragement
st.header("🌟 Daily Encouragement")
encouragements = [
    "Keep pushing forward, every step counts!",
    "Mistakes are proof you are trying!",
    "Struggles lead to growth, embrace them!",
    "Your potential is limitless, keep learning!",
    "Hard work beats talent when talent doesn't work hard!"
]
st.info(random.choice(encouragements))


st.markdown(
    "<p style='text-align:center; font-size:18px; color:#4DB3FF;'><b>Every step—forward or backward—is part of learning. Believe in your growth! 😊</b></p>",
    unsafe_allow_html=True
)
