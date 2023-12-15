### include functions that plot a graph in the given streamlit column
from collections import defaultdict

import streamlit as st
import datetime
import numpy as np
from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import pandas as pd
import random as random
import json
from routeConnectors import pallet, exportConnectors, locationConnectors
from matplotlib import pyplot as plt, dates as mdates
from routeConnectors import pallet
import json
import calendar
import plotly.express as px
from streamlit.elements.image import UseColumnWith




allPallets = json.loads(pallet.getFood())["Pallet"]

df = pd.DataFrame.from_dict(allPallets)
df = df.groupby('inputDate').weight.sum()


print(df)