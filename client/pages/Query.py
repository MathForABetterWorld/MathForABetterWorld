
import streamlit as st
import time
import numpy as np
import pandas as pd


# This should only be available to the employees not volunteers
# could be cool to show on a graph 
st.set_page_config(page_title="Query", page_icon="📈")

st.markdown("# Plotting Demo")

st.write(
    """Food query demo"""
)

last_rows = np.random.randn(1, 1)

sortby = st.selectbox("Sort by", ["Expiration date", "Import date", "Weight", "Rack"])
sortByMap = {"Expiration date": "expirationDate", "Import date":"inputDate", "Weight":"weight", "Rack":"rack"}
st.write('sort by ', sortByMap[sortby])

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

df = df.sort_values(by=["col 1"]) #[sortByMap[sortby]])
st.table(df)


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
