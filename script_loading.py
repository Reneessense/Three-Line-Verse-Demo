import json

def get_example(index:int, data):
    
    item = data[index]
    poem, label_1, label_2, label_3, outline, script = item
    print(f"## 诗歌内容\n\n{poem}\n\n## 剧本元素\n\n{label_1}\n{label_2}\n{label_3}\n\n## 剧本梗概\n\n{outline}")
    flag = input("是否阅读分镜？(y/n)")=='y'
    if flag:
        scripts = '\n-----\n'.join(script)
        print(f"## 分镜内容\n\n{scripts}")
        
    return poem, label_1, label_2, label_3, outline, script

def main():
    
    source_path = './generated_scripts.json'
    with open(source_path, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    
    while True:
        command = input("输入想查看的剧本序号(1-40),ctrl+c退出:")
        try:
            index = int(command)-1
            poem, label_1, label_2, label_3, outline, script = get_example(index, data)
        except:
            print("请输入1-40之间的整数")
            
if __name__=='__main__':
    main()
    