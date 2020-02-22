## APRG Assignment Guidelines 

### 1. HackerRank Account Creation

If you haven't created an account yet, you need to create a new account in HackerRank using your CMI email ID. Once you have created an account, **change the username to your CMI Roll No.** . You can change it in the setting tab which is located in the top right corner. 

### 2. Online Judges 

Since your assignments will be automatically checked against a fixed output, you need to adhere to the output specifications mentioned in the respective problems. Specifically, **do not** prompt any messages while reading input (i.e. `input("enter a number")`) .

### 3. Python3 I/O

All the examples are provided for python3. 

#### a) Reading a list

```
123 33 21 58 9
```

```python
li = list(map(int, input().split()))
```

#### b) Reading a matrix

```
3
1 2 3
4 5 6
7 8 9
```

```python
n = int(input())
matrix = []
for i in range(n):
	matrix.append(list(map(int, input().split())))
```

#### c) Printing a list

```python
print(' '.join(map(str, li)))
```

#### d)  Reading basic data types

```python
a = input() # this reads the entire line as a string
b = int(input()) # this converts the input string to an integer
c = float(input()) 
```

### 4). Basic python tutorials 

If you want some practice for basic python syntax you can try out these problems in [hackerrank](https://www.hackerrank.com/domains/python)