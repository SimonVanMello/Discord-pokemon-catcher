# Discord-pokemon-catcher
Simple python script to catch pokemons on discord from [Toasty bot](https://toastybot.com)

## Install
```
git clone https://github.com/TropicoDebug/Discord-pokemon-catcher.git
cd Discord-pokemon-catcher
pip install -r requirements.txt
```
> You should install the requirements in a python venv if you already have the official discord package since they use the same name

## How to use
You can either run the bot with your main account or run it on an other account (safer).

### Using your main account
Usage is stupid simple, you just need to put your [discord token](https://www.androidauthority.com/get-discord-token-3149920/) and the [id of the channel](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) where you want to catch pokemons in data.json and then run the script.
> You can leave the owner_name field empty

### Using an alt account
If you run the bot on an alt account, you will also need to put your main discord username (example: Tropico#0112) in data.json (in the owner_name field) so that you can securely use the ```giveme command```.
> You also need to fill the 2 other fields
> If you already changed your discord username with an unique one without the 4 digits at the ends, just use your new username followed by `#0` for your username

#### Giveme command
The giveme command allows you to retreive pokemons from your alt account. You can use the command to either get a single pokemon at a time:
```
giveme pokemonName
```
or either multiple pokemons at a time by using the following format:
```
giveme pokemonName1;pokemonName2;pokemonName3
```
> You need to send the command in the channel you specified in data.json
___
PS: using selfbots is not allowed by discord and im not encouraging you to do so.
