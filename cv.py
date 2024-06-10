import streamlit as st

# Font Awesome 스타일을 포함한 HTML 추가
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# 스타일 추가
st.markdown("""
    <style>
        .contact-info {
            text-align: center;  /* 가운데 정렬 */
        }
        .contact-info p {
            margin: 0;  /* 기본 여백 제거 */
        }
        .contact-info a {
            color: inherit !important;  /* 글꼴 색상을 상속받음 */
            text-decoration: none !important;  /* 밑줄 제거 */
        }
        .contact-info i {
            margin-right: 10px;  /* 아이콘과 텍스트 사이에 간격 추가 */
        }
        .contact-info span {
            margin: 0 20px;  /* 항목 사이에 간격 추가 */
        }
        .container {
            display: flex;
            justify-content: space-between;
            width: 100%;
        }
        .left {
            flex: 1;
            text-align: left;
        }
        .right {
            flex: 1;
            text-align: right;
        }
        .clearfix::after {
            content: "";
            clear: both;
            display: table;
        }
        .section-title {
            font-variant: small-caps;
            font-size: 2vw;
        }
        @media (max-width: 768px) {
            .section-title {
                font-size: 4vw;
            }
            h1 {
                font-size: 6vw;
            }
            .contact-info {
                font-size: 4vw;
            }
            .container {
                flex-direction: column;
                align-items: flex-start;
            }
            .left, .right {
                text-align: left;
                width: 100%;
            }
        }
    </style>
""", unsafe_allow_html=True)

# 제목과 소개 (가운데 정렬, 반응형 글씨 크기 및 Small Caps 적용)
st.markdown("<h1 style='text-align: center; font-variant: small-caps;'>Minhyuk Choi</h1>", unsafe_allow_html=True)

# 기본 정보
st.markdown("""
    <div class="contact-info">
        <p>
            <i class="fas fa-envelope"></i><a href="mailto:m120971209@gmail.com">m120971209@gmail.com</a>
            <span>|</span>
            <i class="fas fa-phone"></i> +82-10-9152-9812
            <span>|</span>
            <i class="fas fa-home"></i><a href="https://mhc-cv.streamlit.app" target="_blank">mhc-cv.streamlit.app</a>
        </p>
    </div>
""", unsafe_allow_html=True)

# Interests
st.markdown("---")
st.markdown("<h2 class='section-title'>Interests</h2>", unsafe_allow_html=True)
st.write("""
I am currently interested in Machine Learning and Information Security. After this semester, I plan to study Algorithms, Backend Development, Machine Learning, Mathematics, and English.
""")

# Educations
st.markdown("---")
st.markdown("<h2 class='section-title'>Educations</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class="container clearfix">
        <div class="left">
            <strong>Inha Technical College</strong><br>
            <em>Majoring in Computer Systems Engineering</em>
            <div>GPA: <b>4.43</b> / 4.5</div>
        </div>
        <div class="right">
            <strong>Mar 2018 – Current</strong><br>
            <em>Incheon, Republic of Korea</em>
        </div>
    </div>
""", unsafe_allow_html=True)

# Services
st.markdown("---")
st.markdown("<h2 class='section-title'>Services</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class="container clearfix">
        <div class="left">
            <strong>Republic of Korea Air Force</strong><br>
            <em>Information Systems Operator</em>
        </div>
        <div class="right">
            <strong>Sep 2021 – Jun 2023</strong><br>
            <em>Seoul, Republic of Korea</em>
        </div>
    </div>
""", unsafe_allow_html=True)

# Technical Skills
st.markdown("---")
st.markdown("<h2 class='section-title'>Technical Skills</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class="container clearfix">
        <div class="left">
            <strong>Programming</strong><br>
            <strong>Languages</strong><br>
        </div>
        <div class="right">
            <div>Python, Java, C++</div>
            <div>Korean (Native), English</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 끝
st.write("Thank you for reviewing my CV!")