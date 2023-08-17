from langchain import LLMChain, HuggingFaceHub
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate


load_dotenv()


template = """
Translate English to Sql: {question}

"""
hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikiSQL")
prompt = PromptTemplate(
    input_variables = ['question'],
    template=template
)
hub_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm,
    verbose=True
)


print(hub_chain.run("what is the average age of the correspondents using mobile data?"))





