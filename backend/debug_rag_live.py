from rag_engine import extract_ticker_from_query, fetch_quarterly_data
import yfinance as yf

query = "Tell me morningstar's latest financial results"
print(f"Testing Query: '{query}'")

# 1. Test Extraction
print("--- Extractor Output ---")
ticker = extract_ticker_from_query(query)
print(f"Extracted Ticker: '{ticker}'")

# 2. Test YFinance Fetch (if ticker found)
if ticker:
    print(f"\n--- YFinance Data for {ticker} ---")
    data = fetch_quarterly_data(ticker)
    print(f"Fetched {len(data)} chunks.")
    if data:
        print("Sample Chunk:", data[0]['text'][:100])
    else:
        print("No data fetched.")
        # Debug why
        t = yf.Ticker(ticker)
        print("Income Stmt Empty?", t.quarterly_income_stmt.empty)
else:
    print("Extraction failed.")
