from openai import OpenAI
import re
from utils import calculate_level, generate_progress_bar, extract_feedback_and_score, parse_feedback_score
from config import API_KEY

client = OpenAI(api_key=API_KEY)

#Setting up the chatbot
messages = [{"role": "system",
             "content": """You are a social chatbot that responds to the user exactly
              like a human would, and also provides helpful social feedback to the user after it responds. 
              The name of the chatbot is Alex, and it is pretending to be a human in order to simulate a real 
              human interaction for the user. The goal of the chatbot is to help people with social anxiety and autism 
              learn how to engage and communicate with people better. Additionally, please provide a score (out of 100) 
              for each thing that the user says based on how socially skilled the user's interaction was. And always format it like this: "Score: X/100" Also, if the 
              score is below 90, please give the user an example of a better way to say what they said that would give 
              them a score higher than 90."""}]


# Global variable to store conversation history
conversation_history = []
# Global variable to store the user's total score
user_total_score = 0
# Global variable to store the number of interactions
user_interactions_count = 0


def CustomChatGPT(user_input):
    global conversation_history
    global user_total_score
    global user_interactions_count
    messages.append({"role": "user", "content": user_input})
    conversation_history.append({'role': 'user', 'content': user_input})
    response = client.chat.completions.create(model="gpt-4-1106-preview",
    messages=messages)
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Extract feedback and score from the response
    text_message, feedback, score = extract_feedback_and_score(ChatGPT_reply)

    conversation_history.append({'role': 'assistant', 'content': f"Score: {score}"})
    conversation_history.append({'role': 'assistant', 'content': text_message})
    conversation_history.append({'role': 'assistant', 'content': feedback})
    feedback_score = parse_feedback_score(ChatGPT_reply)
    user_total_score += feedback_score
    user_interactions_count += 1
    average_score = user_total_score / user_interactions_count if user_interactions_count else 0
    # Format the conversation history as HTML with chat bubbles
    formatted_history = ""
    for entry in conversation_history:
        bubble_class = "user-message" if entry["role"] == "user" else "assistant-message"
        formatted_history += f"<div class='message {bubble_class}'><p class='message-text'>{entry['content']}</p></div>"
    #formatted_history = "\n".join([f"{entry['role'].title()}: {entry['content']}" for entry in conversation_history])
    
    # Calculate the current level and progress
    level, points_in_current_level, points_for_next_level = calculate_level(user_total_score)

    # Generate the progress bar HTML
    progress_bar_html = generate_progress_bar(level, points_in_current_level, points_for_next_level)

    # Combine the chat bubbles and the progress bar
    full_html_output = f"<div class='chat-container'>{formatted_history}</div><div class='progress-bar'>{progress_bar_html}</div>"
    return ChatGPT_reply, full_html_output