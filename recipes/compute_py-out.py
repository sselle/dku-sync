# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
revenue_prediction = dataiku.Dataset("revenue_prediction")
revenue_prediction_df = revenue_prediction.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

py_out_df = revenue_prediction_df # For this sample code, simply copy input to output
time.sleep(60)

# Write recipe outputs
py_out = dataiku.Dataset("py-out")
py_out.write_with_schema(py_out_df)
