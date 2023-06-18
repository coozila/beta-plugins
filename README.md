# beta-plugins

> ⚠️💀 **WARNING** 💀⚠️:
> Always examine the code of any plugin you use thoroughly, as plugins can execute any Python code, leading to potential malicious activities such as stealing your API keys.

> ⚙️ **WORK IN PROGRESS** ⚙️:
> The plugin API is still being refined. If you are developing a plugin, expect changes in the upcoming versions.

## Installation

**_⚠️This is a work in progress⚠️_**

Here are the steps to configure beta Plugins:

1. **Install beta**

   If you haven't done so, follow the installation instructions given by [beta](https://github.com/coozila/beta) to install it.

1. **Download the plugins folder from the `root` of `beta` directory**

    To download it directly from your beta directory, you can run this command on Linux or MacOS:

    ```bash
    curl -L -o ./plugins/beta-plugins.zip https://github.com/coozila/beta-plugins/archive/refs/heads/master.zip
    ```

    Or in PowerShell:

    ```pwsh
    Invoke-WebRequest -Uri "https://github.com/coozila/beta-plugins/archive/refs/heads/master.zip"     -OutFile "./plugins/beta-plugins.zip"
    ```

1. **Execute the dependency install script for plugins**

    This can be run via:

    Linux or MacOS:

    ```bash
    ./run.sh --install-plugin-deps
    ```

   Windows:

    ```pwsh
   .\run.bat --install-plugin-deps
    ```

    Or directly via the CLI:

    ```bash
    python -m beta --install-plugin-deps
    ````

## Plugins

> For interactionless use, set `ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3` in your `.env`

There are two categories of plugins: **first party** and **third party**. First-party plugins are included in this repo and are installed by default when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for widely-used plugins, and third-party for your specific needs. **You can view all the plugins and their contributors on this [directory](https://autoplugins.vercel.app/).**

If you've built a plugin and it's not listed in the directory, you can make a PR to this [repo](https://github.com/dylanintech/autoplugins) by adding your plugin to the `data` array in `plugins.tsx`.

You can also see the plugins here:

| Plugin       | Description     | Location |
|--------------|-----------|--------|
| Astro Info   | This gives beta info about astronauts.                                                           | [beta_plugins/astro](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/astro)           |
| API Tools        | This allows beta to make API calls of various kinds.                                                           | [beta_plugins/api_tools](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/api_tools)           |
| Baidu Search |  This search plugin integrates Baidu search engines into beta. | [beta_plugins/baidu_search](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/baidu_search)|
| Bing Search      | This search plugin integrates Bing search engines into beta.                                                  | [beta_plugins/bing_search](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/bing_search)       |
| Bluesky | Enables beta to retrieve posts from Bluesky and create new posts. | [beta_plugins/bluesky](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/bluesky)|
| Email            | Revolutionize email management with the beta Email Plugin, leveraging AI to automate drafting and intelligent replies. | [beta_plugins/email](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/email)                 |
| News Search      | This search plugin integrates News Articles searches, using the NewsAPI aggregator into beta.                 | [beta_plugins/news_search](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/news_search)   |
| Planner          | Simple Task Planner Module for beta  | [beta_plugins/planner](https://github.com/coozila/beta-plugins/blob/master/src/beta_plugins/planner/) |
| Random Values    | Enable beta to generate various random numbers and strings.                                                    | [beta_plugins/random_values](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/random_values) |
| SceneX           | Explore image storytelling beyond pixels with the beta SceneX Plugin.                                        | [beta_plugins/scenex](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/scenex)               |
| Telegram |  A smoothly working Telegram bot that gives you all the messages you would normally get through the Terminal. | [beta_plugins/telegram](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/telegram) |
| Twitter          | beta is capable of retrieving Twitter posts and other related content by accessing the Twitter platform via the v1.1 API using Tweepy.               | [beta_plugins/twitter](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/twitter)           |
| Wikipedia Search | This allows beta to use Wikipedia directly.                                                                    | [beta_plugins/wikipedia_search](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/wikipedia_search) |
| WolframBeta Search | This allows beta to use WolframBeta directly.                                                                                         | [beta_plugins/wolframbeta_search](https://github.com/coozila/beta-plugins/tree/master/src/beta_plugins/wolframbeta_search)|

Some third-party plugins have been created by contributors that are not included in this repository. For more information about these plugins, please visit their respective GitHub pages.

| Plugin       | Description     | Repository |
|--------------|-----------------|-------------|
| Alpaca-Trading | Trade stocks and crypto, paper or live with beta | [danikhan632/beta-AlpacaTrader-Plugin](https://github.com/danikhan632/beta-AlpacaTrader-Plugin)|
| beta User Input Request | Allow beta to specifically request user input in continous mode | [HFrovinJensen/beta-User-Input-Plugin](https://github.com/HFrovinJensen/beta-User-Input-Plugin)|
| BingAI | Enable beta to fetch information via BingAI, saving time, API requests while maintaining accuracy. This does not remove the need for OpenAI API keys | [gravelBridge/beta-BingAI](https://github.com/gravelBridge/beta-BingAI)|
| Crypto | Trade crypto with beta | [isaiahbjork/beta-Crypto-Plugin](https://github.com/isaiahbjork/beta-Crypto-Plugin)|
| Discord | Interact with your beta instance through Discord | [gravelBridge/beta-Discord](https://github.com/gravelBridge/beta-Discord)|
| Dolly beta Cloner | A way to compose & run multiple beta processes that cooperate, till core has multi-agent support | [pr-0f3t/beta-Dolly-Plugin](https://github.com/pr-0f3t/beta-Dolly-Plugin)|
| Google Analytics | Connect your Google Analytics Account to beta. | [isaiahbjork/beta-Google-Analytics-Plugin](https://github.com/isaiahbjork/beta-Google-Analytics-Plugin)|
| IFTTT webhooks | This plugin allows you to easily integrate IFTTT connectivity using Maker | [AntonioCiolino/beta-IFTTT](https://github.com/AntonioCiolino/beta-IFTTT)|
| iMessage | Send and Get iMessages using beta | [danikhan632/beta-Messages-Plugin](https://github.com/danikhan632/beta-Messages-Plugin)|
| Instagram | Instagram access | [jpetzke/beta-Instagram](https://github.com/jpetzke/beta-Instagram)|
| Mastodon  | Simple Mastodon plugin to send toots through a Mastodon account | [ppetermann/BetaMastodonPlugin](https://github.com/ppetermann/BetaMastodonPlugin)|
| MetaTrader | Connect your MetaTrader Account to beta. | [isaiahbjork/beta-MetaTrader-Plugin](https://github.com/isaiahbjork/beta-MetaTrader-Plugin) |
| Notion      | Notion plugin for beta.  | [doutv/beta-Notion](https://github.com/doutv/beta-Notion) |
| Slack | This plugin allows to receive commands and send messages to slack channels | [adithya77/beta-slack-plugin](https://github.com/adithya77/beta-slack-plugin)
| Spoonacular | Find recipe insiprations using beta | [minfenglu/beta-Spoonacular-Plugin](https://github.com/minfenglu/beta-Spoonacular-Plugin)
| System Information      | This plugin adds an extra line to the prompt, serving as a hint for the AI to use shell commands likely supported by the current system. By incorporating this plugin, you can ensure that the AI model provides more accurate and system-specific shell commands, improving its overall performance and usefulness. | [hdkiller/beta-SystemInfo](https://github.com/hdkiller/beta-SystemInfo) |
| TiDB Serverless   | Connect your TiDB Serverless database to beta, enable get query results from database | [pingcap/beta-TiDB-Serverless-Plugin](https://github.com/pingcap/beta-TiDB-Serverless-Plugin)
| Todoist-Plugin | Allow beta to programatically interact with yor Todoist to create, update, and manage your Todoist | [danikhan632/beta-Todoist-Plugin](https://github.com/danikhan632/beta-Todoist-Plugin) |
| Weather | A simple weather plugin wrapping around python-weather | [ppetermann/beta-WeatherPlugin](https://github.com/ppetermann/beta-WeatherPlugin) |
| Web-Interaction | Enable beta to fully interact with websites! Allows beta to click elements, input text, and scroll | [gravelBridge/beta-Web-Interaction](https://github.com/gravelBridge/beta-Web-Interaction)|
| WolframBeta | Access to WolframBeta to do math and get accurate information | [gravelBridge/beta-WolframBeta](https://github.com/gravelBridge/beta-WolframBeta)|
| YouTube   | Various YouTube features including downloading and understanding | [jpetzke/beta-YouTube](https://github.com/jpetzke/beta-YouTube) |
| Zapier webhooks | This plugin allows you to easily integrate Zapier connectivity | [AntonioCiolino/beta-Zapier](https://github.com/AntonioCiolino/beta-Zapier)|
| Project Management | Streamline your Project Management with ease: Jira, Trello, and Google Calendar Made Effortless| [minfenglu/beta-PM-Plugin](https://github.com/minfenglu/beta-PM-Plugin)|

## Configuration

For interactionless use, set:

`ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,etc` in your `.env` file to allow plugins to load without prompting.
`DENYLISTED_PLUGINS=example-plugin1,example-plugin2,etc` in your `.env` file to block plugins from loading without prompting.

## Creating a Plugin

Creating a plugin is a rewarding experience! You can choose between first-party or third-party plugins. First-party plugins are included in this repo and are installed by default along with other plugins when the plugin platform is installed. Third-party plugins need to be added individually. Use first-party plugins for plugins you expect others to use and want, and third-party for things specific to you.

### First Party Plugins How-To

1. Clone the plugins repo
1. Follow the structure of the other plugins, implementing the plugin interface as required
1. Write your tests
1. Add your name to the [codeowners](.github/CODEOWNERS) file
1. Add your plugin to the [Readme](README.md)
1. Add your plugin to the [beta-package](https://github.com/kurtosis-tech/beta-package/blob/main/plugins.star). You can copy the line of any of the standard plugins and just add another entry in the dictionary. Raise a PR & get it merged
1. Add your plugin to the [plugin installation integration test](.github/workflows/test-plugin-installation.yml)
1. Make a PR back to this repo!

### Third Party Plugins How-To

1. Clone [the third party template](https://github.com/coozila/beta-Plugin-Template).
1. Follow the instructions in the [third party template readme](https://github.com/coozila/beta-Plugin-Template).

### Migrating Third Party to First Party

We appreciate your contribution of a plugin to the project!

1. Clone this repository.
1. Make a folder for your plugin under `src/beta_plugins`. Use a simple descriptive name such as `notion`, `twitter`, or `web_ui`.
1. Add the files from your third-party plugin located at `src/beta_plugin_template` into the folder you created.
1. Include your README from your third-party plugin in the folder you created.
1. Add your plugin to the root README with a description and a link to your plugin-specific README.
1. Add your plugin's Python package requirements to `requirements.txt`.
1. Add tests to get your plugin to 80% code coverage.
1. Add your name to the [codeowners](.github/CODEOWNERS) file.
1. Add your plugin to the [Readme](README.md).
1. Submit a pull request back to this repository!

## Get Help

For more information, visit the [discord](https://discord.gg/beta) server.
