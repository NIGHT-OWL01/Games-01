# import psycopg2

# conn = psycopg2.connect("host=localhost dbname=krishikhoj_dev user=ganesh password=password")

# cur = conn.cursor()
# cur.execute('SELECT * FROM profiles_earthmover')

# #insert_query = "INSERT INTO profiles_earthmover VALUES {}".format("(2,'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340','mahindra',1, 32123032123, 1, 15, 123)")
# #cur.execute(insert_query)
# #conn.commit()
# #one = cur.fetchone()
# all = cur.fetchall()
# print(all)
# #print(all)













# from datetime import date
# from numpy import add
# import pandas as pd
#sorted_column = newData.sort_values(['Height'], ascending = False) 2.newData.to_excel('Output File.xlsx')

# import psycopg2
# conn=psycopg2.connect("host=localhost  dbname=krishikhoj_dev user=ganesh password=password ")
# curr=conn.cursor()

# file=('earthmover.xlsx')
# newdata=pd.read_excel(file)
# id=0
# for n in newdata['Phone Number']:
#     id+=1
#     print(id)
   
#     query='INSERT INTO profiles_earthmover VALUES {}'.format(f"({id},'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340',{n},1, 32123032123, 1, 15, 123)")
#     curr.execute(query)
#     conn.commit()


# import pandas as pd
# import psycopg2

# data=pd.read_excel('earthmover.xlsx')

# conn= psycopg2.connect('host=localhost user=ganesh password=password dbname=krishikhoj_dev')
# cur=conn.cursor()

# id=0
# for d in data['Phone Number']:
    
#     query='INSERT INTO profiles_earthmover VALUES {}'.format(f"({id},'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340',{d},1,5155555, 1, 15,  {data['Rate per hour'][id]})")
#     id+=1
#     print(id)
#     cur.execute(query)
#     conn.commit()    



#Read each column
# import pandas as pd

# data = pd.read_excel('earthmover.xlsx')
# print(data.info(1))
# for i in range(len(data)):
#     print(i)
#     print(data.loc[i]['Location/Village'])
#     print(data.loc[i]['Make'])
#     print(data.loc[i]['Vehicle No'])
#     print(data.loc[i]['Contractor Name'])
#     print(data.loc[i]['Rate per hour'])
#     print('\n')


#get lat long from location
# import pandas as pd

# data = pd.read_excel('earthmover.xlsx')

# loc =data.loc[0]['Location/Village']
# lat,long = loc.split(", ")


# print(loc)
# print(lat)
# print(long)


#TYPE TO ID for Earthmover Type


# import pandas as pd

# data = pd.read_excel('earthmover.xlsx')
# # print(data.info())

# for i in range(len(data)):
#     j=i+2
#     contractor={data.loc[i]['Contractor Name']}
#     if data.loc[i]['Earthmover Type']=='Backhoe Loader':
#         print(f'{j} : 1 {contractor}')
#     elif data.loc[i]['Earthmover Type']=='Excavator':
#         print(f'{j} : 2 {contractor}')
#     else:
#         earth_mover=data.loc[0]['Earthmover Type']
#         print('Unlisted Type found!', earth_mover)


#Add vehicle number into table
# import pandas as pd
# import psycopg2

# data = pd.read_excel('earthmover.xlsx')

# print(data['Vehicle No'])

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# cur=conn.cursor()

# for i in range(len(data)):
#     vehicle_number = data.loc[i]['Vehicle No']
#     query='INSERT INTO profiles_earthmover VALUES {}'.format(f"({i},'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340','mahindra',1,'{vehicle_number}',1,15,100)")
#     cur.execute(query)
#     conn.commit()


#Add make to database
# import pandas as pd
# import psycopg2
# data = pd.read_excel('earthmover.xlsx')
# print(data)

