# MyResume
# Fun Project

This project is a fun script written in Python to generate a resume for Asmaa Alrefae. The script utilizes the pandas library to create data frames for work experience and education, and then uses a string template to generate a formatted resume.

## Libraries Used
- pandas

## Personal Information
- Name: Asmaa Alrefae
- Email: asmaa.a.alrefae@gmail.com
- LinkedIn: https://www.linkedin.com/in/asmaaalrefae/

## Work Experience
The `exp` data frame contains the following information for each of Asmaa's work experiences:
- Company name
- Position held
- Start and end dates
- Job description

## Education
The `edu` data frame contains the following information for each of Asmaa's educational qualifications:
- Institution name
- Degree obtained
- Graduation date

## Skills
The `skills` variable is a list of skills that Asmaa possesses.

## Resume Template
The `resume` string variable is the template for the final resume. It contains placeholders for Asmaa's personal information, work experience, education, and skills. The script utilizes a for loop to populate each of these sections with the relevant information from the data frames and skills list.

## Output
The script outputs the `exp` data frame and the final formatted resume generated using the `resume` template.
