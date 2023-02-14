# This code controls a prototype of an automatic irrigation system. 
# The value used in the dry_value variable concerning our tests. 
# We recommend calibrating this value for your environment.
# 
# Copyright 2023 Giuliane Eulália Corrêa
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import board
import time

from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn    #to import the analog input module

# Relay on port 0 of the franzinho
relay = DigitalInOut(board.IO0)
relay.switch_to_output()

# The soil moisture sensors are on port 1, being the analog and port 4, the digital one of the franzinho
humid_analog = AnalogIn(board.IO1)        # analog
humid_digital = DigitalInOut(board.IO4)   # digital
humid_digital.direction = Direction.INPUT # Configure pin as digital input

relay.value = True

wait_time = 1
watering_time = 1

# Adapted according to the soil moisture sensor - value for dry land
dry_value = 51130

while True:
    try:
        # print the values read from the soil moisture sensor
        print("humid (Digital value):", humid_digital.value)
        print("humid (Analogic value):", humid_analog.value)

        time.sleep(1);

        if humid_analog.value > dry_value :
            print("Starting watering...")

            #We connect the relay to be "always closed"
            relay.value = False

            time.sleep(watering_time)
            print("Finishing watering.")

        else:
            # if the level is OK, we just make sure the relay is closed
            relay.value = True
            time.sleep(wait_time)

    except RuntimeError as e:
        print("Read failure")

    time.sleep(1)
