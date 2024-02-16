import streamlit.runtime.scriptrunner.magic_funcs
import streamlit.web.cli as stcli
import os, sys
from pandasql import sqldf
import dask.dataframe as dd
import pandas as pd
from dask import delayed
import streamlit as st
import boto3
import base64
import s3fs
import pyarrow

def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("main.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())