import board
import time
import adafruit_dht
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn    #import módulo de entrada analógica



# DHT na porta 2 da franzinho
# dht = adafruit_dht.DHT11(board.IO2)

# RELÉ na porta 0 da franzinho
# relay = digitalio.DigitalInOut(board.IO0)
# relay.switch_to_output()

# Os sensores de umidade de solo estão na porta 1 sendo o analogio e porta 4 o digital da franzinho
umidade_analog = AnalogIn(board.IO1)        # analogio
umidade_digital = DigitalInOut(board.IO4)   # digital
umidade_digital.direction = Direction.INPUT # Configura pino como entrada digital


# relay.value = True
wait_time = 1
watering_time = 1

# Adaptado de acordo com o sensor de umidade de solo - valor para terra seca
# dry_value = 65535

while True:
    try:
        # valor de leitura
        # temperature = dht.temperature
        # humidity = dht.humidity

        # imprime os valores lidos no sensor de umidade de solo
        print("Umidade (Valor Digital):", umidade_digital.value)
        print("Umidade (Valor Analogico):", umidade_analog.value)

        time.sleep(1);

        # Imprime valores lidos na serial DHT11
        # print("Temperature: {:.1f} °C \t humidity: {}%".format(temperature, humidity))

        # if sensor_value < dry_value :
        # print("Starting watering...")
        # Conectamos o relé para ser "sempre fechado"
        # relay.value = False
        # time.sleep(watering_time)
        # print("Finishing watering.")
        # else:
        # se o nível estiver OK, apenas nos certificamos de que o relé esteja fechado,
        # relay.value = True
        # time.sleep(wait_time)

    except RuntimeError as e:
        # A leitura do DHT11 pode falhar
        # print("Falha na leitura do DHT11: ", e.args)
        print("Falha na leitura")

    time.sleep(1)
