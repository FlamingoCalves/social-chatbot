#Designing the gradio site
custom_css = """
/* Chat container */
body, html, .gradio-container {
    height: 100%;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

/* Message bubbles */
.message {
    position: relative;
    padding: 10px 20px;
    border-radius: 25px;
    margin-bottom: 10px;
    line-height: 1.4;
    max-width: 60%;
}

/* User messages */
.user-message {
    background-color: #0B93F6;
    color: white;
    align-self: flex-end;
}

/* Assistant messages */
.assistant-message {
    background-color: #E5E5EA;
    color: black;
    align-self: flex-start;
}

/* Message text */
.message-text {
    margin: 0;
}

/* Progress bar and level */
.progress-bar {
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Input box styling to resemble iMessage */
input[type='text'] {
    border: none;
    padding: 10px 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    width: calc(100% - 40px); /* Adjust width based on padding */
}

/* Submit button styling */
button {
    background-color: #0B93F6;
    border: none;
    padding: 10px 20px;
    border-radius: 18px;
    color: white;
    font-weight: bold;
    margin-left: 10px;
}

/* Override Gradio styles */
.gradio-toolbar, .gradio-appbar {
    display: none;
}

/* Container for the chat */
.chat-container {
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    padding: 20px;
    gap: 10px;
    flex-grow: 1;
}

/* Progress bar and level */
.progress-bar {
    margin-top: 20px;
    margin-bottom: 20px;
    color: white; /* Set the text color to white for visibility */
}

/* Inside of the progress bar */
.progress-bar div {
    color: white; /* Ensure text inside the bar is visible */
    text-align: center; /* Center the text inside the bar */
    line-height: 20px; /* Center the text vertically */
    font-weight: bold; /* Make the text bold */
}

/* Ensure the text is visible against the background */
.progress-bar-text {
    position: absolute;
    width: 100%;
    text-align: center;
}

/* Progress bar outer container */
.progress-bar-outer {
    background-color: lightgrey;
    border-radius: 10px;
    padding: 3px;
    position: relative;
}

/* Filled part of the progress bar */
.progress-bar-inner {
    background-color: #0B93F6;
    height: 20px;
    border-radius: 7px;
    transition: width 0.5s; /* Smooth transition for the bar animation */
}

/* Centered text over the progress bar */
.progress-bar-text {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
}
"""