import tweepy
import schedule
import time
from datetime import datetime, timedelta

# Replace these values with your own API keys from the Twitter Developer Account
BEARER_TOKEN = "your-bearer-token"
API_KEY = "your-api-key"
API_SECRET = "your-api-secret"
ACCESS_TOKEN = "your-access-token"
ACCESS_SECRET = "your-access-secret"

# Authenticate to the API using the v2 client
def authenticate_twitter_app_v2():
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET
    )
    return client

# Function to post a tweet using v2 API
def post_tweet_v2(content):
    client = authenticate_twitter_app_v2()
    try:
        client.create_tweet(text=content)  # Use the v2 endpoint for posting a tweet
        print(f"Successfully posted: {content}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# Function to schedule a tweet at a specific time
def schedule_tweet(post_content, post_datetime):
    # Calculate the delay until the post time
    now = datetime.now()
    delay = (post_datetime - now).total_seconds()
    
    if delay > 0:
        # Schedule the tweet at the right time
        schedule.every(delay).seconds.do(post_tweet_v2, post_content)
        print(f"Scheduled tweet: '{post_content}' for {post_datetime}")
    else:
        print(f"Cannot schedule tweet: '{post_content}' for past time {post_datetime}")

# Function to generate love post content
def generate_love_content(index):
    love_messages = [
        "Love is not about how many days, months, or years you’ve been together. It's about how much you love each other every day.",
        "Love is that condition in which the happiness of another person is essential to your own.",
        "The best thing to hold onto in life is each other, for love grows with time.",
        "To love and be loved is to feel the sun shining from both sides.",
        "In the end, we discover that to love and to let go can be the same thing.",
        "Where there is love, there is life, and where life exists, so does hope.",
        "Love doesn’t sit still like a stone; it must be made and remade over time.",
        "True love is not about perfection but in embracing each other's flaws.",
        "Love is the bridge that connects two hearts, no matter the distance.",
        "To love deeply in one direction makes us more loving in all others.",
        "Love is the silent whisper that echoes loudly in the hearts of those who truly care.",
        "In love, every moment feels like eternity, and eternity seems too short to express it all.",
        "Love gives us the strength to hold on and the courage to let go.",
        "With love, even the smallest gestures carry the most profound meaning.",
        "The journey of love is a lifetime’s adventure filled with endless moments of wonder.",
        "The beauty of love is found in its simplicity, not in grandeur or complexity.",
        "In the arms of love, we find safety from the storms of life.",
        "Love is the language that transcends words, heard clearly through the heart.",
        "A heart filled with love is never lonely, for love is a constant companion.",
        "Love transforms the ordinary into the extraordinary.",
        "The beauty of love is that it is infinite, growing more radiant as time passes.",
        "When love is real, time stands still in the moments shared together.",
        "Love is the melody that plays softly in the background of life’s most precious moments.",
        "In love, it’s not about the destination but the journey you take together.",
        "Love is the greatest adventure, one without a map but with endless discoveries.",
        "Through love, we find not only each other but also ourselves.",
        "The magic of love is felt in the moments of silence when words are unnecessary.",
        "In love, every day is a new opportunity to rediscover each other.",
        "Love is not measured by the length of time but by the depth of connection.",
        "A true love story never ends; it merely evolves as time moves forward.",
        "Love is the quiet understanding between two souls, often unspoken but always felt.",
        "To love someone is to see the face of God in their smile.",
        "Love is the compass that guides us through life’s most uncertain paths.",
        "In love, we find our truest and most vulnerable selves, unmasked and unafraid.",
        "Love is like the wind, you can’t see it but you can feel it with every breath.",
        "To love is to recognize yourself in another, without fear or doubt.",
        "True love is never easy, but it's always worth the journey.",
        "Love paints life’s canvas with the brightest and most beautiful colors.",
        "In love, even the smallest touch can mean the world.",
        "Through love, life becomes more vibrant, and even the ordinary becomes extraordinary.",
        "Love is the warmth that melts away the coldness of the world.",
        "In the garden of life, love is the flower that blooms eternally.",
        "Love is a light that never fades, even in the darkest of times.",
        "A love shared is a love that grows, expanding beyond borders and boundaries.",
        "Love is the invisible thread that binds us all, connecting hearts across time and space.",
        "To love is to open your heart to the possibility of the unimaginable.",
        "Love is the greatest gift you can give, and the greatest you can receive.",
        "In love, time and space dissolve, leaving only the present moment, shared between two hearts."
    ]
    return love_messages[index % len(love_messages)]

# Starting date and time
start_time = datetime(2024, 9, 15, 16, 5)

# Generate 50 posts
posts = []
for i in range(50):
    post_content = generate_love_content(i)
    post_time = start_time + timedelta(minutes=i)
    post = (post_content, post_time.strftime("%Y-%m-%d"), post_time.strftime("%H:%M"))
    posts.append(post)

# Schedule each tweet
for post in posts:
    content, post_date, post_time = post
    post_datetime = datetime.strptime(f"{post_date} {post_time}", "%Y-%m-%d %H:%M")
    schedule_tweet(content, post_datetime)

# Keep the program running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
