import pika
import json
import sensor_hc_sr04 as lib_hc_sr04


def callback(ch, method, properties, body):
    print(body.decode('utf8'))
    sensor = lib_hc_sr04.hc_sr04(trigger_pin=23, echo_pin=24)
    print(str(sensor.get_distance_cm()))
    ch.basic_ack(delivery_tag=method.delivery_tag)


class ApiCommunicator(object):

    def __init__(self, user, password):
        self.credentials = pika.PlainCredentials(user, password)
        self.parameters = pika.ConnectionParameters('201.75.200.31', 5672, '/', self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def idk_yet(self):
        result = self.channel.queue_declare(queue='MeasureResult')
        data_set = { 'UserId': 1, 'Centimetros': 28 }
        json_dump = json.dumps(data_set)
        self.channel.basic_publish(exchange='', routing_key='MeasureResult', body=json_dump.encode('utf8'))
        print('enviado')

    def queue_consumming(self, _queue_name):
        # _queue_name = 'Measure'
        self.channel.basic_consume(_queue_name, on_message_callback=callback)
        self.channel.start_consuming()