# conn=psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# cur=conn.cursor()
# for i in range(len(data)):
#     j=i+2
#     if data.loc[i]['Earthmover Type']=='Backhoe Loader':
#         type=2
#     elif data.loc[i]['Earthmover Type']=='Excavator':
#         type=1
#     else:
#         earth_mover=data.loc[0]['Earthmover Type']
#         print('Unlisted Type found!', earth_mover)
#     make=data.loc[i]['Village']
#     vno=data.loc[i]['Vehicle No']
#     rate=data.loc[i]['Rate per hour']
#     query='INSERT INTO profiles_earthmover VALUES {}'.format(f"({j}, '0101000020E6100000CABCF45FD5D552403842B6CD0EE03340','{make}',{type},'{vno}',1,15,{rate})")
#     cur.execute(query)
#     conn.commit()



# import pandas as pd
# import psycopg2

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_db user=ganesh password=password')
# cur=conn.cursor()

# df = pd.read_excel('earthmover.xlsx')
# df=df['Photo 2'].fillna(0)
# print(df.to_string())



# j=2
# name='ani'
# phone_no=000000
# village='kasge'
# query='INSERT INTO profiles_user VALUES {}'.format(f"({j},'{name}',{phone_no},'91','{village}', 'JCB Earthmovers_Images/2.User Profile Pic.054935.jpg')")

# curr.execute(query)
# conn.commit()
# import psycopg2
# import pandas as pd

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# curr=conn.cursor()

# data=pd.read_excel('earthmover.xlsx')
# ndata = data.drop_duplicates(subset='Phone Number', keep="first")
# j=-1
# for i in range(len(data)):
#     j=j+1
#     if j==10 or j==16:
#         j=j+1
#     if j==17:
#         j=j+1
#     if  j==18:
#         j=j+1
#     if  j==33:
#         j=j+1
#     if  j==35:
#         j=j+1
#     if  j==41:
#         j=j+1
#     if  j==44:
#         j=j+1
#     if  j==45:
#         j=j+1
#     if  j==54:
#         j=j+1
#     if  j==57:
#         j=j+1
#     if  j==69:
#         j=j+1
#     if  j==89:
#         j=j+1
#     if  j==91:
#         j=j+1
#     if  j==107:
#         j=j+1
#     name=ndata.loc[j]['Contractor Name']
#     Phone_no=ndata.loc[j]['Phone Number']
#     address=ndata.loc[j]['Village']
#     img=ndata.loc[j]['User Profile Pic']
#     query='INSERT INTO profiles_user VALUES {}'.format(f"({j},'{name}','{Phone_no}','91','{address}', '{img}')")
#     curr.execute(query)
#     conn.commit()

# print(ndata.to_string())



# import pandas as pd
# import psycopg2

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# curr = conn.cursor()

# data=pd.read_excel('earthmover.xlsx')
# # for i in range(len(data)):
# #     if i ==41 or i==69 or i==91:
# #        continue
# i=91
# if data.loc[i]['Earthmover Type']=='Backhoe Loader':
#     type=1
# elif data.loc[i]['Earthmover Type']=='Excavator':
#     type=2
# else:
#     earth_mover=data.loc[0]['Earthmover Type']
#     print('Unlisted Type found!', earth_mover)

# #id=int(i)
# print('id',i)
# make=data.loc[i]['Make']
# vehicle_no=data.loc[i]['Vehicle No']
# rate=data.loc[i]['Rate per hour']
# c_name=data.loc[i]['Contractor Name']
# query=f"select id FROM profiles_user WHERE name='{c_name}';"
# #curr.execute(query)
# #all = curr.fetchone()[0]
# #print(all)
# user_id=79
# query='INSERT INTO profiles_earthmover VALUES {}'.format(f"({i},'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340','{make}',{type},'{vehicle_no}',{user_id},15,{rate})")
# curr.execute(query)
# conn.commit()


# name='विशाल गायकवाड'
# query="select id FROM profiles_user WHERE id=1;"
# curr.execute(query)
# all = curr.fetchone()
# conn.commit()

# print(all)





# import psycopg2
# import pandas as pd

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# curr=conn.cursor()

