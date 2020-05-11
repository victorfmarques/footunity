KKKKKKKKKKKKimport pika
import json
import sensor_hc_sr04 as lib_hc_sr04

USER_ID = 0

def callback(ch, method, properties, body):
    obj = json.loads(body)
    USER_ID = int(obj['UserId'])
    ch.basic_ack(delivery_tag=method.delivery_tag)

def measure_procedure(user_id):
    sensor = lib_hc_sr04.hc_sr04(trigger_pin=23, echo_pin=24)
    size = 45 - sensor.get_distance_cm




class ApiCommunicator(object):

    def __init__(self, user, password):
        self.credentials = pika.PlainCredentials(user, password)
        self.parameters = pika.ConnectionParameters('201.75.200.31', 5672, '/', self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def basic_publish(self, _queue_name, _data_set):
        self.channel.queue_declare(queue=_queue_name)
        self.channel.confirm_delivery()
        json_dump = json.dumps(_data_set)
        try:
            print('Dado a ser publicado ->' + json_dump)
            self.channel.basic_publish(exchange='', routing_key=_queue_name, body=json_dump.encode('utf8'))

            print("Dado recebido pelo destinatario")
        except pika.exceptions.UnroutableError:
            print("Dado nao foi recebido pelo destinatario")

    def queue_consumming(self, _queue_name):
        # _queue_name = 'Measure'
        self.channel.basic_consume(_queue_name, on_message_callback=callback, callback=measure_procedure(USER_ID))
        self.channel.start_consuming()
