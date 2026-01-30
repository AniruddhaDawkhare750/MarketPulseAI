from rag_engine import retrieve_context, collection

query = "At what price did TCS close yesterday"
print(f"Query: {query}")

# 1. Check what is currently in the DB for TCS
if collection:
    data = collection.get(where={"ticker": "TATAMOTORS.NS"}) # Just checking if DB is accessible logic
    tcs = collection.get(where={"ticker": "TCS.NS"})
    print(f"\nExisting TCS Documents in DB: {len(tcs['ids'])}")
    for i, doc in enumerate(tcs['documents']):
        print(f"[{i}] Metadata: {tcs['metadatas'][i]}")
        print(f"    Content header: {doc.splitlines()[0]}")

# 2. Run Retrieval
print("\n--- Retrieving Context ---")
context = retrieve_context(query)
print("Context:\n", context)
