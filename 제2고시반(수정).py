import time
import pickle
time.sleep(0.5)
print('Hello world!')
time.sleep(0.5)

addData = 0

def prt(a,b):
	print('\n',end='')
	time.sleep(0.1)
	a = list(a)
	for i in range(0,len(a)):
		time.sleep(float(b))
		print(a[i],end='')
		
def prit(a,b):
	print('\n',end='')
	a = list(a)
	for i in range(0,len(a)):
		time.sleep(float(b))
		print(a[i],end='')


file = open('isDbReady.txt', 'a')
file.close()
        
with open('isDbReady.txt', 'r') as file:
        isDbReady = file.read()

        

test_file = open("comment1.txt", "a", encoding="utf8")
test_file.close()

test_file2 = open("attendanceData1.txt", "a", encoding="utf8")
#test_file2.write(str(-291))
test_file2.close()

test_file3 = open("signoutData1.txt", "a", encoding="utf8")
#signoutDataNow = str(earlytime)
#test_file3.write(str(55))
test_file3.close()

test_file4 = open("additionalStudy1.txt", "a", encoding="utf8")
test_file4.close()

test_file5 = open("additionalStudy2.txt", "a", encoding="utf8")
test_file5.close()


def dataReset(pw):
    if pw == int('0000'):
    	print('warning; data reset')
    	print("if you want to reset data, input 'yes'.")
    	print("'no' or other answer will cancel this procedure.")
    	answer=input("reset data?: ")
    	if answer=='yes':
    		global attend_record
    		global leave_record
    		global attend_num
    		global leave_num
    		global addData
    		attend_record = [0]
    		leave_record = [0]
    		attend_num = 0
    		leave_num = 0
    		addData = [0]
    		with open('isDbReady.txt', 'w') as file:
    			file.write('ready')
                        
    		with open('additionalStudy1.txt', 'w') as file:
    			file.write('')

    		with open('additionalStudy2.txt', 'w') as file:
    			file.write('')
    			
    		with open('attendanceData1.txt', 'w') as file:
    			file.write('')

    		with open('signoutData1.txt', 'w') as file:
    			file.write('')
                    
    		with open(file='picklejar1.pickle',mode='wb') as f:
    			pickle.dump(attend_record,f)
    			pickle.dump(leave_record,f)
    			pickle.dump(attend_num,f)
    			pickle.dump(leave_num,f)
    		with open(file='picklejar2.pickle',mode='wb') as f:
    			pickle.dump(addData,f)
    		print(attend_record)
    		reboot_num = 20
    		print('system rebooting',end='')
    		while reboot_num > 0:
    			print('-',end='')
    			time.sleep(0.01)
    			reboot_num = reboot_num - 1
    		print('-')
    	else:
    		print("data reset procedure is now canceled")
    else :
    	print('비밀번호가 잘못되었습니다. 관리자에게 문의하십시오.')	


                                                                                

def dataInitialize():
    	print('Data Initializing...')
    	print("installing required files")
    	global attend_record
    	global leave_record
    	global attend_num
    	global leave_num
    	global addData
    	attend_record = [0]
    	leave_record = [0]
    	attend_num = 0
    	leave_num = 0
    	addData = [0]
    	with open('isDbReady.txt', 'w') as file:
    		file.write('ready')


    	with open('additionalStduy1.txt', 'w') as file:
    		file.write('')

    	with open('additionalStduy1.txt', 'w') as file:
    		file.write('')

    	with open('attendanceData1.txt', 'w') as file:
    		file.write('')

    	with open('signoutData1.txt', 'w') as file:
    		file.write('')

    		
    	with open(file='picklejar1.pickle',mode='wb') as f:
    		pickle.dump(attend_record,f)
    		pickle.dump(leave_record,f)
    		pickle.dump(attend_num,f)
    		pickle.dump(leave_num,f)
    	with open(file='picklejar2.pickle',mode='wb') as f:
    		pickle.dump(addData,f)
    	print(attend_record)
    	reboot_num = 20
    	print('system rebooting',end='')
    	while reboot_num > 0:
    		print('-',end='')
    		time.sleep(0.01)
    		reboot_num = reboot_num - 1
    	print('-')

    
#dataReset(0000) ##<----in the case of data reset, use this line with correct passwords.##

                                                                        


"""if error occurs in first trial, try input 'dataReset(0000)"""


if isDbReady != 'ready':
        print('DataBase not ready')
        dataInitialize()
elif isDbReady == 'ready':
        print('DataBase ready')




'''
test_file = open("test.txt", "r", encoding="utf8")
print(test_file.read())
test_file.close()
'''

