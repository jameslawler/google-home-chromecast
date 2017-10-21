# google-home-chromecast
Display web content (not video / audio) to TV when asking Google Home

The idea behind this project if the following;

- A small python web server runs on a raspberry pi (which is exposed publicly)
- An IFTTT is setup to call this show-url endpoint when a trigger phrased is said
- The show-url endpoint tells the chromecast to show the url

This could be used with phrases like;

"Show me the weather" and the TV would load the weather outlook for the next week
"Show me how my shares are doing" and the TV would give a summary of your share profits
