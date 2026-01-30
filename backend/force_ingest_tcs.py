from rag_engine import ingest_financial_data, fetch_quarterly_data

# 1. Inspect what chunks are generated
print("Fetching chunks for TCS.NS...")
chunks = fetch_quarterly_data("TCS.NS")
print(f"Generated {len(chunks)} chunks.")
for c in chunks:
    print(f"Type: {c['metadata']['type']}")
    print(f"Text Preview: {c['text'][:50]}...")

# 2. Ingest
print("\nIngesting...")
ingest_financial_data(["TCS.NS"])
print("Done.")
