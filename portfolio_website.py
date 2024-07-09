import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page config
st.set_page_config(page_title="Siddhant Diwaker | Portfolio", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .css-18e3th9 {
        padding-top: 0rem;
        padding-bottom: 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
        padding-right: 1rem;
        padding-bottom: 3.5rem;
        padding-left: 1rem;
    }
    .stTitle {
        font-size: 4rem;
        font-weight: 700;
    }
    .stSubheader {
        font-size: 1.5rem;
    }
    .project-card {
        background-color: #f0f2f6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
def header():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Siddhant Diwaker")
        st.subheader("Mechatronics Engineer | AI Enthusiast | Innovator")
    with col2:
        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        st_lottie(lottie_coding, height=200, key="coding")

# About Section
def about():
    st.header("About Me")
    st.write("""
    I'm a recent graduate in Mechatronics Engineering from SRM University of Science and Technology, 
    with a passion for robotics, AI, and cutting-edge technology. Based in Ahmedabad, I'm actively 
    developing projects that showcase my skills in automation, machine learning, and system integration.
    
    My goal is to leverage my interdisciplinary background to create innovative solutions that bridge 
    the gap between mechanical systems and intelligent software.
    """)

# Skills Section
def skills():
    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        st.progress(90)
        st.caption("Python, C++, MATLAB")
    
    with col2:
        st.subheader("Robotics")
        st.progress(85)
        st.caption("ROS, Arduino, Sensor Integration")
    
    with col3:
        st.subheader("AI/ML")
        st.progress(80)
        st.caption("TensorFlow, PyTorch, Computer Vision")

# Projects Section
def projects():
    st.header("Featured Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.subheader("Autonomous Drone Navigation System")
            st.image("https://via.placeholder.com/400x200.png?text=Drone+Project")
            st.markdown("""
            <div class="project-card">
                • Developed a vision-based navigation system for drones<br>
                • Implemented SLAM algorithms for real-time mapping<br>
                • Achieved 95% accuracy in obstacle avoidance tests
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.subheader("Smart Manufacturing Process Optimizer")
            st.image("https://via.placeholder.com/400x200.png?text=Manufacturing+Project")
            st.markdown("""
            <div class="project-card">
                • Created an AI-driven system to optimize production lines<br>
                • Reduced manufacturing defects by 30%<br>
                • Integrated IoT sensors for real-time monitoring
            </div>
            """, unsafe_allow_html=True)

# Experience Section
def experience():
    st.header("Professional Experience")
    
    st.subheader("Robotics Research Intern | TechInnovate Labs")
    st.write("June 2023 - August 2023")
    st.markdown("""
    • Contributed to the development of an industrial robot arm with advanced grasping capabilities<br>
    • Implemented and fine-tuned machine learning models for object recognition<br>
    • Collaborated with a cross-functional team of engineers and researchers
    """)

# Education Section
def education():
    st.header("Education")
    
    st.subheader("B.Tech in Mechatronics Engineering")
    st.write("SRM University of Science and Technology | 2020 - 2024")
    st.write("CGPA: 3.8/4.0")
    st.markdown("""
    • Relevant Coursework: Robotics, Control Systems, Machine Learning, Embedded Systems<br>
    • Senior Project: Development of a Soft Robotic Gripper for Delicate Object Manipulation
    """)

# Contact Section
def contact():
    st.header("Get in Touch")
    col1, col2, col3 = st.columns([1,1,2])
    
    with col1:
        st.button("📧 Email Me")
    
    with col2:
        st.button("🔗 LinkedIn")
    
    with col3:
        st.text_input("Leave a message", placeholder="Your message here...")

# Main function to organize the layout
def main():
    header()
    about()
    skills()
    projects()
    experience()
    education()
    contact()
    
    st.markdown("---")
    st.markdown("© 2024 Siddhant Diwaker | All Rights Reserved")

if __name__ == "__main__":
    main()
