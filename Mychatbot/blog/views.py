from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from chatterbot import ChatBot
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ListTrainer

# Create and configure the chatbot instance
bot = ChatBot(
    'SmartBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch', 
            'default_response': "I'm sorry, I don't understand that yet. Can you rephrase or contact support?",
            'maximum_similarity_threshold': 0.65
        },
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    statement_comparison_function=LevenshteinDistance
)

training_data = [
    # Intro
    "Hi", "Hello! I'm your virtual assistant, here to help with anything related to telecommunications.",
    "hello", "Hi there! I'm your telecom customer support assistant.",
    "HELLO", "Hey! How can I assist you today with your telecom needs?",
    "How are you?", "I'm functioning well, thank you for asking! How can I assist you today?",
    "how are you", "I'm doing great! Ready to help you with anything you need.",
    "What's your name?", "I'm ChatBot, your smart assistant developed for customer service in the telecommunications industry.",
    "what's your name", "You can call me ChatBot. I'm here to make your life easier!",
    "What can I do?", "I can help you manage your telecom account, troubleshoot technical issues, answer billing questions, and much more. Just ask!",
    "Tell me a joke", "Why don’t scientists trust atoms? Because they make up everything! 😄",
    "Goodbye", "Take care! If you need anything else, I’ll be right here.",
    "bye", "Goodbye! Don’t hesitate to come back if you need assistance.",
    "Thanks", "You're very welcome! Let me know if there's anything else I can help with.",
    "thank you", "My pleasure! Happy to help anytime.",
    "Who created you?", "I was developed as part of a bachelor's degree graduation project in Computer Science to assist users with telecom-related support.",
    "what is Django?", "Django is a powerful and high-level web framework written in Python. It enables developers to build secure, scalable, and maintainable web applications efficiently.",

    # Account Management
    "How can I check my balance?", "You can dial *123# to check your balance or use our mobile app.",
    "I want to recharge my account.", "You can recharge using our app, website, or by dialing *100*scratchcard#.",
    "How can I view my bill?", "Log into your account on our website or mobile app to view your bill.",
    "I want to change my plan.", "You can change your plan through the app or by contacting customer support.",

    # Technical Support
    "My internet is not working.", "Please restart your phone and make sure mobile data is enabled. If the issue persists, contact technical support.",
    "I lost my SIM card.", "Visit the nearest store with a valid ID to request a new SIM card.",
    "How do I activate my SIM card?", "Insert the SIM into your phone and restart it. It should activate automatically.",

    # Roaming Support
    "How do I activate roaming?", "Roaming can be activated through our app or by dialing *200#.",
    "What are the roaming charges?", "Roaming charges depend on the country you visit. Check our website for country-specific rates.",

    # Plans and Packages
    "What internet packages do you have?", "We offer daily, weekly, and monthly data packages. You can find details in our app or website.",
    "How can I unsubscribe from a package?", "Go to the subscriptions tab in our app and click unsubscribe.",

    # Customer Service
    "How can I talk to a representative?", "You can call 121 or use the live chat feature in our app.",
    "Where is the nearest service center?", "Visit our website and use the store locator to find the nearest center.",

    # Document Support
    "Can you help me find a specific document?", "Sure! You can find documents in the ‘Documents’ section of our website or app.",
    "I need help finding a document.", "To locate a specific document, visit the 'Documents' tab on your account page.",
    "Where can I find the document I need?", "Documents are available in the 'Documents' section of your account on the website or mobile app.",
    "How can I search for a document?", "Use the search bar in the 'Documents' section of your account to find the document you're looking for.",
    "Help me find a document.", "You can access your documents via the 'Documents' tab in the app or on the website."
]


# Train the chatbot with the combined training data
list_trainer = ListTrainer(bot)
list_trainer.train(training_data)


# Views
def index(request):
    return HttpResponse("This is my first URL")

def specific(request):
    return HttpResponse("This is the specific URL")

def contact(request):
    return render(request, 'blog/contact.html')

def article(request, article_id):
    return render(request, 'blog/index.html', {
        'articleID': article_id
    })

def getResponse(request):
    # Get the user's message from the query parameter
    user_message = request.GET.get("user_message", "")
    
    # Get a response from the chatbot
    bot_reply = str(bot.get_response(user_message))
    
    # Return the response as JSON
    return JsonResponse({'response': bot_reply})

