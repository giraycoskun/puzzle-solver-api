import pika
from queue import Queue

from src.config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_PUZZLE_QUEUE_NAME, RABBITMQ_RESULT_QUEUE_NAME, RABBITMQ_POOL_SIZE


class RabbitMQRepository:

    __instance = None

    @staticmethod
    def get_instance() -> None:
        """Static method to fetch the singleton instance"""        
        if RabbitMQRepository.__instance is None:
            RabbitMQRepository()
        return RabbitMQRepository.__instance

    def __init__(self) -> None:
        """Private constructor to create a single instance of the class.

        Raises:
            Exception: RabbitMQConnection is a singleton!
        """        
        if RabbitMQRepository.__instance is not None:
            raise Exception("RabbitMQConnection is a singleton!")
        
        parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        )

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_PUZZLE_QUEUE_NAME, durable=True)
        channel.queue_declare(queue=RABBITMQ_RESULT_QUEUE_NAME, durable=True)
        connection.close()

        self.connections = Queue()
        for _ in range(int(RABBITMQ_POOL_SIZE)):
            self.connections.put(pika.BlockingConnection(parameters))
        RabbitMQRepository.__instance = self

    def __get_connection(self) -> pika.BlockingConnection:
        """Get a connection from the pool.

        Returns:
            pika.BlockingConnection: A blocking connection object
        """               
        return self.connections.get()
    
    def __release_connection(self, connection: pika.BlockingConnection) -> None:
        """Release a connection to the pool.

        Args:
            connection (pika.BlockingConnection): A blocking connection object
        """        
        self.connections.put(connection)

    def publish_puzzle(self, puzzle):
        connection = self.__get_connection()
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_PUZZLE_QUEUE_NAME)
        channel.basic_publish(exchange='', routing_key=RABBITMQ_PUZZLE_QUEUE_NAME, body=puzzle)
        self.__release_connection(connection)

    def consume_puzzle(self, callback):
        connection = self.__get_connection()
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_RESULT_QUEUE_NAME)
        channel.basic_consume(queue=RABBITMQ_RESULT_QUEUE_NAME, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
        self.__release_connection(connection)

    def close(self):
        while not self.connections.empty():
            self.connections.get().close()
