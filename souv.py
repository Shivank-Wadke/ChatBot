import pywhatkit #Sending messages to whatsapp via python
import datetime
import smtplib #Sending messages to mails via python 
import regex as re #Data validation
from PIL import Image # PIL - python imaging library
import random
import time
#Greetings for the user
print("\nWelcome to Pimpri Chinchwad University!\nI'm your guide to the exciting tour of education.\nBut, before we begin I would like to know more about you.")
#Getting user information
a = input("\nEnter your full name >")
#Validating Email Address
emailFlag = True;
while emailFlag:
      reg_pattern=(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  
      b=input("\nEnter valid email address >>")
      if (re.fullmatch(reg_pattern,b)):
         emailFlag=False;
      else:
         emailFlag=True;
 #Validating Phone Number
phnFlag = True;
while phnFlag:
      re_pattern= (r"^\+?[0-9]{2,4}\s?[0-9]{9,15}")
      c=input("\nEnter valid phone number with country code >>")
      if (re.fullmatch(re_pattern,c)):
         phnFlag=False;
      else:
         phnFlag=True;
print("Thank you for sharing your details!\n\n-------------------------------------------------------------------------")
#OTP Validation
random_number = random.randint(1000, 9999)
otp_message=("Hello",a,",\nYour email verification code is >>",random_number,"\n\nTeam,\nPCU")
otp = ' '.join(map(str, otp_message))
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("souvbot23@gmail.com","yhyubxaewvbrghts")
server.sendmail("souvbot23@gmail.com",b,otp)
otp_flag=True;
while otp_flag:
    user_otp=int(input("Enter the 4 digit OTP received on your mail to proceed >>"))
    if user_otp==random_number:
       print("User Verified Sucessfully!")
       otp_flag=False;
    else:
       print("OTP entered invalid!")
       otp_flag=True; 
print("\nAt PCU, We offer a variety of courses\nB.tech\nB.Pharm\nBCA\nBBA\n\nType in the course you're interested in!")
course_flag=True;
check = ["B.tech","B.Tech","BTech","b.tech","btech","BTECH","Btech"]
check2=["Placement","Placements","placement","Placements"]
check3=["BCA","Bca","B.C.A","bca","b.c.a"]
check5=["Yes","YES","yes","y","Y"]
check6 =["No","NO","no","n","N"]
check7=["Contact Details","contact","Contact","contact detail","contact details"]
check8=[" Course Syllabus","course syllabus","syllabus","Syllabus","Course","course"]
check9=["Bpharm","B.pharm","b.pharm","BPHARM","bpharm","B.PHARM"]
check10=["Hostel","hostel","HOSTEl"]
check11=["Transportation","transport","Transport","transportation"]
check12=["BBA","bba","Bba","B.b.a","B.B.A","B.b.a"]
while course_flag:
   ask=input(">>")
   if ask in check:
      print("\nYou have chosen Bachelors in Technology.\n------------------------------------------------------------")
      course_flag=False;
   elif ask in check3:
      print("\nYou have chosen Bachelors in Computer Applications.\n------------------------------------------------------------")
      course_flag=False;
   elif ask in check9:
      print("\nYou have chosen Bachelors in Pharmacy.\n------------------------------------------------------------")
      course_flag=False;
   elif ask in check12:
      print("\nYou have chosen Bachelors in Business Administration.\n------------------------------------------------------------")
      course_flag=False;
   else:
        print("Please select an appropriate course!")
        course_flag='True'

print("\nHey",a,"lets explore more!")
def admissions():
   print("\n\nAdmission process :\n1. Register to apply\n2.Complete the applicaion form\n3.Submit the form.\nEvaluation of Candidate profile will be done\n5.Provisional Offer letter\n6.Pay to confirm the seat!\n------------------------------------------------------------")
def fees():
   print("Fees for :\nBtech(All branches) - 2,10,000/yr\n------------------------------------------------------------")
import random
from datetime import time
def generate_random_time(hour):
    minutes = [0, 15, 30, 45]
    minute = random.choice(minutes)
    random_time = time(hour, minute)
    return random_time
hour = 3
random_time = generate_random_time(hour)
def schlolarships():
   print("PCU provides variety of Scholarships!!")
   schlo_flag=True;
   while schlo_flag:
      ask1=input("Did you attempt JEE?")
      if ask1 in check5:
         jee_rank=int(input("Enter your Rank >>"))
         if jee_rank>0 and jee_rank<=4000:
            print("You will be given 70% off on the tuition fees for FY!")
            schlo_flag=False;
         elif jee_rank==0:
            print("No Scholarships based on JEE")
            schlo_flag=False;
         elif jee_rank>4000 and jee_rank<=6000:
            print("You will be given 40% off on the tuition fees for FY!")
            schlo_flag=False;
         elif jee_rank>6000 and jee_rank<=8000:
            print("You will be given 15% off on the tuition fees for FY!")
            schlo_flag=False;
         elif jee_rank>8000:
            print("No Scholarships based on JEE")
            schlo_flag=False;
      elif ask1 in check6:
         board_10=float(input("Enter class 10th board percentage >>"))
         board_12=float(input("Enter class 12th board percentage >>"))
         if board_10>=85 and board_12>=85:
            print("You have a scholarpship available!")
            schlo_flag=False;
         else:
            print("You are not eligible for any scholarships")
            schlo_flag=False;
      else:
         print("Input Invalid!")
         schlo_flag=True;
def placements():
   print("Pimpri Chichwad University is known for its centralised Placement cell!\n")
   print("displaying placement statistics\n------------------------------------------------------------")
def bca_fees():
   print("Fees for BCA - 1,25,000/yr (*3 or 4 year program)\n------------------------------------------------------------")
def bca_eligibility():
   print("Open Category student should have scored minimum 45% of Score at 10+2 level from ICSE/ CBSE/Any State Board Examination\nor equivalent qualification from any recognized board in Science, Commerce with preferably mathematics as subject and 40% for reserved category candidate.\nCandidates are selected on the basis of Merit AND Personal interview conducted by PCU\n------------------------------------------------------------")
def contact_details():
   print("\nWebsite : www.pcupune.in\nEmail :info@pcu.edu.in\nPhone number :+91-9046909003 | 8381814141\n------------------------------------------------------------")
def bca_course():
   print("Displaying Course Syllabus for BCA FY!")
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\bca.png")
   img.show()
def btech_course():
   print("Displaying Course Syllabus for Btech FY!\n------------------------------------------------------------")
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\btech.png")
   img.show()
def bpharm_fees():
   print("Fees for B.Pharm - 1,40,000/yr\n------------------------------------------------------------")
def bca_scholarships():
   print("Currently we don't offer scholarpships for BCA\n------------------------------------------------------------")
def bba_scholarships():
   print("Currently we don't offer scholarpships for BBA\n------------------------------------------------------------")
def bpharm_scholarships():
   print("Currently we don't offer scholarpships for B.Pharm\n------------------------------------------------------------")
def bpharm_course():
   print("Displaying Course Syllabus for B.Pharm FY!\n------------------------------------------------------------")
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\bpharm.png")
   img.show()
def bpharm_eligibility():
   print("Candidate shall have passed 10+2 examination conducted by the respective state/central government authorities recognized as equivalent to 10+2 examination by the \nAssociation of Indian Universities (AIU) with English as one of the subjects and Physics, Chemistry, Mathematics/Biology as optional subjects individually.\n------------------------------------------------------------")
def bpharm_placements():
   print("At PCU we offer centralised placement cells. Students get numerous career opportunities!\n------------------------------------------------------------")
def hostel_info():
   print("\nAll the necessary facilities are provided at our hostel which will ensure mental,physical and social wellbeing!\nHostel is just 2kms away from the campus and bus transport to and from the hostel is included in the fee!\nApartment Fee: 70,000/yr\nMess :40,000/yr\n------------------------------------------------------------")
def be_bc_placement():
   print("Quality placements are offered at PCU starting from 3.5LPA to 61LPA!")
   print("Displaying Quantitative Placement Highlights\n------------------------------------------------------------")
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\placement.png")
   img.show()
def transportation():
   print("PCU provides transportation service from Aundh BRT, Dapodi, Bhosari, Sanghavi to the University. You can board the bus at any predfined stops")
   location_flag=True;
   while location_flag:
      location=input("Enter the route map you want to see >>")
      if location=="aundh" or location=="aundh brt" or location =="Aundh" or location=="Aundh Brt":
         img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\aundh.png")
         print("Displaying Bus route for Aundh")
         img.show()
         location_flag=False;
      elif location=="bhosari" or location=="Bhosari":
         img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\bhosari.png")
         print("Displaying Bus route for Bhosari")
         img.show()
         location_flag=False;
      elif location=="dapodi" or location=="Dapodi":
         img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\dapodi.png")
         print("Displaying Bus route for Dapodi")
         img.show()
         location_flag=False;
      elif location=="Sanghavi" or location=="sanghavi":
         img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\sanghavi.png")
         print("Displaying Bus route for Sanghavi")
         img.show()
         location_flag=False;
      else:
         location_flag=True;
check13=["life","Life","Life at PCU","life at pcu","Life at Pcu"]
def bba_fees():
   print("Fees for BBA : 1,25,000/yr(*3 or 4 year program)")
def bba_eligibility():
   print("Open Category student should have scored minimum 50 % of Score at 10+2 level from ICSE/ CBSE/Any State Board Examination or \nequivalent examination from any recognized board in Art, Science, Commerce or any other stream and 45% for reserved category candidate.")
def bba_course():
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\bba.png")
   print("Displaying course syllabus for BBA FY!")
   img.show()
def pcu_life():
   print("PCU not only focusses on top notch education but life at PCU is filled with any cultural acitvities as well!\nStarting from all the patriotic days like Republic Day and Independence day to the exciting dance,singing competitions.\nYearly we have a cultural event Anantam with lot of performances filled with joy,powerfulness!\nNavratri, Ganesh Chaturti celebrations take place too with Mahaprasad being arranged by the college!")
   img = Image.open(r"C:\Users\Shivank\Desktop\PCU_Chatbot\pcu.png")
   img.show()
def user_continue():
   user_flag=True;
   global detail_flag
   detail_flag=True;
   while user_flag:
      user=input("\nDo you want to explore more (Y/N) >")
      if user in check5:
         print("\n------------------------------------------------------------")
         user_flag=False;
         detail_flag=True;
      elif user in check6:
         print(a,",We look forward to meet you soon!")
         user_flag=False;
         detail_flag=False;
      else:
         print("Input Invalid!")
         user_flag=True;

#Talking with the user about Btech Course
detail_flag=True;
if ask in check:
   while detail_flag:
      print("\nAdmissions\nScholarships\nFee\nCourse Syllabus\nPlacement\nContact Details\nHostel\nTransportation\nLife At PCU")
      detail =input("\nWhat would you like to explore >> ")
      print("\n------------------------------------------------------------")
      if detail == 'admissions' or detail=='Admissions' or detail=='Admission' or detail=='admission' :
         admissions()
         user_continue()
      if detail in check10:
         hostel_info()
         user_continue()
      if detail in check13:
         pcu_life()
         user_continue()
      if detail=="Fees" or detail=="fees" or detail=="fee" or detail =="Fee":
         fees()
         user_continue()
      if detail in check11:
         transportation()
         user_continue()
      if detail=="Scholarship" or detail=="scholarship" or detail=="Scholarships" or detail=="scholarships":
         schlolarships()
         user_continue()
      if detail=="Placements" or detail =="placements" or detail=="Placement" or detail=="placement":
         be_bc_placement()
         user_continue()
      if detail in check7:
         contact_details()
         user_continue()
      if detail in check8:
         btech_course()
         user_continue()
#Talking with the user about BCA course
elif ask in check3:
   while detail_flag:
      print("\nAdmissions\nScholarships\nFee\nPlacement\nCourse Syllabus(FY)\nEligibility\nContact Details\nHostel\nTransportation\nLife at PCU")
      detail =input("\nWhat would you like to explore >>")
      print("\n------------------------------------------------------------")
      if detail == 'admissions' or detail=='Admissions' or detail=='Admission' or detail=='admission' :
         admissions()
         user_continue()
      if detail in check13:
         pcu_life()
         user_continue()
      if detail in check11:
         transportation()
         user_continue()
      if detail=="Fees" or detail=="fees" or detail=="fee" or detail =="Fee":
         bca_fees()
         user_continue()
      if detail in check10:
         hostel_info()
         user_continue()
      if detail=="Scholarship" or detail=="scholarship" or detail=="Scholarships" or detail=="scholarships":
         bca_scholarships()
         user_continue()
      if detail=="Placements" or detail =="placements" or detail=="Placement" or detail=="placement":
         be_bc_placement()
         user_continue()
      if detail=="Eligibility" or detail=="eligibility":
         bca_eligibility()
         user_continue()
      if detail in check7:
         contact_details()
         user_continue()
      if detail in check8:
         bca_course()
         user_continue()
#Talking with the user about B.Pharm Course
elif ask in check9:
   while detail_flag:
      print("\nAdmissions\nScholarships\nFee\nPlacement\nCourse Syllabus(FY)\nEligibility\nContact Details\nHostel\nTransportation\nLife at PCU")
      detail =input("\nWhat would you like to explore >> ")
      print("\n------------------------------------------------------------")
      if detail == 'admissions' or detail=='Admissions' or detail=='Admission' or detail=='admission' :
         admissions()
         user_continue()
      if detail in check13:
         pcu_life()
         user_continue()
      if detail=="Fees" or detail=="fees" or detail=="fee" or detail =="Fee":
         bpharm_fees()
         user_continue()
      if detail in check11:
         transportation()
         user_continue()
      if detail in check10:
         hostel_info()
         user_continue()
      if detail=="Scholarship" or detail=="scholarship" or detail=="Scholarships" or detail=="scholarships":
         bpharm_scholarships()
         user_continue()
      if detail=="Placements" or detail =="placements" or detail=="Placement" or detail=="placement":
         bpharm_placements()
         user_continue()
      if detail=="Eligibility" or detail=="eligibility":
         bpharm_eligibility()
         user_continue()

      if detail in check7:
         contact_details()
         user_continue()
      if detail in check8:
         bpharm_course()
         user_continue()
#Talking with the user about BBA Course
elif ask in check12:
   while detail_flag:
      print("\nAdmissions\nScholarships\nFee\nPlacement\nCourse Syllabus(FY)\nEligibility\nContact Details\nHostel\nTransportation\nLife at PCU")
      detail =input("\nWhat would you like to explore >> ")
      print("\n------------------------------------------------------------")
      if detail == 'admissions' or detail=='Admissions' or detail=='Admission' or detail=='admission' :
         admissions()
         user_continue()
      if detail=="Fees" or detail=="fees" or detail=="fee" or detail =="Fee":
         bba_fees()
         user_continue()
      if detail in check13:
         pcu_life()
         user_continue()
      if detail in check11:
         transportation()
         user_continue()
      if detail in check10:
         hostel_info()
         user_continue()
      if detail=="Scholarship" or detail=="scholarship" or detail=="Scholarships" or detail=="scholarships":
         bba_scholarships()
         user_continue()
      if detail=="Placements" or detail =="placements" or detail=="Placement" or detail=="placement":
         bpharm_placements()
         user_continue()
      if detail=="Eligibility" or detail=="eligibility":
         bba_eligibility()
         user_continue()
      if detail in check7:
         contact_details()
         user_continue()
      if detail in check8:
         bba_course()
         user_continue()

message_text=(a,", Welcome to Pimpri Chinchwad University, Pune! This university comes under PCET and has a legacy of nurturing excellence!\nWe see that you were exploring",ask,"\nWe are excited to tell you more about it!\nOur admission team will connect with you soon.\nFor further queries, Contact- +91-9046909003\n\nTeam,\nPimpri Chinchwad University,\nSate,Maval-412106",)
message_text2=(a,",\nWe see that you were exploring",ask,".\nYou are one step away from getting into the domain you wish to! Don't miss out on this opportunity.\nYour On-Call appointment is at",random_time,"pm on 6th May and you will be counselled by Mr.Harvey James(Admission Head).\n\nTeam,\nPimpri Chinchwad University")
result = ' '.join(map(str, message_text))
result2 = ' '.join(map(str, message_text2))
#Sending an Email to user
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("souvbot23@gmail.com","yhyubxaewvbrghts")
server.sendmail("souvbot23@gmail.com",b,result)

#Sending a whatsapp message to user 
def send_msg():
   now = datetime.datetime.now()
   pywhatkit.sendwhatmsg(c,result2,now.hour,now.minute+1,15)
import time
for i in range(1,10):
   try:
      send_msg()
      print("Message sent sucessfully!")
      break;
   except:
      print("Error in sending message due to whatsapp server. Retrying in 5 seconds")
      time.sleep(5)



