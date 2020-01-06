import datetime
date = datetime.date.today()
course_link = "https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_selfpy101+3_2019/courseware/73c5298a6ce54e9d9c8ebba123050efc/d1521fc3f4164b2eb427b27fae88581d/"
unit_number = 5
subject = "function"
chapter_number = 5.3
chapter_name = "5.3 function input output "
task = "finish the exerice number 5.3.4 lastearly()"



def print_status ():
    print ("======== Python course my progression and status ======== ")
    print ("course link: ", course_link)
    print ("Date:", date.strftime("%d/%m/%Y"))
    print ("unit number = ",unit_number)
    print ("subject = ",subject)
    print ("chapter number = ", chapter_number)
    print ("chapter name = ",chapter_name)
    print ("task = ", task)


print_status()



