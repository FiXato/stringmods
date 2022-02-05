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

# Usage:
If you want to see what a game name gets converted to, visit [your-app.herokuapp.com.example/az?game=Your game name here](https://your-app.herokuapp.com.example/az?game=Your game name here)
Or to get it as a variable name in a Streamlabs bot, use: `{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}}`

## Examples
If you want to set up per-game death counters in your Streamlabs bot, you could use the following custom commands in your bot Dashboard, while replacing `your-app.herokuapp.com.example` with your Heroku app's domain name:

### !death
`/me adjusts number of deaths while playing {channel.game} to {1}: {count cd{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}} {1}}`

### !death+
`/me increments the number of deaths while playing {channel.game}: {count cd{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}} +1}`

### !death-
`/me decreases the number of deaths while playing {channel.game} by one: {count cd{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}} -1}`

### !deathreset
`/me resets the number of deaths while playing {channel.game}: {count cd{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}} 0}`

### !deaths
`/me has witnessed {getcount cd{readapi.https://your-app.herokuapp.com.example/az?game={channel.game}}} deaths while playing {channel.game}.`

### Notes:
- Anything besides a-z, A-Z and 0-9 gets removed from the game name
- Numbers aren't allowed in variable names, so this API replaces numbers with Roman numerals
- Streamlabs bot variable names also have a certain length limit (15 IIRC), so the name needs to be shortened.
- I use a variable prefix here, 'cd', though it technically isn't necessary. It does allow you though to have multiple per-game counters, by replacing 'cd' with something else. (I picked 'cd' for 'countDeaths')
- 'The' at the start of the game name gets removed too, to reduce amount of characters
- Some names can get shortened by common abbreviations; for now this only applies to Legend of Zelda (TLoZ) and Ocarina of Time (OoT)
- `your-app.herokuapp.com.example` needs to be replaced with your Heroku app's domain name
- Probably a good idea to only make the last command, !deaths, usable by everyone, and to restrict the others to streamer and perhaps moderators.
