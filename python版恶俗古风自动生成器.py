"""
python版恶俗古风自动生成器.py
模仿自: http://www.jianshu.com/p/f893291674ca
2016年4月4日 18:37:31 codegay
"""
 
from random import sample
import time
import os
 
words="""朱砂 天下 杀伐 人家 韶华 风华 繁华 血染 墨染 白衣 素衣 嫁衣 倾城 孤城 空城 旧城
 旧人 伊人 心疼 春风 古琴 无情 迷离 奈何 断弦 焚尽 散乱 陌路 乱世 笑靥 浅笑 明眸 轻叹 烟火 
一生 三生 浮生 桃花 梨花 落花 烟花 离殇 情殇 爱殇 剑殇 灼伤 仓皇 匆忙 陌上 清商 焚香 墨香 
微凉 断肠 痴狂 凄凉 黄梁 未央 成双 无恙 虚妄 凝霜 洛阳 长安 江南 忘川 千年 纸伞 烟雨 回眸 
公子 红尘 红颜 红衣 红豆 红线 青丝 青史 青冢 白发 白首 白骨 黄土 黄泉 碧落 紫陌情深缘浅 情深不寿 
莫失莫忘 阴阳相隔 如花美眷 似水流年 眉目如画 曲终人散 繁华落尽 不诉离殇 一世长安 浮屠 斜雨 熏风 流年渐渐
荼靡 飘零 良辰 轻狂 沧海 墨韵 红尘阡陌 尘世 云淡风轻 川穹 苏梗 七漓 白薇 漓云 穹光 青苍 雨辰 云崖 子归 墨漓
"""
 
temp=["xx，xx，xx了xx。","xxxx，xxxx，不过是一场xxxx。",
"你说xxxx，我说xxxx，最后不过xxxx。","xx，xx，许我一场xxxx。",
"一x一x一xx，半x半x半xx。","你说xxxxxxxx，后来xxxxxxxx。","xxxx，xxxx，终不敌xxxx。"]
 
word1=words.replace(" ","").replace("\n","")
word2=[r for r in words.split() if len(r)==2]
word4=[r for r in words.split() if len(r)==4]
 
def bard():
    temp1=sample(temp,1)[0]
    while "xxxx" in temp1:
        temp1=temp1.replace("xxxx",sample(word4,1)[0],1)
    while "xx" in temp1:
        temp1=temp1.replace("xx",sample(word2,1)[0],1)
    while "x" in temp1:
        temp1=temp1.replace("x",sample(word1,1)[0],1)
    print(temp1)
 
os.system("@title python版恶俗古风自动生成器")
 
for r in range(99):
    bard()
    time.sleep(1)
