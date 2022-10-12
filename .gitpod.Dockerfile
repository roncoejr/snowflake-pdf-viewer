FROM gitpod/workspace-base:latest

RUN pip install snowflake-connector-python snowflake-snowpark-python pandas requests
