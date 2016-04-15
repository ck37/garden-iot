# garden-iot

This project seeks to automate a small planter box garden for my office window using Raspberry Pi. I hope to monitor multiple sensors for the garden, take webcam photos, and eventually get it to water itself, send alerts, accept voice control commands, etc. I'm currently working on phases 2 and 3 - sensor monitoring and control.

Photo summary, as of April 7:

![April 7, 2016](https://raw.githubusercontent.com/ck37/garden-iot/master/photos/garden-2016-04-07.jpg)

Latest updates:

* April 14 - Setup powerswitch tail II, so raspberry pi can water the garden ([short youtube vid here](https://www.youtube.com/watch?v=icgMhyhgxM0))! Also setup webcam for remote viewing.

## Phase 1 - Build garden

The garden consists of a wooden window box with a plastic liner to prevent leaking. The soil is water retaining potting soil augmented with vermiculite and fertilizer. Plants are herbs: basil, chives, mint, rosemary, and thyme. The herbs were started from seed at my house under a separate system with a grow light, with the exception of the mint which I bought as a seedling.

My office doesn't have a sink or water access, so a 5 gallon bucket serves as a reservoir. I used [this YouTube video](https://www.youtube.com/watch?v=xGPdEduEmL0) to create a spout for easier water pouring. I can refill the resevoir once a month or so.

Soil temperature is automatically maintained with a thermostat connected to a heating pad. The heating pad is placed under the plastic container and within the wooden box.

#### Phase 1 Part list

Home Depot

- Wooden window box
- Plastic container box
- Potting soil
- Horticultural-grade vermiculite, medium coarsity
- All-purpose fertilizer
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

Collect sensor measurements of the garden that can provide details on garden health. The primary sensors include: soil moisture, soil temperature, light, and a webcam image. Secondary sensors include room temperature and room humidity. The sensors are placed on a protoboard and connect to the Raspberry Pi's GPIO via the Pi Cobbler.

I have some of these sensors working and some still need to be setup. Not yet saving the data either but would want to push regular measurements to the cloud (Pubnub?).

[[Add photo of Pi Cobbler]]

#### Phase 2 Part list

Adafruit
- [Raspberry Pi 3](https://www.adafruit.com/products/3055) - $40
- [Pi T-cobbler Plus](https://www.adafruit.com/products/2028) - $8
- Sensors
  - Soil moisture/humidity ([SHT-10](https://www.adafruit.com/products/1298) - $50)
  - Soil temperature ([DS18B20](https://www.adafruit.com/products/381) - $10)
  - Lux ([TSL2561](https://www.adafruit.com/products/439) - $6)
  - Room temperature & humidity ([DHT22](https://www.adafruit.com/products/385) - $10)

Amazon
- Webcam (in my case, an extra logitech one that I had already)
- Speakers for text-to-speech ([AmazonBasics](smile.amazon.com/AmazonBasics-Powered-Computer-Speakers-A100/dp/B00GHY5F3K) - $14)

## Phase 3 - Control garden

In this phase I will be able to control basic garden functionality (watering, soil temperature) remotely using technology. The reservoir has a water pump that sends water through 1/4" tubing to a t-splitter and two emitters in the garden. I've raised the pump height by putting another bucket under the main reservoir. This way the pump only needs to send the water up a foot to the garden, rather than 3.5 feet originally. This reduces the backpressure on the pump and gives much better water flow.

The water pump is connected to a Pi-controlled relay so that I can water programmatically by turning on a GPIO pin for a certain number of seconds. I still need to integrate the soil heater and fan. I have gotten basic voice recognition to work (via the [Amazon Alexa API](https://www.reddit.com/r/raspberry_pi/comments/494u60/alexapi_amazon_echo_clone/)), so the next step is to develop voice control.

Ideally there would be a dashboard of controls plus sensor measurements, either via a webpage or as a mobile app.

#### Phase 3 Part list

Amazon
- Water pump (currently [Eco 132](http://smile.amazon.com/EcoPlus-728495-Submersible-Pump-132GPH/dp/B002PXDX0E) - $12
- 1/4" tubing and other tubing connectors ([Koram tubing pack](http://smile.amazon.com/Koram-Distribution-Irrigation-Accessories-IR-D/dp/B013JPIJG4) - $26)
- [Powerswitch tail II](https://www.adafruit.com/products/268) - $26
- Air fan
- Possibly other relay module(s)
- Flow meter sensor

## Phase 4 - Automate garden

In this phase the system would automatically be able to water the garden, manage soil temperature, and provide alerts if sensor results are bad. Other functionality might include fan scheduling and fertilizer distribution.

#### Phase 4 Part List

Adafruit
- Reservoir water level sensor

## Phase 5 - Machine learning

The next goal is to use machine learning to improve the system. My current idea is that if I collect many sensor measurements over multiple months and link those to webcam images, I may be able to use machine learning (esp. convolutional neural nets) to estimate the sensor measurements (esp. soil moisture, reservoir water level) based on computer vision alone. I would then be able to remove the more expensive sensors and use them for other projects, lowering the effective equipment cost. Eventually this kind of training data could be aggregated with other people's so that the machine learning is even more accurate and generalizable, and new users would not need to purchase some of the expensive sensors.

Machine learning might also be be used to detect issues like 1) insect infestation, 2) plant dessication, etc. that would be easier to detect visually than with other sensors.

## Phase 6 - Optimization

Once things are all working, I would want to optimize the setup for materials cost, quality assurance, water usage, and power usage. Cost improvements might include building custom circuits & sensors, finding cheaper suppliers, tweaking functionality, etc. Quality assurance would entail adding more checks, alerts, and backup systems to ensure nothing bad happens and error rates are low. Power usage would first need to be measured rigorously.

## Phase 7 - Randomized trials

The final phase would be to develop experimental designs to improve the health of plants. Initial tests might include 1) augmenting the natural light with supplemental grow lighting, 2) soil temperature management, 3) watering schedules, 4) fan scheduling.
