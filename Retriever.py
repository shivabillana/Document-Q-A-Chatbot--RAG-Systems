def retrieve_chunks(collection,question,model):
    query_embedding = model.encode(question)
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = 5
    )

    return results["documents"][0]