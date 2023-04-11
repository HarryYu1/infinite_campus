#SQL test
#from MySQLdb import _mysql
import pymysql
import pandas as pd
#import matplotlib.pyplot as plt

# connects to school sql database
connection = pymysql.connect(host = 'db.redhawks.us', user = 'ic_student', passwd = '1WillN0t$h@reThis!', database = 'naperville')

with connection:
    with connection.cursor() as cursor:
        # fetches data from sql database
        cursor.execute(
            'SELECT * FROM `[203_NCHS_Progress_Grades]`'
        )
        print('connected!')

        # imports data into panda
        df = pd.DataFrame(cursor.fetchall(), columns = ['Index', 'IC_ID', 'CourseName', 'TeacherName', 'LetterGrade', 'Percentage'])
    

#groups data by id 
min_value = df.groupby('IC_ID').Percentage.min()
#merge
df = df.merge(min_value, on='IC_ID',suffixes=('', '_min'))
#drop everything except IC_ID and CourseName
df = df[df.Percentage==df.Percentage_min].drop('Percentage_min', axis=1).drop('TeacherName', axis=1).drop('LetterGrade', axis=1).drop('Percentage', axis=1).drop('Index', axis=1)
print(df)


#taking a peek at the grade distribution of everyone....
#plt.hist(df["Percentage"], bins = 100)
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
