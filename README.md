# Pomodoro CLI
The Pomodoro Command Line Interface (CLI) is a productivity application that will help you in getting things done!

![size](https://img.shields.io/github/repo-size/kobej1/pomodoroCLI?color=brightgreen&logoColor=green "Repo size")
![python](https://img.shields.io/static/v1?label=python&message=3.5|3.6|3.7&color=blueviolet "Python Version")

***Github***<br>
&nbsp;&nbsp;&nbsp;&nbsp;https://github.com/kobej1/pomodoroCLI

## Description
Are you often distracted by external interruptions like incoming e-mails, notifications of your phone, ...? But do you really want to be more focused will working on something? Than you certainly need to give the pomodoro technique a shot!

**How does it work?**<br>
Because of the work cycle isn't that much (traditionally 25 minutes) you will work harder! Otherwise you will maybe start thinking "I have time enough, I can take it easy".

Now, after the (hopefully productive) work cycle your brain needs to rest a little bit, 3-5 minutes is enough to recharge the battery inside your head. Enough time to check your notifications, go to the bathroom, ...

But than the difficult part, starting a new cycle... Than just think back to the initial reason why your done this. Yeah, indeed to become more productive! So let's beat the next cycle! It will become easier after a while.

After 4 such cycles you formed a set, congratulations! Now you certainly deserve to take a longer rest (15-30 minutes). If you want to you can start a new set after this big relax cycle.

**Tips**<br>
* Turn your phone in the 'do not disturb' mode during the work cycle.
* Close all social media related tabs
* Try to complete full sets 

## Getting started

### Clone pomodoroCLI
Go to folder where you want the application to be placed. After that, just run the fashion *git clone* command. 
```bash
$ git clone https://github.com/kobej1/pomodoroCLI
```

### Install pomodoroCLI
Go inside the pomodoroCLI folder (which you normally cloned in the previous step). Then let's install the application by running *sh install.sh*.
```bash
$ cd pomodoroCLI
$ sh install.sh
```

### Start pomodoroCLI
#### Start pomodoroCLI with default values
Start the pomodoroCLI with the default values and without any optional configuration paramaters.<br>
Default values:
* Work cycle: 25 minutes
* Relax cycle: 5 minutes
* Big relax cycle: 5 minutes

```bash
$ pomodoro
```

#### Start pomodoroCLI with changeable values
Start the pomodoroCLI with values chosen by you. All the values are optional.

***Syntax***
```bash
$ pomodoro [--workCycle] [--relaxCycle] [--bigRelaxCycle]
```

***Example***
```bash
$ pomodoro 20 3
```

## Features
✔️ Pomodor timer<br>
✔️ Changeable values for pomodoro timer<br>

## Upcoming Features

📝 Error handling & help messages<br>
📝 Statitics<br>
📝 Settings<br>
📝 Chart<br>


## Contribute
Feel free to create a new pull request to improve the repo! I will always look at new pull requests and give feedback if necessary. If you want to discuss (possible new features, pull requests) something, you can contact me at my e-mail kobejanssens@outlook.com.

## Donate
If this library made you more productive or was helpfull for you, feel free to donate.

***PayPal***<br>
&nbsp;&nbsp;&nbsp;&nbsp;https://www.paypal.me/KobeJanssens

***BTC***<br>
&nbsp;&nbsp;&nbsp;&nbsp;368VXtQjHQFEchJqLQfAtNubxtkezEExFR

***ETH***<br>
&nbsp;&nbsp;&nbsp;&nbsp;0xD323226d6BdF0b518De9Bd6B162c3F30fa64936c (ETH only)

***LTC***<br>
&nbsp;&nbsp;&nbsp;&nbsp;LcP6agK4AVuDpof4mhfnbnWCm6xMUtbEzn

***EOS***<br>
&nbsp;&nbsp;&nbsp;&nbsp;kobejanssens

## License
**MIT** License