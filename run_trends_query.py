from google.cloud import bigquery
import os

def run_query():
    # Set up authentication
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-key.json'

    # Initialize BigQuery client
    client = bigquery.Client()

    # Read the SQL query from trends.sql
    with open('trends.sql', 'r') as file:
        query = file.read()

    # Execute the query
    query_job = client.query(query)

    # Fetch and print results
    results = query_job.result()
    for row in results:
        print(row)

if __name__ == "__main__":
    run_query()