from src.function.helper import split_documents, download_emb_embeddings
from src.loaddata.loaddata import documents

text_chunks = split_documents(documents)  
embeddings = download_emb_embeddings()