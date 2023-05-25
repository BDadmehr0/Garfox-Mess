#!/bin/bash

# نصب بسته‌های مورد نیاز
apt-get install -y python3-pip

# نصب وابستگی‌های پروژه
pip3 install -r requirements.txt

# کپی فایل‌های پروژه به محل مورد نظر
cp -r /path/to/project /opt/myproject

# تنظیمات و پیکربندی دیگر (به طور مثال، تنظیمات فایل‌های پیکربندی)

# ساخت لینک نمادین برای اجرای برنامه
ln -s /opt/myproject/myapp.py /usr/local/bin/myapp

echo "Install Done"
