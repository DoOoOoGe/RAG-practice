"""
基于 Streamlit 完成 web 网页上传文件服务
"""

from KnowledgeBase import KnowledgeBase
from langchain_ollama.embeddings import OllamaEmbeddings

import streamlit as st

st.title("文件上传服务")

upload_file = st.file_uploader(
    "请上传 txt 文件",
    type=['txt'],
    accept_multiple_files=False,
)

if upload_file is not None:
    # 提取的文件信息
    file_name = upload_file.name
    file_type = upload_file.type
    file_size = upload_file.size / 1024

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f}kb")

    text = upload_file.getvalue().decode("utf-8")
    # st.write(text)

    if "service" not in st.session_state:
        st.session_state["service"] = KnowledgeBase(OllamaEmbeddings(model="qwen3-embedding:0.6b"))
    
    result = st.session_state["service"].save_str(text, file_name)
    print("已上传知识库" if result else "上传的文件重复")