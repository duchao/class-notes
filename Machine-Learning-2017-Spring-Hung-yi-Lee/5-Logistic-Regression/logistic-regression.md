### logistic regression

---

> 机器学习**三步骤**
<div  align="center"><img src="../1-Regression/imgs/1-framework-and-examples.png" alt="1.1" align="center" /></div>

---

### 0 步骤一：define a set of functions

模型定义如图1所示，其可视化展示如图2所示：

<div  align="center">
<center>
<img src="imgs/0-1 logistic regression问题定义.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图1 logistic regression模型定义</p>
</center>
</div>
<br>


<div  align="center">
<center>
<img src="imgs/0-2 问题可视化展示.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图2 可视化展示</p>
</center>
</div>
<br>

### 1 步骤二：goodness of function

完成模型定以后，下面需要将模型具体化，即寻找最优参数（此模型中的参数为`w`和`b`）。
与生成模型的思路类似，先假设训练数据服从某种分布，然后对该分布进行参数估计，过程描述如图3所示：

<div  align="center">
<center>
<img src="imgs/1-1 假设空间.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图3 过程描述</p>
</center>
</div>
<br>

> 由图3可知，目标函数为`w^*, b^* = arg max L(w, b)`。

上述目标函数是多个函数连乘，在优化时不易计算（求一阶导麻烦），因此可通过取对数将其转化为连加，如图4所示：

<div  align="center">
<center>
<img src="imgs/1-2 似然-将连乘问题变为连加问题.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图4 问题转换</p>
</center>
</div>
<br>

> 目标函数转为`w^*, b^* = arg min - ln(L(w, b))`。
> 为什么需要取负数？ 因为`L(w, b)`是一个小于1的数，因此`ln(L(w, b))  < 0`，所以在表达式中添加`-`，同时对表达式求`min`。

对目标函数深入分析，如图5所示：

<div  align="center">
<center>
<img src="imgs/1-3 总结目标函数-cross entropy 用于评价两个分布的相似程度.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图5 目标函数深入分析</p>
</center>
</div>
<br>

将`ln(L(w, b))`展开后进行变换，可得`cross entropy`公式。`cross entropy`是一种用于衡量概率分布间相似度的量，在机器学习领域经常使用。  
在`logistics regression`模型中，将`cross entropy`作为其代价函数，如图6所示：

<div  align="center">
<center>
<img src="imgs/1-4 cross entropy minimize的对象.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图6 代价函数</p>
</center>
</div>
<br>

> `cross entropy`与`logloss`的区别？

### 2 步骤三：find the best function

分别对代价函数进行求一阶导（计算梯度），如图7和图8所示：

<div  align="center">
<center>
<img src="imgs/2-1 求导1.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图7 代价函数求导-1</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/2-2 求导2.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图8 代价函数求导-2</p>
</center>
</div>
<br>

最后将两部分的求导结果进行合并，并按照梯度下降法进行参数的迭代进化，如图9所示：

<div  align="center">
<center>
<img src="imgs/2-3 合并-梯度更新.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图9 代价函数求导合并</p>
</center>
</div>
<br>

最后对`logistic regression`与`linear regression`进行比较，如图10所示：

<div  align="center">
<center>
<img src="imgs/2-4 logistic regression与linear regression的区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图10 模型间的比较</p>
</center>
</div>
<br>

可知，两种模型的建模及迭代方法相同，主要不同点在于假设空间定义以及代价函数。下面，将解释为什么`logistic regression`的代价函数为什么不能是`square loss`。

### 3 代价函数比较

假设`logistic regression`模型的代价函数为`square loss`，则模型的迭代步骤如图11、图12所示：

<div  align="center">
<center>
<img src="imgs/3-1 为什么不能使用square loss作为损失函数1.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图11 使用square loss-1</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/3-2 为什么不能使用square loss作为损失函数2.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图12 使用square loss-2</p>
</center>
</div>
<br>

可知，梯度值恒为0，即无法进行参数迭代，其可视化结果如图13所示：

<div  align="center">
<center>
<img src="imgs/3-3 cross entropy与square loss的区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图13 使用square loss-2</p>
</center>
</div>
<br>

### 4 Discriminative v.s. Generative

图14总结了`Discriminative`与`Generative`两种模型间的参数估计过程：

<div  align="center">
<center>
<img src="imgs/4-1 Discriminative v.s. Generative的计算过程区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图14 使`Discriminative`与`Generative`模型比较</p>
</center>
</div>
<br>

两种模型的预测结果如图15所示，可知，`Discriminative`模型的预测结果稍好：

<div  align="center">
<center>
<img src="imgs/4-1-1 Discriminative v.s. Generative的计算结果.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图15 使`Discriminative`与`Generative`模型预测结果比较</p>
</center>
</div>
<br>

图16展示了一种类别不平衡时的预测问题：

<div  align="center">
<center>
<img src="imgs/4-2 类别不均衡时generative model的计算过程.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图16 Generative模型处理类别不平衡问题</p>
</center>
</div>
<br>

而`Discriminative`模型在处理类别不平衡问题时，需要对训练数据进行采样。

图17对`Discriminative`与`Generative`模型进行比较，`Discriminative`模型的预测结果一般比`Generative`模型要好，而`Generative`模型主要有两个优势：**允许使用更少的训练数据**和**对数据中噪声鲁棒性较好**。

<div  align="center">
<center>
<img src="imgs/4-3 generative model的优势-数据量少时-噪声大时.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图17 `Discriminative`与`Generative`模型比较结论</p>
</center>
</div>
<br>

### 5 多分类问题

以上讨论均为二分类问题，多分类问题的分析过程也类似，只不过最后再添加一个`softmax`层，如图18所示：

<div  align="center">
<center>
<img src="imgs/5-1 多目标分类定义-softmax函数.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图18 softmax</p>
</center>
</div>
<br>

图19是一个多分类问题示例：

<div  align="center">
<center>
<img src="imgs/5-2 多分类模型实例.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图19 多分类问题示例</p>
</center>
</div>
<br>

### 6 `logistic regression`模型的局限性

图20模拟了一种场景，此时`logistic regression`模型无法将其正确分类：

<div  align="center">
<center>
<img src="imgs/6-1 logistic regression的局限.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图20 不能正确分类的场景</p>
</center>
</div>
<br>

此时，为了提高模型预测的准确率，有两种途径进行改良，1）寻找更多的特征或在原始特征上进行特征组合变换；2）使用新模型。 

图21展示了一种特征变换方法，进行特征变换后，该问题可通过`logistic regression`模型进行解决。需要注意的是，特征变换需要大量的领域知识。

<div  align="center">
<center>
<img src="imgs/6-2 特征转换的意义.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图21 特征变换</p>
</center>
</div>
<br>

图22从新模型的角度出发，将两个`logistic regression`模型进行叠加：

<div  align="center">
<center>
<img src="imgs/6-3 logistic模型叠加.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图22 模型叠加</p>
</center>
</div>
<br>

可知，特征变换不再需要领域知识，而是通过模型叠加实现，其计算过程如图23、24所示：

<div  align="center">
<center>
<img src="imgs/66-4 初始化w后计算结果.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图23 参数初始化</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/6-5 转化后问题变得线性可分.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图24 模型叠加后分类结果</p>
</center>
</div>
<br>

而模型的叠加，参数共同学习的思路正是深度学习（神经网络）的思路，如图25所示：

<div  align="center">
<center>
<img src="imgs/6-6 引出深度学习.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图25 logistics regression 到 deep learning</p>
</center>
</div>
<br>
