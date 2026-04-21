import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.title("Interactive Histogram: Bin Size Analysis")

# 1. Create or Load Data
# Generating a random normal distribution for demonstration
if 'data' not in st.session_state:
    st.session_state.data = np.random.normal(loc=0, scale=1, size=1000)

data = st.session_state.data

# 2. Sidebar Controls
st.sidebar.header("Configuration")
bin_count = st.sidebar.slider(
    "Select number of bins:",
    min_value=1,
    max_value=100,
    value=30  # Default value
)

# 3. Create the Visualization
fig, ax = plt.subplots()
ax.hist(data, bins=bin_count, color='skyblue', edgecolor='black', alpha=0.7)

# Formatting the plot
ax.set_title(f"Histogram with {bin_count} Bins")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.grid(axis='y', alpha=0.3)

# 4. Display in Streamlit
st.pyplot(fig)

# Brief explanation of the effect
st.write(f"""
### Observations
* **Low Bin Count:** Shows the general shape but loses the granularity of the data.
* **High Bin Count:** Shows more detail, but can become "noisy" or "jagged" if the sample size is small.
""")