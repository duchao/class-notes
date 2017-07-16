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

图7解释了假设训练样本服从高斯分布的原因：对新样本的概率进行预测。

<div  align="center">
<center>
<img src="imgs/1-5 通过服从的高斯分布可以计算新样本的概率值-引出问题 如何计算高斯分布参数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图7 高斯分布用于新样本预测</p>
</center>
</div>
<br>

