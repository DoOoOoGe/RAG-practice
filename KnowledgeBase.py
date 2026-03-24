from MD5Manager import MD5Manager
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import datetime
import config_data

class KnowledgeBase:
    md5_manager = MD5Manager()

    def __init__(self, embed_model: Embeddings, data_base_path: str=config_data.data_base_path):
        os.makedirs(data_base_path, exist_ok=True)

        self.data_base = Chroma(
            collection_name=config_data.collection_name,
            embedding_function=embed_model,
            persist_directory=data_base_path,
        )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config_data.splitter_chunk_size,
            chunk_overlap=config_data.splitter_chunk_overlap,
            separators=config_data.splitter_separtors,
            length_function=len
        )

    def split_str(self, long_str: str) -> list[str]:
        """分割长字符串，如果字符串过短就直接包装为列表"""
        
        if len(long_str) < config_data.split_str_len_limit:
            return [long_str]
        return self.splitter.split_text(long_str)

    def save_str(self, long_str: str, filename: str) -> bool:
        """把文本分割后存入向量库，保证不重复"""

        # 检查md5不重复
        md5_hex: str = KnowledgeBase.md5_manager.get_md5(long_str)
        if KnowledgeBase.md5_manager.is_exist(md5_hex):
            return False
        
        # 分割文本
        texts: list[str] = self.split_str(long_str)
        
        # 生成元数据
        metadata = {
            "source": filename,
            "create_time": datetime.datetime.now().strftime("%Y-%m-%D %H:%M:%S"),
        }

        # 存入向量库
        self.data_base.add_texts(
            texts=texts, 
            metadatas=[metadata for _ in texts]
        )

        # 存入md5文件
        self.md5_manager.save_md5(md5_hex)

        return True

    def clear_data_base(self) -> None:
        self.data_base.delete_collection()
    
    
if __name__ == "__main__":
    from langchain_ollama.embeddings import OllamaEmbeddings
    kb = KnowledgeBase(OllamaEmbeddings(model="qwen3-embedding:0.6b"))
    # kb.clear_data_base()
    inp = input()
    print(kb.save_str(inp, filename="testfile"))