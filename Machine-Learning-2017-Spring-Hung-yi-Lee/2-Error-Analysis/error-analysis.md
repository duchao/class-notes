## 模型误差来源分析

---

> 机器学习**三步骤**
<div  align="center"><img src="../1-Regression/imgs/1-framework-and-examples.png" alt="1.1" align="center" /></div>

---

### 0 误差简介

误差主要体现在测试集上，用于刻画模型预测结果与实际结果的差距，其主要包括两个部分：`bias`和`variance`，分别如图1、2所示。

<div  align="center">
<center>
<img src="imgs/0-1 误差来源定义.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图1 review - 测试集上的误差</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/0-2 误差形象描述.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图2 误差的示例</p>
</center>
</div>
<br>

### 1 误差举例

将3种模型分别在100个训练集上训练，其训练结束后，结果如图3所示。
<div  align="center">
<center>
<img src="imgs/1-1-100 个模型 类似于在100个训练集上训练的结果.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图3 模型训练-一个模型对应100个训练集</p>
</center>
</div>
<br>

#### variance

图4对比了模型`y = b + w * x_cp`与模型`y = b + w_1 * x_cp + w_2 * (x_cp)^2 + w_3 * (x_cp)^3 + w_4 * (x_cp)^4 + w_5 * (x_cp)^5`的结果，得出结论： **`模型越简单，其受数据变化的影响较小，即不容易过拟合`**。

<div  align="center">
<center>
<img src="imgs/1-2 模型越简单 则受到数据集的影响越小.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图3 variance对比</p>
</center>
</div>
<br>

#### bais

`bais`的定义如图4所示，`𝐸[𝑓^∗] =𝑓^-`，反映了模型预测结果与实际结果的`距离`。

<div  align="center">
<center>
<img src="imgs/2-1 bais定义.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图4 bais定义</p>
</center>
</div>
<br>

> 图4中定义了实际结果`𝑓^-`形式。

图5为不同模型下在5000组训练集下的实验结果，注意图中蓝色与红色的含义。

<div  align="center">
<center>
<img src="imgs/2-2 多模型结果图示.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图5 bais-训练结果</p>
</center>
</div>
<br>

图6分析了模型`y = b + w * x_cp`与模型`y = b + w_1 * x_cp + w_2 * (x_cp)^2 + w_3 * (x_cp)^3 + w_4 * (x_cp)^4 + w_5 * (x_cp)^5`分别对应的`bais`，由图可知，模型越复杂，则其对应的`function space`越大，即越有可能学习到最优参数（对历史训练数据的信息捕捉能力越强），因此使得`bais`越小。

<div  align="center">
<center>
<img src="imgs/2-3 bais结论-模型复杂-则function space较大-可能包含最优结果-则bais小.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图6 bais-训练结果</p>
</center>
</div>
<br>

图7对`bais`与`variance`进行总结：

<div  align="center">
<center>
<img src="imgs/2-4 bais vs variance结论.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图7 bais vs variance</p>
</center>
</div>
<br>

> 结论： **大`bais` -> `underfit`**；**大`variance` -> `overfit`**

### 2 模型选择

#### 如何应对大`bais`

<div  align="center">
<center>
<img src="imgs/3-1 bais大时如何处理.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图8 大bais</p>
</center>
</div>
<br>

- 添加更多特征
- 使用更复杂的模型

#### 如何应对大`variance`

<div  align="center">
<center>
<img src="imgs/3-2 variance大时如何处理.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图9 大variance</p>
</center>
</div>
<br>

- 添加更多数据
- 正则化（简化模型）

#### 选择最终的线上模型

模型选择是一个bais-variance的trad-off，图10展示了一种错误的模型选择方法，即**不能根据线下测试集的结果选择模型**：

<div  align="center">
<center>
<img src="imgs/4-1 模型选择-错误选择方法.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图10 一种错误的模型选择方法</p>
</center>
</div>
<br>

正确做法如图11所示：

<div  align="center">
<center>
<img src="imgs/4-3 n-fold cv 模型选择-最后在整个数据集上进行训练模型.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图11 N-fold cross validation</p>
</center>
</div>
<br>
