<br/>
<p align="center">

  <img align="center" width="250" height="250" src="https://i.imgur.com/yPfALyd.png">

  <h3 align="center">YoBot Cogs</h3>

  <p align="center">
    Customization Made Simple, YoBot, yo style!
    <br/>
    <br/>
    <a href="https://github.com/RareMojo/YoBot-Discord/wiki"><strong>Explore the docs »</strong></a>
    <br/>
  </p>
</p>
 
<br>

## Table Of Contents

- Guides
    - [Installation](https://github.com/RareMojo/YoBot-Discord/wiki/Installation)
    - [Configuration](https://github.com/RareMojo/YoBot-Discord/wiki/Configuration)
    - [File Structure](https://github.com/RareMojo/YoBot-Discord/wiki/Filestructure)
    - [Extra Cog Installation](https://github.com/RareMojo/YoBot-Discord-Cogs)
    - [Cog Creation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

<br>

## YoBot Cog Extensions Repository

Welcome to the official Cogs repository for the YoBot-Discord bot.

Cogs are essentially Python scripts that function as extension modules for your YoBot, allowing for additional functionality and customization.

<br>

> :warning: **IMPORTANT: These are Python scripts which can execute arbitrary code on your system. It's crucial that you review each Cog before downloading and installing it into your YoBot. Never download a Cog from a source that you don't trust.**

<br>

## Cogs Installation - First Time Setup

During the initial setup of your YoBot, the setup wizard will ask if you want to download extra Cogs from this repository. Here are the options:

1. **Download all Cogs:** Select this option to download and install all the available Cogs in this repository automatically.

2. **Download selected Cogs:** Choose this option if you want to install specific Cogs. You'll need to specify which Cogs you want to download. Check the list of Cogs in this repository for their names and functions.

3. **Skip downloading Cogs:** Choose this option to skip the downloading of any Cogs during the initial setup.

<br>

## Cogs Management - Terminal Commands

After your YoBot is set up and running, you can manage your Cogs with the following methods.

<br>

### Add Cogs:

1. **Download Cogs:** Trigger the Cog download wizard by running the `getcogs` command. You can choose to download all Cogs or select specific ones.

2. **Reload Cogs:** After the download, `getcogs` will automatically reload all the Cogs in your YoBot, ensuring any new functionality is immediately ready.

3. **Resync Discord Commands:** The `getcogs` command also offers the option to resync the commands on your Discord server with those in your YoBot.

<br>

### Remove Cogs

1. **Remove Cogs:** Trigger the Cog removal wizard by running `removecogs` command. You can choose to remove all Cogs not on the blacklist or select specific ones.
    
2. **Reload Cogs:** After running the command you will need to restart YoBot to put the changes into effect.
 
3. **Restart:** Prepare to shutdown. Then run `quit` or `exit`, and start YoBot your usual way.
    
<br>

### Blacklisting

- You can add cogs to the removal blacklist by adding their names to the `blacklist` section of the config.

- This can be helpful for not accidentally removing a cog.

:warning: (Not recommended unless you know what you're doing)

<br>

```yaml
blacklist:
  cog_removal:
  - examplecog1.py
  - examplecog2.py
```

- You can also edit these through the terminal using the `removeblacklist`(`rmbl`) and `addblacklist`(`addbl`) commands.

<br>

## Cog Submission for YoBot

We are working on a simplified cog submission process for the YoBot community.

1. **Create Your Cog**: Follow the guidelines below.
    - WIP

2. **Submit Your Cog**: Once ready, submit it for review.
    - WIP

3. **Verification**: We'll verify your cog to ensure safety and quality.
    - WIP
    
4. **Publication**: If verified, your cog will be published in the repo.
    - WIP

We're also planning on a YoBot Developer Discord, a guild of sorts, where cog creators can gather, share ideas, and assist each other. 

Please stay tuned for updates!

Happy building!

<br>

## 💰 You can help me by Donating
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/RareMojo) [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RareMojo) [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/RareMojo) [![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/RareMojo) 

