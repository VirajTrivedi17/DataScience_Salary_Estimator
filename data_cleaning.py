
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:17:25 2020

@author: vrjtr
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#salary parsing




#Salary_Evaluation
#make new column for per hour salary
df["hourly"] = df["Salary Estimate"].apply(lambda x : 1 if 'per hour' in x.lower() else 0)

#make new column for employer provided
df["employer_provided"] = df["Salary Estimate"].apply(lambda x : 1 if 'employer provided salary:' in x.lower() else 0)
#remove -1 from the salary estimate column
df = df[df["Salary Estimate"]!= "-1"]
#removing of brackets in Salary Estimate
salary = df["Salary Estimate"].apply(lambda x : x.split(' (')[0])

#remove letters and dollar sign from salary estimate
rem_K_dollar = salary.apply(lambda x: x.replace('K',  " ").replace("$", " "))

#replacing/removing per hour and employer provided 
minus_hr = rem_K_dollar.apply(lambda x : x.lower().replace('per hour', '').replace('employer provided salary:', '').replace("(employer est.)", "").replace("(glassdoor est.)", ""))

#separating the minimum and maximum salary
df["min_salary"] = minus_hr.apply(lambda x : int(x.split("-")[0]))
df["max_salary"] = minus_hr.apply(lambda x : int(x.split("-")[1]))

df["avg_salary"] = (df.min_salary+df.max_salary)/2

#company name text only
df["company_text"] = df.apply(lambda x: x["Company Name"] if x["Rating"]<0 else x["Company Name"][:-3], axis = 1  )

#state column
df["job_state"] = df["Location"].apply(lambda x : x.split(", ")[1])
df.job_state.value_counts()
df["same_state"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company
df["age"] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#parsing of job description
df["Job Description"][0]

#job positions = python,rstudio,excel,bigdataor sprak

df["python"] = df["Job Description"].apply(lambda x : 1 if 'python' in x.lower() else 0)
df.python.value_counts()

df["excel"] = df["Job Description"].apply(lambda x : 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df["spark"] = df["Job Description"].apply(lambda x : 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df["aws"] = df["Job Description"].apply(lambda x : 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#Creating function for job title and position level

def simplified_title(title):
    if "data scientist" in title.lower():
        return "data scientist"
    elif "data engineer" in title.lower():
        return "data engineer"
    elif "machine learning" in title.lower():
        return "machine learning"
    elif "analyst" in title.lower():
        return "analyst"
    elif "manager" in title.lower():
        return "manager"
    elif "director" in title.lower():
        return "director"
    else:
        return "nan"
    
def position_level(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'
        
    
df["simplified_job"] = df["Job Title"].apply(simplified_title)
df.simplified_job.value_counts()


df["position_level"] = df["Job Title"].apply(position_level)
df.position_level.value_counts()


df["Rstudio"] = df["Job Description"].apply(lambda x : 1 if 'r studio' in x.lower() or "r-studio" else 0)
df.Rstudio.value_counts()

#dropping the unnamed column
cleaned_data = df.drop(['Unnamed: 0'], axis = 1)

#convering into .csv file
cleaned_data.to_csv("salary_data_cleaned.csv", index = False)

pd.read_csv("salary_data_cleaned.csv")