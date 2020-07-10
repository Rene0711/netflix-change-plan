# netflix-change-plan

netflix-change-plan is a simple Python script that logs into your netflix account to change your plan to premium and back to basic.

## Installation

```
pip install -r requirements.txt
```

### Google Chrome

Check for existing Google Chrome:

```
google-chrome --version
```

Downloading Google Chrome:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Installing Google Chrome:

```
sudo apt install ./google-chrome-stable_current_amd64.deb
```

### ChromeDriver

Check for existing ChromeDriver:

```
chromedriver --version
```

Copy the latest version of chromedriver_linux64.zip for your current Google Chrome version.

```
https://sites.google.com/a/chromium.org/chromedriver/downloads
```

Example installation of ChromeDriver 83.0.4103.39 for Google Chrome version 83:

```
wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo mv chromedriver /usr/bin/
rm chromedriver_linux64.zip
```

## Usage

```
python netflix-change-plan.py -u USERNAME -p PASSWORD
```

Options:

```
usage: netflix-change-plan.py -u USERNAME -p PASSWORD

optional arguments:
  -h, --help            show this help message and exit
  -s SECONDS, --sleep SECONDS
                        Pause time between plan change

required arguments:
  -u USERNAME, --username USERNAME
                        Your netflix email adress or phone number
  -p PASSWORD, --password PASSWORD
                        Your netflix password
```

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
