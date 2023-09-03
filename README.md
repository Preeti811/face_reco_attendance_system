# Face recognition based attendance system-

### Steps to follow-

- sql file name-  'project_db1'  ;  table name - 'new_table';
- change the path name where image files will be stored accordingly,line no 11 gui file)----   path = 'C:\\Users\\PREETI\\Desktop\\faceimage_database'
- for running file download facerecognition folder and then run finalProject folder after changing the corresponding paths.

### Project flow & explaination
- Used open cv for face detection and determination of contour of image.
- @created database in SQL 
- @created gui using ktinker
- @created face detection and recognition model using Haarcascade
- First it will image capture for new user and will save in a directory and will store personal data of user in SQL database.
- @then it will train images data...
- After image training happens 'Training data.XML'  file will be stored which will contain trained data information.
- From this file only  the features of the  face that is  detected by camera will be compared....and result will be displayed on screen...
- If face is recognised the individual's id will be displayed there
- @then we will open gui 'find face'
- Where it will match face with existing data's....
- If face detected attendance will be marked and will be stored in a .CSV file.

### Screenshots-

### Simple UI
![image](https://user-images.githubusercontent.com/80096242/206753966-cdb7193c-ab0c-4f17-8464-599ed47a7dd8.png)
![image](https://user-images.githubusercontent.com/80096242/206753519-f783454d-11ae-40b5-812c-3627e88873b4.png)

### While taking Attendance-
![image](https://user-images.githubusercontent.com/80096242/206768887-0434919e-974c-4b6a-bd4b-737d798745db.png)


### Attendance in tabular format 
![image](https://user-images.githubusercontent.com/80096242/206753787-f8e0b0cd-f9ba-4194-bc48-429e684afaf6.png)

### If you like it do Star ⭐ the repository!!
