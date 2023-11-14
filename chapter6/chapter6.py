from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain.llms import OpenAI
from langchain import LLMChain, PromptTemplate
import json

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)
