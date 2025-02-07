# platforms/langchain_demo.py
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def langchain_demo():
    prompt_template = PromptTemplate(
        input_variables=["question"],
        template="質問: {question}\n回答:"
    )
    llm = OpenAI(model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    question = input("質問を入力してください: ")
    response = chain.run(question)
    print("LangChainの回答:", response)

if __name__ == "__main__":
    langchain_demo()
