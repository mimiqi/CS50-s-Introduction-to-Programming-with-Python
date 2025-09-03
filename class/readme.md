# Python 属性方法 vs 实例属性详解

## 概述
这个示例展示了 Python 中 `@property` 装饰器的使用，以及属性方法（property methods）与普通实例属性的区别。同时演示了类继承中属性方法的使用。

## 类结构

### Person 类

#### 实例属性 (Instance Attributes)
- **`_name`**: 存储姓名的私有属性
- **`_age`**: 存储年龄的私有属性

#### 属性方法 (Property Methods)
- **`name`**: 通过 `@property` 装饰器定义的 getter 方法
- **`name`**: 通过 `@name.setter` 装饰器定义的 setter 方法
- **`age`**: 通过 `@property` 装饰器定义的 getter 方法
- **`age`**: 通过 `@age.setter` 装饰器定义的 setter 方法

#### 其他方法
- **`__init__(self, name, age)`**: 构造函数
- **`__str__(self)`**: 字符串表示方法

### Student 类 (继承自 Person)

#### 新增实例属性
- **`_subject`**: 存储学科的私有属性

#### 新增属性方法
- **`subject`**: 通过 `@property` 装饰器定义的 getter 方法
- **`subject`**: 通过 `@subject.setter` 装饰器定义的 setter 方法

#### 重写的方法
- **`__init__(self, name, age, subject)`**: 扩展的构造函数，调用父类构造函数
- **`__str__(self)`**: 重写的字符串表示方法，包含学科信息

## 关键概念

### 1. 初始化过程

#### Person 类初始化
```python
def __init__(self, name, age):
    self.name = name  # 调用 name.setter 方法
    self.age = age    # 调用 age.setter 方法
```

#### Student 类初始化（继承）
```python
def __init__(self, name, age, subject):
    super().__init__(name, age)  # 调用父类构造函数
    self.subject = subject       # 调用 subject.setter 方法
```

**重要说明：**
- 在 `__init__` 中，通过属性方法赋值会触发相应的 setter 方法
- 如果直接赋值给 `_name`、`_age` 或 `_subject`，则不会调用 setter
- 子类构造函数中调用 `super().__init__()` 会触发父类的 setter 方法

### 2. 访问方式对比

#### 直接属性访问 (`_name`, `_age`, `_subject`)
```python
# 访问
value = person._name     # 直接获取属性值，不调用任何方法
value = student._subject # 直接获取属性值，不调用任何方法

# 赋值
person._name = "新名字"     # 直接设置属性值，不调用任何方法
student._subject = "物理"   # 直接设置属性值，不调用任何方法
```

#### 属性方法访问 (`name`, `age`, `subject`)
```python
# 访问
value = person.name      # 调用 name 的 getter 方法
value = student.subject  # 调用 subject 的 getter 方法

# 赋值
person.name = "新名字"     # 调用 name 的 setter 方法
student.subject = "物理"   # 调用 subject 的 setter 方法
```

### 3. 实际存储
- **只有 `_name`、`_age` 和 `_subject` 是真正的实例属性**，存储在对象的内存中
- **`name`、`age` 和 `subject` 是方法**，不是属性，通过 `@property` 装饰器实现类似属性的访问方式

### 4. `__str__` 方法的重要性
```python
def __str__(self):
    return f"Name: {self.name}, Age: {self.age}"  # 正确：返回字符串

# 错误示例：
def __str__(self):
    print(f"Name: {self.name}, Age: {self.age}")  # 错误：返回 None
```

**关键点：**
- `__str__` 方法必须**返回**字符串，而不是**打印**字符串
- 当使用 `print(object)` 时，Python 会调用对象的 `__str__` 方法
- 如果 `__str__` 返回 `None`，会导致 `TypeError`

## 使用建议

### 何时使用属性方法
- 需要在赋值时进行验证或处理
- 需要计算属性值
- 需要控制属性的访问权限
- 需要保持向后兼容性

### 何时使用直接属性
- 简单的数据存储
- 不需要额外处理的情况
- 性能要求较高的场景

## 示例输出
运行 `class.py` 会看到：

### Person 对象创建
```
name.setter is called
age.setter is called
Person John 20 is created
Name: John, Age: 20
```

### Student 对象创建
```
name.setter is called
age.setter is called
subject.setter is called
Student Jane 21 Math is created
Name: Jane, Age: 21, Subject: Math
```

**输出说明：**
1. 初始化时 setter 方法的调用顺序
2. 继承关系中父类和子类构造函数的执行
3. 属性方法在继承中的工作方式
4. `__str__` 方法的正确使用

## 继承中的属性方法

### 继承的优势
- 子类可以继承父类的所有属性方法
- 子类可以添加新的属性方法
- 子类可以重写父类的方法（如 `__str__`）

### 最佳实践
- 在子类构造函数中使用 `super().__init__()` 调用父类构造函数
- 重写 `__str__` 方法时，确保返回字符串而不是打印
- 保持属性方法的一致性（getter 和 setter 配对）

## 总结
- **实例属性** (`_name`, `_age`, `_subject`): 直接存储数据，访问速度快
- **属性方法** (`name`, `age`, `subject`): 通过方法实现，可以添加额外逻辑，但访问稍慢
- **继承**: 允许子类扩展父类功能，同时保持代码复用
- **`__str__` 方法**: 必须返回字符串，用于对象的字符串表示
- 选择哪种方式取决于具体需求和设计目标