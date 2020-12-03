import numpy as np

# 一维测试
#arr =np.array([1,2,3,4,5,6]) #用列表初始化
#print("arr=",arr)
#print("size=",arr.size,",shape=",arr.shape)
# 二维测试
#arr =np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]]) #初始化二维数组
#print(arr)
#print("size=",arr.size,",shape=",arr.shape) #shape(2,6) 2是行，6是列
# 三维测试
#arr =np.array([[[1,2,3,4],[5,6,7,8]],[[4,3,2,1],[8,7,6,5]]])
#print(arr)
#print("size=",arr.size,",shape=",arr.shape) #shape(2,2,4) 2是块，2是行，4是列

#特殊数组的创建
print("----------------------------------特殊数组创建---------------------------------------")

# 创建一维数组
#arr  =np.arange(0,10,1) #不包括10，步长为1 
#print(arr)
#
#arr = np.arange(10) #起始为0，步长为1，可以省略
#print(arr) # 上下两个效果相同#

#创建 等差数组 
#arr =np.linspace(0,10,11) #参数1起始位置，参数2结束位置 参数3 元素个数,不指定默认为50
#print(arr)
#
#arr =np.linspace(0,10) #参数1起始位置为0，也不能省略，参数2结束位置 参数3 元素个数,不指定默认为50
#print(arr)

#创建等比数组
#arr = np.logspace(2,8,3) 
#print(arr)

#ones/zeros数组
#arr = np.ones(10)
#print(arr)
#
#arr=np.zeros(5)
#print(arr)

#diags/eye 数组
#arr = np.diag([1,3,4,7])
#print(arr)
#
#arr=np.eye(3)
#print(arr)

#创建随机数组 均匀分布、正态分布，随机整数数组
#arr=np.random.randint(0,20,10)
#print(arr)
#
#arr=np.random.randint(1,10,(2,4)) #参数3可以是元素个数和形状
#print(arr)

#数组的索引
print("--------------------------------------------数组索引-------------------------------------------")

# 一维数组
#arr = np.arange(1,13,1)
#print(arr)
#
#print(arr[2],arr[-1]) # 下标方式获取
#print(arr[2:3:1])    #切片方式
#
#print(arr[[2,-1]]) #获取多个元素，利用下标列表方式
#print(arr[2:10:1]) # 获取多个元素，利用切片方式

# 二维数组
arr =np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]]) #初始化二维数组
#print(arr)
#
#print(arr[1,0],arr[1,1],arr[0,2]) #下标方式7,8,3
#print(arr[1:2,0:1]) #切片方式 
#print(arr[0,2:3]) #切片和下标配合方式

#print(arr[[0,0,1,1],[1,2,1,3]]) #获得多个元素，利用下标列表方式
#print(arr[1:3,1:3])  #获得多个元素，采用下标列表方式
#print(arr[0:2,0:4])  #获得多个元素，采用下标列表方式,行只能是0，1，列可以是0，1，2，3
#print(arr[1:2,:]) #行是第一行，列是所有列

# 利用bool 数组来获取
#bool_column= np.array([0,1,1,0,0,1],dtype=np.bool)
#bool_row= np.array([0,1],dtype=np.bool)
#print(bool_column)
#print(bool_row)
#print(arr[bool_row,:])
#print(arr[:,bool_column]) #保留true的列
