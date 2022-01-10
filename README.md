# docProcessing-webApp

## Setup
Install all the python packages required by running `pip install -r requirements.txt`. Then running `python app.py` will launch the web server at `localhost:2000`.

## File structure
```
docProcessing-webApp/
├─ server/
│  ├─ static/
│  │  ├─ style.css
│  │  ├─ index.js
│  ├─ templates/
│  │  ├─ index.html
│  ├─ __init__.py
│  ├─ settings.py
|  ├─ views.py
├─ scripts/
├─ requirements.txt
├─ app.py
├─ utils.py
```

### `server`
`Server` contains all the files for the flask server.

- `static` contains the javascript and CSS files for the web app interface.
- `templates` contains the HTML files for different URLs defined in flask views
- `settings.py` defines the configuration parameters for the flask server
- `views.py` defines views (URLs) that the server will serve upon request. This is also where the web app interacts with the algorithms. Upon receiving certain request, the function calls the algorithm in scripts relaying the parameters sent by user and returns the response back to the user.

### `scripts`
Put all your functions in this folder and import them in `views.py`.

### `app.py`
This is the entry point to the web app.