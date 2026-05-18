from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

loader = TextLoader("data/company_policy.txt") 
docs = loader.load() 

# Split documents into overlapping chunks so retrieval
# keeps enough surrounding context during semantic search.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

# Local embedding model used for converting text chunks
# into dense vectors for FAISS similarity search.
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Build FAISS index from embedded document chunks.
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local("faiss_index")

print("FAISS index built successfully")