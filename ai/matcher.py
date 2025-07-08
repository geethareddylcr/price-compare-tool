from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def ai_match(query: str, results: list):
    query_embedding = model.encode(query, convert_to_tensor=True)
    filtered = []
    
    for r in results:
        product_embedding = model.encode(r["productName"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(query_embedding, product_embedding).item()
        if score > 0.6:
            filtered.append(r)
    
    return filtered if filtered else results
