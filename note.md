# tensorflow

## tensorboard

- **关于tensorboard不显示问题**
本人测试存放events文件的目录必须在c盘，根据网上说明tensorflow运行后的events文件的路径需要在python启动的时的路径下。 
例如在windows 启动tensorboard的路径为 C:\Users\Administrator> 
则events文件必须在该文件下。

## others
- **PCA（Principal Component Analysis）**

	PCA是一种常用的数据分析方法PCA 通过线性变换将原始数据变换为一组各维度线性无关的表示，可用于提取数据的主要特征分量，常用于高维数据的降维。

	一般的，如果我们有M个N维向量，想将其转化为R个N维向量表示新的空间中，那么首先将R个基按行组成矩阵A，然后将向量按列组成矩阵B，那么两个矩阵的乘积AB就是变换的结果，其中AB的第m列为A中第m列变换后的结果。
	$$\begin{pmatrix}
	  p_1 \\
	  p_2 \\
	  \vdots \\
	  p_R
	\end{pmatrix}
	\begin{pmatrix}
	  a_1 & a_2 & \cdots & a_M
	\end{pmatrix}
	=
	\begin{pmatrix}
	  p_1a_1 & p_1a_2 & \cdots & p_1a_M \\
	  p_2a_1 & p_2a_2 & \cdots & p_2a_M \\
	  \vdots & \vdots & \ddots & \vdots \\
	  p_Ra_1 & p_Ra_2 & \cdots & p_Ra_M
	\end{pmatrix}$$
	其中$p_i$是一个行向量，表示第i个基，$a_j$是一个列向量，表示第j个原始数据。

	特别要注意的是，这里R可以小于N，而R决定了变换后数据的维数。也就是说，我们可以将一N维数据变换到更低维度的空间中去，变换后的维度取决于基的数量。因此这种矩阵相乘的表示也可以表示降维变换。

	最后，上述分析同时给矩阵相乘找到了一种物理解释：两个矩阵相乘的意义是将右边矩阵中的每一列列向量变换到左边矩阵中每一行行向量为基所表示的空间中去。更抽象的说，一个矩阵可以表示一种线性变换。

	具体的数学方法涉及到方差、协方差、矩阵对角化以及特征值和特征向量的知识，详细步骤可以参看原文

	总结一下PCA的算法步骤：

	设有m条n维数据。

	1）将原始数据按列组成n行m列矩阵X

	2）将X的每一行（代表一个属性字段）进行零均值化，即减去这一行的均值

	3）求出协方差矩阵C=1mXXTC=1mXXT

	4）求出协方差矩阵的特征值及对应的特征向量

	5）将特征向量按对应特征值大小从上到下按行排列成矩阵，取前k行组成矩阵P

	6）Y=PXY=PX即为降维到k维后的数据
（参考文章[PCA的数学原理](http://blog.codinglabs.org/articles/pca-tutorial.html)）

- 