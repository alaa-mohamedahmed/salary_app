import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finaldata.csv")

def show_explore_page():
    st.title("Explore Salaries")
    st.write("""### Stack Overflow 2023 Developer Survey """)
   
    st.write("""#### Survey Participants""")

    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90, labeldistance=1.1)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.xticks(rotation=45)
    
    st.pyplot(fig1)

    st.write(
        """
    #### Mean Salary Based On Country
    """
    )
   
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )
   
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)