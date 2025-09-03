# Python 属性方法 vs 实例属性详解

## 概述
这个示例展示了 Python 中 `@property` 装饰器的使用，以及属性方法（property methods）与普通实例属性的区别。

## Person 类结构

### 实例属性 (Instance Attributes)
- **`_name`**: 存储姓名的私有属性
- **`_age`**: 存储年龄的私有属性

### 属性方法 (Property Methods)
- **`name`**: 通过 `@property` 装饰器定义的 getter 方法
- **`name`**: 通过 `@name.setter` 装饰器定义的 setter 方法
- **`age`**: 通过 `@property` 装饰器定义的 getter 方法
- **`age`**: 通过 `@age.setter` 装饰器定义的 setter 方法

## 关键区别

### 1. 初始化过程
```python
def __init__(self, name, age):
    self.name = name  # 调用 name.setter 方法
    self.age = age    # 调用 age.setter 方法
```
- 在 `__init__` 中，通过属性方法赋值会触发相应的 setter 方法
- 如果直接赋值给 `_name` 和 `_age`，则不会调用 setter

### 2. 访问方式对比

#### 直接属性访问 (`_name`, `_age`)
```python
# 访问
value = person._name  # 直接获取属性值，不调用任何方法

# 赋值
person._name = "新名字"  # 直接设置属性值，不调用任何方法
```

#### 属性方法访问 (`name`, `age`)
```python
# 访问
value = person.name  # 调用 name 的 getter 方法

# 赋值
person.name = "新名字"  # 调用 name 的 setter 方法
```

### 3. 实际存储
- **只有 `_name` 和 `_age` 是真正的实例属性**，存储在对象的内存中
- **`name` 和 `age` 是方法**，不是属性，通过 `@property` 装饰器实现类似属性的访问方式

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
1. 初始化时 setter 方法的调用
2. 直接属性访问和属性方法访问的区别
3. 修改属性时 setter 方法的触发

## 总结
- **实例属性** (`_name`, `_age`): 直接存储数据，访问速度快
- **属性方法** (`name`, `age`): 通过方法实现，可以添加额外逻辑，但访问稍慢
- 选择哪种方式取决于具体需求和设计目标