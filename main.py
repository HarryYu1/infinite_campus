import pymysql
import pandas as pd
import matplotlib.pyplot as plt

# connects to school sql database
connection = pymysql.connect(host = 'db.redhawks.us', user = 'ic_student', passwd = '1WillN0t$h@reThis!', database = 'naperville')

with connection.cursor() as cursor:
  # fetches data from sql database
  # sorts each student's classes from lowest grade to highest
  cursor.execute('''
                SELECT StudentID, CourseName 
                FROM `[203_NCHS_Progress_Grades]` 
                ORDER BY StudentID ASC, CoursePercent ASC
                ''')
  print('connected!')

  # imports data into panda
  df = pd.DataFrame(cursor.fetchall(), columns = ['IC_ID', 'CourseName'])

df = df.groupby('IC_ID')['CourseName'].apply(list)

# pseudocode for SOAR class assignment (WIP)
# for (student class)

print(df)

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