# data=pd.read_excel('earthmover.xlsx')
# ndata = data.drop_duplicates(subset='Phone Number', keep="first")

# for i in range(len(data)):
#     id=i+2
#     name=ndata.loc[i]['Contractor Name']
#     Phone_no=ndata.loc[i]['Phone Number']
#     address=ndata.loc[i]['Village']
#     img=ndata.loc[i]['User Profile Pic']
#     query='INSERT INTO profiles_user VALUES {}'.format(f"({id},'{name}','{Phone_no}','91','{address}', '{img}')")
#     curr.execute(query)
#     conn.commit()



# import psycopg2
# import pandas as pd


# conn = psycopg2.connect('user=ganesh password=password host=localhost dbname=krishikhoj_dev')
# cur=conn.cursor()
# query= "select id FROM profiles_earthmover WHERE vehicle_number='not available!'"
# update_query="UPDATE profiles_earthmover SET vehicle_number='not available' WHERE vehicle_number='MH02AB1234';"
# cur.execute(query)

# print(cur.fetchall())
# conn.commit()
#dummy vehical no changed
#[(0,), (1,), (11,), (14,), (26,), (27,), (30,), (32,), (34,), (35,), (37,), (38,), (40,), (44,), (46,), (51,), (52,), (56,),
#  (58,), (59,), (61,), (62,), (64,), (65,), (66,), (73,), (74,), (77,),
#  (78,), (80,), (83,), (84,), (85,), (86,), (88,), (90,), (94,), (95,), (96,), (98,), (101,), (103,), (105,)]



###################################BorewellBorewellBorewellBorewellBorewellBorewell################################################

# import psycopg2
# import pandas as pd 

# conn=psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# cur=conn.cursor()

# data = pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Borewell')
# #print(data)

# # for i in range(len(data)):
# #     if i==5:
# #         continue
# #     print('id',i)
# i=13
# id=118
# name=data.loc[i]['Contractor Name']
# Phone_no=int(data.loc[i]['Phone Number'])
# address=data.loc[i]['Village']
# img=data.loc[i]['User Profile Pic']
# print(name,Phone_no,address,img)
# query='INSERT INTO profiles_user VALUES {}'.format(f"({id},'{name}','{Phone_no}','91','{address}', '{img}')")
# cur.execute(query)
# conn.commit()


##################################ADDING BOREWELL AND LINK WITH USERS#######################################
# import psycopg2
# import pandas as pd

# conn = psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# cur=conn.cursor()
# data = pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Borewell')
# print(data)
# for i in range(len(data)):
#     print(i)
#     c_name=data.loc[i]['Contractor Name']
#     query = f"select id FROM profiles_user WHERE name='{c_name}';"
#     cur.execute(query)
#     all = cur.fetchone()[0]
#     print(all)
#     user_id=all
#     rate=data.loc[i]['Rate per hour']
#     shop_name=data.loc[i]['Shop Name']
#     village=data.loc[i]['Village']


#     query ="INSERT INTO profiles_borewell VALUES{}".format(f"({i},'0101000020E6100000CABCF45FD5D552403842B6CD0EE03340',{user_id},{rate},'{shop_name}','{village}')")
#     cur.execute(query)
#     conn.commit()



########################IMPORTANT#############IMPORTANTIMPORTANTIMPORTANTIMPORTANT###########################IMPORTANTIMPORTANT
#################################################script to find duplicates in column with many values in one row separated by commas
#######################################Value of i is 2 less than record
# import psycopg2
# import pandas as pd
# l=[]
# s={()}
# conn= psycopg2.connect('host=localhost dbname=krishikhoj_dev user=ganesh password=password')
# cur=conn.cursor()

# data=pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Tractor')

# for i in range(len(data)):
#     #print(i)
#     if i==42 or i==126 or i==149 or i==213 or i==229 or i==232:
#         #print('special for blank',i)
#         continue
#     implements=data.loc[i]['Implements']

#     implements_in=implements.split(", ")

#     for imp in implements_in:
#         s.add(imp)
# #print(s)

