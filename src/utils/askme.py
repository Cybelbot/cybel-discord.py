"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""
from chatterbot import ChatBot
from src.utils import utils

BOTNAME = utils.BOTNAME

def askMe(question):
	chatbot = ChatBot(BOTNAME,
		logic_adapters=[
        {	
			'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. Please can you write full sentense\nExample:- I am good instead of only good',
            'maximum_similarity_threshold': 0.8,
        },
			'chatterbot.logic.MathematicalEvaluation',
		],
		preprocessors = [
			"chatterbot.preprocessors.clean_whitespace",
		],
		input_adaptor="chatterbot.input.TerminalAdaptor",
        output_adaptor="chatterbot.output.TerminalAdaptor",
		database_uri='sqlite:///database.sqlite3')
	'''
	trainer = ChatterBotCorpusTrainer(chatbot)
	trainer.train(
		"trainingData/custom",
		"trainingData/english"
		)
	'''
	bot_respose = chatbot.get_response(question)

	return bot_respose