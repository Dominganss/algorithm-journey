import os
import re

# 你存放代码的文件夹列表（以后加了新分类，就在这里填上名字）
CODE_DIRS = ['Sliding_Window', 'Hash_Table'] 
NOTES_DIR = 'Notes' # 统一存放笔记的文件夹

def extract_and_sync():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
        
    for category in CODE_DIRS:
        if not os.path.exists(category):
            continue
            
        # 准备生成针对这个分类的 Markdown 笔记文件
        note_file_path = os.path.join(NOTES_DIR, f"{category}_笔记.md")
        compiled_notes = f"# 📚 {category} 核心复盘笔记\n\n"
        
        # 遍历该分类下的所有 Python 文件
        for filename in sorted(os.listdir(category)):
            if not filename.endswith('.py'):
                continue
                
            filepath = os.path.join(category, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 使用正则寻找我们约定的暗号："""@THOUGHTS ... """
                match = re.search(r'"""@THOUGHTS(.*?)"""', content, re.DOTALL)
                if match:
                    thoughts = match.group(1).strip()
                    compiled_notes += f"##  来源文件：`{filename}`\n"
                    compiled_notes += f"{thoughts}\n\n---\n\n"
                    
        # 将提取到的笔记写入专门的 Markdown 文件
        with open(note_file_path, 'w', encoding='utf-8') as f:
            f.write(compiled_notes)
            
    print("✅ 魔法完成！所有思考记录已自动同步到 /Notes 文件夹！")

if __name__ == '__main__':
    extract_and_sync()
