
from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='div20041',
    author_email='123divyareddy456@gmail.com',
    install_requires=["groq","langchain","langchain-groq","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)