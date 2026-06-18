from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite Database
DATABASE_URL = "sqlite:///website_audit_tool.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def init_db():
    from backend.app.models.user import User
    from backend.app.models.audit import Audit
    from backend.app.models.finding import Finding
    from backend.app.models.user_settings import UserSettings

    Base.metadata.create_all(bind=engine)

    print("✅ SQLite Database Connected")
    print("✅ Tables Created Successfully")


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()