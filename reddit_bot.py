
import praw
import config
import time

def bot_login():
	
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "boty-boop's odgovara v0.1")

	return r

def run_bot(r):
	print("Obtaining 25 comments...")
	
	print "Sleeping for 10 seconds..."
	try:
		[comment.reply("I also love dogs! [Here](http://i.imgur.com/LLgRKeq.jpg) is an image of one!") for comment in r.subreddit('Test_Posts').comments(limit=25) if "dog" in comment.body]

	except:
		exception('Cannot comment!')
			
	time.sleep(10)


r = bot_login()
while True:
	run_bot(r)
