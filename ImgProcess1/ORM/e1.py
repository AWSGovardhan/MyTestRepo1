from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define your PostgreSQL database connection URL
# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your actual database credentials
# DB_URL = "postgresql://username:password@hostname:port/database_name"
DB_URL = "postgresql://postgres:Dell@12345@localhost:5432/postgres"

# Create a SQLAlchemy engine
engine = create_engine(DB_URL)

# Define the data model
Base = declarative_base()

class Student(Base):
    __tablename__ = 'stud'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the database table (if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add data to the database
new_data = Student(name="John Doe", age=30)
session.add(new_data)
session.commit()

# Query data from the database
results = session.query(Student).all()
for result in results:
    print(f"ID: {result.id}, Name: {result.name}, Age: {result.age}")

# Close the session
session.close()
