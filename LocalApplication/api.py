KKKKKKKKKKKKimport pika
import json
import sensor_hc_sr04 as lib_hc_sr04



class ApiCommunicator(object):

    def __init__(self, user, password):
        self.credentials = pika.PlainCredentials(user, password)
        self.parameters = pika.ConnectionParameters('201.75.200.31', 5672, '/', self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.user_id = 0
        self.size = 0

    def measure_procedure(self):
        sensor = lib_hc_sr04.hc_sr04(trigger_pin=23, echo_pin=24)
        self.size = 45 - sensor.get_distance_cm

    def callback(self, ch, method, properties, body):
        obj = json.loads(body)
        self.user_id = int(obj['UserId'])
        ch.basic_ack(delivery_tag=method.delivery_tag)
        self.measure_procedure()

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
        self.channel.basic_consume(
            _queue_name,
            on_message_callback=self.callback,
            callback=self.basic_publish(_queue_name='MeasureResult', _data_set={'UserId': self.user_id,
                                                                                'Centimetros': self.size}
                                        )
        )
        self.channel.start_consuming()
