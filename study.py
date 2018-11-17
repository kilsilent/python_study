Name=input('输入你的名字：')
name_dict={'张三':'北京','李四':'上海','王五':'重庆','赵六':'济南'}
if Name in name_dict:
    print('呀！都是%s的老乡' % name_dict.get('李四'))
else

