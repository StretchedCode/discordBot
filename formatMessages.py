import discord

def createEmbed(data):
    name = data["data"][0]["titles"][0]["title"]
    embedImg = data["data"][0]["images"]["jpg"]["image_url"]
    description = data["data"][0]["synopsis"]
    sourceMaterial = data["data"][0]["source"]
    typeOfMedia = data["data"][0]["type"]
    status = data["data"][0]["status"]
    epNum = data["data"][0]["episodes"]
    genres = []

    for obj in data["data"][0]["genres"]:
        genres.append(obj["name"])

    genreString = f"Genres: " + (" | ".join(genres)) + f"\nStatus: {status}\t Episodes: {epNum}"
    materialString = f"Source Material: {sourceMaterial}\nType Of Media: {typeOfMedia}"

    newEmbed = discord.Embed(title=name, color=discord.Colour.from_rgb(219, 172, 52), description=description)
    newEmbed.set_image(url=embedImg)
    newEmbed.set_footer(text=genreString)
    newEmbed.set_author(name=materialString)

    return newEmbed

def createPersonalList(data, user: str):

    desc = ""
    title = f"{user.name}'s favourite shows."
    
    for x in range(len(data)):
        desc += f"{x}. {data[x]}\n"
    
    personalListEmbed = discord.Embed(title=title, color=discord.Colour.from_rgb(255,182,193), description=desc)

    return personalListEmbed