# i=0
# for implement in s:
#     i+=1
#     print(i,implement)

#########################TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTemp############################################
#     categories=category.split(", ")

#     for category in categories:
#         s.add(category)
#         print(category)
# print(type(s))
# print(len(s))
# print(s)
##################TTTTTTTTTTTTTTTTTTTT###############################TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT




############################################Adding nursery users and nursery###########################################
'''
import django
django.setup() 
from contextlib import closing
from numpy import add
import pandas as pd
from pandas.core.indexes.base import InvalidIndexError
from profiles.models import Borewell, NurseryPicture, User, Nursery
# borewell = Borewell.objects.all()
# print(borewell)

data = pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Nursery')
#print(data.to_string())
# s={()}
for i in range(len(data)):
    c_name=data.loc[i]['Nursery Owner Name']
    c_phone_number=int(data.loc[i]['Phone Number'])
    c_address=data.loc[i]['Address']

    #for nursery
    c_nursery_name=data.loc[i]['Nursery Name']
    #c_working_days = data.loc[i]['Working Days']
    c_opening_time = data.loc[i]['Opening Time']
    c_closing_time = data.loc[i]['Closing Time']
    c_category= data.loc[i]['Categories']
    c_img = data.loc[i]['User Profile Pic']
    
    np_img=data.loc[i]['Menu Photo 1']

    s=""
    c_working_days = data.loc[9]['Working Days']
    days=c_working_days.split(", ")

    if 'Sun ' in days or 'Sun' in days:
        s+='1'
    else:
        s+='0'
    if 'Mon ' in days or 'Mon' in days:
        s+='1'
    else:
        s+='0'
    if 'Tue ' in days or 'Tue' in days:
        s+='1'
    else:
        s+='0'
    if 'Wed ' in days or 'Wed' in days:
        s+='1'
    else:
        s+='0'
    if 'Thu ' in days or 'Thu' in days:
        s+='1'
    else:
        s+='0'
    if 'Fri ' in days or 'Fri' in days:
        s+='1'
    else:
        s+='0'
    if 'Sat ' in days or 'Sat' in days:
        s+='1'
    else:
        s+='0'
    print(days)
    print(len(s))
    print(s)
    
    c_location='0101000020E6100000CABCF45FD5D552403842B6CD0EE03340'#data.loc[i]['Location']

    
    user,created=User.objects.get_or_create(id=id,name=f'{c_name}', phone_number=f'{c_phone_number}', country_code='91',address=f'{c_address}', image_url=f'{c_img}')
    print(user, created)
    nursery=Nursery.objects.create(user=user, location=c_location, name=c_name, address=c_address, working_days=s, opening_time=c_opening_time,closing_time=c_closing_time)
    nursery.save()
    nursery_picture=NurseryPicture(nursery=nursery,image_url=np_img)
    nursery_picture.save()
'''
#################################################################################################################################################################################################

'''
from os import name
import pandas as pd
from profiles.models import User,Veterinarian

data = pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Veterinary Doctor')

################163###########################163##################################163##############################################

for i in range(len(data)):
    u_name=data.loc[i]['Doctor Name']
    
    phone_number=int(data.loc[i]['Phone Number'])
    c_address=data.loc[i]['Village']
    c_img=data.loc[i]['User Profile Pic']

    c_education=data.loc[i]['Education']
    c_experiance=data.loc[i]['Years of Experience']
    c_expertise=data.loc[i]['Expertise']
    id=i+163
    #print(i+2,u_name,phone_number)
    u=User.objects.filter(name=u_name, phone_number=phone_number).exists()
    if u:
        c_user=User.objects.get(name=u_name, phone_number=phone_number)
        print(u_name,phone_number,u,'exists!')
    else:
        c_user=User.objects.get_or_create(id=id,name=u_name, phone_number=phone_number, country_code='91',address=f'{c_address}', image_url=f'{c_img}')
        print(c_user, 'created')
        veternary_doctor=Veterinarian(user=c_user,radius_of_operation='',education=c_education,experience=c_experiance,expertise=c_expertise)
    


#print(data)




#https://www.appsheet.com/template/gettablefileurl?appname=KrishiKhoj-3813356&tableName=Nursery&fileName=User+Profile+Pic/Nursery_Images/3.User%20Profile%20Pic.053730.jpg
'''
'''
import pandas as pd
from profiles.models import User,Veterinarian,NurseryProductCategory

data = pd.read_excel('Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Nursery')

n=data.loc[0]['Categories']

print(n)
categorys=n.replace(" ","").lower().split(",")

print(categorys)

for category in categorys:
    print(category)
    if category=='fruitplants':
        id=1
    if category=='vegetableplants':
        id=2
    if category=='fruitplantsaa':
        id=3
    if category=='fruitplantsdas':
        id=4

npc=NurseryProductCategory.objects.get(id=id)
print(npc)
'''

