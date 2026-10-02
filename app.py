import streamlit as st


st.set_page_config(page_title="Noongar Language Explorer", page_icon="📖")


def navigate_to(page):
    st.session_state["page"] = page


if "page" not in st.session_state:
    st.session_state["page"] = "Home"

st.title("Noongar Language Explorer")
st.caption("Explore terms and translations from a published, approved source.")

st.sidebar.title("Navigation")
st.sidebar.radio("Choose a view", ["Home", "Terms", "Translation"], key="page")

if st.session_state["page"] == "Home":
    st.header("Welcome")
    st.write("Choose a section to get started.")

    terms_column, translation_column = st.columns(2)

    with terms_column:
        st.subheader("Terms")
        st.write("Browse terms from your selected dataset.")
        st.button(
            "Open Terms",
            on_click=navigate_to,
            args=("Terms",),
            use_container_width=True,
        )

    with translation_column:
        st.subheader("Translation")
        st.write("Look up a term using the published dataset.")
        st.button(
            "Open Translation",
            on_click=navigate_to,
            args=("Translation",),
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