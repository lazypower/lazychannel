#Lazy Channel

lazychannel is a python project intended to be used in the aggregation of Creative Commons music from various sources around the internet.

## Installation

    pip install lazychannel

## Usage

LazyChannel can be run from a cron job, or manually from the CLI. Before you do anything relating to using this script as an automated utility - you will need to generate the configuration.

    lazy init ~/.lazychannel

This will generate a boilerplate config.yaml in ~/.lazychannel

   settings:
        dir: ~/Music/lazychannel
        limit: 5
        cache: "{}.cache"
    youtube:
        ArgoFoxCreativeCommons: UC56Qctnsu8wAyvzf4Yx6LIw
 
#### The configuration breakdown

 Settings are global declarations to lazychannel, and provide sane defaults

 - **dir**: Where lazychannel will initialize its directory structure, and place fetched media
 - **limit**: The number of items to process for each "channel" or "stream"
 - **cache**: A template file for naming the channel cache - `{}` will be replaced with the service name.

## Support

Visit our [Github Issues](https://github.com/chuckbutler/lazychannel/issues)