import django
django.setup()
from django.contrib.gis.db.models.fields import PointField
import pandas as pd
from profiles.models import AgriShop, Borewell, EarthMover, Nursery, User,NurseryPicture
from django.contrib.gis.geos import Point

# b=Borewell.objects.get(id=1)

# b.location=Point((0,0),srid=4326)
# b.save()
# print(b)

#data=pd.read_excel('imgwork/Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Borewell')


#print(data)

#print(data.loc[2]['Phone Number'])
'''
ph=data.loc[2]['Phone Number']

u=User.objects.get(phone_number=ph)
print(u)
b=Borewell.objects.filter(user=u).count()

print(b)
'''
'''
for u in User.objects.all():
    b=Borewell.objects.filter(user=u).exists()
    if b:
        b=Borewell.objects.filter(user=u)
    bc=Borewell.objects.filter(user=u).count()
    
    if bc>0:
        print(u.id)
        print(u.name)
        print(bc)
        print(b)

print('==============================================================================')
u=User.objects.get(phone_number=9767514283)
print(u.id)
print(u)
b=Borewell.objects.get(user=u)


print(b)
print(b.user.id)
'''

'''
for i in range(len(data)):
    ph=data.loc[i]['Phone Number']
    location=data.loc[i]['Location']
    locs=location.split(",")
    print(locs)

    lat=float(locs[0].replace(" ",""))
    long=float(locs[1].replace(" ",""))
    print(lat,long)
    
    u=User.objects.get(phone_number=ph)
    print(u)

    b=Borewell.objects.get(user=u)
    b.location=Point((long,lat),srid=4326)
    b.save()
    print(b)
'''
'''
for u in User.objects.all():

    e=EarthMover.objects.filter(user=u).exists()
    if e:
        e=EarthMover.objects.filter(user=u)
    ec=EarthMover.objects.filter(user=u).count()
    
    if ec>1:
        print(u.id)
        print(u.name)
        print(ec)
        print(e)

'''
'''
u=User.objects.get(phone_number=9022699090)
print('user',u.id)
e=EarthMover.objects.get(id=76)
print(e)

e.user=u


#e.user=u
#b.save()
'''

#n=Nursery.objects.get(id=21).nursery_productcategories.all()
#n.nursery_productcategories.set([1,2])
#n.save()
#print(n)

'''
data=pd.read_excel('imgwork/Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Nursery')

for i in range(len(data)):
    n=data.loc[i]['Categories']

    #print(n)
    categorys=n.replace(" ","").lower().split(",")

    print(categorys)
    id=[]
    for category in categorys:
        #print(category)
        if category=='ऊसाचीरोपे' or category=='ऊसाचेबेणे':
            id.append(6)
        if category=='fruitplants' or category=='द्राक्षे' or category=='शिताफळ':
            id.append(1)
        if category=='vegetableplants':
            id.append(2)
        if category=='forestplants':
            id.append(3)
        if category=='medicinalandaromaticplants':
            id.append(4)
        if category=='ornamentalplants':
            id.append(5)
        
    print(id)
    ph=data.loc[i]['Phone Number']
    u=User.objects.get(phone_number=ph)

    n=Nursery.objects.get(user=u)
    n.nursery_productcategories.set(id)
    n.save()
    print(n)'''

