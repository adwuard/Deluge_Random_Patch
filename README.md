# Deluge-Random-Patch
Simple python script that generates Deluge compatible XML patches.
This can quickly generate massive amount patches in the smallest amount of time.
Since it is a "random" patch generator. Some sound may be inspiring for creating music, but most are just worst patch and worst sound design ever. 
This script has the widest possible range on each Deluge's parameters. So most patches will be crazy. Hence some tweaking may required so it fit better to your taste.  
All in all, hope this will bring some surprise to your music creation. Enjoy and have fun. 

# Tweek the affected parameters


### Patch Points
If you dont want certain parameter be in the random patch point. You can simply remove it from the list   
```
PATCH_CABLES_MAX = 15  # random patch cables from place to place. Allowing maximum of 15 cable
```
patch points
```
patch_from = ["random", "envelope1", "envelope2", "lfo1", "lfo2", "compressor", "velocity", "note"]
patch_destination = ["volume",
                     "carrier1Feedback", "carrier2Feedback",
                     "volumePostReverbSend", "volumePostReverbSum",
                     "lpfFrequency", "lpfResonance",
                     "pitch", "pan",
                     "oscAVolume", "oscBVolume",
                     "env1Decay", "env2Decay",
                     "lsenv1Attack", "env2Attack",
                     "env1Release", "env2Release",
                     "oscAPhaseWidth", "oscBPhaseWidth",
                     "delayRate"]
```

### Effected parameters in the "defaultParams" section
you can also remove items from the list if you don't want randomness in certain parameters  
ie: removing "patchCables" then no patch cables will be added.  

```
effectedParams = [
    "@arpeggiatorGate", "@portamento", "@compressorShape", "@oscAVolume",
    "@oscAPulseWidth", "@oscBVolume", "@oscBPulseWidth", "@noiseVolume", "@volume", "@pan", "@lpfFrequency",
    "@lpfResonance", "@hpfFrequency", "@hpfResonance", "@lfo1Rate", "@lfo2Rate", "@modulator1Amount",
    "@modulator1Feedback", "@modulator2Amount", "@modulator2Feedback", "@carrier1Feedback", "@carrier2Feedback",
    "@modFXRate", "@modFXDepth", "@reverbAmount", "@arpeggiatorRate",
    "@stutterRate", "@sampleRateReduction", "@bitCrush", "@modFXOffset", "@modFXFeedback",
    "envelope1", "envelope2", "patchCables"]
```

### Random Range
You will see this function throughout the script. You can basically adjust two variable to your tasting.   
For Example if you want is osc1 transpose to be randomized in a shorter and smaller range.  
You can do:  
```
random.randint(-8, 12)
```
At full range:
```
random.randint(-24, 12)
```
Note that your range has to be legal to the Deluge.



## Installation
This is an python script and supported to 2.7, and tested on the newest 3.7.
Not going through how to install python or run python. There are lots of information online.
Two libraries are required if not installed already. Execute the following command in terminal and install under your python environment. 
```
sudo pip install xmltodict
sudo pip install xmljson
```

To run the script `cd` to project folder
```
sudo python RandXMLGenerator.py
```
if you see `ImportError: No module named ---- ` that means modules are missing and you need to install them. See above.


## Usage
Run the code and the XML patches will be saved to the folder call exported.
Copy the XML patches to you Deluge SD card (under `SYNTH` folder) folder. Then you are good to go.
Note: each export files in exported will be overwritten.


## Support Me
I am an independent developer. Anything supports for what I love creating. If you find this project useful of interesting.   
Please [Buy me a cup of coffee ☕](http://tinyurl.com/y4jezlod)   
Thank You!! 

## Lisense
It is basically do what ever you want license. Do whatever you want with it. :) 