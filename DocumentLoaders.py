import os
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders import Docx2txtLoader, TextLoader, BSHTMLLoader

def fileloader(file_path):

    loaders = {
        ".pdf": PyMuPDF4LLMLoader,
        ".docx": Docx2txtLoader,
        ".txt": TextLoader,
        ".html": BSHTMLLoader
    }

    _,ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext not in loaders:
        raise ValueError(f"Unsupported file type : {ext}")
    
    loader = loaders[ext](file_path)
    documents = loader.load()

    return documents
    

#file =r"/workspaces/codespaces-blank/RESUME (2).pdf"
#result = fileloader(file)