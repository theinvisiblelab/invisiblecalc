import streamlit as st
import random

# Set page to wide mode
st.set_page_config(page_icon="🕯️", page_title="the (in)visible lab")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("🕯️ The (In)visible Lab")
st.write(":gray[_Enabling fairer knowledge access_]")
st.write("&nbsp;")

st.header("🔦 Discover")

st.sidebar.info("The (In)visible Lab is housed in the Amsterdam School of Communication Research, University of Amsterdam. Please reach out to our [team](https://theinvisiblelab.streamlit.app/team) for more information.")

# Define a list of films as above
films = [
    {
        "title": "The Invisible Man",
        "director": "James Whale",
        "year": 1933,
        "plot": "After developing a way to become invisible, Dr. Jack Griffin, a scientist, becomes tragically insane and vengeful."
    },
    {
        "title": "Hollow Man",
        "director": "Paul Verhoeven",
        "year": 2000,
        "plot": "Scientists discover how to make humans invisible, but their test subject becomes an insane killer who stalks the team."
    },
    {
        "title": "Memoirs of an Invisible Man",
        "director": "John Carpenter",
        "year": 1992,
        "plot": "After a freak accident, a man is rendered invisible and becomes pursued by a ruthless government agent."
    },
    {
        "title": "The Invisible",
        "director": "David S. Goyer",
        "year": 2007,
        "plot": "A teenager is attacked and left for dead, but finds himself trapped in a ghostly limbo where no one can see him."
    },
    {
        "title": "Invisible Agent",
        "director": "Edwin L. Marin",
        "year": 1942,
        "plot": "The grandson of the original Invisible Man uses his grandfather's formula to spy on Nazi Germany during WWII."
    },
    {
        "title": "The Invisible Woman",
        "director": "A. Edward Sutherland",
        "year": 1940,
        "plot": "A department store model volunteers for an experiment with an invisibility machine."
    },
    {
        "title": "Invisibility",
        "director": "Paolo Bertola",
        "year": 2013,
        "plot": "Explores the concept of invisibility from a philosophical perspective, questioning the visibility in society and relationships."
    },
    {
        "title": "The Invisible Boy",
        "director": "Gabriele Salvatores",
        "year": 2014,
        "plot": "A shy and unassuming boy discovers he has the power to become invisible, leading him on an unexpected adventure."
    },
    {
        "title": "The Invisible Man Returns",
        "director": "Joe May",
        "year": 1940,
        "plot": "Accused of a murder he didn't commit, a man uses an invisibility formula to escape prison and clear his name."
    },
    {
        "title": "The Invisible Man's Revenge",
        "director": "Ford Beebe",
        "year": 1944,
        "plot": "A man uses an invisibility formula to exact revenge on those he believes have wronged him."
    },
    {
        "title": "Abbott and Costello Meet the Invisible Man",
        "director": "Charles Lamont",
        "year": 1951,
        "plot": "The comedy duo helps a man wrongly accused of murder, who uses an invisibility serum to evade the police."
    },
    {
        "title": "Invisible Sister",
        "director": "Paul Hoen",
        "year": 2015,
        "plot": "A science project goes awry, making a teenager's sister become invisible, leading to unexpected antics and a closer bond."
    },
    {
        "title": "The Amazing Transparent Man",
        "director": "Edgar G. Ulmer",
        "year": 1960,
        "plot": "An ex-army major uses a prisoner to become invisible and steal nuclear material for an experiment."
    },
    {
        "title": "Invisible Avenger",
        "director": "James Wong Howe, Ben Parker",
        "year": 1958,
        "plot": "A man with the power of invisibility is drawn into a conflict with a gangster to protect a refugee."
    },
    {
        "title": "The League of Extraordinary Gentlemen",
        "director": "Stephen Norrington",
        "year": 2003,
        "plot": "A team of extraordinary figures, including an invisible man, is assembled to stop a terrorist plot."
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "director": "Chris Columbus",
        "year": 2001,
        "plot": "A young wizard finds an invisibility cloak, which plays a crucial role in his adventures at Hogwarts."
    },
    {
        "title": "Predator",
        "director": "John McTiernan",
        "year": 1987,
        "plot": "A commando unit in the Central American jungle faces off against an alien warrior that uses invisibility to hunt."
    },
    {
        "title": "Ghost in the Shell",
        "director": "Rupert Sanders",
        "year": 2017,
        "plot": "In the near future, a cyber-enhanced soldier hunts down a hacker, using therm-optic camouflage to become invisible."
    },
    {
        "title": "The Invisible Maniac",
        "director": "Adam Rifkin",
        "year": 1990,
        "plot": "A mad scientist escapes from a mental institution and becomes a high school physics teacher, with deadly consequences."
    },
    {
        "title": "Invisible Strangler",
        "director": "John Florea",
        "year": 1976,
        "plot": "An invisible man escapes from an asylum and seeks vengeance against those responsible for his wrongful imprisonment."
    }
]

# Dropdown for page
st.write("Choose a category to explore invisible content.")
tab1, tab2, tab3, tab4 = st.tabs(['Films', 'Music', 'Books', 'News'])

with tab1:

    if st.button('Find an invisible film!'):
        st.write("&nbsp;")
        selected_film = random.choice(films)

        st.write(f"**{selected_film['title']}** ({selected_film['year']})")

        random_number = random.randint(1, 250)
        image_url = f"https://picsum.photos/id/{random_number}/200/300"
        st.markdown(f"<img src='{image_url}'/>", unsafe_allow_html=True)

        st.write("&nbsp;")
        st.write(selected_film['plot'])

        table_markdown = f"""
        | Title          | Director       | Year |
        |----------------|----------------|------|
        | {selected_film['title']} | {selected_film['director']} | {selected_film['year']} |
        """
        st.markdown(table_markdown)

        st.write("&nbsp;")
        st.info("Dummy responses above! Application under development...")

with tab2:
    # Here, you can add functionality to find invisible music.
    # Since we're dealing with dummy responses for now:
    if st.button('Find an invisible piece of music!'):
        st.info("Application under development...")

with tab3:
    # Similarly, add functionality for finding invisible books.
    if st.button('Find an invisible book!'):
        st.info("Application under development...")

with tab4:
    # And functionality for finding invisible news.
    if st.button('Find some invisible news!'):
        st.info("Application under development...")