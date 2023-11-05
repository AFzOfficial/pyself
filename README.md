# Pyself - Telegram Self Bot

Pyself is a Telegram Cli bot you can manage your account and have a series of cool features such as:  
- Time on the profile  
- Changing the profile picture and writing the time on the profile picture  
- Keep the account online forever  
- Download photos and videos that have a time limit

and other cool features.  

### Technologies
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) 

## How to Run?
### Clone the project
```bash
git clone https://github.com/AFzOfficial/pyself.git

cd pyself
```

### Setup env
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install Depends
```bash
pip install -r requirements.txt
```
### Setup your config.ini
```
cp config.ini.example config.ini
```
### Run
```bash
# Start a tmux session for keep bot running
tmux

python3 main.py
```