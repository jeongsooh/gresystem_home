# build_files.sh
pip3 install urllib3==1.26.15
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput
