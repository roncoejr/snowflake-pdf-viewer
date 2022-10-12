FROM gitpod/workspace-base:latest

FROM python:3.8

RUN pip install snowflake-connector-python snowflake-snowpark-python pandas requests
