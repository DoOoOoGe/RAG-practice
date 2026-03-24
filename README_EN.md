# RAG Practice Project

[中文文档](README.md) | [English README](README_EN.md)

## Basic Introduction

This project is designed for personal practice using the LangChain Python library.

> [!WARNING]
> The page functionality of this project is not yet complete, only command-line interaction with the model is available
> The test code of this project uses locally deployed models via Ollama. If changes are needed, please modify the code accordingly. See [Environment](#environment) and [Future Work](#future-work) for details

## Technical Features

- **Test Model Used**: Local model ([Ollama](https://ollama.com/) deployment)

- **Large Model Framework**: [Langchain](https://github.com/langchain-ai/langchain)

- **Page Display**: [Streamlit](https://streamlit.io/)

- **Vector Storage**: [Chroma](https://github.com/chroma-core/chroma)

1. Using the LangChain framework combined with Chroma vector database and Ollama local model to build a complete RAG system

2. Supporting localized deployment, using Ollama to run local models, protecting data privacy while reducing usage costs

3. Having comprehensive document processing capabilities, capable of intelligent segmentation of long documents and establishing vector indexes

4. Implementing deduplication mechanism, avoiding repeated storage of duplicate content through MD5 verification

5. Providing Streamlit interface to support file uploads, while retaining command-line interaction methods, flexible to use

6. Separately storing and managing chat history and vector data, facilitating subsequent data maintenance and system expansion

7. Centralized management of configuration parameters, allowing users to adjust system behavior and performance parameters as needed

## Environment

This project uses Python and can be managed using pip package manager. The following packages need to be installed:

| Package Name        | Test Version |
| ------------------- | ------------ |
| langchain           | 1.1.2        |
| langchain-community | 0.4.1        |
| langchain-ollama    | 1.0.1        |
| dashscope           |              |
| chromadb            | 1.5.5        |
| streamlit           | 1.55.0       |

To run with Ollama local models, you need to install [Ollama](https://ollama.com/). During testing, I used the models `qwen3-embedding:0.6b` and `qwen3:0.6b`. If you need the same versions, you can execute the following command in the command line after installing Ollama:

```bash
ollama pull qwen3:0.6b qwen3-embedding:0.6b
```

If you need to change models or use APIs, you need to modify the code yourself:

- In the `RAGService.py` file, lines 91, 92 for langchain model packages, and lines 94, 95 for model objects

- In the `app_file_uploader.py` file, line 6 for langchain model packages, and line 31 for model objects

## Running Method

### Offline Process

The offline process is used to upload documents, vectorize knowledge, and add them to the knowledge base.

You need to run the following command to open the server and webpage (usually auto-opens, if not please visit manually):

```bash
streamlit run app_file_uploader.py
```

### Online Process (Work in progress)

Currently you can execute:

```bash
python RAGService.py
```

Run the program, input content and press Enter to send questions to the AI, prompts will be printed in the terminal for debugging.

Input `q` and press Enter to exit.

## Data Management

Not implemented yet...

- Vector (knowledge) information is stored in the `./chroma_db` folder

- Context history is stored in the `./chat_histories` folder.

To reset, you need to manually delete the above two folders (only generated after the first knowledge addition and conversation)

## Future Work

Due to lack of time, the following features may not be implemented soon (maybe never 😰)

- [ ] Implementing user-model interaction pages
- [ ] Session switching functionality
- [ ] Session list
- [ ] Session management
- [ ] Vector database management
- [ ] Input custom API, using user-specified models

## References

[Heima Programmer Large Model RAG and Agent Intelligent System Practical Tutorial, Based on Mainstream LangChain Technology from Large Model Prompts to Practical Projects](https://www.bilibili.com/video/BV1yjz5BLEoY/)

[langchain-ai/langchain: The agent engineering platform](https://github.com/langchain-ai/langchain)

