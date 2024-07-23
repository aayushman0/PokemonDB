from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

env = dotenv_values(".env")
BaseModel = declarative_base()


class Pokemon(BaseModel):
    __tablename__ = "pokemon"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, index=True, unique=True, nullable=False)
    type = Column("type", String, index=True, nullable=False)
    image = Column("image", String)

    def __init__(self, name: str, type: str, image: str):
        self.name = name
        self.type = type
        self.image = image

    def __repr__(self):
        return f"{self.id}. {self.name}"


db_url = f"postgresql+psycopg2://{env.get('DB_USERNAME')}:{env.get('DB_PASSWORD')}@{env.get('DB_HOST')}/{env.get('DB_DATABASE')}"
engine = create_engine(db_url, echo=False)
BaseModel.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
