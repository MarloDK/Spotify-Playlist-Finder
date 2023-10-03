
# Playlist Finder

A web app that allows musicians to search for playlists on Spotify with an email in the playlist description to make music marketing easier.


## Installation
*Note, this is a very early version of the project, so installing the project won't be required in the future.*


First of all, make sure you have both NodeJS and Python installed on your system. If you don't have them downloaded, you can do so with the links below.

https://nodejs.org/en/download/current

https://www.python.org/downloads/

#### Once you have them installed, you're ready to install the project!
To get started, download the repository on your local machine. You can do so by clicking the download icon in the top right of this page, or by using Git.

#### Git
```bash
    git clone https://github.com/MarloDK/Spotify-Playlist-Finder
```


After downloading the project, install the required packages for NodeJS and Python.
```bash
    npm install
    pip install -r requirements.txt
```
When all the packages are installed, you can go ahead and run the API handler and the web server.


Next, you need an API Key from Spotify.


### Getting a Spotify API Key

#### Creating the Spotify API App
Once you have installed the application using the guide above, you're ready to get your Spotify API keys. To do so, head over to https://developer.spotify.com/ and log in to your Spotify account.

Once logged in, you should see this page: ![Spotify Developer Dashboard](<Github Readme/Untitled-1.PNG>)

Next, click the 'Create App' button. On this page, fill out the fields 'App name' and 'App description'. Spotify also wants a redirect URL. For now, just go ahead and set that as `https://github.com/`.

Now, the submission form should look something like this:
![[Spotify App Creation Example](<Github Readme/Spotify App Creation.PNG>)

Go ahead and agree to the terms of service, and click the 'Create app' button.

#### Getting the Client ID and Client Secret
To get the Client ID and Client Secret, go ahead and click settings button in the top right of the screen. Now, click the 'View client secret' button below the Client ID field in the top left.

Now that we have the Client ID and Client Secret, all you have to do is create a .env file in the same folder as the project files you downloaded earlier.

To do so, head to the file location you downloaded the project. Next, create a new file by right clicking and choose make a new text file. Open this file, and type in the  following:
```
    CLIENT_ID="[Your Client ID]"
    CLIENT_SECRET="[Insert your Client Secret here]"
```
Go ahead and replace both `[Your Client ID]` and `[Your Client Secret]` with your Client ID and Client Secret respectfully.  

After you've done so, it should look something like this:
```
    CLIENT_ID="yi0T4Etbe5rZKZr04mle2bJCUrIgMY6h"
    CLIENT_SECRET="xNJ6RXvxy7BqrwqjhsCMfIPjNix8drzD"
```

#### Now you're all set!
To start up the web server and API handler, type in these two commands in their own respective consoles.

To start the web server, use the following command:
```bash
    nodemon server.js
```
To start the API handler, use the following command:
```bash
    python request_handler.js
```

Once both the web server and the API handler are up and running, head to http://localhost:8080/ to open the web app.
# How to use
Once you've gotten access to the web server, you can type in a keyword in the search bar and click search to find playlists with the keyword in the title. The application will now look through 1000 different Spotify playlists with that keyword in the title, and return the ones that have an email in the description, as well as:
* A link to the playlist
* The name of the playlist
* The owner of the playlist
* The amount of songs are on the playlist
* The amount of followers the playlist has

This process might take a while as making 1000 API calls takes a bit of time since the application doesn't have priority in the incoming API calls to Spotify. So be patient, playlists will appear a little while after starting the search.

Another important thing to mention is that if you make enough searches, you might end up being rate limited by Spotify and will have to wait a couple of hours before using the application again.

*Sometimes the API will send an empty object and crash the API server, the issue will be resolved soon!*
## Roadmap

- Add exceptions and error messages on web page, as well as handle empty API returns instead of the API server just throwing an error.

- Improve the speed of the application to show results faster.

- Add social media contact support, which links directly to the social media account run by the playlist curator.

- Save found playlists in a database to greatly improve search time.

- Clean up the file structure and code.

- Run the whole application on a website, so users don't have to download the project and get their own API keys.


## Authors

- [@MarloDK / Marcus](https://www.github.com/MarloDK)

