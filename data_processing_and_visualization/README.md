# Task 2: Data Processing and Visualization

For this task, I tried to find an API that could be used to fetch student scores but I couldn't find the right fit, so I made a simple REST API using Flask and put 10 students mock data into it.

### Here's a the REST API running locally on my PC:

![api](screenshots/api.jpg)

After that I used requests library to fetch the data from the API and parsed it into proper JSON format.

### Here's the response from the API:

![api response](screenshots/api_response.jpg)

After retrieving the data, I converted it into a Pandas DataFrame, calculated and added total_score, average_score columns to the DataFrame.

### Here's the final processed DataFrame:

![dataframe](screenshots/df.jpg)

Finally using the matplotlib library, I visualized the data using bar charts for average scores and all three subjects.

### Bar Charts
![average score](screenshots/average_score.png)
![math score](screenshots/math_score.png)
![physics score](screenshots/physics_score.png)
![chemistry score](screenshots/chem_score.png)