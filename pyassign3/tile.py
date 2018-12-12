def mainpart(m,n,a,b,alls=[],i=0,j=0,ans=[],lst=[]):
    '''主体部分，应用递归'''
    if lst==[]:
        lst = [i for i in range(m*n)]
    if i==m:
        j=j+1
        i=0
    if (lst==[-1]*m*n) and (ans not in alls):
        alls.append(ans[:])
    if ((j*m)+i)<(m*n) and lst[j*m+i]== -1:
        mainpart(m,n,a,b,alls,i+1,j,ans,lst)
    else:
        if jud(m,n,a,b,i,j,lst):
            lst1=lst[:]
            ans1=ans[:]
            do(a,b,m,i,j,lst1,ans1)
            mainpart(m,n,a,b,alls,i+1,j,ans1,lst1)
        if jud(m,n,b,a,i,j,lst):
            lst1=lst[:]
            ans1=ans[:]
            do(b,a,m,i,j,lst1,ans1)
            mainpart(m,n,a,b,alls,i+1,j,ans1,lst1)
        
        
def jud(m,n,a,b,i,j,lst):
    '''判断是否能铺，包括长和宽'''
    if (i+a)>m or (j+b)>n:
        return False
    for j in range(j,j+b):
        for i in range(i,i+a):
            if lst[j*m+i]==-1:
                return False
    return True

def do(a,b,m,i,j,lst,ans):
    '''铺砖的方法，ans表示其中一种铺法，re是元组（a,b,……）'''
    re=()
    for i in range(i,i+a):
        for j in range(j,j+b):
            k=j*m+i
            lst[k]=-1
            re=re+(k,)
    ans.append(re)

import turtle

def visible(m,n,t,i=0):
    '''将用户选择的铺法可视化'''
    wn=turtle.Screen()
    l=turtle.Turtle()
    wn=turtle.Screen()
    l=turtle.Turtle() 
    l.hideturtle()
    k=t[i]
    x0=int(k[0]%m)
    y0=int(k[0]//m)
    x1=int(k[-1]%m+1)
    y1=int(k[-1]//m+1)
    l.up()
    l.goto(x1*30,y1*30)
    l.down()
    l.goto(x0*30,y1*30)
    l.goto(x0*30,y0*30)
    l.goto(x1*30,y0*30)
    l.goto(x1*30,y1*30)
    if i<len(t)-1:
        visible(m,n,t,i+1)    
    
def main():
    wall=input('请输入墙的尺寸（如4，2）').split(',')
    brick=input('请输入砖的尺寸（如2，1）').split(',')
    m=int(wall[0])
    n=int(wall[1])
    a=int(brick[0])
    b=int(brick[1])
    answer=[]
    mainpart(m,n,a,b,answer)
    print(answer)
    if answer!=[]:
        x=int(input('请输入您需要将第几种可视化（从左到右排）（如6）'))
        t=answer[x-1]
        visible(m,n,t,i=0)
    
if __name__=='__main__':
    main()
