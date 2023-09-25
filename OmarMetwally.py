####################################################### LIBRARIES ########################################################
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
#########################################################################################################################


data = pd.read_csv('C:\\Users\\Ahmad\\Desktop\\Airline Dataset.csv')

st.set_page_config(page_title = 'Omar Dashboard',
                    page_icon = 'bar_chart:',
                    layout = 'wide'
)

st.set_option('deprecation.showPyplotGlobalUse', False)
##################################################################################################################################




######################################################### TABS AND SESSIONS #################################################
# Create a dictionary to store the session state
session_state = st.session_state



# Main app
st.title("Airline Dataset Visualization")

# Chart 1: Bar Chart - Gender Distribution
gender_count = data['Gender'].value_counts()
st.subheader("Gender Distribution")
fig1 = px.bar(gender_count, x=gender_count.index, y=gender_count.values, labels={'x':'Gender', 'y':'Count'})
st.plotly_chart(fig1)

# Chart 2: Histogram - Age Distribution
# Customizing the histogram
fig2 = px.histogram(data, x='Age', nbins=20, title="Age Distribution", labels={'Age': 'Age Range'})
fig2.update_xaxes(dtick=5)  # Add spacing between the bins
fig2.update_layout(xaxis_title="Age Range", yaxis_title="Count")
fig2.update_traces(marker_color='#1f77b4', marker_line_color='black', marker_line_width=1)
fig2.update_layout(showlegend=False)

st.plotly_chart(fig2)

# Chart 3: Pie Chart - Nationality Distribution
# Calculate the top 5 nationalities
top_nationalities = data['Nationality'].value_counts().head(5).reset_index()
top_nationalities.columns = ['Nationality', 'Count']

# Streamlit app
st.title("Top 5 Passenger Nationalities")

# Display the top 5 nationalities as a pie chart
fig = px.pie(top_nationalities, names='Nationality', values='Count', title='Top 5 Passenger Nationalities')
st.plotly_chart(fig)