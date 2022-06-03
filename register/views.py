from django.shortcuts import render
import mysql.connector as sql
n=''
s=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global n,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="hima17",database='sample_website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                n=value
            if key=="gender":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}')".format(n,em,s,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'register_page.html')