#출석시각 = 0
#퇴실시각 = 0
#attend_record = [0]
#출석넘버 = 0
#leave_record = [0]
#퇴실넘버 = 0
#study_time = 0

'''with open('attendence_data.p','wb') as file:
	pickle.dump(attend_record, file)
	pickle.dump(leave_record, file)
	
with open('attendence_data.p','rb')as file:
	attend_record = pickle.load(file)
	leave_record = pickle.load(file)
	print(attend_record)
	print(leave_record)'''
	


'''def nowtime():
    global mt
    mt = (int(time.ctime()[11:13])*60)+(int(time.ctime()[14:16]))'''

def hold():
    time.sleep(0.1)
    print('')
    
def line():
    print('')
    time.sleep(0.1)
    print('---------------------------------------------')
    print('')
    time.sleep(0.1)
    
#print(time.ctime()[0:3])
    

    
with open(file='picklejar1.pickle',mode='rb') as f:
	attend_record=pickle.load(f)
	leave_record=pickle.load(f)
	attend_num=pickle.load(f)
	leave_num=pickle.load(f)

def systemcheck():
    line()
    print('system check')
    time.sleep(0.1)
    #print('출석시각:',출석시각)
    time.sleep(0.1)
    #print('퇴실시각:',퇴실시각)
    time.sleep(0.1)
    print('출석기록:',attend_record)
    time.sleep(0.1)
    print('출석넘버:',attend_num)
    time.sleep(0.1)
    print('퇴실기록:',leave_record)
    time.sleep(0.1)
    print('퇴실넘버:',leave_num)
    #time.sleep(0.1)
    #print('출석일:',len(attend_record)-1,'일')
    #time.sleep(0.1)
    #print('hour:',int(time.ctime()[11:13]))
    #time.sleep(0.1)
    #print('minute:',int(time.ctime()[14:16]))
    #time.sleep(0.1)
    #minutetime()
    #print('minutetime:',mt)
    time.sleep(0.1)
    test_file2 = open("attendanceData1.txt", "r", encoding="utf8")
    print('attendance data :',test_file2.read())
    time.sleep(0.1)
    test_file3 = open("signoutData1.txt", "r", encoding="utf8")
    print('signout data :',test_file3.read())
    time.sleep(0.1)
    test_file4 = open("additionalStudy1.txt", "r", encoding="utf8")
    print('additional signin data :',test_file4.read())
    time.sleep(0.1)
    test_file5 = open("additionalStudy2.txt", "r", encoding="utf8")
    print('additional signout :',test_file5.read())
    time.sleep(0.1)
    print("현재시각:",int(time.ctime()[11:13]),'시',int(time.ctime()[14:16]),'분')
    

    
hold()    
systemcheck()

time.sleep(0.3)                                                                                
prit('''

                                
                               ~$@@@@@@@@@@@@@@$;                               
                         ;@@@@@@@@@@@@@@@@@@@@@@@@@@@@$                         
                     $@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                  @@@@@@@@@@@~                    ,#@@@@@@@@@@.                 
               !@@@@@@@@*                              ,@@@@@@@@@               
             @@@@@@@@.                                     @@@@@@@@             
           @@@@@@@!                        ;                  @@@@@@@           
         ;@@@@@@.                          @                    @@@@@@@         
        @@@@@@,                           ,@;                     @@@@@@        
       @@@@@@                      ~@      @-                      ~@@@@@$      
     ;@@@@@.         -@@@@      @@@@@@     @      :             ;    @@@@@@     
    !@@@@@         #@@@@@@@  @@@@@@@@*     ;    ,@@!           =@@    @@@@@@    
   ,@@@@@           @@@@@@@@@@@@@@                ,            @@      @@@@@@   
   @@@@@             @@@@@@@@                                 @@.       @@@@@-  
  @@@@@.         @@@~@@@@@@@@@.                    @@        @!          @@@@@  
  @@@@@      =@@@@@@@, *@@@@#!!                   :@@;      @$           :@@@@@ 
 @@@@@      =@@@@@@     -@!!!                     @@@@     :              @@@@@ 
 @@@@@       *@~                                 @@@@@@                   $@@@@,
.@@@@$                                          @@@@@@@@                   @@@@@
=@@@@,                                         :@@@@@@@@!                  @@@@@
@@@@@                                          @@@@@@@@@@                  @@@@@
=@@@@.                                        @@@@@@@@@@@@                 @@@@@
.@@@@=                                       @@@@@@@@@@@@@@                @@@@@
 @@@@@    ......                   @@       :@@@@@@@@@@@@@#-              =@@@@-
 @@@@@    @@!!!!                   @@       @@@@@@@@@@@#   $              @@@@@ 
 .@@@@@   @@      @@  #@! $@.@@@!  @@~@@@  @     @@@@@@  @@@@   *@@@@    ,@@@@@ 
  @@@@@   @@@@@@  @@  #@! =@@  @@  @@   @@@@@@@#  @@@@-  @@@@@ @@.  @@   @@@@@  
   @@@@@  @@      @@  #@! =@=  @@  @@   @@@@  @@  @@@@@  @@@@@*@@   @@. @@@@@;  
   :@@@@@ @@@@@@  @@@$@@* =@=  @@  @@   @@@;  $   @@@@@#   .. @.@@-$@@ @  #@@   
    #@@@@@                              @@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@    
     =@@@@@                            @@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@     
      -@@@@@=                         =@@@@@@@@@@@@@@@@@@@@@@@@@@* .@@@@@@      
        @@@@@@                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,       
         $@@@@@@                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
           @@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
             @@@@@@@@              *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             
               #@@@@@@@@,          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                  @@@@@@@@@@=     @@@@@@@@@@@@@@@@@@@@@@@@@@@@~                 
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                    
                         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                        
                              ,*@@@@@@@@@@@@@@@@$-                              
''',0.0001)                                                                                
                                                                                
