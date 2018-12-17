def mainpart(m,n,a,b,alls=[],i=0,j=0,ans=[],lst=[]):
    '''主体部分，应用递归
       alls表示包含所有铺法的列表
       ans表示其中一种铺法
       m,n表示墙的长和宽
       a,b表示砖的长和宽
       i表示第几列
       j表示第几行'''
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
    '''判断是否能铺
       包括：
       长度符合
       宽度符合
       铺砖的位置没有其他砖'''
    if (i+a)>m or (j+b)>n:
        return False
    for z in range(j,j+b):
        for x in range(i,i+a):
            if lst[z*m+x]==-1:
                return False
    return True

def do(a,b,m,i,j,lst,ans):
    '''铺砖的方法
       ans表示其中一种铺法
       re是元组（表示一块砖铺的位点）'''
    re=()
    for z in range(j,j+b):
        for x in range(i,i+a):
            k=z*m+x
            lst[k]=-1
            re=re+(k,)
    ans.append(re)

import turtle
wn=turtle.Screen()

def visible(m,n,t,i=0):
    '''通过turtle将用户选择的铺法可视化'''    
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
    l.goto(x1*30,-y1*30)
    l.down()
    l.goto(x0*30,-y1*30)
    l.goto(x0*30,-y0*30)
    l.goto(x1*30,-y0*30)
    l.goto(x1*30,-y1*30)
    if i<len(t)-1:
        visible(m,n,t,i+1)

def signal(m,n,number=0):
    '''通过turtle给砖标号
       验证结果'''
    l2=turtle.Turtle()
    for i in range(n):
        for j in range(m):
            l2.up()
            l2.goto(30*j+20,-(30*i+20))
            l2.write(number,False,align="center")
            number+=1
    l2.hideturtle()

def main():
    '''数字间的逗号为英文符号'''
    wall=input('请输入墙的尺寸（如4，2）').split(',')
    brick=input('请输入砖的尺寸（如2，1）').split(',')
    m=int(wall[0])
    n=int(wall[1])
    a=int(brick[0])
    b=int(brick[1])
    answer=[]
    mainpart(m,n,a,b,answer)
    print('有{0}种铺法，分别是：'.format(len(answer)))
    for i in range(len(answer)):        
        print('方案{0}：{1}'.format(i+1,answer[i]))
    if answer!=[]:
        x=int(input('请输入您需要将第几种可视化（从左到右排）（如6）'))
        t=answer[x-1]
        signal(m,n,number=0)
        visible(m,n,t,i=0)
        
if __name__=='__main__':
    main()
