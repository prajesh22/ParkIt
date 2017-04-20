import numpy as np
import cv2
import math

car_cascade = cv2.CascadeClassifier('parking_new.xml')

img = cv2.imread('ist1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text_file = open("coords.txt", "w")

spot = ["-77.869411,40.794049$-77.869370,40.794081$-77.869388,40.794101$-77.869433,40.794066", ##lot1
        "-77.869390,40.794033$-77.869348,40.794061$-77.869370,40.794081$-77.869411,40.794049",
        "-77.869369,40.794017$-77.869328,40.794045$-77.869348,40.794061$-77.869390,40.794033",
        "-77.869347,40.794001$-77.869311,40.794030$-77.869328,40.794045$-77.869369,40.794017",
        "-77.869325,40.793984$-77.869285,40.794014$-77.869311,40.794030$-77.869347,40.794001",
        "-77.869304,40.793968$-77.869263,40.793996$-77.869285,40.794014$-77.869325,40.793984",
        "-77.869284,40.793950$-77.869244,40.793980$-77.869263,40.793996$-77.869304,40.793968",
        "-77.869261,40.793935$-77.869220,40.793965$-77.869244,40.793980$-77.869284,40.793950",
        "-77.869240,40.793919$-77.869199,40.793948$-77.869220,40.793965$-77.869261,40.793935",
        "-77.869219,40.793903$-77.869181,40.793930$-77.869199,40.793948$-77.869240,40.793919",
        "-77.869198,40.793885$-77.869158,40.793917$-77.869181,40.793930$-77.869219,40.793903",
        "-77.869177,40.793868$-77.869136,40.793899$-77.869158,40.793917$-77.869198,40.793885",
        "-77.869156,40.793852$-77.869119,40.793882$-77.869136,40.793899$-77.869177,40.793868",
        "-77.869135,40.793837$-77.869093,40.793864$-77.869119,40.793882$-77.869156,40.793852",
        "-77.869114,40.793820$-77.869073,40.793849$-77.869093,40.793864$-77.869135,40.793837", ##lot 15
        "-77.869452,40.794019$-77.869410,40.794050$-77.869436,40.794067$-77.869481,40.794033",
        "-77.869431,40.794004$-77.869390,40.794033$-77.869410,40.794050$-77.869452,40.794019",
        "-77.869409,40.793987$-77.869369,40.794015$-77.869390,40.794033$-77.869431,40.794004",
        "-77.869388,40.793969$-77.869348,40.794001$-77.869369,40.794015$-77.869409,40.793987",
        "-77.869369,40.793953$-77.869326,40.793983$-77.869348,40.794001$-77.869388,40.793969",
        "-77.869345,40.793938$-77.869305,40.793966$-77.869326,40.793983$-77.869369,40.793953",
        "-77.869326,40.793920$-77.869284,40.793951$-77.869305,40.793966$-77.869345,40.793938",
        "-77.869303,40.793905$-77.869261,40.793934$-77.869284,40.793951$-77.869326,40.793920",
        "-77.869282,40.793888$-77.869241,40.793916$-77.869261,40.793934$-77.869303,40.793905",
        "-77.869258,40.793873$-77.869219,40.793901$-77.869241,40.793916$-77.869282,40.793888",
        "-77.869238,40.793855$-77.869199,40.793883$-77.869219,40.793901$-77.869258,40.793873",
        "-77.869216,40.793839$-77.869177,40.793868$-77.869199,40.793883$-77.869238,40.793855",
        "-77.869196,40.793824$-77.869155,40.793852$-77.869177,40.793868$-77.869216,40.793839",
        "-77.869175,40.793806$-77.869134,40.793836$-77.869155,40.793852$-77.869196,40.793824",
        "-77.869155,40.793790$-77.869115,40.793819$-77.869134,40.793836$-77.869175,40.793806",
        "-77.869131,40.793773$-77.869093,40.793803$-77.869115,40.793819$-77.869155,40.793790",##lot 31
        "-77.869321,40.794152$-77.869289,40.794176$-77.869316,40.794193$-77.869345,40.794170",
        "-77.869313,40.794134$-77.869281,40.794161$-77.869300,40.794176$-77.869321,40.794152",
        "-77.869275,40.794120$-77.869243,40.794145$-77.869263,40.794160$-77.869313,40.794134",
        "-77.869254,40.794102$-77.869222,40.794126$-77.869242,40.794144$-77.869275,40.794120",
        "-77.869235,40.794084$-77.869200,40.794110$-77.869219,40.794126$-77.869254,40.794102",
        "-77.869212,40.794069$-77.869178,40.794094$-77.869199,40.794110$-77.869235,40.794084",
        "-77.869190,40.794054$-77.869160,40.794079$-77.869178,40.794094$-77.869212,40.794069",
        "-77.869170,40.794036$-77.869136,40.794061$-77.869157,40.794079$-77.869190,40.794054",
        "-77.869147,40.794020$-77.869115,40.794045$-77.869135,40.794060$-77.869170,40.794036",
        "-77.869129,40.794003$-77.869093,40.794026$-77.869115,40.794045$-77.869147,40.794020",
        "-77.869110,40.793986$-77.869074,40.794013$-77.869093,40.794028$-77.869129,40.794003",
        "-77.869092,40.793967$-77.869049,40.793994$-77.869073,40.794013$-77.869110,40.793986",
        "-77.869065,40.793950$-77.869027,40.793977$-77.869049,40.793994$-77.869092,40.793967",
        "-77.869043,40.793934$-77.869006,40.793962$-77.869026,40.793977$-77.869065,40.793950",
        "-77.869025,40.793914$-77.868985,40.793943$-77.869006,40.793961$-77.869043,40.793934",
        "-77.869002,40.793898$-77.868963,40.793926$-77.868983,40.793943$-77.869025,40.793914",
        "-77.868982,40.793879$-77.868939,40.793910$-77.868962,40.793926$-77.869002,40.793898"]##lot 48

cars = car_cascade.detectMultiScale(gray, 5, 4, 0,(0,0),(70,35))
for (x,y,w,h) in cars:
    if (abs(x-38)<= 28) | (abs(x-95)<= 28) | (abs(x-240)<=28):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.circle(img,(x,y), 5, (255,0,0), -1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if math.sqrt((x-95)**2.0+(y-31)**2.0)<= 28:
            text_file.write(spot[0])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-65)**2.0)<= 28:
            text_file.write(spot[1])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-94)**2.0)<= 28:
            text_file.write(spot[2])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-124)**2.0)<= 28:
            text_file.write(spot[3])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-154)**2.0)<= 28:
            text_file.write(spot[4])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-183)**2.0)<= 28:
            text_file.write(spot[5])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-215)**2.0)<= 28:
            text_file.write(spot[6])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-243)**2.0)<= 28:
            text_file.write(spot[7])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-274)**2.0)<= 28:
            text_file.write(spot[8])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-303)**2.0)<= 28:
            text_file.write(spot[9])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-334)**2.0)<= 28:
            text_file.write(spot[10])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-364)**2.0)<= 28:
            text_file.write(spot[11])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-393)**2.0)<= 28:
            text_file.write(spot[12])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-423)**2.0)<= 28:
            text_file.write(spot[13])
            text_file.write("\n")
        if math.sqrt((x-95)**2.0+(y-455)**2.0)<= 28:
            text_file.write(spot[14])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-30)**2.0)<= 28:
            text_file.write(spot[15])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-63)**2.0)<= 28:
            text_file.write(spot[16])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-93)**2.0)<= 28:
            text_file.write(spot[17])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-123)**2.0)<= 28:
            text_file.write(spot[18])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-153)**2.0)<= 28:
            text_file.write(spot[19])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-183)**2.0)<= 28:
            text_file.write(spot[20])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-213)**2.0)<= 28:
            text_file.write(spot[21])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-243)**2.0)<= 28:
            text_file.write(spot[22])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-274)**2.0)<= 28:
            text_file.write(spot[23])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-302)**2.0)<= 28:
            text_file.write(spot[24])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-333)**2.0)<= 28:
            text_file.write(spot[25])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-363)**2.0)<= 28:
            text_file.write(spot[26])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-392)**2.0)<= 28:
            text_file.write(spot[27])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-423)**2.0)<= 28:
            text_file.write(spot[28])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-454)**2.0)<= 28:
            text_file.write(spot[29])
            text_file.write("\n")
        if math.sqrt((x-38)**2.0+(y-484)**2.0)<= 28:
            text_file.write(spot[30])##spot 31
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-5)**2.0)<= 28:
            text_file.write(spot[31])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-32)**2.0)<= 28:
            text_file.write(spot[32])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-64)**2.0)<= 28:
            text_file.write(spot[33])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-92)**2.0)<= 28:
            text_file.write(spot[34])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-124)**2.0)<= 28:
            text_file.write(spot[35])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-154)**2.0)<= 28:
            text_file.write(spot[36])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-184)**2.0)<= 28:
            text_file.write(spot[37])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-214)**2.0)<= 28:
            text_file.write(spot[38])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-244)**2.0)<= 28:
            text_file.write(spot[39])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-275)**2.0)<= 28:
            text_file.write(spot[40])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-304)**2.0)<= 28:
            text_file.write(spot[41])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-331)**2.0)<= 28:
            text_file.write(spot[42])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-365)**2.0)<= 28:
            text_file.write(spot[43])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-399)**2.0)<= 28:
            text_file.write(spot[44])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-428)**2.0)<= 28:
            text_file.write(spot[45])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-457)**2.0)<= 28:
            text_file.write(spot[46])
            text_file.write("\n")
        if math.sqrt((x-245)**2.0+(y-489)**2.0)<= 28:
            text_file.write(spot[47])
            text_file.write("\n")
        
text_file.close()            
##cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
