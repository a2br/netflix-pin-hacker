# netflix-pin-hacker
Get the Netflix PIN code your parents use to restrict your access (or anything else, by the way). The following scripts have been tested on the [Netflix Desktop](https://www.microsoft.com/fr-fr/p/netflix/9wzdncrfj3tj) native app.

## How to use these scripts
### Pre-requirements
You will need to have Python installed as well as the [`keyboard` package](https://pypi.org/project/keyboard/).

### Step-by-step
#### 1. Open Netflix
Open the Netflix native app and select a protected content. Play it. A prompt should appear.
#### 2. Open a script
Open the script you want (eg, miner.py). It has to be opened with the admin rights. On Windows: `Win+R`, write `cmd`, press `Ctrl+Maj+Enter` and log in as an admin. Navigate to the right directory. Put the app on one side of the screen and your terminal on another, so you can see both.
#### 3. Launch it
Run it with `py ./path/to/your/miner.py`, or anything else really. You can skip the inputs and press `Enter` all the way to the end, or adjust the settings as they come. When the blue text appears in the CLI, select the PIN field on the Netflix app. When you're ready, press `Maj` and let it start its thing. Make sure the numbers aren't poping in the CLI faster than Netflix gets them. When Netflix unlocks, watch the range of numbers that hacked it, and start again with a thinner amount of number (eg, 1200-1250), so you can determine what is the code for further use.
#### 4. Enjoy
Enjoy your movie and star this repo. You're welcome, keep your money.


## Scripts
### miner.py
This one will type all the combinations in a range you precised. You can select the speed of typing and the how long it has to pause between each code it types. All formats of PIN codes are supported, from `1` to `00000001` and beyond, in case you want to use it elsewhere. This parameter is determined in function of the length of the string you filled in the `End at:` input.

### day.py
`day.py` will try all the combinations of days and months (hi, 31/02) to get all the dates that exist (and, for simplicity reasons, it includes those that do not exist). There are 372 of them. Since dates are very commonly used as PINs, this script could speed up your search by 96%... or slow it down by 4%.
