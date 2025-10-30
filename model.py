from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class BaseModel(DeclarativeBase):
    pass


class Genre(BaseModel):
    __tablename__ = "genre"
    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)
    book = relationship("Book", back_populates="genre")


class Author(BaseModel):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)
    book = relationship("Book", back_populates="author")


class City(BaseModel):
    __tablename__ = "city"
    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)


class Book(BaseModel):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.author_id"))
    genre_id = Column(Integer, ForeignKey("genre.genre_id"))
    price = Column(Integer)
    amount = Column(Integer)
    author = relationship("Author", "book")
    genre = relationship("Genre", "book")


class Client(BaseModel):
    __tablename__ = "client"
    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    email = Column(String, unique=True)
    city_id = Column(Integer, ForeignKey("city.city_id"))
    city = relationship("City", "client")


class Buy(BaseModel):
    __tablename__ = "buy"
    buy_id = Column(Integer, primary_key=True)
    buy_discription = Column(Text)
    client_id = Column(Integer, ForeignKey("client.client_id"))
    client = relationship("Client", "buy")


class Step(BaseModel):
    __tablename__ = "step"
    step_id = Column(Integer, primary_key=True)
    name_step = Column(String)


class BuyBook(BaseModel):
    __tablename__ = "buy_book"
    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    book_id = Column(Integer, ForeignKey("book.book_id"))
    amount = Column(Integer)
    buy = relationship("Buy", "buy_book")
    book = relationship("Book", "buy_book")


class BuyStep(BaseModel):
    __tablename__ = "buy_step"
    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    step_id = Column(Integer, ForeignKey("step.step_id"))
    date_step_beg = Column(DateTime)
    date_step_end = Column(DateTime)
    buy = relationship("Buy", "buy_step")
    step = relationship("Step", "buy_step")
