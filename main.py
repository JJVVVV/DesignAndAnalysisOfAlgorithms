# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    with open("./data/test2.txt", 'r', encoding='utf8') as f:
        lines = f.readlines()
        lines = list(map(lambda item: (str(int(item.split()[0])+1), str(int(item.split()[1])+1)), lines))
        lines = list(map(lambda item: ' '.join(item)+'\n', lines))
        print(lines)
    with open('data/test2.txt', 'w', encoding='utf8') as f:
        f.writelines(lines)
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
