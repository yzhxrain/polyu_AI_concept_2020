# from math import log
# import operator
#
#
# def calcShannonEnt(dataset):
#     numEntries = len(dataset)  # 输入样本个数
#     labelCounts = {}  # 存类别及相应的数量
#     for featVec in dataset:  # 一行即是一个特征向量
#         currentLable = featVec[-1] # 取每个样本的类别
#         if currentLable not in labelCounts.keys():# 如果变量已经有类别，则在数量上+1，如果没有，则先新建一个再+1
#             labelCounts[currentLable] = 0
#         labelCounts[currentLable] += 1
#     shannoEnt = 0
#     for key in labelCounts:
#         prob = float(labelCounts[key])/float(numEntries)
#         shannoEnt += -prob*log(prob, 2)  # 计算所有样本的信息熵
#     return shannoEnt
#
#
# def creaDataSet1():
#     dataSet = pd.read_csv("census.csv")
#     labels = ['身高', '财富', '外貌']
#     return dataSet, labels
#
#
# def splitDataSet(dataSet, axis, value):
#     retDataset = []
#     for feaVec in dataSet:  # 迭代每一个样本
#         if feaVec[axis] == value:  # 如果样本的这个特征值=要求的值
#             reducedFeatVec = feaVec[:axis] # 取这个样本的前N个特征，直到筛选的这个特征
#             reducedFeatVec.extend(feaVec[axis+1:]) #拼接这个特征之后的所有特征值，相当于去掉这个特征
#             retDataset.append(reducedFeatVec)  # 给出按这个特征值分类后的剩余特征
#     return retDataset
#
#
# def chooseBestFeatureToSplit(dataset):
#     numFeatures = len(dataset[0]) - 1  #特征个数
#     baseEntropy = calcShannonEnt(dataset) # 计算信息熵
#     bestInfoGain = 0
#     bestFeature = -1
#     for i in range(numFeatures):# 迭代每一个特征
#         featList = [example[i] for example in dataset]  # 找出这个特征的所有属性值
#         uniqueVals = set(featList)  # 这个特征的唯一属性值
#         newEntropy = 0
#         for value in uniqueVals:
#             subDataset = splitDataSet(dataset, i, value)  # 按这个特征这个属性值分类后的子集
#             prob = float(len(subDataset))/float(len(dataset))  # 子集在全样本集中的概率
#             newEntropy += prob*calcShannonEnt(subDataset)  # 计算按这个特征这个属性分裂后的信息熵，直接迭代完这个特征所有的属性值，得到按这个特征分裂后所有的条件熵
#         infoGain = baseEntropy - newEntropy # 计算信息增益
#         if (infoGain > bestInfoGain):
#             bestInfoGain = infoGain  # 最佳的信息增益
#             bestFeature = i  # 最佳的特征
#     return bestFeature
#
#
# def majorityCnt(classList):
#     classCount = {}
#     for vote in classList: # 对提供的样本类别列表进行计数
#         if vote not in classCount.keys():
#             classCount[vote] = 0
#         classCount[vote] += 1
#     sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True) # 倒排，找到个数最多的样品类别，则为这个节点的类别
#     return sortedClassCount[0][0]
#
#
# def createTree(dataset, labels):
#     classList = [example[-1] for example in dataset] # 得到所有样本的类别
#     if classList.count(classList[0]) == len(classList): # 如果样本都是一个类别，则直接按这个类别就行了
#         return classList[0]
#     if len(dataset[0]) == 1: # 如果只剩下一个特征，？
#         return majorityCnt(classList)
#     bestFeat = chooseBestFeatureToSplit(dataset)  # 筛选最佳的特征
#     print(labels) # 对应的特征名
#     bestFeatLabel = labels[bestFeat] # 得到最佳的特征名
#     myTree = {bestFeatLabel:{}}
#     del (labels[bestFeat]) # 删除已经用于分裂的特征
#     featValues = [example[bestFeat] for example in dataset]  # 按此特征的所有特征值
#     uniqueVals = set(featValues)  # 特征值的唯一
#     for value in uniqueVals:
#         subLablels = labels[:] # 剩余可以用于分裂的特征
#         print('sub"', subLablels)
#         myTree[bestFeatLabel][value] = createTree(splitDataSet(dataset, bestFeat, value), subLablels)
#     # 先按最优特征值的某一个属性分裂，得到子集，对子集再找最优特征分裂，直到全部类别一样，或者已经没有特征可选时采用最大投票法得出分类结果；迭代的结果全部依次存入mytree字典中
#     return myTree
#
#
# if __name__ == '__main__':
#     dataSet, labels = creaDataSet1()
#     map = createTree(dataSet, labels)
#     print(map)
