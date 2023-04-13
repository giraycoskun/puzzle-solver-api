from multiprocessing import Process, cpu_count, current_process
import pika
from loguru import logger
from os import getcwd
print(getcwd())

from src.config import ENVIRONMENT, SOLVER_WORKER_SIZE, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_PUZZLE_QUEUE_NAME, RABBITMQ_RESULT_QUEUE_NAME

def start_solver():
    logger.info("Solver Environment: {env}", env=ENVIRONMENT)
    logger.info("Starting Solver Service")
    #nb_cores = cpu_count()
    #logger.info(f"Number of cores: {nb_cores}")
    processes = []
    for _ in range(int(SOLVER_WORKER_SIZE)):
        p = Process(target=solver_worker)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        
    logger.error("Solver Service stopped")

def solver_worker():
    
    logger.info("Solver Worker started {pid}", pid=current_process().name)
    parameters = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)
    channel.queue_declare(queue=RABBITMQ_PUZZLE_QUEUE_NAME, durable=True)
    channel.basic_consume(queue=RABBITMQ_PUZZLE_QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()

def callback(ch, method, properties, body):
    logger.info("ch: {ch}", ch=ch)
    logger.info("method: {method}", method=method)
    logger.info("properties: {properties}", properties=properties)
    logger.info("body: {body}", body=body)
    ch.basic_publish(exchange='', routing_key=RABBITMQ_RESULT_QUEUE_NAME, body=body)
    logger.info("Solver Worker finished {pid}", pid=current_process().name)

if __name__ == "__main__":
    start_solver()