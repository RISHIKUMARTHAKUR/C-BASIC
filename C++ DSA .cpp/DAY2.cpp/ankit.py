import pandas as pd
import matplotlib.pyplot as plt

def menu():

    print()
    print('*******************************************************************')
    print(             '        MEDICAL STORE MANAGEMENT SYSTEM ')
    print('*******************************************************************')
    print('        0. know about the project ')
    print('        1. reading file stock')
    print('        2. reading file stock without index')
    print('        3. make an entry of new medicine in stock')
    print('        4. arrange medicine in stock alphabetically')
    print('        5. delete medicine details if it is out of stock')
    print('        6. update details of medicine in stock')
    print('        7. show list of medicine in stock')
    print('        8. read few records from stock')
    print('        9. read top 2 medicines details 2 from bottom arranged according to code')
    print('        10. show price list of medicines')
    print('        11. show records of staff in the store')
    print('        12. add new employee record in staff')
    print('        13. find maximum salary of staff')
    print('        14. find minimum salary in staff')
    print('        15. record of sold medicines in detail')
    print('        16. customer order for medicine')
    print('        17. search medicine by name')
    print('        18. line plot')
    print('        19. line1 plot')
    print('        20. bar plot')
    print('        21. bar1 plot')
    print('        22. barh plot')
    print('        23. barh1 plot')
    print()
    print('*********************************************************************')



menu()
def about():
    print(' in MEDICAL STORE MANAGEMENT SYSTEM project there are 3 CSV files named as\ stock,staff and bill. \there are 23 options including 6 plots')

def stockcsv():
    print(' reading file stock')
    print()
    print()
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv')
    print(df)



def no_index():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col=0)
    print('without index')
    print()
    print(df)
    print()


def newmed():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col=0)
    print(df)
    a=int(input('enter medicine code : '))
    b=(input('enter medicine name : '))
    c=(input('enter date of expiry : '))
    df.loc[a]=[b,c,d,e]
    print(df)


def sortmed():
    print('display names of medicines in ascending order ')
    print()
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col=0)
    df=df.sort_values('mname')
    print(df)


def removemed():
    print('deleting medicine from file stock ')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col='mcode')
    print(df)
    mcode=int(input('enter mcode : '))
    df.drop(mcode,axis=0,inplace=True)

    print('record of medicine temperarily deleted')
    print(df)
    print(df)


def updatemed():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col='mcode')
    print(df)
    a=int(input('enter medicine code which needs to be updated : '))
    b=(input('enter medicine name : '))
    c=(input('enter date of expiry : '))
    d=int(input('enter quantity : '))
    e=int(input('enter price : '))
    df.loc[a]=[b,c,d,e]
    print('data successfully updated')
    print(df)
    df.to_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv')
    print(df)


def medstock():
    print('display only account no. , name and balance ')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',usecols=['mname','quantity'])
    print(df)


def read_rows():
    print('show only few records')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',nrows=2)
    print('show 2 records')
    print(df)


def top_bottom():
    print('show only few records from top and bottom ')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv')
    print('top 2 records')
    print(df.head(2))
    print()
    print()
    print('last 2 records')
    print(df.tail(2))


def pricelist():
    print('sorting medicine names in ascending order')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock .csv',index_col=0,usecol=['mname','price'])
    df=df.sort_values('mname')
    print(df)


def readstaff():
    print('reading file mstaff')
    print()
    print()
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\mstaff.csv',index_col=0)
    print(df)


def new_staff():
    print()
    print('old employees record in file mstaff')
    print()
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\mstaff.csv')
    print(df)
    print()
    print()
    print('new employee added')
    print()
    df.at['6',:]=['206','aman','29','salesman','9817090718','17000']
    print(df)


def maxsal():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\mstaff.csv')
    print(df)
    print('highest salary of staff')
    print(df.salary.max())


def minsal():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\mstaff.csv')
    print(df)
    print('lowest salary of staff')
    print(df.salary.min())


def billrec():
    print('reading sales records')
    print()
    print()
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\bill.csv',index_col=0)
    print(df)


def order():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\bill.csv',index_col=0)
    print(df)
    m=(input('enter mobile no. : '))

    n=(input('enter medicine name : '))

    q=int(input('enter quantity : '))
    p=int(input('enter price : '))
    bill=q*p
    price(m,' yopur bill is ' , bill , ' you have bought ',n,q,'pieces')
    p=int(input('enter payment you are giving : '))
    balance=bill-p
    print('you will get back Rs. ',balance)


def searchmed():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    print()
    print(df.loc[df['mname'] == 'vicks 50mg'])


def line_plot():
    print('line plot')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    x=df['mname']
    y=df['price']
    plt.title('medicine names and prices')
    plt.xlabel('medicine')
    plt.ylabel('price')
    plt.xticks(rotation=30)
    plt.plot(x,y,marker='*',linewidth=4,color='black')
    plt.grid(True)
    plt.show()


def line1_plot():
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    plt.plot(df['mname'],df['price'],color['red'], marker='0')
    plt.title('medicine names and prices ')
    plt.xlabel('medicine')
    plt.ylabel('price')
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.show()



def bar_plot():
    print('bar plot')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    x=df['mname']
    y=df['dateofexp']
    plt.title('names of medicines and their date of expiry')
    plt.xlabel('medicine')
    plt.ylabel('date of expiry')
    plt.xticks(rotation=30)
    plt.bar(x,y,color=['red','black'])
    plt.show()


def bar1_plot():
    print('bar plot')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\mstaff.csv')
    print(df)
    x=df['name']
    y=df['salary']
    plt.title('employees names and their salary')
    plt.xlabel('names')
    plt.ylabel('salary')
    plt.xticks(rotation=30)
    plt.bar(x,y,color=['red','black'])
    plt.show()


def barh_plot():
    print('horizontal bar plot')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    x=df['mnames']
    y=df['quantity']
    plt.title('medicines names and quantity in stock')
    plt.xlabel('medicines')
    plt.ylabel('quantity')
    plt.barh(x,y,color='blue',edgecolor='black')
    plt.show()


def barh1_plot():
    print('horizontal bar plot')
    df=pd.read_csv('C:\\Users\\91993\\OneDrive\\Documents\\Csv_Files\\Mstock.csv')
    print(df)
    x=df['mnames']
    y=df['price']
    plt.title('medicine names')
    plt.xlabel('medicine')
    plt.ylabel('price')
    plt.barh(x,y,color='orange',edgecolor='red')
    plt.show()


opt=''
opt=int(input('enter your choice : '))
if opt==0:
    about()
elif opt==1:
    stockcsv()
elif opt==2:
    no-index()
elif opt==3:
    newmed()
elif opt==4:
    sortmed()
elif opt==5:
    removemed()
elif opt==6:
    updatemed()
elif opt==7:
    medstock()
elif opt==8:
    read_rows()
elif opt==9:
    top_bottom()
elif opt==10:
    pricelist()
elif opt==11:
    readstaff()
elif opt==12:
    new_staff()
elif opt==13:
    maxsal()
elif opt==14:
    minsal()
elif opt==15:
    billrec()
elif opt==16:
    order()
elif opt==17:
    searchmed()
elif opt==18:
    line_plot()
elif opt==19:
    line1_plot()
elif opt==20:
    bar_plot()
elif opt==21:
    bar1_plot()
elif opt==22:
    barh_plot()
elif opt==23:
    barh1_plot()
else:

    print('invalid option')
    print('\a')

    


    
    
