from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStoreRetriever
import config_data

class VectorSearch:
    def __init__(self, embed_model: Embeddings):
        self.model = embed_model
        self.data_base = Chroma(
            collection_name=config_data.collection_name,
            persist_directory=config_data.data_base_path,
            embedding_function=embed_model,
        )

    def get_retriever(self) -> VectorStoreRetriever:
        return self.data_base.as_retriever(search_kwargs={"k": config_data.search_num})