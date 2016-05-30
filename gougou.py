import pandas as pd
import time
import sys

def CompareXlsx(filename):
    #Program begin
    Gou = []
    for fid,fname in enumerate(filename):
        df=pd.read_excel(fname,sheetname='Sheet1',header=None,parse_cols=[8,9])
        df.columns=['ID','name']
        df.sort_values(by='ID',inplace=True)    
        df.dropna(inplace=True)
        df.drop_duplicates(subset='ID',inplace=True)
        df.reset_index(drop=True,inplace=True)
        for idnum in range(len(df['ID'])-1,-1,-1):
            if isinstance(df['ID'][idnum], int):
                break
            df.drop(idnum,inplace=True)
        excel = df.reset_index(drop=True)
        Gou.append(excel['ID'])
        del excel
        del df
    
    com1=Gou[1][Gou[1].isin(Gou[0])]
    for comnum in range(2,len(filename)):
        com2=Gou[comnum].isin(com1)
        if 0==sum(com2):
            com1=[]
            print('Output:')
            print('No Same data')
            return
        com1=com1[com2]
    
    del Gou
    com1.reset_index(drop=True,inplace=True)
    samenum=len(com1)
    print('Output:')
    print('SAME:')
    pd.set_option('display.max_rows',samenum)
    print(com1)
    pd.reset_option('display.max_rows')
    print('NUM:%d' %samenum)
    com1.to_csv('compare.csv',index=False)
    
if __name__=="__main__":
    #start time
    start = time.clock()
    if len(sys.argv)<=1:
        filename=['partly.xlsx','radical.xlsx']
    elif len(sys.argv)==2:
        print('Not enough input file')
        sys.exit(0)
    else:
        filename=sys.argv[1:]
    print('Compare FILE is')
    print(filename)
    CompareXlsx(filename)
    #end time
    end = time.clock()
    print("The function run time is : %.03f seconds" %(end-start))
    