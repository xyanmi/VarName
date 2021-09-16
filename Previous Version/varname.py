import googletrans
import hyper
import re
from xpinyin import Pinyin
import string
from zhon import hanzi
'''
文件 过旧，不再适用，编写新版本中
'''

'''
算法

首先判断给进来的元组是不是符合标准，判断空格和空串
接下来就是去除给进来的语句的所有标点符号

分两种情况：中文输入，非纯中文输入
中文输入：英文翻译和全拼，很好办

非纯中文输入难办
以下结构：
提取中文和英文，我把其结构归于中文处理结果+ 英文处理结果
所以根据这些来处理
'''

class VarName:

    #将语句变成小驼峰格式
    def smallFeng(self,melist):
        inStr =''
        for i in melist:
            if melist.index(i) == 0:
                inStr = inStr + i.lower()
            else:
                inStr = inStr + i[0].upper() + i[1:].lower()
        return inStr

    # 将语句变成大驼峰格式
    def BigFeng(self,melist):
        inStr = ''
        for i in melist:
            inStr = inStr + i[0].upper() + i[1:]
        return inStr

    # 将语句变成下划线格式
    def lower_style(self,melist):
        in_str = ''
        for i in melist:
            if melist.index(i) == 0 :
                in_str = in_str + i
            else:
                in_str = in_str + '_' + i
        return in_str

    #除去符号
    def subsgin(self,strsname):
        return re.sub("\\n|\\r|\\xa0|\\t|[%s%s]"%(string.punctuation,hanzi.punctuation),"",strsname)

    
    #判断里面是不是有英文字符
    def cnen(self,strsname):
        for i in strsname:
            if ord(i) < 127:
                return 0
        else:
            return 1

    #提取英文字符并且翻译处理
    def geten(self,strsname):
        return_list = []
        #提取翻译过程
        tranMass = googletrans.Translator(service_urls=['translate.google.cn'])

        cnstr = ''
        enstr = ''

        #提取
        for i in strsname:
            if ord(i) < 127:
                enstr = enstr + i
            else:
                cnstr = cnstr + i

        en_cn_str_get = tranMass.translate(cnstr).text
        en_cn_str_get = re.sub("[%s]*"%string.punctuation,"",en_cn_str_get)
        my_list = en_cn_str_get.split(" ")

        #去掉my_list中的空字符串
        
        enstr = re.sub("  "," ",enstr)
        enstr_list = enstr.split(" ")
        for i in enstr_list:
            my_list.append(i)
        #处理空字符
        for i in my_list:
            if not i :
                my_list.pop(my_list.index(i))
            else:
                pass
        #生成小驼峰式
        return_list.append(self.smallFeng(my_list))

        #生成大驼峰式
        return_list.append(self.BigFeng(my_list))

        #生成_接式
        return_list.append(self.lower_style(my_list))

        return return_list
    
    #提取英文字符并且全拼处理
    def getcn(self,strsname):
        #提取
        cnstr = ''
        enstr = ''
        for i in strsname:
            if ord(i) <127:
                enstr = enstr + i
            else:
                cnstr = cnstr + i
        enstr = re.sub("  "," ",enstr)
        enstr_list = enstr.split(" ")
        #处理

        pinyin_get = Pinyin()
        return_list = []
        my_list_str = pinyin_get.get_pinyin(cnstr)
        my_list = my_list_str.split("-")
        #去掉my_list中的空字符串
        for i in enstr_list:
            my_list.append(i)

        for i in my_list:
            if not i :
                my_list.pop(my_list.index(i))
            else:
                pass
        #生成小驼峰式
        return_list.append(self.smallFeng(my_list))

        #生成大驼峰式
        return_list.append(self.BigFeng(my_list))

        #生成_接式
        return_list.append(self.lower_style(my_list))

        return return_list
        
            
    #pinyin语句化处理
    def setence(self,strsname):
        return_list = []
        my_list_str = strsname
        my_list = my_list_str.split("-")

        #生成小驼峰式
        return_list.append(self.smallFeng(my_list))

        #生成大驼峰式
        return_list.append(self.BigFeng(my_list))

        #生成_接式
        return_list.append(self.lower_style(my_list))

        return return_list

        
    #拼音式处理
    def quanpin(self,strsname):
        pinyin_get = Pinyin()
        return_list = []
        my_list_str = pinyin_get.get_pinyin(strsname)
        my_list = my_list_str.split("-")

        #生成小驼峰式
        return_list.append(self.smallFeng(my_list))

        #生成大驼峰式
        return_list.append(self.BigFeng(my_list))

        #生成_接式
        return_list.append(self.lower_style(my_list))

        return return_list

        
    #翻译处理
    def operate(self,strsname):
        tranMass = googletrans.Translator(service_urls=['translate.google.cn'])
        strsname = tranMass.translate(strsname).text
        strsname = re.sub("[%s]*"%string.punctuation,"",strsname)
        return_list = []
        my_list = strsname.split(" ")
        
        #生成小驼峰式
        return_list.append(self.smallFeng(my_list))

        #生成大驼峰式
        return_list.append(self.BigFeng(my_list))

        #生成_接式
        return_list.append(self.lower_style(my_list))

        return return_list
        
        
    def getName(self,strsTuple):
        never = list(strsTuple)
        for i in range(0,len(never)):
            never[i] = self.subsgin(never[i])
        get = []
        get2 = []
        for i in never:
            if not re.sub("[ ]+","",i):
                get.append('         ')
                get2.append('         ')
            elif self.cnen(i):
                get.append(self.operate(i))
                get2.append(self.quanpin(i))
            else:
                i = re.sub("[ ]+"," ",i)
                get.append(self.geten(i))
                get2.append(self.getcn(i))

        #输出
        #模式字符ni 
        desc = ["小驼峰式：","大驼峰式：","下划线式："]
        givemess = ["英语","全拼"]

        for i in range(0,len(desc)):
            print(givemess[0]+desc[i],end="")
            for j in range(0,len(get)):
                print(get[j][i],end = ",")
            print()

        for i in range(0,len(desc)):
            print(givemess[1]+desc[i],end="")
            for j in range(0,len(get)):
                print(get2[j][i],end = ",")
            print()


def main():
    s = []
    getVarName = VarName()
    while True:
        getIt = input("--->")
        if getIt == "":
            break
        s.append(getIt)
    s = tuple(s)
    getVarName.getName(s)


if __name__ == "__main__":
    main()
        
        
    
        
