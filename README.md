# 我想要一个优雅的变量名？
> 正在更新中  Imporove

#### 先下载或者克隆 VarName.py文件:  

``` shell
git clone https://github.com/Tikmoing/VarName.git  
```

#### 使用:(两种方法)

1. shell下使用：

   ``` shell
   python3 VarName.py
   ```

   之后屏幕上会出现:

   ``` shell
   >
   ```

   现在输入你想要的变量的表达的中文意思：

   ```shell
   > 随机变量
   >
   ```

   然后回车；但是因为为了让你有更多描述，所以再回车之后需要再输入一次，要截至输出只需要什么都不输入然后回车即可。

   之后会发现出现的结果:

   ``` shell
   英语小驼峰式：randomVariables,
   英语大驼峰式：RandomVariables,
   英语下划线式：Random_Variables,
   全拼小驼峰式：suiJiBianLiang,
   全拼大驼峰式：SuiJiBianLiang,
   全拼下划线式：sui_ji_bian_liang,
   ```

2. python程序或者交互端引入该文件

   ```python
   import varname
   var_get = varname.VarName()
   description = '随机过程'    #description是对变量作用的描述
   var_get.getName((description,))  #传入的参数必须是元组
   
   '''
   Output:
   英语小驼峰式：randomVariables,
   英语大驼峰式：RandomVariables,
   英语下划线式：Random_Variables,
   全拼小驼峰式：suiJiBianLiang,
   全拼大驼峰式：SuiJiBianLiang,
   全拼下划线式：sui_ji_bian_liang,
   '''
   ```

   输出的结果为:

   ``` shel
   英语小驼峰式：randomVariables,
   英语大驼峰式：RandomVariables,
   英语下划线式：Random_Variables,
   全拼小驼峰式：suiJiBianLiang,
   全拼大驼峰式：SuiJiBianLiang,
   全拼下划线式：sui_ji_bian_liang,
   ```

#### 说明：

1. 可以输入多个变量描述来获取同一个变量的不同变量名:

   ```shell
   >随机过程
   >随机事件
   >
   ```
   
   输出:
   
   ```shell
   英语小驼峰式：stochasticProcess,randomEvents,
   英语大驼峰式：StochasticProcess,RandomEvents,
   英语下划线式：stochastic_process,Random_events,
   全拼小驼峰式：suiJiGuoCheng,suiJiShiJian,
   全拼大驼峰式：SuiJiGuoCheng,SuiJiShiJian,
   全拼下划线式：sui_ji_guo_cheng,sui_ji_shi_jian,
   ```
   
2. 可以输入多个变量描述来获取不同变量的变量名

   ```shell
   >随机事件
   >输出打印
   >
   ```
   
   结果：
   
   ```shell
   英语小驼峰式：randomEvents,outputPrint,
   英语大驼峰式：RandomEvents,OutputPrint,
   英语下划线式：Random_events,Output_Print,
   全拼小驼峰式：suiJiShiJian,shuChuDaYin,
   全拼大驼峰式：SuiJiShiJian,ShuChuDaYin,
   全拼下划线式：sui_ji_shi_jian,shu_chu_da_yin,
   ```
   
3. 英文字符整合:

   如果这么输入:

   ```shell
   >random event
   >
   ```
   
   结果如下：
   
   ```shell
   英语小驼峰式：randomEvent,
   英语大驼峰式：RandomEvent,
   英语下划线式：random_event,
   全拼小驼峰式：randomEvent,
   全拼大驼峰式：RandomEvent,
   全拼下划线式：random_event,
   ```
   
4. 符号处理：

   如果这么输入：

   ```null
   >random ^^^ev##ent
   >
   ```

   结果如下：

   ```shell
   英语小驼峰式：randomEvent,
   英语大驼峰式：RandomEvent,
   英语下划线式：random_event,
   全拼小驼峰式：randomEvent,
   全拼大驼峰式：RandomEvent,
   全拼下划线式：random_event,
   ```