import subprocess
from db_config import mysql_config

user_name = mysql_config['user']
password = mysql_config['password']
host = mysql_config['host']
port = mysql_config['port']
database = mysql_config['database']

# 替换为实际的数据库连接信息
output_file = "models.py"
# ... existing code ...
db_url = f'mysql+pymysql://{user_name}:{password}@{host}:{port}/{database}'
print(f"Generated DB URL: {db_url}")
# ... existing code ...

try:
    result = subprocess.run(['sqlacodegen', db_url], capture_output=True, text=True, check=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result.stdout)
    print(f"模型文件已成功保存为 {output_file} (UTF-8 编码)")
except subprocess.CalledProcessError as e:
    print(f"执行 sqlacodegen 时出错: {e.stderr}")
except Exception as e:
    print(f"发生未知错误: {e}")