import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def set_ch():
    from matplotlib.pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
    #对应文件名字叫做msyh.ttf
    #1、先将名字参数映射为文件名（fontManager中的注册的名字），根据文件名在fonts文件夹中寻找字体文件进行加载
    #2、也可以直接修改matplotlibrc配置文件，在sans-serif参数中加入'Microsoft YaHei'，使得导入matplotlib时生成的配置字典改变
    #但以上两种都必须导入字体文件才行
    #字体注意用ttf文件，不要用ttc文件，好像不怎么支持ttc。
    mpl.rcParams['axes.unicode_minus'] = False     
set_ch()

def dataframe_split1(a,b):
    s=a[b].str.split(expand=True)
    print(s)
    print(type(s))
# dataframe_split1(df,'发单时间')
#将日期进行分割  pandas.Series.str.split
    

df=pd.read_excel('C:/Users/Administrator/Desktop/1111.xls',sheetname=0)
namelist=pd.read_excel('C:/Users/Administrator/Desktop/namelist.xls',sheetname=0)
df['发单时间']=pd.to_datetime(df['发单时间'])
#sheetname的第一个参数是从0开始的
# print(df)
# print(df['订单时长'])
# print(df.dtypes)
# print(type(df['发单时间']))

if '订单时长' in df:
    print('yyyy')
else:
    print('nnnn')


df['is_completed']='否'
df.ix[(df['发单状态']=='匹配成功')&(df['是否异常']=="否")&(df['是否进入通话']=='是'),'is_completed']='是'
# df.loc[(df['发单状态']=='匹配成功')&(df['是否异常']=="否")&(df['是否进入通话']=='是'),'is_completed']='是'#报错

# df['is_completed']='是'
# df.ix[df['发单状态']!='匹配成功','is_completed']='否'
# df.ix[df['是否异常']!='否','is_completed']='否'
# df.ix[df['是否进入通话']!='是','is_completed']='否'

df2=df.drop(['服务','订单语言','订单时长','志愿者','发单方式','推送B端人数','推送B端','应付款','实际付款'],axis=1)
#df没有变，执行后的结果需要赋值给一个变量才行
df3=df.reindex(columns=['订单时长','志愿者','发单方式','服务','订单语言','推送B端人数','推送B端','应付款','实际付款'])


time_start=(2016,10,26,20,00,00)
time_end=(2016,10,26,22,00,00)
# df5=df.pivot(index='发单用户id',columns='订单时长',values='发单方式')
#暂时不要用，好像有问题


def count(series):
    return series.value_counts().get('是',default=0)

# df5t=pd.pivot_table(df,index=['发单用户id','发单用户昵称'],columns='B端设备',values='is_completed',aggfunc=count)


# df5.insert(0,'add',df5.index)#插入列

df_vlookup=pd.merge(df,namelist,how='inner',left_on='发单用户id',right_on='用户ID',indicator=True)
df_v_pivot=pd.pivot_table(df_vlookup,index=['发单用户id','发单用户昵称'],columns='B端设备',values='is_completed',aggfunc=count)
df6=df_v_pivot.reset_index()

df5=pd.pivot_table(df_vlookup,index='发单用户id',columns='订单时长',values='is_completed',aggfunc=count)
# df2.insert(6, "abbrev", np.nan)#把"abbrev"插入到第6列，填充方法是np.nan
# df['abbrev'] = df.apply(convert_state, axis=1)#对each column 使用convert_state函数
# df=df.append(df_sum,ignore_index=True)#填充行数据

# print(df['is_completed'])
# print(df.dtypes)
# df=df.to_excel('C:/Users/Administrator/Desktop/123.xls',sheet_name=1)
#注意和read_excel的区别，sheet_name|sheetname细节不一样，还不能用int
# df.info()

df7=df_v_pivot.append(df_v_pivot.sum(numeric_only=True).reindex(index=df_v_pivot.columns).T.rename('sum'))

df8=pd.concat([df_v_pivot,df_v_pivot.sum(numeric_only=True).to_frame(name='sum').T])

df_res=df.reindex(columns=['发单时间','is_completed']).set_index('发单时间')
df_res=df_res.resample('30min').apply(count)

# df9=df_res[(df_res.index>'%d/%d/%d  %d:%d:%d'%(year,month,day,hour,mins,seconds))&(df_res.index<'%d/%d/%d  %d:%d:%d'%(year,month,day,hour,mins,seconds))]
df9=df_res[(df_res.index>='%d/%d/%d  %d:%d:%d'%time_start)&(df_res.index<='%d/%d/%d  %d:%d:%d'%time_end)]

# df9.plot.pie(subplots=True)
# df9.plot.density()
df9.plot(kind='bar',title='发单时序统计',grid=True,)
plt.show()

df_groupby=df.groupby(list(df.columns)[0:len(df.columns)-1]).sum()


with pd.ExcelWriter('C:/Users/Administrator/Desktop/1234.xls') as a:
    df.to_excel(a,sheet_name='df')
    df2.to_excel(a,sheet_name='drop')
    df3.to_excel(a,sheet_name='实现重组')
    df5.to_excel(a,sheet_name='pivot')
    df_vlookup.to_excel(a,sheet_name='merge_vlookup')
    df_v_pivot.to_excel(a,sheet_name='pivot2')
    df6.to_excel(a,sheet_name='pivot2_reset_index')
    df7.to_excel(a,sheet_name='append')
    df8.to_excel(a,sheet_name='concat')
    df_res.to_excel(a,sheet_name='res')
    df9.to_excel(a,sheet_name='res_index_filtration')
    df_groupby.to_excel(a,sheet_name='df_groupby')
    

# df.to_excel('C:/Users/Administrator/Desktop/1111111.xls',sheet_name='zhanghui1')
#没有文件的话会新建一个文件


# df.info#nothing happended
df.info()