from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import load_prompt
from llama_index import GPTIndex, SimpleDirectoryReader
from langchain.retrievers import Retriever
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

# Set up your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Initialize the LLM (Language Model)
llm = OpenAI(temperature=0.7)

# Create a memory object to store conversation history
memory = ConversationBufferMemory()

# Create the conversational chain using LangChain's ConversationChain
conversation_chain = ConversationChain(
    llm=llm,
    memory=memory
)

# Initialize the llamaindex (GPT Index) and load a knowledge base from a directory
documents = SimpleDirectoryReader('knowledge_base').load_data()
gpt_index = GPTIndex.from_documents(documents)

# Set up the RAG (Retrieval-Augmented Generation) design
embeddings = OpenAIEmbeddings()
vector_store = Chroma.from_documents(documents, embeddings)
retriever = Retriever(vector_store=vector_store)

# Function to interact with the chatbot
def chat_with_bot(input_text):
    # First, try to retrieve relevant information using the retriever
    retrieved_docs = retriever.retrieve(input_text)
    if retrieved_docs:
        context = "\n".join([doc.page_content for doc in retrieved_docs])
        response = llm(f"Context: {context}\nQuestion: {input_text}")
        return response
    else:
        # If no relevant information found in the retriever, query the knowledge base using llamaindex
        response_from_knowledge_base = gpt_index.query(input_text)
        if response_from_knowledge_base:
            return response_from_knowledge_base.response
        else:
            # If no relevant information found in knowledge base, continue with the conversation chain
            response = conversation_chain.run(input_text)
            return response

if __name__ == "__main__":
    print("Hello! I am an AI FAQ chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_with_bot(user_input)
        print(f"Bot: {response}")
