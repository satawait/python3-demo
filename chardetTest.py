import chardet
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))