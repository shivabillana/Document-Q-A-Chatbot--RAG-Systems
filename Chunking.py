from langchain_text_splitters import RecursiveCharacterTextSplitter

def divdingchunks(document):

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len,
    separators=[ "\n\n","\n"," ",".",",",""]
)
    text = text_splitter.split_documents(document)
    return text

#chunks = divdingchunks(result)