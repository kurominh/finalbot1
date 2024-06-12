import discord 
from discord.ext import commands
import os 
import random 
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv
load_dotenv() 
intents = discord.Intents.default()
intents.message_content = True 
intents.messages = True 

ip_address = ec2_metadata.public_ipv4 or ec2_metadata.private_ipv4
region = ec2_metadata.region
availability_zone = ec2_metadata.availability_zone
  
client = commands.Bot(command_prefix ="!", intents=intents)

@client.command() 
async def ping(ctx): 
  await ctx.send('Pong!')

token = os.getenv('TOKEN')

@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))
    print(f'Your EC2 data are as follow: Ip Address: {ip_address}, Region: {region}, Availability Zone: {availability_zone}')

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
  
    if channel == "bottest": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}') 
        elif user_message.lower() == "tell me a joke": 
            jokes = [1,2,3] 
            await message.channel.send(random.choice(jokes)) 
        elif user_message.lower() == "tell me about my server!":
            await message.channel.send(f'Your EC2 data are as follow: Ip Address: {ip_address}, Region: {region}, Availability Zone: {availability_zone}')
    await client.process_commands(message)
client.run(token)  