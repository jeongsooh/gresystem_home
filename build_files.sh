# build_files.sh
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements in venv..."
pip install --upgrade pip
pip install urllib3==1.26.15
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput
