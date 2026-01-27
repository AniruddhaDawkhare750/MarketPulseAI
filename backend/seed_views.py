
from database import get_db, NewsAnalytics, init_db
from sqlalchemy.orm import Session

# Initialize DB (create tables if needed)
init_db()

def seed_views():
    db = next(get_db())
    
    # Fake link from the debug output
    link = "https://www.moneycontrol.com/news/opinion/cop30-china-charts-climate-course-to-enhance-global-clout-13686501.html"
    
    # Check if exists
    item = db.query(NewsAnalytics).filter(NewsAnalytics.news_link == link).first()
    if not item:
        item = NewsAnalytics(news_link=link, views=100)
        db.add(item)
    else:
        item.views = 100
    
    db.commit()
    print(f"Seeded views for {link} to 100")

if __name__ == "__main__":
    seed_views()
