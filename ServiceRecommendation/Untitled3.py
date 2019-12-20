
import pandas as pd


def conversion(xx):
    data=pd.read_csv('Book1.csv')
    data.drop(columns='user_ID')
    gk = data.groupby('recommended_service_ID')
    sone=gk.get_group('s1')
    x1=sone.shape[0]
    c1=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s2')
    x1=sone.shape[0]
    c2=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s3')
    x1=sone.shape[0]
    c3=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s4')
    x1=sone.shape[0]
    c4=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s5')
    x1=sone.shape[0]
    c5=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s6')
    x1=sone.shape[0]
    c6=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s7')
    x1=sone.shape[0]
    c7=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s8')
    x1=sone.shape[0]
    c8=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s9')
    x1=sone.shape[0]
    c9=sone[sone['conversion']=='yes'].shape[0]/x1
    sone=gk.get_group('s10')
    x1=sone.shape[0]
    c10=sone[sone['conversion']=='yes'].shape[0]/x1
    if xx == 'S1':
     print("conversion rate of service1 is",c1)
    if xx == 'S2':
        print("conversion rate of service1 is",c2)
    if xx == 'S3':
        print("conversion rate of service1 is",c3)
    if xx == 'S4':
        print("conversion rate of service1 is",c4)
    if xx == 'S5':
        print("conversion rate of service1 is",c5)
    if xx == 'S6':
        print("conversion rate of service1 is",c6)
    if xx == 'S7':
        print("conversion rate of service1 is",c7)
    if xx == 'S8':
        print("conversion rate of service1 is",c8)
    if xx == 'S9':
        print("conversion rate of service1 is",c9)
    if xx == 'S10':
        print("conversion rate of service1 is",c10)

def main():
    x = ('print the conversion rate for....')
    conversion(x)

if __name__ == "__main__" :
    main()



