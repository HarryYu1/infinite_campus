#import pymysql
import pandas as pd
import datetime
from decimal import *
#import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy import URL
from sqlalchemy.dialects.mssql import pymssql


#========================================
#   fill with study halls
#========================================
def makeStudyHall(course):
  while len(course) < 3:
    course.append("Study Hall")
  return course




#==============================================================
#   find the lowest grades for people and create a dataframe
#==============================================================
#@param  :  date is a datetime for the soardate to check for assigned
def create_priority_table(date):

  url_object = URL.create(
      "mssql+pymssql",
      username="student",
      password="1WillN0t$h@reThis!",  # plain (unescaped) text
      host="naperville203.infinitecampus.org",
      database="naperville",
      port = 7771
  )

  # connects to school sql database
  #connection = pymysql.connect(host = 'db.redhawks.us', user = 'ic_student', passwd = '1WillN0t$h@reThis!', database = 'naperville')
  engine = sqlalchemy.create_engine(url_object)

  with engine.connect() as cursor:
    # fetches data from sql database
    # sorts each student's classes from lowest grade to highest
    result = cursor.execute(sqlalchemy.text('''
                SELECT StudentID, CourseNumber, CourseName, CoursePercent 
                FROM [dbo].[203_NCHS_Progress_Grades]
                WHERE CoursePercent IS NOT NULL
                ORDER BY StudentID ASC, CoursePercent ASC
                '''))
    print('connected, fetched from grades')

    # imports data into panda
    grade_data = pd.DataFrame(result.fetchall(), columns = ['StudentID', 'CourseNumber', 'CourseName', 'CoursePercent'])
    
    #grab the list of students that have been assigned
    result = cursor.execute(sqlalchemy.text('''
                SELECT personGUID, startDate
                FROM [dbo].[203_NCHS_Assigned_Students]
                '''))
    print('fetched from assigned students')

    assigned_students = pd.DataFrame(result.fetchall(), columns = [ 'personGUID', 'startDate'])

    cursor.commit()
    cursor.close()

    engine.dispose()
  #drop the rows where the date is not the same as ours
  assigned_students = assigned_students[assigned_students.startDate == date]
  print(assigned_students)

  #drop rows in the grade_data based on if a student exists in the assigned students
  IDlist = assigned_students['personGUID'].tolist()
  grade_data = grade_data[grade_data.StudentID.isin(IDlist) == False]
  grade_data.reset_index()

  print(grade_data)


  # removes renames classes with a high enough grade as study hall then removes all but the 3 lowest classess and assesses priority
  for i in grade_data.index:
    if grade_data['CoursePercent'][i] >= 89.5: 
      grade_data['CourseName'][i] = 'Study Hall'
      grade_data['CourseNumber'][i] = '000000'
  
  grade_data = grade_data.groupby('StudentID').head(3).reset_index().rename(columns={'CoursePercent': 'Priority'})

  grade_data.drop('index', axis = 1, inplace = True)
  
  for i in grade_data.index:
    grade_data['Priority'][i] = (i % 3) + 1

  return grade_data





#========================================
#     WRITE TO DATABASE
#========================================
def write_to_database(currdate, soardate):
  #we are going to use place holders for the dates as of now

  #need the two date columns to continue

  dates = {
  "ResponsiveDate" : soardate,
  "ModifiedDate" : currdate
  }

  #fetch the dataframe
  df = create_priority_table(soardate)

  #add the dates
  df = pd.concat([df, pd.DataFrame(dates, index= df.index)], axis = 1)

  print(df)

  url_object = URL.create(
      "mssql+pymssql",
      username="student",
      password="1WillN0t$h@reThis!",  # plain (unescaped) text
      host="naperville203.infinitecampus.org",
      database="naperville",
      port = 7771
  )

  engine = sqlalchemy.create_engine(url_object)

  #writes the data to the table
  connection = engine.connect()
  transaction = connection.begin()
  #try:
  df.to_sql(name = "[dbo].[203_NCHS_Schedule_Priority]", con = connection, if_exists='replace')
  transaction.commit()
  #return True
  #except Exception as e: 
  #  transaction.rollback()
  #  print('Error Occured', error)
  #  return False

  #commented out try accept for error detection














# pseudocode for SOAR class assignment (WIP)
# for (student in database)
#   for (courses student is taking)
#     if (SOAR for class isn't full)
#       assign student to SOAR period
#       return
#   assign student to study hall

# taking a peek at the grade distribution of everyone....
#plt.hist(df["CourseName"], bins = 100)
#plt.show()

'''
#grant all privileges on *.* to 'ic_student'@'%' with grant option;
SELECT current_user();
SELECT user();
#GRANT ALL PRIVILEGES ON naperville.* TO 'ic_student'@'%';
#FLUSH PRIVILEGES;
CREATE USER 'ic_student'@"%" IDENTIFIED BY '1WillN0t$h@reThis!';
GRANT ALL PRIVILEGES ON DATABASE.* TO 'ic_student'@"%" IDENTIFIED BY '1WillN0t$h@reThis!';
SHOW GRANTS;'''
