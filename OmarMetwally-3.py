####################################################### LIBRARIES ########################################################
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
#########################################################################################################################


data = pd.read_csv('Airline Dataset.csv')

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
st.markdown("<h1 style='text-align: Left; font-size: 100; color: #F63366;'>Airline Dataset Visualization</h1>", unsafe_allow_html=True)
#st.title("Airline Dataset Visualization")

# Continent selection in the sidebar
with st.sidebar:
    selected_continent = st.selectbox('Select Continent:', data['Continents'].unique())

# Filter data based on the selected continent
continent_filtered_data = data[data['Continents'] == selected_continent]

# Country selection in the sidebar
with st.sidebar:
    selected_country = st.selectbox(f'Select Country in {selected_continent}:', continent_filtered_data['Country Name'].unique())

# Filter data based on the selected country
filtered_data = continent_filtered_data[continent_filtered_data['Country Name'] == selected_country]




# Chart 1: Bar Chart - Gender Distribution
gender_count = filtered_data['Gender'].value_counts()
st.subheader("Gender Distribution by Country")
fig1 = px.bar(gender_count, x=gender_count.index, y=gender_count.values, labels={'x':'Gender', 'y':'Count'})
st.plotly_chart(fig1)
st.markdown("""
- A bar chart showing the number of male and female passengers on the airline to compare which gender has more passengers.
- The above visualization shows that approximately the same number of men and women travel on the airline, but there are slightly more male passengers.
- There is no significant gender difference in the number of people who travel by airline. This suggests that both men and women are equally interested in traveling.
""")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

# Chart 2: Histogram - Age Distribution
# Customizing the histogram
fig2 = px.histogram(filtered_data, x='Age', nbins=20, labels={'Age': 'Age Range'})
fig2.update_xaxes(dtick=5)  # Add spacing between the bins
fig2.update_layout(xaxis_title="Age Range", yaxis_title="Count")
fig2.update_traces(marker_color='#1f77b4', marker_line_color='black', marker_line_width=1)
fig2.update_layout(showlegend=False)
st.subheader("Age Distribution by Country")
st.plotly_chart(fig2)
st.markdown("""
- A bar chart showing the number of passengers in each age group, from 0 to 5 years old up to and including 90 years old and above.
- The bar chart shows that the most common age groups for passengers are 25-30, 45-50, 55-60, 65-70, and 80-85. This is interesting because it suggests that travel is popular for people of all ages, not just young people.
- It is also interesting to note that there is a large number of passengers who are 80 to 85 years old.
- The fewest passengers are 90 years old and older. This is to be expected, as people in this age group are more likely to have health problems or other limitations that make travel difficult.
""")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


st.subheader("Top 5 Passenger Nationalities by Month")
# Convert the 'Departure Date' column to a datetime object
data['Departure Date'] = pd.to_datetime(data['Departure Date'])

# Create a Streamlit slider for selecting a specific month
selected_month = st.slider("Select a Month", 1, 12, 1)  # Assuming months are represented by integers 1 to 12

# Filter the data for the selected month
filtered_data = data[data['Departure Date'].dt.month == selected_month]

# Get the top nationalities for the selected month
top_nationalities = filtered_data['Nationality'].value_counts().head(5).reset_index()
top_nationalities.columns = ['Nationality', 'Count']

# Create the Plotly pie chart
fig = px.pie(top_nationalities, names='Nationality', values='Count')

# Display the pie chart in the Streamlit app
st.plotly_chart(fig)

st.markdown("""
- Pie chart showing the Top 5 highest passengers traveling based on their nationalities.
- China, which has the highest population in the world, has the most passengers with Chinese nationality.
- Indonesia has the second highest number of passengers, even though it has the fourth highest population in the world.
- We recognized that over the fiscal year of 2022, from January till December always China, Indonesia, Russia, Philippines, and Brazil are the top 5 countries.
""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

# Count the number of delayed flights by country
delayed_count = data[data["Flight Status"] == "Delayed"].groupby("Country Name").size().reset_index()
delayed_count.columns = ["Country Name", "Delayed Flights"]

custom_colorscale = [
    [0.0, 'blue'],
    [0.0005, 'lightblue'],
    [0.001, 'lightcyan'],
    [0.08, 'lightgray'],
    [0.15, 'lightpink'],
    [0.3, 'lightcoral'],
    [0.5, 'salmon'],
    [0.75, 'orangered'],
    [0.9, 'red'],
    [1.0, 'darkred']
]

# Create the choropleth map
fig = px.choropleth(
    delayed_count,
    locations="Country Name",
    locationmode="country names",
    color="Delayed Flights",
    color_continuous_scale=custom_colorscale,
    
)

# Create a Streamlit app
st.subheader("Number of Delayed Flights by Country")
st.plotly_chart(fig)
st.markdown("""
- Observing the global map provided, it becomes evident that the United States stands out as the country with a significantly greater number of delayed flights compared to others.
- This can result from various factors, including weather events, stringent security measures in the United States, the high demand for air travel, and more.
- Conversely, Australia ranks second for experiencing a substantial volume of flight delays.
""")
