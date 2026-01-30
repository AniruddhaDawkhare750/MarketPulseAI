from rag_engine import extract_ticker_from_query

queries = [
    "Tell me morningstar's latest financial results",
    "How is Apple doing?",
    "What about Reliance?",
    "Price of Tesla",
    "News on Tata Motors"
]

for q in queries:
    print(f"Query: {q}")
    t = extract_ticker_from_query(q)
    print(f"Result: {t}\n")
