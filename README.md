# garden-iot

This project seeks to create a small window-based planter box garden for my office. I hope to monitor multiple sensors for the garden, take webcam photos, and eventually get it to water itself, send alerts, accept voice control commands, etc.

Currently working on phases 2 and 3.

![April 7, 2016](https://raw.githubusercontent.com/ck37/garden-iot/master/photos/garden-2016-04-07.jpg)

## Phase 1 - Build garden

The garden consists of a wooden window box with a plastic liner to prevent leaking. The soil is water retaining potting soil augmented with vermiculite and fertilizer. Plants are herbs: basil, chives, mint, rosemary, and thyme. The herbs were started from seed at my house under a separate system with a grow light, with the exception of the mint which I bought as a seedling

My office doesn't have a sink or water access, so a 5 gallon bucket serves as a reservoir. I used this YouTube video (LINK) to create a spout for easier water pouring. I can refill the resevoir once a month or so.

Soil temperature is automatically maintained with a thermostat connected to a heating pad.

#### Phase 1 Part list

Home Depot

- Window box
- Plastic linear box
- Potting soil
- Fertilizer
- 5 gallon bucket
- Spout
- Bulkhead
- Plumber's tape
- Mint seedling
- Seeds: basil, chives, rosemary, thyme

Amazon

- Thermostat controller ([Inkbird ITC-308 digital](http://smile.amazon.com/Inkbird-Itc-308-Temperature-Controller-Thermostat/dp/B011296704) - $39)
- Heading pad ([Apollo seedling mat, 10"x20"](http://smile.amazon.com/Apollo-Horticulture-Seedling-Propagation-Cloning/dp/B00S1VJ0OC) - $23)

## Phase 2 - Monitor garden

Collect sensor measurements of the garden that can provide details on garden health. The primary sensors include: soil moisture, soil temperature, light, and a webcam image. Secondary sensors include room temperature and room humidity.

I have some of these sensors working and some still need to be setup. Not yet saving the data either but would want to push regular measurements to the cloud (Pubnub?).

#### Phase 2 Part list

Adafruit
- Raspberry Pi 3
- Pi cobbler
- Sensors
  - Soil temperature
  - Soil humidity
  - Lux
  - Room temperature
  - Room humidity

Amazon
- Webcam (in my case, an extra logitech one that I had already)
- Speakers for text-to-speech ([AmazonBasics](smile.amazon.com/AmazonBasics-Powered-Computer-Speakers-A100/dp/B00GHY5F3K) - $14)

## Phase 3 - Control garden

In this phase I will be able to control basic garden functionality (watering, soil temperature) remotely using technology. The reservoir has a water pump that sends water through 1/4" tubing to a t-splitter and two emitters in the garden. In my case the pump needs to send water up about 4 feet to the window sill, so that extra backpressure means the pump needs to be stronger than if it were moving the water laterally or downward.

I'm working to connect the water pump, soil heater, and fan to relays that can be controlled via the Raspberry Pi.

I'm working on voice recognition (via the Amazon Alexa API [[LINK]]) for control via voice.

Ideally there would be a dashboard of controls plus sensor measurements, either via a webpage or as a mobile app.

#### Phase 3 Part list

Amazon
- Water pump (currently [Eco 132](http://smile.amazon.com/EcoPlus-728495-Submersible-Pump-132GPH/dp/B002PXDX0E) - $12, may be upgrading to a stronger pump)
- 1/4" tubing and other tubing connectors ([Koram tubing pack](http://smile.amazon.com/Koram-Distribution-Irrigation-Accessories-IR-D/dp/B013JPIJG4) - $26)
- Powerswitch tail II
- Air fan
- Possibly other relay module(s)
- Flow meter sensor

## Phase 4 - Automate garden

In this phase the system would automatically be able to water the garden, manage soil temperature, and provide alerts if sensor results are bad. Other functionality might include fan scheduling and fertilizer distribution.

#### Phase 4 Part List

Adafruit
- Reservoir water level sensor

## Phase 5 - Machine learning

The next goal is to use machine learning to improve the system. My current idea is that if I collect many sensor measurements over multiple months and link those to webcam images, I may be able to use machine learning (esp. convolutional neural nets) to estimate the sensor measurements (esp. soil moisture, reservoir water level) based on computer vision alone. I would then be able to remove the more expensive sensors and use them for other projects. Eventually this kind of training data could be aggregated with other people's so that the machine learning is even more accurate and generalizable, and new users would not need to purchase some of the expensive sensors.

Machine learning might also be be used to detect issues like 1) insect infestation, 2) plant dessication, etc. that would be easier to detect visually than with other sensors.

## Phase 6 - Randomized trials

Develop experimental designs to improve the health of plants. Initial tests might include 1) augmenting the natural light with supplemental grow lighting, 2) soil temperature management, 3) watering schedules.

## Phase 7 - Optimization

Once things are all working, I would want to optimize the setup for materials cost, quality assurance, water usage, and power usage. Cost improvements might include building custom circuits & sensors, finding cheaper suppliers, tweaking functionality, etc. Quality assurance would entail adding more checks, alerts, and backup systems to ensure nothing bad happens and error rates are low. Power usage would first need to be measured rigorously.
