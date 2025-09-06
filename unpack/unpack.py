list1 = [1, 2, 3, 4]

dict1 = {"name": "Littorio", "nation": "Italy"}

def f1(a, b, c, d):
    print(f"You entered {a} {b} {c} {d} in func f") 

def f2(name, nation):
    print(f"Hello {name} from {nation}")

def f3(*args):
    print(args)

def f4(**kwargs):
    print(kwargs)

def f5(*args, **kwargs):
    print(args, "These are args.")
    print(kwargs, "These are kwargs.")

def f6(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

def main():
    print("=== 原始调用 ===")
    f1(*list1)
    f2(**dict1)
    f3(list1)
    f4(**dict1)
    f5([1, 3, 5, 7, 9], {"name": "Veneto", "nation": "Italy"})
    
    print("\n=== 正确的调用方式 ===")
    # 方式1：使用关键字参数
    f5(1, 3, 5, 7, 9, name="Veneto", nation="Italy")
    
    # 方式2：解包字典
    f5(1, 3, 5, 7, 9, **{"name": "Veneto", "nation": "Italy"})
    
    # 方式3：混合使用
    f5(*[1, 3, 5, 7, 9], name="Veneto", nation="Italy")

if __name__ == "__main__":
    main()
