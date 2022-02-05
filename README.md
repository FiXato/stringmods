# stringmods
a very simple web API for converting (Twitch) game name into a shorter variable name that can be used for streamlabs counters

# Deployment:
1. Create a new app on Heroku
2. Be sure you are logged in via the Heroku-cli: `heroku login`
3. Clone the repo and add a remote for your Heroku app:
```
git clone https://github.com/FiXato/stringmods.git
cd stringmods
heroku git:remote -a your-app-name
```
4. Push code: `git push heroku main`
