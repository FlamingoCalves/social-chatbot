import re

# Define a simple leveling system
level_thresholds = [0, 100, 250, 450, 700, 1000]  #TODO: Add more thresholds as needed

# Calculate user's current level and progress towards the next level
def calculate_level(score):
    level = 0
    while level < len(level_thresholds) - 1 and score >= level_thresholds[level + 1]:
        level += 1
    points_for_next_level = level_thresholds[level + 1] if level < len(level_thresholds) - 1 else None
    points_in_current_level = score - level_thresholds[level]
    return level, points_in_current_level, points_for_next_level

# Progress bar HTML generator
def generate_progress_bar(level, points, points_for_next_level):
    progress_percentage = (points / (points_for_next_level - level_thresholds[level])) * 100 if points_for_next_level else 100
    progress_bar_html = f"""
    <div class="progress-bar-outer" style="background-color: lightgrey; border-radius: 10px; padding: 3px; position: relative;">
        <div class="progress-bar-inner" style="background-color: #0B93F6; height: 20px; width: {progress_percentage}%; border-radius: 7px;"></div>
        <div class="progress-bar-text" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: center;">
            Level {level} - {points}/{points_for_next_level if points_for_next_level else 'Max Level'}
        </div>
    </div>
    """
    return progress_bar_html

# Implement logic to extract feedback and score from the reply
def extract_feedback_and_score(reply):
    parts = reply.split("Score:")
    response = parts[0].strip()
    feedback_match = re.search(r'Score: (\d+\/100)(.*)', reply, re.DOTALL)
    if feedback_match:
        score = feedback_match.group(1)
        feedback = feedback_match.group(2).strip()
        return response, feedback, score
    return '', ''

# Extract the feedback score from the reply using a regex or string parsing
def parse_feedback_score(reply):
    match = re.search(r'Score: (\d+)/100', reply)
    if match:
        return int(match.group(1))
    else:
        return 0  # Default score if not found or if the reply does not contain a score
