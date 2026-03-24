from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableWithMessageHistory, RunnableLambda
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.documents import Document
from VectorSearch import VectorSearch
from ChatHistoryManager import ChatHistoryManager

class RAGService:
    def __init__(self, embed_model: Embeddings, chat_model: BaseChatModel):
        self.embed_model = embed_model

        self.chat_model = chat_model

        self.retriever = VectorSearch(embed_model).get_retriever()

        self.prompt = self.__get_prompt()

        self.chain = self.__get_chain()

        
        
    def __get_prompt(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个秘书，可以根据资料与对话历史简洁专业地回答用户的问题"),
                ("system", "资料：{context}\n对话历史："),
                MessagesPlaceholder("history"),
                ("human", "用户的提问：{input}")
            ]
        )

    @staticmethod
    def vector_result_flatten(vector_results: list[Document]) -> str:
        if not vector_results:
            return "无参考资料"

        res: str = ""
        for d in vector_results:
            res += f"资料片段：{d.page_content}\n资料元数据：{d.metadata}\n\n"
        
        return res
    
    @staticmethod
    def __print_prompt(input) -> str:
        print(input.to_string())
        return input
        
    @staticmethod
    def __get_session_history(session_id: str):
        return ChatHistoryManager("chat_histories", session_id).file_history

    @staticmethod
    def __export_input(input_dict: dict[str, str | list]) -> str:
        return input_dict["input"]
    
    @staticmethod
    def __export_history(input_dict: dict[str, str | list]) -> list:
        return input_dict["history"]
    
    
    def __get_chain(self) -> RunnableSequence:
        chain: RunnableSequence = ( 
            {
                "input": self.__export_input,
                "context": self.__export_input | self.retriever | self.vector_result_flatten,
                "history": self.__export_history
            }
            | self.prompt | self.__print_prompt | self.chat_model | StrOutputParser()
        )
        history_chain = RunnableWithMessageHistory(
            chain,
            get_session_history=self.__get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return history_chain

    def get_invoke(self, input: str, session_id: str) -> str:
        session_config = {
            "configurable": {
                "session_id": session_id
            }
        }
        return self.chain.invoke({"input": input}, session_config)

if __name__ == "__main__":
    from langchain_ollama.chat_models import ChatOllama
    from langchain_ollama.embeddings import OllamaEmbeddings
    
    server = RAGService(
        OllamaEmbeddings(model="qwen3-embedding:0.6b"),
        ChatOllama(model="qwen3:0.6b"),
    )

    inp: str = input()
    while inp != "q":
        print(server.get_invoke(inp, "user001"))
        inp = input()