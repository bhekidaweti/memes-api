# memes-api
This API allows you to scrape and retrieve memes from Reddit and upload your own memes. It is built using FastAPI and utilizes the PRAW library for Reddit API interaction.

# Setup
clone the repository:
git clone 
install the required dependecies:
pip install -r requiremnets.txt
Create a .env file in the root directory with the following content:
### These credencials are obtainable from reddit.com/prefs/apps and you'll need to first create a reddit account if you dont have one already
CLIENT_ID=<your-reddit-client-id> 
CLIENT_SECRET=<your-reddit-client-secret>
USER_AGENT=<your-reddit-user-agent>
# Running the Application:
uvicorn main:app --reload
Visit http://127.0.0.1:8000 in your browser to access the API documentation (Swagger UI) and explore the available endpoints.
# API Endpoints
1. Retrieve General Memes
Endpoint: /general-memes
Method: GET
Description: Retrieve a random meme from the "memes" subreddit.
Response:
Returns the meme as an image file.
2. Upload Meme
Endpoint: /memes
Method: POST
Description: Upload a meme to the "memes" collection.
Request:
Form parameter: image (file upload)
Response:
Returns the path to the uploaded meme file.
3. Welcome Message
Endpoint: /
Method: GET
Description: Displays a welcome message.
Response:
Returns a JSON response with a welcome message

# Notes
Ensure that your Reddit API credentials are correctly set in the .env file.
The application uses the PRAW library for Reddit interaction, and FastAPI for the web framework.
Uploaded memes are stored in the "memes" directory.
The API documentation provides detailed information on available endpoints and how to use them.
Feel free to explore, contribute, and have fun with memes using this API!
