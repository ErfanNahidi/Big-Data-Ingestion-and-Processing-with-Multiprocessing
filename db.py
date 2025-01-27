import time
import faker_input_v2
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import multiprocessing as mp
from sqlalchemy.pool import QueuePool

Base = declarative_base()

class OnlineMarket(Base):
    __tablename__ = "customers"

    c_id = Column("c_id", Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column("first_name", String(50), nullable=False)
    last_name = Column("last_name", String(50), nullable=False)
    age = Column("age", Integer)
    state = Column("state", String(50))
    city = Column("city", String(50))
    street = Column("street", String(100))
    building_number = Column("building_number", String(10))
    phone_number = Column("phone_number", String(15))
    post_code = Column("post_code", String(20))

    def __repr__(self):
        return f"<Customer(c_id={self.c_id}, first_name={self.first_name}, last_name={self.last_name})>"

# Set up a pool of database connections for concurrency
engine = create_engine("mysql+pymysql://username:pass@address/OnlineMarket", 
                       echo=True, poolclass=QueuePool, pool_size=10, max_overflow=20)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

Generator = faker_input_v2.StreamFastGenerator()

def insert_data_to_db(chunk_size):
    session = Session()
    batch_size = 500  # Insert data in batches
    for i in range(chunk_size):
        gen_data = Generator.generate_data(num_records=1)[0]  # Now it correctly gets the first item from the list
        data = OnlineMarket(**gen_data)

        try:
            session.add(data)

            # Commit after each batch
            if (i + 1) % batch_size == 0 or (i + 1) == chunk_size:
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")
    session.close()

def generate_and_insert_data(data_count):
    chunk_size = data_count // 8
    pool_args = [chunk_size] * 8  # Create a list with 8 elements (each representing a chunk_size)
    with mp.Pool(processes=8) as pool:
        pool.map(insert_data_to_db, pool_args)  # Pass the iterable correctly

if __name__ == "__main__":
    data_count = int(input("How many data you want?"))
    start = time.time()

    generate_and_insert_data(data_count)

    end = time.time()
    print(f"{data_count} data inserted into database in {end - start} seconds")

