import os
from taskmanager import app


#  telling app where and how to run app. If it's a match
# taking 3 arguments
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=os.environ.get("DEBUG")
    )