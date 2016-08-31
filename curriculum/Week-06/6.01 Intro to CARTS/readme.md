# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Classification and Regression Trees (CARTs)
## By Patrick D. Smith

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 mins | [Opening](#opening) | Opening |
| 45 min | [Introduction](#introduction) | Intro to Classification and Regression Trees |
| 10 mins | [Discussion](#discussion) | Discussion: The ID3 Algorithm for decision trees |
| 10 mins | [Guided-practice](#guided-practice) | Guided Practice: Decision trees pros and cons |
| 10 mins | [Ind-practice](#ind-practice) | Independent Practice: Decision trees as a service |
| 5 mins | [Conclusion](#conclusion) | Conclusion |

<a name="opening"></a>
## Opening 

Last week we, we started getting into some of the meat of data science. This week, we're going to learn about tree and ensemble methods, and it all starts with it's most basic algorithm - the decision tree - otherwise known as the classification and regression tre. 

These are very powerful machine learning tools that allow us to solve complex problems in a very performant way. Also, they are easy to visualize and communicate, making them extremely powerful in a context where other (non-technical) stakeholders are involved.

<a name="introduction"></a>
## Intro to Decision Trees 

### The Intuition of Decision Trees

Decisions trees are similar to the game 20 questions. They make predictions by answering a series of questions, most often yes or no questions. What we typically want is the smallest set of questions to get to the right answer. We want each question to reduce our search space as much as possible.

Trees are a data structure made up of nodes and branches. Each node typically has two (or more) branches that connect it to it's children. Each child is another node in the tree and contains it's own subtree. Nodes without any children are known as leaf nodes.

A decision tree contains a question at every node. Depending on the answer to that question, we will proceed down the left or right branch of the tree and ask another question. Once we don't have any more questions at the leaf nodes, we make a prediction.

It's important to note the next question we ask is always dependent on the last. We'll see how this sets decision trees apart from previous models. For example, suppose we want to predict if an article is a news article. We may start by asking: does it mention a President?

- If it does, it must be a news article
- If not, let's ask another question - does the article contain other political figures?
- If not, does the article contain references to political topics?
- Etc

### Comparison to Previous Models

Decision trees have an advantage over logistic regression by being non-linear. A linear model is one in which a change in an input variable has a constant change on the output variable.

An example of this difference is the relationship between years of education and salary. We know that as education increases, salary should as well. A linear model would say this effect is constant. As your years of education goes from 10 to 15 years or 15 to 20 years, the corresponding increase in salary would be about the same. A non-linear model allows us to change the effect depending on the input. For instance, with a non-linear model you could show how the relationship of education to salary changes dramatically from 0-15 years, but neglibly from years 15-20.

Additionally, trees automatically contain interactions of features. Since each question is dependent on the last, the features are naturally interacting.






### What a Decision Tree is
_Decision trees_ are a _non-parametric hierarchical_ classification technique.

- **_non-parametric_** means that the model is not described in terms of parameters like for example Logistic Regression. It also means that there is no underlying assumption on the distribution of data and of the error. In a sense this makes _DT_ agnostic to the data.
- **_hierarchical_** means that the model consists of a sequence of questions which yield a class label when applied to any record. In other words, once trained, the model behaves like a recipe, which will tell us a result if followed exactly.

Consider the following example. Suppose I have a dataset of weather data, with 3 features: Outlook, Humidity, Wind, and a binary target variable which indicates if I should play golf on that day or not, depending on the weather. I could build a hierarchical tree of decisions like this one:

![golf-tree](./assets/images/golf-tree.png)

The tree gives me a precise rule to make a decision depending on the values assumed by the features.

**Check:** According to this tree, should I play golf in a day where:
- Outlook = Sunny
- Humidity = High
- Wind = Strong

Let's learn a little vocabulary. The tree is a case of _Directed Acyclical Graph (DAG)_, and as such it has _Nodes_ and _Edges_. Nodes correspond to questions or decisions, while edges correspond to possible answers to a given question.

DAG is simply a complicated way of saying: 
- **D**irected: The connections between the graph's nodes have a direction
- **A**crylic: AKA "non-cicular," we move in one direction and never encounter a single node twice
- **G**raph: A structure consisting of nodes 


The top node is also called _root node_ it has 0 incoming edges, and 2+ outgoing edges. Internal nodes test a condition on a specific feature. They have 1 incoming edge, and 2+ outgoing edges. Finally a leaf node contains a class label (or a regression value). It has 1 incoming edge and 0 outgoing edges.

### How to build a decision tree

In order to build a decision tree we need an algorithm that is capable of determining optimal choices for each node. One such algorithm is _Hunt's algorithm_: a _greedy recursive_ algorithm that leads to a _local optimum_.

- _greedy_: algorithm makes locally optimal decision at each step
- _recursive_: splits task into subtasks, solves each the same way
- _local optimum_: solution for a given neighborhood of points

The algorithm works by recursively partitioning records into smaller and smaller subsets. Like all data science techniques, we need to quantify this segregation. We can do so with any of the following metrics:

- [Classification Error]
- [Entropy]
- Gini

Each of these measures the purity of the separation. The partitioning decision is made at each node according to a metric called _purity_. A node is said to be 100% pure when all of its records belong to a single class (or have the same value).

Classification error asks: what percent are positive in each group? The lowest error would be a separation that has 100% positive in one group and 0% in the other (completely separating news stories from non-news stories.)

When training, we want to choose the question that gives us the best change in our purity measure. Given our current set of data points (articles), you could ask: what question will make the largest change in purity? We'll come back to this concept in a bit. 

At each training step, we take our current set and choose the best feature to split (in other words, the best question to ask) based on information gain. After splitting, we then have two new groups. This process is next repeated recursively for each of those two groups.

### Visual Example of a Decision Tree

Let's build a sample tree for our evergreen prediction problem from last week. Assume our features are:

Whether the article contains a recipe
The image ratio
The html ratio

First, we want to choose the feature the gives us the highest purity. In this case, we choose the recipe feature.

![](./assets/single-node-tree.png)

Then, we take each side of the tree and repeat the process, choosing the feature that best splits the remaining samples.

![](./assets/depth-2-tree.png)

As you can see the best feature is different on both sides of this tree, which shows the interaction of features. If the article does not contain 'recipe', then we care about the image_ratio, but otherwise we don't.

We can continue that process until we have asked as many questions as we want or until our leaf nodes are completely pure.

###Multi-Way Splits

![multi-way](./assets/images/multi-way.png)

###Continuous Measure Descisions

![Continuous-features](./assets/images/Continuous-features.png)

### Making Predictions from a Decision Tree

Predictions are made in the decision tree from answering each of the questions. Once we reach a leaf node, our prediction is made by taking the majority label of the training samples that fulfill the questions. If there are 10 training samples that match our new sample, and 6 are positive, we will predict positive since 6/10 (60%) are positive.

In the sample tree, if we want to classify a new article, we can proceed by first asking - does the article contain the word recipe? If it doesn't, we can check: does the article have a lot of images? If it does, 630 / 943 articles are evergreen - so we can assign a 0.67 probability for evergreen sites.

<a name="reprise"></a>
## Decision Trees part 2 

**Check:** What is overfitting? Why do we want to avoid it?
> Answer: Overfitting occurs when a statistical model describes random error or noise instead of the underlying relationship. Overfitting generally occurs when a model is excessively complex, such as having too many parameters relative to the number of observations. A model that has been overfit will generally have poor predictive performance, as it can exaggerate minor fluctuations in the data.

### Preventing overfitting

Decision trees tend to be weak models because they can memorize or overfit to a dataset. Remember, a model is overfit when it instead of picking up on general trends in the data, it memorizes or bends to a few specific examples. If we simply memorized each article and it's classification, our model would overfit. This is like using every word in every article as a feature.

Recall that the **stopping criterion** determines when to no longer construct further nodes.

We can stop when all records belong to the same class, or when all records have the same attributes. This maximizes variance at the expense of bias, leading to overfitting.

**Subtree replacement:** One possible way to prevent overfitting is **pre-pruning**, which involves setting a minimum threshold on the gain, and stopping when no split achieves a gain above this threshold. It is difficult to calibrate in practice.

**Subtree raising:** Alternatively we can build the full tree and then perform pruning as a post-processing step. To prune a tree, the nodes are examinde from the bottom-up and pieces of the tree are simplified according to some criteria. Complicated subtrees can be replaced either with a single node or with a simpler (child) subtree.

### Decision tree regression

In the case of regression, the outcome variable is not a category but a continuous value. We cannot therefore use the same measure of purity we used for classification. Instead we will use the following variation of the algorithm:

At each node calculate the variance of the data points at that node, then choose the split that generates the largest decrease in total variance for the children nodes. In other words we use variance as our measure of impurity and we want to maximize the decrease of total variance at each split.

In a regression tree the idea is this: since the target variable does not have classes, we fit a regression model to the target variable using each of the independent variables. Then for each independent variable, the data is split at several split points. At each split point, the "error" between the predicted value and the actual values is squared to get a sum of squared errors (SSE). The split point errors across the variables are compared and the variable/point yielding the lowest SSE is chosen as the root node/split point. This process is recursively continued.

<a name="guided-practice"></a>
## CART Advantages and Disadvantages

### CART Advantages

- Simple to understand and interpret. People are able to understand decision tree models after a brief explanation.
- Useful to work with non technical departments (marketing/sales).
- Requires little data preparation.
- Other techniques often require data normalization, dummy variables need to be created and blank values to be removed.
- Able to handle both numerical and categorical data.
    - Other techniques are usually specialized in analyzing datasets that have only one type of variable.
- Uses a white box model.
    - If a given situation is observable in a model the explanation for the condition is easily explained by boolean logic.
    - By contrast, in a black box model, the explanation for the results is typically difficult to understand, for example in neural networks.
- Possible to validate a model using statistical tests. That makes it possible to account for the reliability of the model.
- Robust. Performs well even if its assumptions are somewhat violated by the true model from which the data were generated.
- Performs well with large datasets. Large amounts of data can be analyzed using standard computing resources in reasonable time.
- Once trained can be implemented on hardware and has extremely fast execution.
    - Real-time applications like trading, for example.


### CART Disadvantages

- Locally-optimal
    - Practical decision-tree learning algorithms are based on heuristics such as the greedy algorithm where locally-optimal decisions are made at each node.
    - Such algorithms cannot guarantee to return the globally-optimal decision tree.
- Overfitting
    - Decision-tree learners can create over-complex trees that do not generalize well from the training data.
- There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems. In such cases, the decision tree becomes prohibitively large.
    - **Neural networks**, for example, are superior for these problems.
- Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.


<a name="ind-practice"></a>
## Independent Practice: Decision trees as a service 

There are several companies that offer decision trees as service. Two famous ones are BigML and WiseIO. Let's split the class in 2. One half will look at BigML case studies and the other half will look at WiseIO case studies.

- [BigML](https://bigml.com/gallery/models)
- [WiseIO](http://www.wise.io/resources)

Review a few of them with your team mates and choose one that you find particularly interesting. Then present it to the other group.

<a name="conclusion"></a>
## Conclusion 

In this class we learned about Classification and Regression trees. We learned how Hunt's algorithm helps us recursively partition our data and how impurity gain is useful for determining optimal splits.
We've also reviewed the pros and cons of decision trees and industry
applications. In the next class we will learn to use them in `Scikit-learn`.

### ADDITIONAL RESOURCES

- [Decision trees on wikipedia](https://en.wikipedia.org/wiki/Decision_tree_learning)
- [Decision tree regression explained](http://www.saedsayad.com/decision_tree_reg.htm)
