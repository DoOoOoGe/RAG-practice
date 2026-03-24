# RAG 练习项目

## 基本介绍

这个项目是个人用于练习 LangChain Python 库的使用制作的项目。

> [!WARNING]
> 本项目的页面功能尚未完成，仅可使用命令行与模型交互
> 本项目的测试代码均使用 Ollama 部署的本地模型测试，如有更换需要，请在代码中修改，详见[环境](#环境)与[未来工作](#未来工作)

## 使用技术特点

- **测试使用模型**：本地模型（[Ollama](https://ollama.com/) 部署）

- **大模型框架**：[Langchain](https://github.com/langchain-ai/langchain)

- **页面展示**：[Streamlit](https://streamlit.io/)

- **向量存储**：[Chroma](https://github.com/chroma-core/chroma)

1. 使用LangChain框架结合Chroma向量数据库和Ollama本地模型，构建了完整的RAG系统

2. 支持本地化部署，使用Ollama运行本地模型，保护数据隐私的同时降低了使用成本

3. 具备完善的文档处理能力，能够对长文档进行智能分割并建立向量索引

4. 实现了去重机制，通过MD5校验避免重复内容被多次存储

5. 提供了Streamlit界面支持文件上传，同时保留命令行交互方式，使用灵活

6. 聊天历史和向量数据分别存储管理，便于后续的数据维护和系统扩展

7. 配置参数集中管理，方便用户根据需要调整系统行为和性能参数

## 环境

本项目使用 Python，可以使用 pip 包管理器，需要安装如下包

| 包名                | 测试用版本 |
| ------------------- | ---------- |
| langchain           | 1.1.2      |
| langchain-community | 0.4.1      |
| langchain-ollama    | 1.0.1      |
| dashscope           |            |
| chromadb            | 1.5.5      |
| streamlit           | 1.55.0     |

使用 Ollama 本地模型运行，需要安装[Ollama](https://ollama.com/)。在测试时，我使用的模型为 `qwen3-embedding:0.6b` 和 `qwen3:0.6b`，如果你也需要相同的版本，可以在安装完 Ollama 后在命令行执行

```bash
ollama pull qwen3:0.6b qwen3-embedding:0.6b
```

如果你需要更换模型，或使用 API，你需要自行修改代码：

- `RAGService.py` 文件中第91、92行的 langchain 模型包，以及第94、95行的模型对象

- `app_file_uploader.py` 文件中第6行的 langchain 模型包，以及第31行的模型对象

## 运行方法

### 离线流程

离线流程用于上传文档，向量化知识，并将其加入知识库。

你需要运行以下命令打开服务器与网页（通常会自动弹出，若无请手动访问）

```bash
streamlit run app_file_uploader.py
```

### 在线流程（待完工）

目前可以执行

```bash
python RAGService.py
```

运行程序，输入内容并回车来发送问题给 AI ，终端中会打印提示词用于调试。

输入 `q` 并回车可以退出。

## 数据管理

没有实现……

- 向量（知识）信息存储在 `./chroma_db` 文件夹下

- 上下文历史存储在 `./chat_histories` 文件夹下。

如需重置，你需要手动删除上述两个文件夹（只有在第一次添加知识和对话后才会生成）

## 未来工作

因为没什么时间，可能以下的功能不会很快实现（也许永远也不会实现😰）

- [ ] 实现用户与模型交互的页面
- [ ] 会话切换功能
- [ ] 会话列表
- [ ] 会话管理
- [ ] 向量数据库管理
- [ ] 输入自定义API，使用用户指定的模型

## 参考资料

[黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目](https://www.bilibili.com/video/BV1yjz5BLEoY/)

[langchain-ai/langchain: The agent engineering platform](https://github.com/langchain-ai/langchain)
