from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from src.vector_store import docsearch as load_docsearch
from src.prompt.propmt import system_prompt

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    HumanMessagePromptTemplate.from_template("{input}")
])

chat_model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",   
    temperature=0
)

retriever = load_docsearch.as_retriever(search_type="similarity", k=3)

Question_answeer_chain = create_stuff_documents_chain(chat_model, prompt)

rag_chain = create_retrieval_chain(retriever, Question_answeer_chain)