# Movies Extract, Transform and Load (ETL) Challenge
## Overview of Project
This challenge involved learning about and implementing the data pipeline process known as ETL. This is 
the workhorse for moving information between databases. ETL is a core concept in data engineering 
ensuring that data is consistent and maintains its integrity. Without consistent, robust data, any form of 
analysis is impossible. A well-designed ETL pipeline strives to automate as much data wrangling as it can. 
The ETL process can also create data stores that perform more efficiently, reducing the time it takes to 
run analyses.  In this project I assisted Britta, a member of the Amazing Prime video team. Amazing 
Prime Video was a platform for streaming movies and TV shows on Amazing Prime, the world’s largest online
 retailer. The Amazing Prime video team would like to develop an algorithm to predict which low budget 
 movies being released will become popular so that they can buy the streaming rights at a bargain. To 
 inspire the team, have some fun, and connect with the local coding community, Amazing Prime has decided to 
 sponsor a hackathon. Providing a clean data set of move data and asking participants to predict the popular 
 pictures. Britta and I were tasked with creating the datasets for the hackathon.  </p>

## Project Steps
There were two data sources: a scrape of Wikipedia for all movies released since 1990, and rating data from 
the Movie Land’s website. I extracted the data from the two sources, transformed it into one clean data set, 
and finally loaded that data set into a SQL database. I used Python, Jupyter Notebook and Pandas to perform data 
wrangling, and PostgresSQL to store the finished data. </p>

## Challenges
I experienced challenges in learning steps to complete the ETL process. This included understanding and 
developing code to clean the data. I referenced files from both M_Fullerton and Raquely44 (Raquel Yates) from 
GitHub on their respective ETL challenge to correct errors in the code. Finally, I learned that using Python 
code rather than using SQL is less intuitive to follow the process steps.</p>

## Results
I developed four deliverable Python files to complete the process: 
* “ETL_function_test.ipynb” file: wrote an ETL function to read three data files.
* “ETL_clean_wiki_movies.ipynb” file: extracted and transformed the Wikipedia data.
* “ETL_clean_kaggle_data.ipynb” file: extracted and transformed the Kaggle data.
* “ETL_create_database.ipynb”: created the movie database. </p>

