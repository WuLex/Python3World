"""

"""
 
from random import sample
import time
import os
 
words="""朱砂 天下 杀伐 人家 韶华 风华 繁华 血染 墨染 白衣 素衣 嫁衣 倾城 孤城 空城 旧城
 旧人 伊人 心疼 春风 古琴 无情 迷离 奈何 断弦 焚尽 散乱 陌路 乱世 笑靥 浅笑 明眸 轻叹 烟火 
一生 三生 浮生 桃花 梨花 落花 烟花 离殇 情殇 爱殇 剑殇 灼伤 仓皇 匆忙 陌上 清商 焚香 墨香 
微凉 断肠 痴狂 凄凉 黄梁 未央 成双 无恙 虚妄 凝霜 洛阳 长安 江南 忘川 千年 纸伞 烟雨 回眸 
缥缈 纷扬 虚幻 莫测 锦绣 明媚 凉薄 萧瑟 纷纭 幽深 昏暗 清冷 翩跹 心碎 离愁 凄美 风干 坚定 
云散 相思 风尘 清澈 水漾 明澈 黯淡 泛黄 灼热 灼灼 清幽 纯净 凄凉 孤寂 皎洁 红莲 长久 绵长 
绵绵 凄美 潺潺 浩渺 清渺 萦绕 纤细 妩媚 苍茫 朦胧 姗姗 细微 萦回 凉意 灯火 温暖 安然 惊艳 
冷傲 沉淀 盈盈 浅笑 俏丽 倾城 
公子 红尘 红颜 红衣 红豆 红线 青丝 青史 青冢 白发 白首 白骨 黄土 黄泉 碧落 紫陌情深缘浅 情深不寿 
莫失莫忘 阴阳相隔 如花美眷 似水流年 眉目如画 曲终人散 繁华落尽 不诉离殇 一世长安 浮屠 斜雨 熏风 流年渐渐
荼靡 飘零 良辰 轻狂 沧海 墨韵 红尘阡陌 尘世 云淡风轻 川穹 苏梗 七漓 白薇 漓云 穹光 青苍 雨辰 云崖 子归 墨漓
水色浮华 烟花三月 落花流水 长夜漫漫 美人离殇 魂牵梦萦 清风明月 落霞满天 琴瑟和鸣 离别多情 水波不兴 锦瑟年华 
风华绝代 蝶恋花影 天涯海角 夜深人静 长夜漫漫 旧事如烟 凤求凰舞 芳华如梦 烟波江上 人在江湖 锦绣前程 花落花开 
一笑倾城 千年流光 断桥残雪 天长地久 月影当时 云烟过眼 千年风华 剑锋所指 画船听雨 天马行空 悲欢离合 长云万里 
相思成灾 莺莺燕燕 梦醒时分 万水千山 雨恨云愁 细水长流 春梦无痕 一往情深
寒 梦 舞 愁 凉 泪 伤 思 忆 花 霜 殇 青 烟 妆 幽 笑 雪 波 泪 落 恨 月 酒 眠 风 痕 妖 浅 雁 独 离 剑 苦 盼 舟 绝 伤 露 醉 零 虞 寻 散 镜 辞 心
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
 
os.system("@title python版古风诗词自动生成器")

for r in range(99):
    bard()
    time.sleep(1)
