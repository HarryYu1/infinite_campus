#SQL test
#from MySQLdb import _mysql
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from decouple import config # allows .env files

# Import variables from the .env file
env_HOST = config('HOST')
env_USER = config('USER')
env_PASSWORD = config('PASSWORD')
env_DATABASE = config('DATABASE')

# Modified to use ENV variables
connection = pymysql.connect(host = env_HOST, user = env_USER, passwd = env_PASSWORD, database = env_DATABASE)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM `[203_NCHS_Progress_Grades]`'
        )
        print('connected!')

        df = pd.DataFrame(cursor.fetchall(), columns = ['Index', 'IC_ID', 'CourseName', 'TeacherName', 'LetterGrade', 'Percentage'])
    

#students = df['IC_ID'].unique()

#print(students)
#print(students.size)

#groups data in 
min_value = df.groupby('IC_ID').Percentage.min()
#merge
df = df.merge(min_value, on='IC_ID',suffixes=('', '_min'))
#drop B_min and also keep only data where B = min
df = df[df.Percentage==df.Percentage_min].drop('Percentage_min', axis=1)

print(df)

#taking a peek at the grade distribution of everyone....
plt.hist(df["Percentage"], bins = 100)
plt.show()

'''
#grant all privileges on *.* to 'ic_student'@'%' with grant option;
SELECT current_user();
SELECT user();
#GRANT ALL PRIVILEGES ON naperville.* TO 'ic_student'@'%';
#FLUSH PRIVILEGES;

CREATE USER 'ic_student'@"%" IDENTIFIED BY '1WillN0t$h@reThis!';
GRANT ALL PRIVILEGES ON DATABASE.* TO 'ic_student'@"%" IDENTIFIED BY '1WillN0t$h@reThis!';

SHOW GRANTS;'''