##################IMPIMP######IMP#####################AGRISHOP#####################IMP#####################IMP#########################IMP########
################################NURSERY#######start#at#170###########################################################
'''
data=pd.read_excel('imgwork/Krishikhoj Service provider sheet v2 .xlsx', sheet_name='Agrishops')
j=170
for i in range(len(data)):
    u_name=data.loc[i]['Shop Owner Name']
    ph=data.loc[i]['Phone Number']

    add=data.loc[i]['Address']
    location=data.loc[i]['Location']
    locs=location.split(",")
    print(locs)

    lat=float(locs[0].replace(" ",""))
    long=float(locs[1].replace(" ",""))
    print(lat,long)
    Loc=Point((long,lat),srid=4326)

    c_working_days = data.loc[i]['Working Days']
    days=c_working_days.split(", ")
    s=""
    if 'Sun ' in days or 'Sun' in days:
        s+='1'
    else:
        s+='0'
    if 'Mon ' in days or 'Mon' in days:
        s+='1'
    else:
        s+='0'
    if 'Tue ' in days or 'Tue' in days:
        s+='1'
    else:
        s+='0'
    if 'Wed ' in days or 'Wed' in days:
        s+='1'
    else:
        s+='0'
    if 'Thu ' in days or 'Thu' in days:
        s+='1'
    else:
        s+='0'
    if 'Fri ' in days or 'Fri' in days:
        s+='1'
    else:
        s+='0'
    if 'Sat ' in days or 'Sat' in days:
        s+='1'
    else:
        s+='0'
    print(days)

    c_opening_time=data.loc[i]['Opening Time']
    c_closing_time=data.loc[i]['Closing Time']
    profile_pic=data.loc[i]['User Profile Pic']

    shop_name=data.loc[i]['Shop Name']

    print(u_name)
    print(ph)
    
    u=User.objects.filter(phone_number=ph).exists()
    if u:
        u=User.objects.get(phone_number=ph)
        print('user exists',u)
        agriShop=AgriShop.objects.create(user=u,location=Loc,name=shop_name,address=add,working_days=s,opening_time=c_opening_time,closing_time=c_closing_time)
        agriShop.save()
        print('Agrishop created : ',agriShop)
    else:
        j+=1
        id=j+i
        u=User.objects.create(id=id,name=u_name,phone_number=ph,country_code='91',address=add,image_url=profile_pic)
        print('user Created',u)
        agriShop=AgriShop.objects.create(user=u,location=Loc,name=shop_name,address=add,working_days=s,opening_time=c_opening_time,closing_time=c_closing_time)
        agriShop.save()
        print('Agrishop created : ',agriShop)
'''
'''
#unique categories in Agrishop
cat={()}
for i in range(len(data)):
    c=data.loc[i]['Categories']
    categories=c.replace(" ","").lower().split(",")
    #print(categories)
    
    for category in categories:
        #print(category)
        cat.add(category)
print(cat)
print(len(cat))
'''

import openpyxl

data=pd.read_excel('text2.xlsx', sheet_name='Nursery')
xfile = openpyxl.load_workbook('text2.xlsx')

'''
for i in range(len(data)):
    no=data.loc[i]['Phone Number']
    u=User.objects.get(phone_number=no)
    n=Nursery.objects.get(user=u)

    np=NurseryPicture.objects.filter(nursery=n)
    print(n)


    sheet = xfile.get_sheet_by_name('Nursery')
#sheet['K1'] = 'hello world'
#xfile.save('text2.xlsx')
    value=''
    for nurseryImg in np:
        value+=f'*{nurseryImg.image_url}'
    sheet[f'U{i+2}']=value
    print(sheet[f'U{i+2}'].value)

    xfile.save('text2.xlsx')

    #l=[value.split("*")]
    #print('l',l)

'''

