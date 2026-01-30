from rag_engine import extract_ticker_from_query

query = "At what price did TCS close yesterday"
print(f"Query: {query}")
ticker = extract_ticker_from_query(query)
print(f"Extracted Ticker: '{ticker}'")
