import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ["a","b","c"])

c = (alt.Chart(chart_data)
     .mark_circle()
     .encode(x="a",y="b",size = "c", color = "c",tooltip = ["a","b","c"])

     )
#set the title of the chart
c = c.properties(title="Scatter Plot with Altair")
st.altair_chart(c)