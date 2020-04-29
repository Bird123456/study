from gensim.models import word2vec
from sklearn.cluster import KMeans
import gensim
import numpy



#获取句子
sentences=word2vec.Text8Corpus("kjcg.txt")
# print(sentences)

#sg=1是skip—gram算法，对低频词敏感，默认sg=0为CBOW算法
#size是神经网络层数，值太大则会耗内存并使算法计算变慢，一般值取为100到200之间。
#window是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b个词，后面看b个词（b在0-3之间随机）
#min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。
#negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3,
#negative: 如果>0,则会采用negativesamping，用于设置多少个noise words
#hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用。
#workers是线程数，此参数只有在安装了Cpython后才有效，否则只能使用单核
model=gensim.models.Word2Vec(sentences,sg=0,size=100,window=5,min_count=2,workers=4)

#创建模型
model.save("kjcg_test1.txt")	#模型会保存到该 .py文件同级目录下，该模型打开为乱码

#对.sava保存的模型的加载：
model=gensim.models.Word2Vec.load("kjcg_test3.txt")


# 获取model里面的所有关键词
keys = model.wv.vocab.keys()
# print(keys)
# print(type(keys))
# print(list(keys)[0])

# 获取词对于的词向量
wordvector = []
for key in keys:
    wordvector.append(model[key])
# print(wordvector)

 #分类
classCount=10 #分类数
clf = KMeans(n_clusters=classCount)
s = clf.fit(wordvector)
# print(s)
#获取到所有词向量所属类别

labels=clf.labels_
print('类别：',labels)
# print(type(labels))

#把是一类的放入到一个字典里
classCollects={}
for i in range(len(keys)):

    # print('len(keys):',len(keys))#长度
    # print('classCollects的keys:',classCollects.keys())
    # print('labels[i]',labels[i])
    # print(keys)
    # print('dict_keys:',list(keys)[0])#将dict_keys转换为list，输出第一个元素
    # print(type(classCollects.keys()))
    # print(type(classCollects))

    # print(i)
    # print(classCollects.keys())
    print(list(classCollects.keys()))

    if labels[i] in list(classCollects.keys()):
        print('-----------------')
        classCollects[labels[i]].append(list(keys)[i])
    else:
        classCollects={0:[],1:[],2:[],3:[],4:[],    5:[],6:[],7:[],8:[],9:[]}

print('0类：',classCollects[0])
print('1类：',classCollects[1])
print('2类：',classCollects[2])
print('3类：',classCollects[3])
print('4类：',classCollects[4])
print('5类：',classCollects[5])
print('6类：',classCollects[6])
print('7类：',classCollects[7])
print('8类：',classCollects[8])
print('9类：',classCollects[9])