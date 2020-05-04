from api import ApiCommunicator

api_communicator = ApiCommunicator(user='admin', password='senhabemsecreta')
api_communicator.queue_consumming('Measure')