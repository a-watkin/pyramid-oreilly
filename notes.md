# Install package from setup.py

`pip install -e .`

## Using a `requirments.txt` file
`pip install -e . -r requirements.txt`

# waitress install

For some reason waitress would not install until installing from `requiremnets.txt`

# Live reloading - restarts the application on changes

`pserve development.ini --reload`

# Pyramid tries the most exact matching view first

If you have multiple views, it wil match based on HTTP method.

You can even have a view that triggers only when a certain button is pressed in a template.

