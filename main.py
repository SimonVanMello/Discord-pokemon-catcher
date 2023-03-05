import discord, json, asyncio

class Client(discord.Client):
    async def on_connect(self):
        pokecount: int = 0
        try:
            channel = client.get_channel(data["channel_id"])
            while True:
                await channel.send(";pokemon")
                pokecount += 1
                print(f"{pokecount} pokemon caught")
                await asyncio.sleep(60*60*3+5)
        except Exception as e:
            print(f"error : {e}")

def loadData() -> dict:
    with open("data.json") as f:
        return json.load(f)

def validData(data: dict) -> bool:
    if type(data["channel_id"]) != int:
        return False
    if not data["token"] or "." not in data["token"]:
        return False
    return True


data: dict = loadData()
if validData(data):
    client = Client()
    client.run(data["token"])
else:
    print("Invalid value in data.json")