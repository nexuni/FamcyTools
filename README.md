# FAMCY Tools Documentation
Famcy is an Automatic Management Console for You (FAMCY). It is designed for Nexuni Management Console development. It is based in Flask framework and contains various useful plugins for backend management and user dashboard actions. This repository contains tools to initialize and configure famcy environment. 

## Installation
1. 在本機 安裝 famcytools (pip3 install famcytools)
2. 裝完之後輸入 famcy init {PROJECT_NAME} (e.g. famcy init pms)
3. 輸入之後經過一系列等待，可能會有warning不要理他，就會在 ~/.local/share/famcy/{PROJECT_NAME} 裡面產生 console, venv, logs
4. 這時候你可以先把template console裡面的東西都覆蓋掉，新增你自己的application repo
5. 確認好之後就跑famcy deploy {PROJECT_NAME} (e.g. famcy deploy pms)
6. 這時候會輸出類似下面的cli輸出
```
== Copy the following part and setup system service == (Need to change path if necessary)

[Unit]
Description=uWSGI instance to serve famcy
After=network.target

[Service]
User=minc
Group=www-data
WorkingDirectory=/home/minc/.local/share/famcy/pms/venv/lib/python3.7/site-packages/Famcy
Environment="PATH=/home/minc/.local/share/famcy/pms/venv/bin"
ExecStart=/home/minc/.local/share/famcy/pms/venv/bin/uwsgi --ini famcy.ini --lazy

[Install]
WantedBy=multi-user.target


== Copy the following part to nginx configurations == (Need to change alias path if necessary)

location / {
	include uwsgi_params;
	uwsgi_pass unix:/tmp/pms.sock;
}

location /static  {
    alias /home/minc/.local/share/famcy/pms/venv/lib/python3.7/site-packages/Famcy/static;
}

Deployed to wsgi
```
7. 自己要新增一個system service把上面的範例copy進去，照理來講是直接copy就能用但還是稍微看一下路徑
8. 自己要新增nginx configuration 把輸出的範例copy進去
9. nginx configuration最好要是主路徑（也可以試試看後面加個subpath但我沒試過），所以你可能要自己產生一個新的server name -> 建立DNS
10. 最後一步要修改/etc/nginx/nginx.conf第一行的user, 要從www-data改成本機 user name
11. 然後全部好了systemctl 重啟你設的service就可以用了
------------
未來要更新famcy
1. famcy upgrade {PROJECT_NAME}
2. famcy deploy {PROJECT_NAME}
3. 完成