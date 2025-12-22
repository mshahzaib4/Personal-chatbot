from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain_core.documents import Document

def load_pdf_file(file_path):
    # Load the PDF document
    loader = TextLoader(file_path)
    documents = loader.load()   
    return documents


# only select pagecontent attribute from Document
def extract_page_contents(docs: List[Document]) -> List[str]:
    return [doc.page_content for doc in docs]


def split_documents(documents):
    # If documents are strings, convert them to Document objects
    if isinstance(documents, str):
        documents = [Document(page_content=documents)]
    elif documents and isinstance(documents[0], str):
        documents = [Document(page_content=doc) for doc in documents]
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)
    return docs

def download_emb_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

