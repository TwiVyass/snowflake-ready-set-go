import snowflake.connector
import streamlit as st
from mistralai import Mistral
import os
import hashlib
import pickle
import time
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Access the MISTRAL_API_KEY from environment variables
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)
embed_model = "mistral-embed"
generate_model = "open-mistral-7b"

# Cache for embeddings
embedding_cache_file = "embedding_cache.pkl"

# Load embedding cache
if os.path.exists(embedding_cache_file):
    with open(embedding_cache_file, "rb") as f:
        embedding_cache = pickle.load(f)
else:
    embedding_cache = {}

# Save embedding cache
def save_embedding_cache():
    with open(embedding_cache_file, "wb") as f:
        pickle.dump(embedding_cache, f)

# Snowflake connection
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE")
)

# Helper functions
def hash_text(text):
    """Generate a hash for the given text."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def generate_embeddings(texts):
    """Generate embeddings with caching."""
    embeddings = []
    for text in texts:
        text_hash = hash_text(text)
        if text_hash in embedding_cache:
            embeddings.append(embedding_cache[text_hash])
        else:
            try:
                embeddings_batch_response = client.embeddings.create(
                    model=embed_model,
                    inputs=[text]
                )
                embedding = embeddings_batch_response.data[0].embedding
                embedding_cache[text_hash] = embedding
                embeddings.append(embedding)
                save_embedding_cache()
            except Exception as e:
                print(f"Error generating embedding for text: {text}. Error: {e}")
                time.sleep(5)
                embeddings.append(None)
    return embeddings

def generate_text(prompt):
    """Generate text using the Mistral API."""
    MAX_INPUT_LENGTH = 1000
    if len(prompt) > MAX_INPUT_LENGTH:
        prompt = prompt[:MAX_INPUT_LENGTH]
    retries = 3
    while retries > 0:
        try:
            generation_response = client.chat.complete(
                model=generate_model,
                messages=[{"role": "user", "content": prompt}]
            )
            return generation_response.choices[0].message.content
        except Exception as e:
            print(f"Error generating text: {e}")
            time.sleep(10)
            retries -= 1
    return "Sorry, something went wrong. Please try again later."

def fetch_documents():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ID, CONTENT
        FROM knowledge_base
        LIMIT 5
    """)
    return cursor.fetchall()

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("Screenshot 2025-01-20 235204.png")

# Streamlit app
#st.title('Packing For Survival, Simplified')
st.markdown('<h1 style="text-align: center;">Packing For Survival, Simplified</h1>', unsafe_allow_html=True)


# Initialize session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("What's the emergency?"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate embedding for query
    query_embedding = generate_embeddings([user_input])[0]

    # Fetch relevant documents from Snowflake
    documents = fetch_documents()
    context = "\n".join([doc[1] for doc in documents])[:1000] if documents else ""

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Typing...")
    generated_response = generate_text(f"Context: {context}\nQuery: {user_input}\nResponse:")
    #placeholder.markdown(generated_response)

    # Generate response
    #generated_response = generate_text(f"Context: {context}\nQuery: {user_input}\nResponse:")

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(generated_response)

    # Add assistant's message to session state
    st.session_state.messages.append({"role": "assistant", "content": generated_response})
