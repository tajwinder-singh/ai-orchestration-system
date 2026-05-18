from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Same embedding model must be reused during retrieval
# so query vectors exist in the same semantic space
# as stored document vectors.
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Loading locally generated FAISS artifacts.
# Safe here because the index is created internally,
# not from untrusted external uploads.
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,  
    allow_dangerous_deserialization=True  
)

retriever = vectorstore.as_retriever(  
    search_kwargs={"k": 3}
)