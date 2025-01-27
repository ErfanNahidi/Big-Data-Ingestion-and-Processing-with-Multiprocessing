# Big Data Ingestion and Processing with Multiprocessing
## Description:
This project demonstrates the ingestion and processing of large-scale synthetic data into a relational database using SQLAlchemy and multiprocessing in Python. The system is designed to simulate data generation using the Faker library, followed by parallelized insertion into a MySQL database. The project leverages Python's multiprocessing library to speed up the process of inserting millions of records by distributing the workload across multiple CPU cores.

This approach is scalable and can be adapted for larger datasets, showcasing efficient handling of Big Data operations and high-performance database interaction.

## Key Features:
- **Data Generation**: Uses the Faker library to generate synthetic data for testing and simulation purposes.
- **Multiprocessing**: Implements parallel data insertion using Python's `multiprocessing` to efficiently use multiple CPU cores.
- **Database Interaction**: Connects to a MySQL database using SQLAlchemy ORM for structured data insertion.
- **Batch Processing**: Data is inserted in batches to optimize database transactions and reduce I/O overhead.
- **Error Handling**: Robust error handling and transaction management with automatic rollback in case of failure.
- **Optimized Performance**: Designed to handle millions of records efficiently by optimizing database operations and parallel processing.

## Technologies Used:
- Python (version 3.13+)
- Faker for synthetic data generation
- SQLAlchemy ORM
- MySQL (or any other relational database)
- Multiprocessing for parallel processing
- QueuePool for managing database connections efficiently

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/ErfanNahidi/Big-Data-Ingestion-and-Processing-with-Multiprocessing.git
   cd Big-Data-Ingestion-and-Processing-with-Multiprocessing
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a MySQL database running and replace the connection string in the code (`mysql+pymysql://root:password@localhost/OnlineMarket`) with your own credentials.

## How to Use:
1. Run the script:
   ```bash
   python db.py
   ```

2. Input the number of records you want to insert into the database when prompted.

3. The data generation will start, and the records will be inserted into the `customers` table in batches for optimal performance.

## Test Results and Performance Profiling:

The following test was conducted to measure the performance of the data insertion process for large datasets (1 million records). The process involved parallelizing the insertion across 8 CPU cores, with each core handling a chunk of the data.

**Test Setup:**
- **Number of records**: 1,000,000
- **Chunk size**: 125,000 records per process (split into 8 processes)
- **Database**: MySQL (local)

**Test Result:**
- **Time to insert 1,000,000 records**: 69.43 seconds

This performance is considered highly efficient, leveraging Python's multiprocessing capabilities to split the workload across multiple CPU cores.

**Profiling Results:**
The profiling results indicate that the use of multiprocessing significantly reduced the time taken to insert data compared to a single-threaded approach. The batch processing method also reduced the overhead of committing records to the database multiple times, improving both speed and efficiency.

## Challenges and Future Work:
- **Scalability**: Although this implementation works efficiently for 1 million records, further scalability testing is needed for datasets with billions of records.
- **Error Handling in Distributed Systems**: While the current system handles errors at the process level, a more robust distributed error-handling mechanism could be implemented to address potential issues when scaling.
- **Database Tuning**: Future work may involve optimizing the database schema, indexing, and other configurations to improve performance at scale.

## Code Structure:
- `db.py`: Main script for data generation, processing, and insertion into the database.
- `faker_input_v2.py`: Custom data generator class (StreamFastGenerator) that uses Faker to generate synthetic data.
- `requirements.txt`: List of dependencies required for the project.

## Contributing:
Feel free to fork this project, submit issues, and make pull requests for improvements. Contributions are welcome to help scale the solution and optimize the performance further.

## License:
MIT License

