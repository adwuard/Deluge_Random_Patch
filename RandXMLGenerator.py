import os

import xmltodict
from xml.etree.ElementTree import Element, tostring
from xmljson import badgerfish as bf
import random

# Note: Generated patchs will be saved(overwriting) to generated folder call "exported" under the same directory

# Number of random patches generated
generating = 100

# ------- XML init config --------
FIRMWARE_VERSION = "3.0.2"
EARLIEST_COMPATABLE_FIRMWARE = "3.0.0"

# ------- Each Available Options--------
polyphonic = ["poly", "mono", "auto", "lega"]
mode = ["fm", "subtractive"]
osc_type = ["saw", "sine", "triangle", "square", "analogSquare", "analogSaw", "analogTriangle", "analogSine"]
lfo_type = ["triangle", "sine"]
lfo_syncLevel = [0, 1, 2, 3, 4, 5, 6, 7]
unison_num = [0, 1, 2, 3, 4, 5, 6]
unison_detune = [0, 1, 2, 3, 4, 5, 6]

# ----------- Patch Points --------------
# If you dont want certain parameter be in the random patch point. You can simply remove it from the list 
PATCH_CABLES_MAX = 15  # random patch cables from place to place. Allowing maximum of 15 cable
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

# ------------ Deluge knob param 0-50 map and corresponds to this list ------------
paramMatchTable = ["0x80000000", "0x851EB851", "0x8A3D70A2", "0x8F5C28F3", "0x947AE144",
                   "0x99999995", "0x9EB851E6", "0xA3D70A37", "0xA8F5C288", "0xAE147AD9",
                   "0xB333332A", "0xB851EB7B", "0xBD70A3CC", "0xC28F5C1D", "0xC7AE146E",
                   "0xCCCCCCBF", "0xD1EB8510", "0xD70A3D61", "0xDC28F5B2", "0xE147AE03",
                   "0xE6666654", "0xEB851EA5", "0xF0A3D6F6", "0xF5C28F47", "0xFAE14798",
                   "0x00000000", "0x051EB83A", "0x0A3D708B", "0x0F5C28DC", "0x147AE12D",
                   "0x1999997E", "0x1EB851CF", "0x23D70A20", "0x28F5C271", "0x2E147AC2",
                   "0x33333313", "0x3851EB64", "0x3D70A3B5", "0x428F5C06", "0x47AE1457",
                   "0x4CCCCCA8", "0x51EB84F9", "0x570A3D4A", "0x5C28F59B", "0x6147ADEC",
                   "0x6666663D", "0x6B851E8E", "0x70A3D6DF", "0x75C28F30", "0x7AE14781",
                   "0x7FFFFFD2"]

# ------------------ Effected parameters in the "defaultParams" section ------------------
# you can also remove items from the list if you don't want randomness in certain parameters
# ie: removing "patchCables" then no patch cables will be added.

effectedParams = [
    "@arpeggiatorGate", "@portamento", "@compressorShape", "@oscAVolume",
    "@oscAPulseWidth", "@oscBVolume", "@oscBPulseWidth", "@noiseVolume", "@volume", "@pan", "@lpfFrequency",
    "@lpfResonance", "@hpfFrequency", "@hpfResonance", "@lfo1Rate", "@lfo2Rate", "@modulator1Amount",
    "@modulator1Feedback", "@modulator2Amount", "@modulator2Feedback", "@carrier1Feedback", "@carrier2Feedback",
    "@modFXRate", "@modFXDepth", "@reverbAmount", "@arpeggiatorRate",
    "@stutterRate", "@sampleRateReduction", "@bitCrush", "@modFXOffset", "@modFXFeedback",
    "envelope1", "envelope2", "patchCables"]


def JsonParseXML(json):
    result = bf.etree(json, root=Element('root'))
    return tostring(result)


