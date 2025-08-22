import streamlit as st
from utils import loader,chunker,vectorstore,final_chain
import tempfile

st.image('ResearchPal_logo_wordmark.png')


uploaded_file = st.file_uploader("Upload a research paper", type="pdf")
query = st.text_input("Ask a question about the paper")

if uploaded_file and st.button("Generate Result"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    docs = loader.load_docs(tmp_file_path)
    chunks = chunker.chunk_docs(docs=docs)
    retriever = vectorstore.create_vector_store(chunks)
    response_chain = final_chain.output(retriever)

    response = response_chain.invoke(query)

    st.markdown("### Response:")
    st.write(response)


    #history
    