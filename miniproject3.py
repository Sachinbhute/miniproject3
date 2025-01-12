from altair import themes
import streamlit as st

ans_list = []

st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f9 !important;
    }
    h1 {
        font-family: 'Arial', sans-serif;
        font-size: 50px;
    }
    p {
        font-family: 'Helvetica', sans-serif;
    }
    .stRadio > div > label {
        font-size: 22px;
        color: #4a4a4a;
    }
    .stRadio > div > div > label > div {
        background-color: #e0f7fa;
        border-radius: 10px;
        padding: 5px;
        transition: 0.3s;
    }
    .stRadio > div > div > label:hover > div {
        background-color: #4CAF50;
        color: white;
    }
    .stRadio > div > div > label > div::before {
        color: #4CAF50;
    }
    .stButton button {
        background-color: #FF9800;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 20px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #FF5722;
    }
    .tips {
        background-color: #e8f5e9;
        padding: 15px;
        border-left: 5px solid #4CAF50;
        font-size: 18px;
        margin-top: 20px;
        border-radius: 10px;
        color: #000000;
    }
    </style>
    <h1 style='text-align: center; color: #4CAF50;'>Know Your Learning Style</h1>
    <p style='text-align: center; color: gray; font-size: 18px;'>
        Answer these questions to discover your preferred learning method!
    </p>
    <hr>
    """, 
    unsafe_allow_html=True
)


options1 = ["Watching a video or diagram", "Listening to a lecture or podcast", 
            "Reading instructions or writing notes", "Hands-on practice or experimenting"]
choice1 = st.radio(
    "1. When trying to learn something new, what method do you naturally prefer?", 
    options1
)
ans_list.append(options1.index(choice1) + 1)

options2 = ["Charts, graphs, or diagrams", "Recordings or group discussions", 
            "Written summaries or textbooks", "Practice tests or building models"]
choice2 = st.radio(
    "2. What type of resource do you find most helpful when preparing for an exam or project?", 
    options2
)
ans_list.append(options2.index(choice2) + 1)


options3 = ["Draw it out or create a flowchart", "Talk it through or listen to an explanation", 
            "Write down the steps to analyze", "Experiment physically or try trial-and-error"]
choice3 = st.radio(
    "3. When you are solving a problem, how do you prefer to approach it?", 
    options3
)
ans_list.append(options3.index(choice3) + 1)


options4 = ["By picturing them in my head", "By saying them aloud or hearing someone explain", 
            "By writing them down repeatedly", "By doing the task or moving around"]
choice4 = st.radio(
    "4. How do you remember things best?", 
    options4
)
ans_list.append(options4.index(choice4) + 1)

options5 = ["Visual aids like slides or videos", "The speaker's tone and explanations", 
            "Taking notes to review later", "Being actively involved or working alongside the presentation"]
choice5 = st.radio(
    "5. What helps you stay focused during a lecture or presentation?", 
    options5
)
ans_list.append(options5.index(choice5) + 1)


options6 = ["I visualize the scenes or information", "I remember how it sounded or was described", 
            "I think of specific phrases or passages", "I imagine myself experiencing the events"]
choice6 = st.radio(
    "6. When you read a book, how do you usually recall the content?", 
    options6
)
ans_list.append(options6.index(choice6) + 1)

options7 = ["Art, design, or puzzles", "Listening to music or podcasts", 
            "Reading or writing stories or essays", "Sports, crafts, or DIY projects"]
choice7 = st.radio(
    "7. What kind of activities do you enjoy most?", 
    options7
)
ans_list.append(options7.index(choice7) + 1)

options8 = ["Use landmarks or sketches to guide", "Give step-by-step verbal instructions", 
            "Write down the route", "Prefer to physically show the way"]
choice8 = st.radio(
    "8.When giving directions, how do you usually explain?", 
    options8
)
ans_list.append(options8.index(choice8) + 1)

options9 = ["When I can visualize or recreate it in my mind", "When I can explain it to someone else", 
            "When I have written a detailed summary", "When I have successfully practiced or applied it"]
choice9 = st.radio(
    "9. How do you feel most confident after learning something new?", 
    options9
)
ans_list.append(options9.index(choice9) + 1)

options10 = ["Lack of visuals", "Poor audio quality or unclear explanations", 
            "Lack of detailed written instructions", "Not being able to try it hands-on"]
choice10 = st.radio(
    "What frustrates you most while learning?", 
    options10
)
ans_list.append(options10.index(choice10) + 1)




if st.button("Know Your Score"):
    
    v, a, k, w = 0, 0, 0, 0
    for ele in ans_list:
        if ele == 1:
            v += 1
        elif ele == 2:
            a += 1
        elif ele == 3:
            w += 1
        else:
            k += 1

   
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <h2>Your Learning Style</h2>
            <p>You are:</p>
            <p style='font-size: 20px; color: #4CAF50;'>🌟 {v / 10:.2%} Visual</p>
            <p style='font-size: 20px; color: #FF9800;'>🎧 {a / 10:.2%} Auditory</p>
            <p style='font-size: 20px; color: #03A9F4;'>✍️ {w / 10:.2%} Writer</p>
            <p style='font-size: 20px; color: #9C27B0;'>🛠️ {k / 10:.2%} Kinesthetic</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    scores = {
        "Visual": v / len(ans_list),
        "Auditory": a / len(ans_list),
        "Writer": w / len(ans_list),
        "Kinesthetic": k / len(ans_list)
    }
    dominant_style = max(scores, key=scores.get)

    tips = {
        "Visual": [
            "Use visual aids like diagrams, charts, and videos.",
            "Try mind mapping to organize your thoughts.",
            "Color-code your notes to make them more engaging."
        ],
        "Auditory": [
            "Listen to podcasts or audiobooks to absorb information.",
            "Discuss topics in a group to reinforce understanding.",
            "Repeat information aloud to help remember it."
        ],
        "Writer": [
            "Take detailed notes in your own words.",
            "Create summaries or outlines of what you've learned.",
            "Use flashcards to reinforce key points."
        ],
        "Kinesthetic": [
            "Engage in hands-on activities like labs or experiments.",
            "Use simulations or role-playing to understand concepts.",
            "Practice by doing rather than just observing."
        ]
    }

    st.markdown(f"### Your Dominant Learning Style: **{dominant_style}**")
    st.markdown("### Here are some tips to help you learn faster:")
    for tip in tips[dominant_style]:
        st.markdown(f"<div class='tips'>🔹 {tip}</div>", unsafe_allow_html=True)
