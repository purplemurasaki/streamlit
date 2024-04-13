import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Penguins")
df = sns.load_dataset("penguins")
st.write(df)

code = """
import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Penguins")
df = sns.load_dataset("penguins")
st.write(df)
"""

st.code(code)
