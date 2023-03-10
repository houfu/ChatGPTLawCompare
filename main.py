import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Let's Compare ChatGPT and GPT-3+",
    layout="wide",
)

st.title("ChatGPT and Data Augmentation Compare")

with st.expander("What is this about?"):
    """
    I try to compare the results of what ChatGPT and a GPT-3 with data augmented vector search (or "Custom").

    **How is Custom derived?**
    
    I broadly followed 
    [langchain's VectorDB Question/Answering](https://langchain.readthedocs.io/en/latest/modules/indexes/chain_examples/vector_db_qa.html)
    
    The documents were compiled by scraping the "About Singapore law" in Singapore Law Watch, being:
    * https://www.singaporelawwatch.sg/About-Singapore-Law/Overview
    * https://www.singaporelawwatch.sg/About-Singapore-Law/Commercial-Law
    * https://www.singaporelawwatch.sg/About-Singapore-Law/Singapore-Legal-System
    
    The text was then broken into smaller documents and then saved into a vector database.
    
    After the vector database is prepared, the GPT3 model is prompted with the following text:
    """
    st.code(body="""
Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
\n\n{context}\n\nQuestion: {question}\nHelpful Detailed Answer:
    """)

    "Sources are also saved to show the context which the GPT-3 model saw to make the answer."

    """
    **What is ChatGPT+?**
    
    ChatGPT+ attempts to combine the data augmention method used in Custom with ChatGPT.
    Using a series of system messages, the ChatGPT is shown the same context as Custom and 
    is asked to provide an answer.
    
    ```
    System Message: ("You are a helpful assistant. Use the following pieces of context to answer the question at 
    the end. If the context does not help, don't use them. Don't try to make up an answer")
    
    System Message: For each context shown to Custom, ("Context: {context}")
    
    Human Message: "Question: {question}"
    ```
    
    For more information on how the various responses are generated, see 
    [the code in the repo](https://github.com/houfu/ChatGPTLawCompare/blob/master/prepare_data.py).

    """


with st.expander("How do I use this?"):
    """
    Click on the spinner to show the various prompts and answers, and compare!    
    """

data = pd.read_csv('results.csv')

question = st.select_slider("Select a question", data)

question_series = data.iloc[question]

chatgpt_response = question_series['ChatGPT'].replace('\n', '')
custom_response = question_series['Custom'].replace('\n', '')
chatgpt_plus_response = question_series['ChatGPT+'].replace('\n', '')


table = [
    "| Description |  Value | Notes |",
    "|-------------| -------| --- |",
    f"| **Question** | {question_series['question']} | The question asked to the LLM| ",
    f"| **Notes** | {question_series['answer']} | My model answer for reference| ",
    f"| **ChatGPT** | {chatgpt_response} | ChatGPT's response| ",
    f"| **Custom** | {custom_response} | Data Augmented GPT-3's response| ",
    f"| **ChatGPT+** | {chatgpt_plus_response} | Data Augmented ChatGPT's response| ",
]
st.markdown("\n".join(table))
