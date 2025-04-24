# Running trends.sql with Python and Google Cloud BigQuery

## Overview
This document outlines the steps to execute the SQL query in `trends.sql` using Python and Google Cloud BigQuery. The query retrieves the most searched term in India on Good Friday, April 18, 2025.

## Prerequisites
1. **Google Cloud Project**: Ensure you have a Google Cloud project with BigQuery API enabled.
2. **Service Account Key**: Download a service account key JSON file with BigQuery access.
3. **Python Environment**: Set up a Python environment with the required libraries.

## Steps

### 1. Install Required Libraries
Install the `google-cloud-bigquery` library to interact with BigQuery.
```bash
pip install google-cloud-bigquery
```

### 2. Authenticate with Google Cloud
Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file.
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
```

### 3. Python Script
Create a Python script to execute the SQL query.

#### Example Code
```python
from google.cloud import bigquery

def run_query():
    # Initialize BigQuery client
    client = bigquery.Client()

    # Read the SQL query from the file
    with open('sql/trends.sql', 'r') as file:
        query = file.read()

    # Execute the query
    query_job = client.query(query)

    # Fetch and print results
    results = query_job.result()
    for row in results:
        print(f"Date: {row.refresh_date}, Country: {row.country_code}, Term: {row.term}, Rank: {row.rank}")

if __name__ == "__main__":
    run_query()
```

### 4. Run the Script
Execute the Python script.
```bash
python your_script_name.py
```

## Notes
- Ensure the `trends.sql` file is in the correct path relative to your Python script.
- Verify that your Google Cloud project has sufficient permissions to access the BigQuery dataset.

## References
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [google-cloud-bigquery Python Client](https://googleapis.dev/python/bigquery/latest/index.html)
