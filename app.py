import streamlit as st


st.set_page_config(page_title="Noongar Language Explorer", page_icon="📖")

st.markdown(
    """
    <style>
    @media (min-width: 768px) {
        section[data-testid="stSidebar"] {
            width: 12rem !important;
            min-width: 12rem !important;
            flex-basis: 12rem !important;
        }
    }
    .noongar-welcome {
        background: #fff7d8;
        border-top: 6px solid #e2bd24;
        border-bottom: 3px solid #a83225;
        border-radius: 4px;
        padding: 1.25rem;
        margin: 0.5rem 0 1rem;
        text-align: center;
    }
    .noongar-welcome .direction {
        color: #67502a;
        font-size: 0.8rem;
        margin: 0;
    }
    .noongar-welcome h2 {
        color: #a83225;
        font-size: 1.7rem;
        letter-spacing: 0;
        margin: 0.25rem 0;
    }
    .noongar-welcome .translation {
        color: #30291f;
        margin: 0;
    }
    .home-title {
        color: #30291f;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0.75rem 0 0.25rem;
        text-align: center;
    }
    .home-caption {
        color: #67502a;
        margin: 0 0 1rem;
        text-align: center;
    }
    .home-wave-border {
        position: fixed;
        top: 9vh;
        right: 0;
        width: 5rem;
        height: 82vh;
        pointer-events: none;
        z-index: 0;
    }
    @media (max-width: 900px) {
        .home-wave-border {
            display: none;
        }
    }
    .stButton button[kind="primary"] {
        background-color: #a83225;
        border-color: #a83225;
        color: white;
    }
    .stButton button[kind="primary"]:hover {
        background-color: #e2bd24;
        border-color: #e2bd24;
        color: #30291f;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def navigate_to(page):
    st.session_state["page"] = page


if "page" not in st.session_state:
    st.session_state["page"] = "Home"

st.sidebar.title("Navigation")
st.sidebar.radio("Choose a view", ["Home", "Terms", "Translation"], key="page")

if st.session_state["page"] == "Home":
    st.markdown(
        """
        <svg class="home-wave-border" viewBox="0 0 100 640" preserveAspectRatio="none" aria-hidden="true" focusable="false">
            <path d="M100 0 L55 0 C10 40 10 120 55 160 C100 200 100 280 55 320 C10 360 10 440 55 480 C100 520 100 600 55 640 L100 640 Z" fill="#e2bd24" />
            <path d="M100 0 L82 0 C62 40 62 120 82 160 C100 200 100 280 82 320 C62 360 62 440 82 480 C100 520 100 600 82 640 L100 640 Z" fill="#a83225" />
        </svg>
        <div class="noongar-welcome">
            <p class="direction">Noongar to English</p>
            <h2>Wanju / Wanjoo</h2>
            <p class="translation">Welcome</p>
        </div>
        <div class="home-title">Noongar Language Explorer</div>
        <p class="home-caption">Explore terms and translations from a published, approved source.</p>
        """,
        unsafe_allow_html=True,
    )
    st.write("Choose a section to get started.")

    st.subheader("Aboriginal Flag")
    st.image(
        "https://media.australian.museum/media/dd/images/Some_image.width-1600.9bc6ad1.jpg",
        caption="Image: Harold Joseph Thomas © First Nations | Source: Australian Museum",
        width=480,
    )

    terms_column, translation_column = st.columns(2)

    with terms_column:
        st.subheader("Terms")
        st.write("Browse terms from your selected dataset.")
        st.button(
            "Open Terms",
            on_click=navigate_to,
            args=("Terms",),
            type="primary",
            use_container_width=True,
        )

    with translation_column:
        st.subheader("Translation")
        st.write("Look up a term using the published dataset.")
        st.button(
            "Open Translation",
            on_click=navigate_to,
            args=("Translation",),
            type="primary",
            use_container_width=True,
        )

elif st.session_state["page"] == "Terms":
    st.header("Terms")
    st.text_input("Search terms")
    st.info("Your approved terms dataset will be displayed here.")

else:
    st.header("Translation")
    st.text_input("Enter a term to search")
    st.button("Search")
    st.info("Search results will appear here after you connect your approved dataset.")