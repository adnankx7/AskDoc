from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG AskDoc",
    version="0.1",
    author="Muhammad Adnan",
    packages=find_packages(),
    install_requires = requirements,
)