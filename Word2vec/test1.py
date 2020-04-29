from gensim.models import word2vec
import gensim

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


model=gensim.models.Word2Vec(sentences,sg=0,size=2,window=10,min_count=2,negative=3,sample=0.001,hs=1,workers=4)
# 获取model里面的所有关键词
keys = model.wv.vocab.keys()
# print(keys)
# 获取词对于的词向量
wordvector = []
for key in keys:
    wordvector.append(model[key])
print(wordvector)


# print(model.wv.vocab)

# words = model.wv.vocab
# size = model.wv.vectors
# i=0
# for word in words:
#
#     print(i)
#     print(word)
#     print(size[i])
#     i+=1
#创建模型
# model.save("kjcg_test1.txt")	#模型会保存到该 .py文件同级目录下，该模型打开为乱码
# model.wv.save_word2vec_format("kjcg_test2.txt",binary = "Ture")  #通过该方式保存的模型，能通过文本格式打开，也能通过设置binary是否保存为二进制文件。但该模型在保存时丢弃了树的保存形式（详情参加word2vec构建过程，以类似哈夫曼树的形式保存词），所以在后续不能对模型进行追加训练



#对.sava保存的模型的加载：
# model=gensim.models.Word2Vec.load("kjcg_test1.txt")

#对..wv.save_word2vec_format保存的模型的加载：
# model = model.wv.load_word2vec_format('kjcg_test1.txt')

#模型追加训练（不懂）
# model.train(more_sentences)



# print(model.most_similar("研究",topn=10))	#计算与该 词最近似的词，topn指定排名前n的词
#
# # 计算两个词的相似度：
# print(model.similarity("研究","农业"))
#
# # 获取词向量（有了这个不就意味着可以进行相关词语的加减等运算，虽然我不是太懂）：
# print('研究：',model ['研究'])
