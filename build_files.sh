# build_files.sh
pip3 install urllib3==1.26.15 --break-system-packages
pip3 install -r requirements.txt --break-system-packages
python3 manage.py collectstatic --noinput
