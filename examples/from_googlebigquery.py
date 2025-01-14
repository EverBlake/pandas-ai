from pandasai import SmartDataframe

# A license might be required for using Snowflake with PandasAI
from pandasai.ee.connectors import GoogleBigQueryConnector
from pandasai.llm import OpenAI

# ENV's
# BIG_QUERY_DATABASE
# KEYFILE_PATH
# PROJECT_ID

bigquery_connectors = GoogleBigQueryConnector(
    config={
        "credentials_path": "credentials.json",
        "database": "loan_payments",
        "table": "loan_payments",
        "projectID": "project_id",
        "where": [["Gender", "=", "female"]],
    }
)

llm = OpenAI("OPEN_AI_KEY")
df = SmartDataframe(bigquery_connectors, config={"llm": llm})

response = df.chat("How many rows are there in data ?")
print(response)
