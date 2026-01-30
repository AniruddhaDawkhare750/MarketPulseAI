from rag_engine import collection

print("Dumping ALL documents (limit 10):")
results = collection.get(limit=10)
for i, doc in enumerate(results['documents']):
    print(f"\n--- Document {i} ---")
    print(f"ID: {results['ids'][i]}")
    print(f"Metadata: {results['metadatas'][i]}")
    print(f"Content:\n{doc}")
