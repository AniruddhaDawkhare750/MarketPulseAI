from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import User, WatchlistItem, Base

# Assuming DB is in local file `marketpulse.db`
SQLALCHEMY_DATABASE_URL = "sqlite:///./marketpulse.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

print("--- Users ---")
users = db.query(User).all()
for user in users:
    print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
    print(f"  Watchlist ({len(user.watchlist)} items):")
    for item in user.watchlist:
        print(f"    - {item.symbol} ({item.name})")
    print("")

if not users:
    print("No users found in database.")
