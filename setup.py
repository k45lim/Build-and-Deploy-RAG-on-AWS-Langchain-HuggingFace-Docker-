# setup

from setuptools import find_packages, setup  # type: ignore[import]

setup(
    name="qasystem",
    version="0.0.1",
    author="kirk",
    author_email="k45lim@gmail.com",
    packages=find_packages(),
    install_requires=["langchain", "langchainhub", "bs4", "tiktoken", "openai", "boto3==1.34.37", "langchain_community", "chromadb", "awscli",
                      "streamlit",
                      "pypdf",
                      "faiss-cpu"]
)
