# Space Instagram

The program provides you possibility to automatic download space-thematics photos and publish this to your [instagram](https://www.instagram.com) -account.
Program consist of these independent modules:
- `fetch_spacex.py` - download collection of photos with last [spacex](https://www.spacex.com/)- launch  
- `fetch_hubble.py` - download collection of photos made by [Hubble Space Telescope](https://www.nasa.gov/mission_pages/hubble/main/index.html)
- `instagram_publish.py` - publish downloaded images to your [instagram](https://www.instagram.com) -account. 

### How to install

bit.ly wouldn't provide you data, until you get access-token. It needs to communicate with API Bitly. All you need - is:

- Create account in the instagram, or use existing
- Remember your login and password
- Create file `.env` in the script directory
- Add the following records to the `.env-file`:
  - INST_LOGIN="Your instagram login"
  - INST_PASSWD="Your instagram password"
- Decide where you'd like to store downloaded photos. By default, script will create `image` -folder in the script-root directory.
  You must have read and write permissions to this folder. 


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).