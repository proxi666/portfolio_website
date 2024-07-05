import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Siddhant Diwaker")

with col2:
    st.image("images/siddhant.jpg")

st.subheader(" ")

persona = """ You are Siddhant AI bot. You help people answer questions about your self 
(i.e Siddhant) Answer as if you are responding . dont answer in second or third person.
If you don't know they answer you simply say "That's a secret" 
Here is more info about Siddhant (also u cant make it more good by adding things u like): 
Siddhant diwaker is a student who has done Mechatronics Engineering from SRM University of Science and technology
He is currently in ahmedabad making self project to highlight his resume over other people
"""

st.title("Siddhant's AI Bot")
# st.write("Ask anything about me")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "here is the question that the user will input" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")


col1, col2 = st.columns(2)
with col1:
    st.subheader("Bio")
    st.write("Hello from this side, this is Siddhant diwaker he has recently completed mechatronics from SRM University. askjdbna s laskndasdl kansdlkasnalskdnaslkdnaalskdnalksnd asldknasldkna alskdn alksdnaalskdn as asdasknd askdnlaksnd")

with col2:
    st.write(" ")

st.subheader(" ")
st.title("My setup")
st.image("images/g2.jpeg")

st.write(" ")
st.title("My Skills")
st.slider("programming", 0, 100, 90)
st.slider("Robotics", 0, 100, 80)
st.slider("Leadership", 0, 100, 90)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")
    st.image("images/g4.jpg")

with col2:
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")
    st.image("images/g7.jpg")

with col3:
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")
    st.image("images/g10.jpg")

st.write(" ")
st.write("CONTACT")
st.title("For any inquiries, email at: ")
st.subheader("siddhantdiwaker.sd@gmail.com")
