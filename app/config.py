DB_USER = "aiman"
DB_PASSWORD = "aiman"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "notes_db"

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SECRET_KEY = "supersecretkey123"  # Замените на свой уникальный ключ в реальном проекте
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30