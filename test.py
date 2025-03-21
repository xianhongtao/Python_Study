import jieba
import jieba.analyse

String = "我是一个中国人，我爱我的祖国"
# 使用默认分词
seg_list = jieba.cut(String, cut_all=False)
#输出分词
print("Default Mode: " + "/ ".join(seg_list))
