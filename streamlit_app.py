import streamlit as st
import numpy as np
import pandas as pd

st.title("Interactive Histogram")

# 1. Generate Data
if 'data' not in st.session_state:
    st.session_state.data = np.random.normal(loc=0, scale=1, size=1000)

data = st.session_state.data

# 2. Sidebar Slider
bin_count = st.sidebar.slider("Number of bins:", 5, 100, 30)

# 3. Calculate Histogram with Numpy
# counts: the number of items in each bin
# bin_edges: the numerical boundaries of the bins
counts, bin_edges = np.histogram(data, bins=bin_count)

# 4. Prepare data for st.bar_chart
# We use the bin centers as labels for a cleaner look
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
chart_data = pd.DataFrame({
    'Frequency': counts,
    'Bin Center': np.round(bin_centers, 2)
}).set_index('Bin Center')

# 5. Display Chart
st.bar_chart(chart_data)

st.info(f"Currently displaying {bin_count} intervals across the data range.")