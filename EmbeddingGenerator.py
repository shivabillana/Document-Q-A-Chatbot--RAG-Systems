def generate_embeddings(chunks,model):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = model.encode(texts)
    return texts,embeddings

#texts, embeddings = generate_embeddings(chunks)