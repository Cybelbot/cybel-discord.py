import random
import requests
import discord


def _sendEmbed(title, description, name, value, url):
    """ Send Discord Embed """
    embed = discord.Embed(title=title, description=description)
    embed.add_field(name=name, value=value)
    embed.set_image(url=url)
    return embed


def _getGitUserData(username):
    """ Function to get GitHUb User Data in json format """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        userData = response.json()
        return userData


def _getIfscDetails(ifscCode):
    """ Function to fetch Bank details by IFSC number """
    url = f"https://ifsc.razorpay.com/{ifscCode}"
    response = requests.get(url)
    if response.status_code == 200:
        bankData = response.json()
        return bankData


def _UrlShortner(website):
    """ function to shorten url using cleanuri """
    data = {'url': website}
    response = requests.post('https://cleanuri.com/api/v1/shorten', data=data)
    if response.status_code == 200:
        shortUrl = response.json()['result_url']
        return shortUrl


def _getRandomDogPicture():
    """ function to fetch random dog picture """
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()

        fileSize = result['fileSizeBytes']
        print(fileSize)
        dogImageUrl = result['url']

        embed = _sendEmbed(title="Random Dog image",
                           description=f"File Size: {fileSize}",
                           name="CYBEL BoT",
                           value=f"ImageURL: {dogImageUrl}",
                           url=dogImageUrl)
        return embed


def _getRandomCatPicture():
    """ function to fetch random cat pictures """
    url = "https://thatcopy.pw/catapi/rest/"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()

        catPictureURL = result["url"]
        embed = _sendEmbed(title="Random Cat image",
                           description=f"File Size: Unknown",
                           name="CYBEL BoT",
                           value=f"ImageURL: {catPictureURL}",
                           url=catPictureURL)
        return embed


def _getRanomJoke():
    """ function to fetch random joke """
    try:
        randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
        response = requests.get(randomJokeURL)
        if response.status_code == 200:
            randomJoke = response.json()['joke']
            return randomJoke
        else:
            return response.status_code
    except Exception as error:
        return error


def _getRandomFact():
    """ function to fetch random fact """
    try:
        randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
        response = requests.get(randomFactURL)
        if response.status_code == 200:
            randomFact = response.json()['text']
            return randomFact
        else:
            return response.status_code
    except Exception as error:
        return error


def _getRandomQuote():
    """ function to fetch random quote """
    try:
        randomQuoteURL = 'https://zenquotes.io/api/random'
        response = requests.get(randomQuoteURL)
        if response.status_code == 200:
            randomQuote = f'{response.json()[0]["q"]} -**{response.json()[0]["a"]}**'
            return randomQuote
        else:
            return response.status_code
    except Exception as error:
        return error


def _rollTheDice(dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        return 'Format has to be in NdN!'

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    return result