sheet = xfile.get_sheet_by_name('Nursery')
p=[]
'''
for i in range(len(data)):
    u_name=data.loc[i]['Nursery Owner Name']
    u_number=data.loc[i]['Phone Number']   
    u_address=data.loc[i]['Address']   
    user=User.objects.filter(phone_number=u_number).exists()
    print(user)
    if user:
        user=User.objects.get(phone_number=u_number)
        n=Nursery.objects.get(user=user)
        img_url=sheet[f'U{i+2}'].value.split("*")
        p+=img_url.pop(0)
        #print(img_url)
        NurseryPicture.objects.create(nursery=n,image_url=img_url)
    else:
        user=User.objects.create(name=u_name,phone_number=u_number,address=u_address)
        n=Nursery.objects.get(user=user)
        img_url=sheet[f'U{i+2}'].value.split("*")
        p+=img_url.pop(0)
        #print(img_url)
        NurseryPicture.objects.create(nursery=n,image_url=img_url)
print('p',p)

'''

##script for creating nursery and nursery users.

sheet = xfile.get_sheet_by_name('Nursery')
p=[]
for i in range(len(data)):
    u_name=data.loc[i]['Nursery Owner Name']
    u_number=data.loc[i]['Phone Number']   
    u_address=data.loc[i]['Address']
    
    #for nursery
    n_name=data.loc[i]['Nursery Name']
    n_opening_time=data.loc[i]['Opening Time']
    n_closing_time=data.loc[i]['Closing Time']
    #for location
    location=data.loc[i]['Location']
    locs=location.split(",")
    print(locs)

    lat=float(locs[0].replace(" ",""))
    long=float(locs[1].replace(" ",""))
    print(lat,long)
    Loc=Point((long,lat),srid=4326)
    
    #working days
    n_working_days = data.loc[i]['Working Days']
    days=n_working_days.split(", ")
    s=""
    if 'Sun ' in days or 'Sun' in days:
        s+='1'
    else:
        s+='0'
    if 'Mon ' in days or 'Mon' in days:
        s+='1'
    else:
        s+='0'
    if 'Tue ' in days or 'Tue' in days:
        s+='1'
    else:
        s+='0'
    if 'Wed ' in days or 'Wed' in days:
        s+='1'
    else:
        s+='0'
    if 'Thu ' in days or 'Thu' in days:
        s+='1'
    else:
        s+='0'
    if 'Fri ' in days or 'Fri' in days:
        s+='1'
    else:
        s+='0'
    if 'Sat ' in days or 'Sat' in days:
        s+='1'
    else:
        s+='0'
    print(days)

    user=User.objects.filter(phone_number=u_number).exists()
    print(user)
    if user:
        user=User.objects.get(phone_number=u_number)
        n=Nursery.objects.create(user=user,location=Loc,name=n_name,address=u_address,working_days=s,opening_time=n_opening_time,closing_time=n_closing_time)
        
        img_url_list=sheet[f'U{i+2}'].value.split("*")
        p+=img_url_list.pop(0)
    
        for img_url in img_url_list:
            print(i+2,img_url)
            NurseryPicture.objects.create(nursery=n,image_url=img_url)
    else:
        user=User.objects.create(name=u_name,phone_number=u_number,address=u_address)
        n=Nursery.objects.create(user=user,location=Loc,name=n_name,address=u_address,working_days=s,opening_time=n_opening_time,closing_time=n_closing_time)
        
        img_url_list=sheet[f'U{i+2}'].value.split("*")
        p+=img_url_list.pop(0)

        for img_url in img_url_list:
            print(i+2,img_url)
            NurseryPicture.objects.create(nursery=n,image_url=img_url)
'''
for i in range(len(data)):
    img_url_list=sheet[f'U{i+2}'].value.split("*")
    p+=img_url_list.pop(0)
    
    for img_url in img_url_list:
        print(i+2,img_url)
        NurseryPicture.objects.create(nursery=n,image_url=img_url)
'''