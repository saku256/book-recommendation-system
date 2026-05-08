import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="Book Recommendation System",
    layout="wide"
)

# Sidebar
st.sidebar.title("About")

st.sidebar.info(
    """
    This is a Machine Learning based Book Recommendation System.

    Select a book and get similar book recommendations instantly.
    """
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    margin-bottom: 40px;
}

.stSelectbox label {
    color: white !important;
    font-size: 20px;
}

.stButton > button {
    width: 100%;
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
}

.book-title {
    text-align: center;
    color: white;
    font-size: 16px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# Load data
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(book):

    index = books[books['title'] == book].index[0]

    distances = similarity[index]

    book_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_books = []
    recommended_posters = []

    for i in book_list:
        recommended_books.append(books.iloc[i[0]].title)
        recommended_posters.append(books.iloc[i[0]].image_url)

    return recommended_books, recommended_posters

# Title
st.markdown(
    '<div class="title">Book Recommendation System</div>',
    unsafe_allow_html=True
)

# Dropdown
selected_book = st.selectbox(
    "Search or Select a Book",
    books['title'].values
)
# Recommend button
# Recommend button
if st.button("Recommend"):

    with st.spinner("Finding similar books..."):

        names, posters = recommend(selected_book)

        cols = st.columns(5)

        for idx, col in enumerate(cols):

            with col:

                try:
                    st.image(posters[idx], width=150)

                except:
                    st.image(
                        "https://via.placeholder.com/150x220?text=No+Image",
                        width=150
                    )

                st.markdown(
                    f"""
                    <div style='
                        text-align: center;
                        color: white;
                        font-size: 16px;
                        margin-top: 10px;
                        min-height: 70px;
                    '>
                        {names[idx]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.markdown(
    """
    <hr>
    <div style='text-align:center; color:gray;'>
        Built with Streamlit and Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)


