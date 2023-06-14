import discord, json, asyncio, re

class Client(discord.Client):
    async def on_connect(self: object):
        pokecount: int = 0
        try:
            while True:
                await self.get_channel(data["channel_id"]).send(";pokemon")
                pokecount += 1
                print(f"{pokecount} pokemon caught")
                await asyncio.sleep(60*60*3+3)
        except Exception as e:
            print(f"error : {e}")

    async def on_message(self: object, message: object):
        async def sendPokemon(channel: object, message: object, pokemon: str):
            try:
                await channel.send(f";give {message.author.mention} {pokemon}")
                await asyncio.sleep(1)
                await channel.send("yes")
                await asyncio.sleep(1)
            except Exception as e:
                print(f"error : {e}")

        # only proceed the message if it starts with "giveme"
        if not str(message.content).startswith("giveme"):
            return
        # check if the owner name is set in data.json
        if not data["owner_name"]:
            return
        # check if the message author is the one specified in data.json ()
        if str(message.author) != data["owner_name"]:
            return
        # check if the message was sent in the channel specified in data.json
        if message.channel.id != data["channel_id"]:
            return
        
        # tranform the message into a list of pokemons
        pokemons = str(message.content)[6:].split(";")
        
        # give each pokemon of the list to the owner set in data.json
        for pokemon in pokemons:
            await sendPokemon(self.get_channel(data["channel_id"]), message, pokemon)


def loadData() -> dict:
    with open("data.json") as f:
        return json.load(f)

def validData(data: dict) -> bool:
    if type(data["channel_id"]) == str:
        try:
            data["channel_id"] = int(data["channel_id"])
        except Exception as e:
            return False
    if type(data["channel_id"]) != int:
        return False
    if not data["bot_token"]:
        return False
    if len(data["bot_token"].split(".")) != 3:
        return False
    if data["owner_name"] and not re.search("^.{3,32}#[0-9]{1,4}$", data["owner_name"]):
        return False
    return True


data: dict = loadData()
if validData(data):
    client = Client()
    client.run(data["bot_token"])
else:
    print("Invalid value in data.json")
