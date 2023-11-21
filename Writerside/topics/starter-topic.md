# About BasicAlarmSystem

<!--Writerside adds this topic when you create a new documentation project.
You can use it as a sandbox to play with Writerside features, and remove it from the TOC when you don't need it anymore.-->

## Introduction
BasicAlarmSystem is about designing and implementing a smart environmental monitoring system that can detect gas leakage and light conditions, and send alert messages via GSM module.
Based on DragonBoard 410c, MQ-2 gas sensor, MH-Sensor Flying-Fish and SIM800A

![Alarm System](system_image.jpg){border-effect=line}

## Prepare Materials
Materials that must be prepared:

<procedure title="Prepare Materials" id="materials">
    <step>
        <p>DragonBoard 410c x1</p>
        <img src="dragonboard_410c.jpg" alt="dragonboard 410c qualcom" border-effect="line"/>
    </step>
    <step>
        <p>MH-Sensor Flying-Fish x1 (4-pin photoresistor module)</p>
        <img src="sensors.jpg" alt="MH-Sensor Flying Fish and MQ-2 gas sensor" border-effect="line"/>
    </step>
    <step>
        <p>MQ-2 Gas Sensor x1</p>
        <tip>image as above (left)</tip>
    </step>
    <step>
        <p>SIM800A GMS module x1</p>
        <img src="sim800a.jpg" alt="SIM800A GMS module" border-effect="line"/>
    </step>
    <step>
        <p>Other Requirements</p>
        <tabs>
        <tab title="Dupont wires">
        </tab>
        <tab title="Breadboard">
        </tab>
        <tab title="Display">
        </tab>
        <tab title="HDMI converter">
        </tab>
        <tab title="Power adapter">
        </tab>
        </tabs>
    </step>
</procedure>

## Hardware Setup

1. Connect SIM800A module to DragonBoard 410c’s USB port via USB to TTL serial cable, insert SIM card and check antenna status
2. Connect photoresistor module’s VCC pin to DragonBoard 410c’s 5V pin, GND pin to DragonBoard 410c’s GND pin, DO pin to DragonBoard 410c’s GPIO_34 pin
3. Connect gas sensor module’s VCC pin to DragonBoard 410c’s 5V pin, GND pin to DragonBoard 410c’s GND pin, DO pin to DragonBoard 410c’s GPIO_30 pin
4. Connect DragonBoard 410c to display via HDMI cable, and plug in power cord and keyboard mouse