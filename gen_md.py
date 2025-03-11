import os

# 设定要扫描的目录
ROOT_DIR = "CS"
OUTPUT_FILE = "README.md"


def generate_md_structure(root_dir):
    md_content = "# 目录结构\n\n"
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = "  " * level
        # 添加目录
        if root == root_dir:
            md_content += f"- {os.path.basename(root)}/\n"
        else:
            md_content += f"{indent}- {os.path.basename(root)}/\n"

        # 添加文件（使用 Markdown 链接格式）
        for f in files:
            file_path = os.path.join(root, f).replace("\\", "/")  # 兼容 Windows 和 Linux
            relative_path = os.path.relpath(file_path, root_dir).replace("\\", "/")
            md_content += f"{indent}  - [{f}]({relative_path})\n"

    return md_content


# 生成 Markdown 并写入文件
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(generate_md_structure(ROOT_DIR))

print(f"Markdown 目录已生成: {OUTPUT_FILE}")
