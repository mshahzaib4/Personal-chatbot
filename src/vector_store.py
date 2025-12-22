from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.constants.constants import PC
from src.Perprocessing.preprocessing import text_chunks, embeddings

index_name = "chatbot"
try:
    PC.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
except Exception as e:
    if "already exists" in str(e).lower():
        pass  
    else:
        raise  
index = PC.Index(index_name)


index_name = "chatbot"
try:
    PC.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
except Exception as e:
    if "already exists" in str(e).lower():
        pass  
    else:
        raise  


# Load the index from Pinecone
index = PC.Index(index_name)
docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

docsearch.add_documents(text_chunks) 