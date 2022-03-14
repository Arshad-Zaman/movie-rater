# Installation instructions:
- In terminal do the things below:
    - Clone repo using `git clone git@github.com:csc4350-sp22/milestone3-azaman3.git`
    - Go into directory `cd milestone3-azaman3`
    - Make a .env file and place `DATABASE_URL="" SECRET_KEY="" TMDB_API_KEY=""`
    - Go into project directory `cd project`
    - Get the node modules `npm ci`

# Run from localhost:5000:
- In terminal do the things below:
    - Set flask env variable using `export FLASK_APP=__init__.py`
    - Enable debug mode `export FLASK_DEBUG=1`
    - Run app using `npm run build` and `flask run` (use second command after build is done). You might have to sign up and login and post a review if you haven't to see something load onto the review page. Or login as cherubini.

# Technical Problems
1. I had issues rendering the react page from the ./static/react. The errorcode I got was no such template review / review.html. I spend a lot of time looking on google and youtube, but nothing really helped. I called up my friend who uses React a lot and we both tried to fix it. While he explained the folder structure of React, I realized the issue was that ./static/react doesn't exist because I built on the root level not the project level.The issue was my project setting. My app.py equivalent is inside the project folder so I had rebuild using `npm ci` on the project folder.
2. The next issue was sending json data to the React page using flask. It gave me an error that it expect tuple, array, or string but list was sent. I googled that error and it said that using flask_marshmallow helps. So I youtube'd "flask sqlalchemy send table data" and I got a video that was using flask_marshmallow and marshmallow_sqlalchemy. It was an older video so I got an error which said "ma doesn't have an attribute RelationalSchema" so I looked at the latest docs and changed it to the new equivalent ([https://flask-marshmallow.readthedocs.io/en/latest/](latest flask_marshmallow docs)).
3. Final technical issue I had was the save all the updated data to the database. The issue stemmed from my understanding of what data I recieved to the flask route and also rushing to implement a solution. I took a break and came back, I jotted down my thought process on a .txt file and then I typed the type of data I was using on the notepad. I figured out the type of data I was using by plugging in print statements around my recieve_data route.

# Hardest part and learning experience
The hardest part probably was working with React. I felt like the 2 classes on React wasn't sufficient for this project. I watched a lot of youtube videos to figure out how to use useState and useEffect hooks. I couldn't figure out how to change a comment while it is being mapped. I also didn't know much about the file structure of react but that wasn't an issue after I worked with my friend to solve technical problem #1. I learned the most while following along with different tutorials on youtube and also some while reading stackexchange articles on useState and useEffect. I guess what I learned start as early as possible when using new technologies and ask plenty of questions after a reasonable amount of effort to reduce time wasted. But through struggling I learned a lot about working with json data.