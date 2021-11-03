# TikTok Tracking Exposed

TikTok tracking exposed (tktrex) is a browser extension built on NodeJS, that collects data from TikTok and store it in a MongoDB for data analysis purposes.

## About this branch: Dev

This branch is experimental and is used to test new features. Use at your own risk.

## Installing the tktrex-extension

1) Clone this repo and install the required NodeJS dependencies:

```
git clone https://github.com/tracking-exposed/tktrex.git
cd tktrex/extension
npm install
```

2) Build the extension in development mode:
```
npm run build
```

3) Load the extension into Google Chrome:

Go to address `chrome://extensions/`, click on "load unpacked" and select the folder "tktrex/extension/build"

## Setting up the tktrex-backend

At the moment the data collected are stored on a local MongoDB, make sure you have installed it to the latest version.

1) Install the NodeJS dependencies for the backend:

```
cd tktrex/backend
npm install
```

2) Run the development server:
```
npm run watch
```


4) Start your mongodb and navigate to tiktok. You should see receive some feedback about the data collected in the dev tool console.

## MongoDB schema
By default the database is set to be reachable at mongodb://localhost:27017/tktrex

The db properties can be changed in backend/config/settings.json

### DBs
There are 4 different databases:

- admin
- config
- local
- tktrex

### Collections

- local/startup_log: contains info regarding the starting of the mongodb such as *startTime*
- tktrex/htmls: holds the htmls snippets of the extracted content, alongside with some of the metadata
- tktrex/metadata
- tktrex/supporters

##