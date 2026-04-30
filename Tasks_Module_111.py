from sqlalchemy import create_engine, ForeignKey, String, Integer, Date, PrimaryKeyConstraint, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from datetime import date


engine = create_engine("postgresql+psycopg://postgres:123456789@localhost:5432/module11", echo=False)


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    biography: Mapped[str] = mapped_column(Text, nullable=True)

    books: Mapped[list["Book"]] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), onupdate="CASCADE")
    published_year: Mapped[int] = mapped_column(Integer, nullable=True)
    isbn: Mapped[str] = mapped_column(String(13), unique=True, nullable=True)

    author: Mapped[Author] = relationship(back_populates="books")
    loans: Mapped[list["Loan"]] = relationship(back_populates="book")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(254), unique=True, nullable=True)

    loans: Mapped[list["Loan"]] = relationship(back_populates="user")


class Loan(Base):
    __tablename__ = "loans"

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    loan_date: Mapped[date] = mapped_column(Date, nullable=False, server_default=func.current_date())
    return_date: Mapped[date] = mapped_column(Date, nullable=True)

    book: Mapped[Book] = relationship(back_populates="loans")
    user: Mapped[User] = relationship(back_populates="loans")

    __table_args__ = (
        PrimaryKeyConstraint(book_id, user_id, loan_date, name='loans_pk'),
    )


# Base.metadata.drop_all(engine)

# Base.metadata.create_all(engine)

with Session(engine) as session:
    a1 = Author(name="Лев Толстой")
    a2 = Author(name="Александр Пушкин")
    a3 = Author(name="Николай Гоголь")

    b1 = Book(title="Анна Каренина", author=a1, published_year=2011)
    b2 = Book(title="Война и мир", author=a1, published_year=2000)
    b3 = Book(title="Евгений Онегин", author=a2, published_year=2015)
    b4 = Book(title="Капитанская дочка", author=a2, published_year=1990)
    b5 = Book(title="Мертвые души", author=a3, published_year=2016)
    b6 = Book(title="Ревизор", author=a3, published_year=2011)

    u1 = User(full_name="Иван Иванов", email="ivan_ivanov@mail.ru")
    u2 = User(full_name="Петр Петров", email="petrov_p@gmail.com")
    u3 = User(full_name="Василий Васильев", email="vasya@gmail.com")

    l1 = Loan(book=b2, user=u3, loan_date=date(2026, 2, 13), return_date=date(2026, 3, 25))
    l2 = Loan(book=b5, user=u1, loan_date=date(2026, 3, 13))
    l3 = Loan(book=b1, user=u3, loan_date=date(2026, 3, 25))
    l4 = Loan(book=b3, user=u2, loan_date=date(2026, 2, 25), return_date=date(2026, 3, 26))

    # session.add_all([a1, a2, a3])
    # session.add_all([b1, b2, b3, b4, b5, b6])
    # session.add_all([u1, u2, u3])
    # session.add_all([l1, l2, l3, l4])

    session.commit()

with Session(engine) as session:
    print("Названия всех книг, изданных после 2010 года:")
    books_after_2010 = session.query(Book).filter(Book.published_year >= 2010).all()

    for book in books_after_2010:
        print(f"Книга '{book.title}', год публикации {book.published_year}")

    print('---------')

    print("Список всех книг с именами их авторов:")
    books_all = session.query(Book).join(Author).all()

    for book in books_all:
        print(f"Книга '{book.title}', год публикации {book.published_year}, автор {book.author.name}")

    print('---------')

    print("Пользователей, чья электронная почта заканчивается на @gmail.com:")
    users_gmailcom = session.query(User).filter(User.email.like('%@gmail.com')).all()

    for user in users_gmailcom:
        print(f"Пользователь '{user.full_name}', электронная почта {user.email}")

    print('---------')

    print("Общее количество книг у каждого автора в базе:")
    author_books_count = session.query(Author.id, Author.name, func.count(Book.id).label('book_count')).join(Book).group_by(Author.id, Author.name).all()

    for author in author_books_count:
        print(f"Автор '{author.name}', количество книг {author.book_count}")

    print('---------')

    print("Имена читателей и названия книг, которые они взяли, но еще не вернули:")
    loads_not_return = (
        session.query(Loan)
        .join(Book)
        .join(User)
        .filter(Loan.return_date.is_(None))
        .all()
    )
    for loan in loads_not_return:
        print(f"Пользователь '{loan.user.full_name}', книга {loan.book.title}")
    print('---------')
