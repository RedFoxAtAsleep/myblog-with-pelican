source venv/bin/activate  # 激活环境
pelican content  # pelican命令 content文件夹路径
ghp-import output -b gh-pages  # output文件夹路径 gh-pages分支
git push origin gh-pages