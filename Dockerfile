# 使用 Python 3.9 作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到容器中
COPY requirements.txt .

# 安装依赖项
RUN pip install -r requirements.txt

# 将当前目录复制到容器中
COPY . .

COPY video-temp /app/video-temp
# 设置环境变量
ENV PORT=8001

# 运行 Django 服务器
CMD python manage.py runserver 0.0.0.0:$PORT --settings=Graduation_Project.settings_fake