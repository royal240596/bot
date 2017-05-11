
import praw
import config
import time

def bot_login():
	print "Loggin in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "boty-boop's odgovara v0.1")
	print "Logged in!"

	return r

def run_bot(r):
	print "Obtaining 25 comments..."
	for comment in r.subreddit('Test_Posts').comments(limit=25):
		if "dog" in comment.body:
			print "String with \"dog\" found in comment " + comment.id
			comment.reply("I also love dogs! [Here](http://i.imgur.com/LLgRKeq.jpg) is an image of one!")
			print "Replied to comment "

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

print "reddit"
r = bot_login()
while True:
	run_bot(r)
