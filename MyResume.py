# Import necessary libraries
import pandas as pd

# Define personal information
name = "Asmaa Alrefae"
email = "asmaa.a.alrefae@gmail.com"
linkedin ="https://www.linkedin.com/in/asmaaalrefae/"


# Define work experience
exp = pd.DataFrame({
    'Company': ['General Assembly','General Assembly', "Aquat Food", "Statistical Consulting Service Unit"],
    
    
    'Position': ["Instructional Associate for DAPI3",
    "Instructional Associate for DAPI1",
    'Senior Data Analyst', 'Intern'], 
    
    'Start Date': ['03-2021',"11-2020","05-2015"
    ,"01-2014"],
     'End Date': ['04-2021',"01-2021","09-2019"
    ,"04-2014"],
  'Description': [  'A Project-based program where I mentor a total of 38 students to learn about Data Analysis, Advanced Excel, SQL, Tableau, Python Fundamentals.',
  
  'A Project-based program where I mentor a total of 37 students to learn about Data Analysis, Advanced Excel, SQL, Tableau, Python Fundamentals.',
  
  
'Joined as Junior Analyst, then got promoted within seven months to mid-level Analyst and to a Senior Analyst within a year. Key Achievements:\n- Built and automated Key Performance Indicators report using Microsoft Excel, resulted in a 90% decrease in delivery time.\n- Improved annual evaluation process, leading to 70% reduction in delivery time.\n- Performed analysis of satisfaction surveys resulting in an 80% improvement.\n- Presented and interpreted analytical insights to business leaders.\n- Documented business workflows for stakeholder review.\n- Managed and trained HR development teams across multiple geographical locations, resulting in the successful franchising of plants.'  ,

    'Assist the Researcher in: \n- Designing and evaluating surveys\n- Identifying sample sizes\n- Interpreting and analyzing data\n- Determining the Statistical Methods to be used\n- Developing reports and metrics to the related audiences']})

# Define education
edu = pd.DataFrame({
    'Institution': [ "General Assembly","General Assembly",'King Abdulaziz University' ],
     'Degree': ["Certified Product Management","Certified Data Scientist",'Bachelor of Science in Statistics' ],
   'Graduation Date': ["17-03-2021",'19-12-2019',
   '19-06-2014' ]  })

# Define skills
skills = ["Research","Reporting", "Statistics",
 "Problem-solving", "Analytical Skills" , 
 "Data analysis", "Predictive models" ,
 "Machine Learning", "Data Visualization",
 "Microsoft Excel", "Python", "R" , "SPSS", "SQL"]


# Define resume template
resume = f"""
{name}
{email}
{linkedin}

Work Experience
----------------
"""

for i in range(len(exp)):
    resume += f"{exp.iloc[i]['Position']} at {exp.iloc[i]['Company']} ({exp.iloc[i]['Start Date']} - {exp.iloc[i]['End Date']})\n"
    resume += f"- {exp.iloc[i]['Description']}\n\n"

resume += "Education\n---------\n"

for i in range(len(edu)):
    resume += f"{edu.iloc[i]['Degree']} from {edu.iloc[i]['Institution']} ({edu.iloc[i]['Graduation Date']})\n\n"

resume += "Skills\n------\n"

for skill in skills:
    resume += f"{skill}\n"

# Print resume
print(exp)
print(resume)