for k in range(0, generating):
    f = open("Template/SYNT001.XML", "r")
    o = xmltodict.parse(f.read())

    # ----------------------- Basics Rand Section ---------------------------
    o["sound"]["@firmwareVersion"] = FIRMWARE_VERSION
    o["sound"]["@earliestCompatibleFirmware"] = EARLIEST_COMPATABLE_FIRMWARE
    o["sound"]["@polyphonic"] = polyphonic[random.randint(0, len(polyphonic)) - 1]
    o["sound"]["@voicePriority"] = 1

    # FM synth mode?
    fm_modeFlag = random.randint(0, 100) % 2
    if fm_modeFlag:
        o["sound"]["@mode"] = "fm"
    else:
        o["sound"]["@mode"] = "subtractive"

    o["sound"]["@lpfMode"] = "24dB"
    o["sound"]["@modFXType"] = "none"

    # ----------------------- OSC1 and OSC2 Rand Section ---------------------------
    if not fm_modeFlag:
        o["sound"]["osc1"]["@type"] = osc_type[random.randint(0, len(osc_type) - 1)]
    o["sound"]["osc1"]["@transpose"] = random.randint(-24, 12)
    o["sound"]["osc1"]["@cents"] = 0
    o["sound"]["osc1"]["@retrigPhase"] = 0

    if not fm_modeFlag:
        o["sound"]["osc2"]["@type"] = osc_type[random.randint(0, len(osc_type) - 1)]
    o["sound"]["osc2"]["@transpose"] = random.randint(-24, 12)
    o["sound"]["osc2"]["@cents"] = 0
    o["sound"]["osc2"]["@retrigPhase"] = 0

    # ----------------------- lfo Rand Section ---------------------------
    # <lfo1 type="triangle" syncLevel="0" />
    # <lfo2 type="triangle" />
    o["sound"]["lfo1"]["@type"] = lfo_type[random.randint(0, len(lfo_type) - 1)]
    o["sound"]["lfo2"]["@type"] = lfo_type[random.randint(0, len(lfo_type) - 1)]
    o["sound"]["lfo1"]["@syncLevel"] = 0

    # ----------------------- unison Rand Section ---------------------------
    # <unison num="1" detune="8" />
    o["sound"]["unison"]["@num"] = random.randint(1, 8)
    o["sound"]["unison"]["@detune"] = random.randint(0, 50)

    # ----------------------- compressor Rand Section ---------------------------
    # ---- Not implemented -------

    # ----------------------- delay Rand Section ---------------------------
    # ---- Not implemented -------

    # ----------------------- Modulator Rand Section ---------------------------
    # Enabled only if its FM synth mode
    if fm_modeFlag:
        o["sound"]["modulator1"] = {}
        o["sound"]["modulator2"] = {}

        o["sound"]["modulator1"]["@transpose"] = random.randint(-9, 9)
        o["sound"]["modulator1"]["@cents"] = random.randint(-9, 9)
        o["sound"]["modulator1"]["@retrigPhase"] = random.randint(0, 36) * 10

        o["sound"]["modulator2"]["@transpose"] = random.randint(-9, 9)
        o["sound"]["modulator2"]["@cents"] = random.randint(-9, 9)
        o["sound"]["modulator2"]["@retrigPhase"] = random.randint(0, 36) * 10
        o["sound"]["modulator2"]["@toModulator1"] = random.randint(-9, 9)
    else:
        if "modulator1" in o["sound"]:
            del o["sound"]["modulator1"]
        if "modulator2" in o["sound"]:
            del o["sound"]["modulator2"]

    # ----------------------- defaultParams Rand Section ---------------------------
    ls = o["sound"]["defaultParams"]
    for i in range(0, len(effectedParams)):
        if effectedParams[i] == "envelope1" or effectedParams[i] == "envelope2":
            ls[effectedParams[i]]["@attack"] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]
            ls[effectedParams[i]]["@decay"] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]
            ls[effectedParams[i]]["@sustain"] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]
            ls[effectedParams[i]]["@release"] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]

        elif effectedParams[i] == "patchCables":
            # list to avoid redundant patching
            occuredCheck = []
            ls[effectedParams[i]] = {"patchCable": []}
            for _ in range(0, random.randint(0, PATCH_CABLES_MAX)):
                dic = {}
                s = patch_from[random.randint(0, len(patch_from) - 1)]
                d = patch_destination[random.randint(0, len(patch_destination) - 1)]
                dic["@source"] = s
                dic["@destination"] = d
                dic["@amount"] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]
                # Ensure is not patch already
                if [s, d] not in occuredCheck:
                    occuredCheck.append([s, d])
                    ls[effectedParams[i]]["patchCable"].append(dic)

        else:
            change = random.randint(0, 1)
            if "delay" not in ls[effectedParams[i]]:
                if change:
                    ls[effectedParams[i]] = paramMatchTable[random.randint(0, len(paramMatchTable) - 1)]
    # Replace the new dict into
    o["sound"]["defaultParams"] = [ls]

    # ----------- arpeggiator rand section -----------
    # ------------ NOT implemented ---------------
    # <arpeggiator
    # 		mode="off"
    # 		numOctaves="2"
    # 		syncLevel="7" />

    # print(json.dumps(o, indent=2))

    # Convert and exported as XML file
    newXML = JsonParseXML(o)
    newXML = str(newXML, "utf-8")
    newXML = newXML.replace("<root>", "")
    newXML = newXML.replace("</root>", "")
    print("Exporting patch", str(k) + "_rand_patch.XML")

    if not os.path.exists('exported'):
        os.makedirs('exported')

    f = open("exported/" + str(k) + "_rand_patch.XML", "w")
    f.write(newXML)
    f.close()
