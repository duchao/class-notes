## probabilistic generative model 概率生成模型

---

> 机器学习**三步骤**
<div  align="center"><img src="../1-Regression/imgs/1-framework-and-examples.png" alt="1.1" align="center" /></div>

---

### 0 概率回顾

在介绍概率生成模型之前，先对概率计算方法做一个回顾，如图1所示，**计算从箱子1中取出蓝色球的概率**：

<div  align="center">
<center>
<img src="imgs/0-1 概率计算回顾.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图1 gradient descent原理</p>
</center>
</div>
<br>

概率计算问题转化为分类问题：

<div  align="center">
<center>
<img src="imgs/0-2 转化为分类问题-generative model.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图2 概率计算到分类</p>
</center>
</div>
<br>

> 生成模型（二分类）: p(x) = p(x|c1)p(c1) + p(x|c2)p(c2)

其中，`p(x|c1)`，`p(c1)`，`p(x|c2)`，`p(c2)`均可通过训练样本计算得到。

### 1 生成模型计算

#### prior概率

图3展示了如何通过训练样本计算`p(c1)`，`p(c2)`：

<div  align="center">
<center>
<img src="imgs/1-1 prior概率计算.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图3 prior概率计算</p>
</center>
</div>
<br>

#### `p(x|c)`计算

在`p(x|c)`中，`c`代表了分类的类别，如二分类时的0或1，而`x`对应于输入的特征，如图4所述：

<div  align="center">
<center>
<img src="imgs/1-2 如何计算p(x|c).png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图4 输入x含义</p>
</center>
</div>
<br>

当`x`的维度很高时，会出现一个问题，如图5所示，预测样本（土黄色点）在训练集中未出现时，该如何计算其对应的概率呢？

<div  align="center">
<center>
<img src="imgs/1-3 如何估测未在训练样本中出现的样本的概率？- 高斯分布估计.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图5 新样本问题</p>
</center>
</div>
<br>

由图5可知，一种解决方案是假设数据服从高斯分布，通过训练数据预估高斯分布的参数。对于新样本，可通过参数已知高斯分布计算该样本服从该分布的概率，即得到`p(x|c)`的值。

高斯分布简介如图6所示，其核心参数为`mean`和`covariance matrix`：

<div  align="center">
<center>
<img src="imgs/1-4 高斯分布介绍.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图6 高斯分布</p>
</center>
</div>
<br>

图7解释了假设训练样本服从高斯分布的原因：**对新样本的概率进行预测**。

<div  align="center">
<center>
<img src="imgs/1-5 通过服从的高斯分布可以计算新样本的概率值-引出问题 如何计算高斯分布参数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图7 高斯分布用于新样本预测</p>
</center>
</div>
<br>

那么问题就在于如何通过这些训练数据，确定其所服从的高斯分布，即确定高斯分布的参数。
这里使用的参数估计方法为**最大似然估计**，参考[链接](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E4%BC%BC%E7%84%B6%E4%BC%B0%E8%AE%A1)，如图8所示：

> 概率分布：  
> 概率密度函数：

<div  align="center">
<center>
<img src="imgs/1-6 maximum likehood计算高斯分布参数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图8 最大似然参数估计</p>
</center>
</div>

图9是最大似然的计算过程：

<div  align="center">
<center>
<img src="imgs/1-7 计算过程-.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图9 最大似然参数计算过程</p>
</center>
</div>

在模型实际过程中，会对每个类别上的训练数据进行一次参数估计，如图10所示：

<div  align="center">
<center>
<img src="imgs/1-8 数据集上计算结果.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图10 分类别进行参数估计</p>
</center>
</div>

完成上述计算后，即可对新数据进行分类预测，如图11所示：

<div  align="center">
<center>
<img src="imgs/1-9 用于实际分类.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图11 实际分类模型</p>
</center>
</div>

分类结果如图12所示，分类准确率为47%：

<div  align="center">
<center>
<img src="imgs/1-10 实际结果研究.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图12 实际分类结果</p>
</center>
</div>

#### 模型优化

如图13所示，使两组训练数据的`covariance matrix`相同：

<div  align="center">
<center>
<img src="imgs/2-1 模型优化-减少参数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图13 模型优化思路</p>
</center>
</div>

新模型的参数估计如图14所示：

<div  align="center">
<center>
<img src="imgs/2-2 新模型计算参数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图14 新模型参数估计</p>
</center>
</div>

新模型的预测结果如图15所示，准确率提升到73%：

<div  align="center">
<center>
<img src="imgs/2-3 新模型预测结果.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图15 新模型预测结果</p>
</center>
</div>

### 2 总结

概率模型解决问题的3个步骤如图16所示：

<div  align="center">
<center>
<img src="imgs/3-1 总结-回顾模型的三个步骤.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图16 概率模型三步骤</p>
</center>
</div>

在上一节中，计算`p(x|c)`比较复杂，需要假设数据服从某一种分布，然后根据样本进行参数估计。现在考虑一种特殊情况，即假设特征间互相独立，如图17所示，那么`p(x|c)`的计算将变得很简单：

<div  align="center">
<center>
<img src="imgs/3-2 模型假设分布的讨论-不同的数据集可以假设不同的分布.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图17 概率模型三步骤</p>
</center>
</div>

此时模型称为`naive bayes分类器`，该模型在文本数据分类中用的尤其多。

下面对分类模型换个角度进行分析，如图18所示：

<div  align="center">
<center>
<img src="imgs/3-3 后验概率-引出logistics regression.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图18 后验概率深入分析</p>
</center>
</div>

经过一番理论推导过后，可得到图19所示的结论：

<div  align="center">
<center>
<img src="imgs/3-4 先求出分布的参数在求出w和b-引出如何直接求w和b的问题.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图19 结论</p>
</center>
</div>

如图19所示，在概率模型中，计算出所需参数后可得到参数`w`和`b`，那么有没有一种通过训练样本直接计算`w`和`b`呢？
