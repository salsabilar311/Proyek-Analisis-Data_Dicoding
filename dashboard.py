import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Bike Sharing Dataset Analysis')
tab1, tab2 = st.tabs(["Weather Effects", "Users Comparison"])

df = pd.read_csv('day.csv')

with tab1:
    st.write("""This time I will analyze the bike sharing dataset. And extract knowledge that can be used to make decisions. 
        This dataset contains bike renter data and some weather attributes.""")
    st.dataframe(data=df, width=500, height=150)
    st.write("""After looking at this data I can conclude 2 questions, namely:""")
    st.write("""1. How does the season affect the number of bike rentals?""")
    st.write("""2. How does the number of bike rentals by casual users and registered users compare?""") 
    st.write("""To analyze the bike sharing dataset and answer the two questions, 
             I will analyze and visualize the data. First, I will examine the correlation between the seasonal
              variables and the number of bike loans. Next, I will compare the number of bike loans by casual 
             users and registered users using the corresponding graphs.""")
    
    st.header("Analyze the effect of seasonality on bicycle rentals")
    st.subheader("Analysis of bicycle rentals in 2011")

    # Memisahkan dataframe yang memiliki tahun 2012
    for i in range(len(df)) :
        if df['yr'][i] == 0 :
            df_1_1 = pd.concat([df, pd.DataFrame([df.loc[i]])], ignore_index=True)

    # Groupby data dengan season sebagai key
    df_1_1 = df_1_1.groupby(by='season').cnt.sum()

    # Visualisasi data menggunakan bar chart
    colors = ['lightgreen', 'lightgreen', 'mediumseagreen', 'lightgreen']
    plt.figure(figsize=(8, 5))
    df_1_1.plot(kind='bar', color=colors)
    plt.title('Total Bike Rentals by Season in 2011')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    new_labels = ['Springer', 'Summer', 'Fall', 'Winter']
    plt.xticks(range(len(new_labels)), new_labels, rotation=0)
    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Explanation"):
        st.write(
            """Based on the graph shown, it appears that the number of bicycle rentals peaks in the fall. 
            This suggests that fall is the most desirable period for bicycle renters. 
            This phenomenon may be due to several factors, including more stable weather conditions, 
            an increase in outdoor activities, or perhaps the presence of special events that attract tourists 
            or locals in that season. In addition, the possibility of school holidays could also be a contributing 
            factor in the increase in the number of bike rentals.
            """
        )

    st.subheader("Analysis of bicycle rentals in 2012")

    # Memisahkan dataframe yang memiliki tahun 2012
    for i in range(len(df)) :
        if df['yr'][i] == 1 :
            df_1_2 = pd.concat([df, pd.DataFrame([df.loc[i]])], ignore_index=True)

    # Groupby data dengan season sebagai key
    df_1_2 = df_1_2.groupby(by='season').cnt.sum()

    # Visualisasi data menggunakan bar chart
    colors = ['lightpink', 'lightpink', 'crimson', 'lightpink']
    plt.figure(figsize=(8, 5))
    df_1_1.plot(kind='bar', color=colors)
    plt.title('Total Bike Rentals by Season in 2012')
    plt.xlabel('Season')
    plt.ylabel('Total Bike Rentals')
    new_labels = ['Springer', 'Summer', 'Fall', 'Winter']
    plt.xticks(range(len(new_labels)), new_labels, rotation=0)
    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Explanation"):
        st.write(
            """Similarly, in 2012, fall was one of the most popular periods for cycling renters.
            """
        )

with tab2:
    st.write("""This time I will analyze the bike sharing dataset. And extract knowledge that can be used to make decisions. 
        This dataset contains bike renter data and some weather attributes.""")
    st.dataframe(data=df, width=500, height=150)
    st.write("""After looking at this data I can conclude 2 questions, namely:""")
    st.write("""1. How does the season affect the number of bike rentals?""")
    st.write("""2. How does the number of bike rentals by casual users and registered users compare?""") 
    st.write("""To analyze the bike sharing dataset and answer the two questions, 
             I will analyze and visualize the data. First, I will examine the correlation between the seasonal
              variables and the number of bike loans. Next, I will compare the number of bike loans by casual 
             users and registered users using the corresponding graphs.""")
    
    st.header("Comparison of casual users and user registrations for bicycle rental")

    # Groupby user berdasarkan tahun
    df_2_1 = df.groupby(by='yr').agg({
        "casual": "mean",
        "registered":  "mean"
    })

    # Visualisasi menggunakan clustered bar chart
    plt.figure(figsize=(10, 6))
    width = 0.40
    plt.bar(df_2_1.index-0.2, df_2_1['casual'], width, label='Casual', color='#E69A8D')
    plt.bar(df_2_1.index+0.2, df_2_1['registered'], width, label='Registered', color='#5F4B8B')

    plt.title('Average Casual and Registered Users per Year')
    plt.xlabel('Year')
    plt.ylabel('Average User')

    new_labels = ['2011', '2012']
    plt.xticks(range(len(new_labels)), new_labels, rotation=0)

    plt.legend()
    plt.xticks(df_2_1.index)
    plt.tight_layout()
    st.pyplot(plt)

    with st.expander("Explanation"):
        st.write(
            """Based on the graph above, we can see the comparison of casual users and registered users. 
            The comparison is very far with registered users who rent bicycles the most. 
            From this graph it can be concluded that we succeeded in making the bicycle rental 
            service has successfully attracted the interest and trust of a large number of registered users.
            """
        )