time.sleep(0.3)                                                                                

order = 0
while order == 0 :
    line()
#    a = list("if you want to 출석체크, input 'attend'")
#    for i in range(0,len(a)):
#    	time.sleep(0.05)
#    	print(a[i],end='')
#    print('\n',end='')
#    del a
    prt("orders?;",0.01)
    print('')
    prt("if you want to 출석체크, input 'attend'",0.0001)
    prt("if you want to 퇴실체크, input 'leave'",0.0001)
    prt("if you want to 출결확인, input 'check'",0.0001)
    prt("if you want to leave comment, input 'comment'",0.0001)
    prt("if you want to read comments, input 'read'",0.0001)
    prt("if you want to sign in or sign out 시간외근무, input 'additional'",0.0001)
    print('\n')
    prt("input: ",0.1)
    order = input()
    if order == 'dataReset(0000)':
    	dataReset(0000)
    	order=0
    elif order == 'additional':
    	if addData != 1:
    		test_file4 = open("additionalStudy1.txt", "a", encoding="utf8")
    		additional1 = time.ctime()
    		addTime1 = int(time.ctime()[11:13])*60 + int(time.ctime()[14:16])
    		test_file4.write(additional1)
    		test_file4.write("\n")
    		test_file4.close()
    		addData = 1
    		with open(file='picklejar2.pickle',mode='wb') as f:
    			pickle.dump(addData,f)
    		print("you signed in additional study")
    	else:
    		test_file5 = open("additionalStudy2.txt", "a", encoding="utf8")
    		additional2 = time.ctime()
    		addTime2 = int(time.ctime()[11:13])*60 + int(time.ctime()[14:16])
    		test_file5.write(additional2)
    		test_file5.write("\n")
    		test_file5.close()
    		addData = 0
    		with open(file='picklejar2.pickle', mode='wb') as f:
    			pickle.dump(addData,f)
    		print("you signed out additional study")
    		additional_time = addTime2 - addTime1
    		print('additional :',additional_time//60,'시간',additional_time%60,'분')

    	order=0
    elif order == 'check':
    	systemcheck()
    	order=0
    elif order == 'comment':
    	line()
    	test_file = open("comment1.txt", "a", encoding="utf8")
    	comment_now1 = (input("write comment: "),time.ctime())
    	comment_now2 = str(comment_now1)
    	test_file.write(comment_now2)
    	test_file.write("\n")
    	prt('comment uploaded to external file.',0.01)
    	del comment_now1
    	del comment_now2
    	test_file.close()
    	order=0
    elif order == 'read':
    	line()
    	test_file = open("comment1.txt", "r", encoding="utf8")
    	prt(test_file.read(),0.001)
    	test_file.close()
    	order=0
    elif order == 'attend':
        line()
        prt('출석체크',0.1)
        hold()
        if len(attend_record) == len(leave_record):   # 그리고 gps좌표값이 설정 범위 이내라면 <-- 나중에 휴가나가면 기능추가
            #minutetime()
            #출석시각=mt
            attendDate = int(time.ctime()[8:10])
            attend_record[attend_num]=time.ctime()
            attend_record=attend_record+[0]
            attend_num=attend_num+1
            with open('picklejar1.pickle',mode='wb') as f:
            	pickle.dump(attend_record, f)
            	pickle.dump(leave_record, f)
            	pickle.dump(attend_num, f)
            	pickle.dump(leave_num, f)
            print('현재시각 :',time.ctime())
            timecheck = int(time.ctime()[11:13])*60 + int(time.ctime()[14:16])
            #hourcheck = int(time.ctime()[11:13])
            #minutecheck = int(time.ctieme()[14:16])
            daycheck = (time.ctime()[0:3])
            hold()
            print('출석완료')
            hold()
            if daycheck == 'SAT' or daycheck == 'SUN':
            	if timecheck < 420:
            		earlytime = 420 - timecheck 
            		print("early attendance",earlytime//60,"hours",earlytime%60,"minutes")
            	elif timecheck == 420:
            		earlytime = 0
            		print('You are at time.')
            	else:
            		earlytime = 420 - timecheck
            		latetime = timecheck - 420
            		print("late attendance",latetime//60,"hours",latetime%60,"minutes")
            else:
            	if timecheck < 1140:
            		earlytime = 1140 - timecheck 
            		print("early attendance",earlytime//60,"hours",earlytime%60,"minutes")
            	elif timecheck == 1140:
            		earlytime = 0
            		print('You are at time.')
            	else:
            		earlytime = 1140 - timecheck
            		latetime = timecheck - 1140
            		print("late attendance",latetime//60,"hours",latetime%60,"minutes")
            test_file2 = open("attendanceData1.txt", "a", encoding="utf8")
            attendanceDataNow = str(earlytime)
            test_file2.write(attendanceDataNow)
            test_file2.write("\n")
            test_file2.close()
            		
            
            
            order=0
        else :
            prt('이미 출석체크 되었습니다.',0.01)
            order=0
                
    elif order == 'leave':
        line()
        prt('퇴실체크',0.01)
        hold()
        if len(attend_record) == len(leave_record):
            prt('아직 출석체크하지 않았습니다.',0.01)
            order=0
        else :
            hold()
            #minutetime()
            #퇴실시각=mt
            leaveDate = int(time.ctime()[8:10])
            timecheck2 = int(time.ctime()[11:13])*60 + int(time.ctime()[14:16])
            if int(attend_record[attend_num - 1][8:10]) != leaveDate:
            	timecheck2 = timecheck2 + 1440
            leave_record[leave_num]=time.ctime()
            leave_record=leave_record+[0]
            leave_num=leave_num+1
            with open('picklejar1.pickle',mode='wb') as f:
            	pickle.dump(attend_record, f)
            	pickle.dump(leave_record, f)
            	pickle.dump(attend_num, f)
            	pickle.dump(leave_num, f)
            print('현재시각 :',time.ctime())
            hold()
            prt('퇴실완료',0.1)
            hold()
            if timecheck2 < 1440:
            	earlytime = timecheck2 - 1440
            	latetime = 1440 - timecheck2
            	print("early signout",latetime//60,"hours",latetime%60,"minutes")
            elif timecheck2 == 1440:
            	earlytime = 0
            	print('You signed out at time.')
            else:
            	earlytime = timecheck2 - 1440
            	print("late signout",earlytime//60,"hours",earlytime%60,"minutes")
            test_file3 = open("signoutData1.txt", "a", encoding="utf8")
            signoutDataNow = str(earlytime)
            test_file3.write(signoutDataNow)
            test_file3.write("\n")
            test_file3.close()
            attend_time = attend_record[-2]
            attend_minutetime = (int(attend_time[11:13])*60)+(int(attend_time[14:16]))
            leave_time = leave_record[-2]
            leave_minutetime = (int(leave_time[11:13])*60)+(int(leave_time[14:16]))
            if leave_minutetime >= attend_minutetime:
                study_time = (leave_minutetime)-(attend_minutetime)
            else :
                study_time = (leave_minutetime + (24*60))-attend_minutetime
            print('공부시간 :',study_time//60,'시간',study_time%60,'분')
            hold()
            #prt('출석 데이터 저장 완료, 다음 측정을 위해 출석/퇴실 시각을 초기화합니다.',0.1)
            print('출석 데이터 저장 완료, 다음 측정을 위해 출석/퇴실 시각을 초기화합니다.')
            attend_minutetime=0
            leave_minutetime=0
            study_time=0
            order=0
            #hold()
            systemcheck()
            with open('picklejar1.pickle',mode='rb')as f:
            	attend_record=pickle.load(f)
            	leave_record=pickle.load(f)
            #print(attend_record)
            #print(leave_record)
            
    else : 
        line()
        prt("input error\nplease input 'attend', 'leave' or 'check'.\nonly english is acceptable as input.",0.01)
        order = 0
