import pymysql
import pandas as pd
import datetime
from decimal import *
import matplotlib.pyplot as plt

def makeStudyHall(course):
  while len(course) < 3:
    course.append("Study Hall")
  return course

# connects to school sql database
connection = pymysql.connect(host = 'db.redhawks.us', user = 'ic_student', passwd = '1WillN0t$h@reThis!', database = 'naperville')

with connection.cursor() as cursor:
  # fetches data from sql database
  # sorts each student's classes from lowest grade to highest
  cursor.execute('''
                SELECT StudentID, CourseName, CoursePercent 
                FROM `[203_NCHS_Progress_Grades]`
                WHERE CoursePercent IS NOT NULL
                ORDER BY StudentID ASC, CoursePercent ASC
                ''')
  print('connected!')

  # imports data into panda
  df = pd.DataFrame(cursor.fetchall(), columns = ['StudentID', 'CourseName', 'CoursePercent'])

# takes the Coursename column and groups them by the student ID, then turns it into a list, then takes the 3 lowest grades from that list
for i in df.index:
  if df['CoursePercent'][i] >= 90: 
    df['CourseName'][i] = 'Study Hall'

df = df.groupby('StudentID')['CourseName'].apply(list).apply(lambda x : x[:3]).reset_index(name='CourseName').explode('CourseName').reset_index()

df['Priority'] = df.groupby('index').cumcount() + 1

df.drop(['index'], axis = 1, inplace = True)

now = datetime.datetime(2009, 5, 5)



print(df)



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
