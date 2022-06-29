tmux kill-server
cd johns-portfolio-mlh
git fetch && git reset origin/main --hard
dnf install tmux
tmux new
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
flask run --host=0.0.0.0
