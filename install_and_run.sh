echo "Starting installation..."

echo "Setting up Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r dev-requirements.txt

echo "Starting Streamlit application..."
python -m streamlit run computer_use_demo/streamlit.py
