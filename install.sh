#!/bin/bash

# نصب بسته‌های مورد نیاز
apt-get install -y python3-pip
apt-get install -y python3

# نصب وابستگی‌های پروژه
pip3 install -r requirements.txt

# کپی فایل‌های پروژه به محل مورد نظر
cp -r ./Garfox-mess /opt/Garfox-mess

# تنظیمات و پیکربندی دیگر (به طور مثال، تنظیمات فایل‌های پیکربندی)

# ساخت لینک نمادین برای اجرای برنامه
ln -s /opt/Garfox-mess/GM.py /usr/local/bin/myapp

python3 /opt/Garfox-mess/GM.py

echo "Install Done"
