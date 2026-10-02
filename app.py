import streamlit as st


st.set_page_config(page_title="Noongar Language Explorer", page_icon="📖")

st.markdown(
    """
    <style>
    .noongar-welcome {
        background: #fff7d8;
        border-left: 6px solid #e2bd24;
        border-bottom: 3px solid #a83225;
        border-radius: 0 4px 4px 0;
        padding: 1rem 1.25rem;
        margin: 0.5rem 0 1rem;
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

st.title("Noongar Language Explorer")
st.caption("Explore terms and translations from a published, approved source.")

st.sidebar.title("Navigation")
st.sidebar.radio("Choose a view", ["Home", "Terms", "Translation"], key="page")

if st.session_state["page"] == "Home":
    st.markdown(
        """
        <div class="noongar-welcome">
            <p class="direction">Noongar to English</p>
            <h2>Wanju / Wanjoo</h2>
            <p class="translation">Welcome</p>
        </div>
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