# API Tools Plugin

The API Tools Plugin enables beta to communicate with APIs.

## Key Features:
- Supports GET, POST, PUT, DELETE, PATCH, HEAD and OPTIONS
- Tries to recover from strange values being used as parameters
- Accepts custom header values

## Installation:
As part of the beta plugins package, follow the [installation instructions](https://github.com/coozila/beta-plugins) on the beta-plugins GitHub reporistory README page.

## beta Configuration
Set `ALLOWLISTED_PLUGINS=BetaApiTools,example-plugin1,example-plugin2,etc` in your beta `.env` file.
