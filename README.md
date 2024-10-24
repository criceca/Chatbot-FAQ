# AI FAQ Chatbot with RAG Design

This project is an AI chatbot that uses `langchain` and `llamaindex` (GPTIndex) to respond to user queries in a conversational manner. The chatbot is enhanced by a Retrieval-Augmented Generation (RAG) design, which allows it to retrieve relevant information from a knowledge base and generate accurate responses. The bot works as an FAQ assistant, leveraging both retrieval and generative capabilities to provide meaningful answers.

## Features
- Conversational AI using OpenAI's language model.
- Knowledge base integration using `llamaindex` (GPTIndex).
- Retrieval-Augmented Generation (RAG) to find and use relevant information.
- Ability to respond to FAQ-type questions by retrieving answers from a knowledge base and generating contextual responses.

## Technologies Used
- **Langchain**: Provides tools to manage language model interactions and conversational chains.
- **OpenAI API**: Used for generating responses from the language model.
- **LlamaIndex (GPTIndex)**: Used to index and query the knowledge base.
- **Chroma**: A vector store used to store document embeddings for retrieval purposes.
- **OpenAI Embeddings**: Used for creating embeddings of the documents for efficient retrieval.

## Installation
To run this project, you'll need Python and the following Python libraries:

- `langchain`
- `openai`
- `llama-index`
- `chromadb`

You can install the required packages using:

```sh
pip install langchain openai llama-index chromadb
```

## Setup
1. Clone the repository.
2. Set up your OpenAI API key by replacing `YOUR_OPENAI_API_KEY` in the code with your actual API key.
3. Create a folder named `knowledge_base` and populate it with documents (e.g., text files) that the chatbot will use to answer questions.

## Usage
Run the chatbot script:

```sh
python chatbot.py
```

After running the script, the chatbot will greet you and wait for your input. You can ask questions, and the bot will retrieve relevant information from the knowledge base and generate a response. Type 'exit' to end the conversation.

## How It Works
1. **Knowledge Base Loading**: The knowledge base is loaded using `SimpleDirectoryReader` from the `llamaindex`. This forms the initial data used by the bot.
2. **RAG Flow**:
   - The retriever (`Chroma` vector store) is used to find relevant documents for the user input.
   - If relevant documents are found, they are used to generate a response using the LLM.
   - If no documents are retrieved, the `llamaindex` is used to query the knowledge base.
   - If both fail, the bot falls back to the conversation chain to generate a response based on the context of the conversation.

## Example Interaction
```sh
Hello! I am an AI FAQ chatbot. Type 'exit' to end the chat.
You: What are the features of this product?
Bot: The product includes features like X, Y, and Z, which are designed to improve user experience.
```

## Customization
- **Knowledge Base**: You can customize the knowledge base by adding or updating the documents in the `knowledge_base` folder.
- **LLM Temperature**: Adjust the `temperature` parameter when initializing the OpenAI LLM to control the creativity of responses.

## Limitations
- The chatbot relies on the quality of the knowledge base. Ensure that the documents are comprehensive and up-to-date for the best performance.
- The retrieval process might return less relevant information if the embeddings are not properly configured or the documents lack context.

## Future Improvements
- **Enhanced Retrieval**: Use more advanced retrieval mechanisms or add ranking to improve the relevance of retrieved documents.
- **Context Management**: Improve the context management by adding more sophisticated memory tracking.
- **Multi-turn Conversations**: Expand the capabilities to handle more complex, multi-turn dialogues effectively.

## License
This project is licensed under the MIT License.

