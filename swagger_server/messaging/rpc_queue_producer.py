#!/usr/bin/env python
import pika
import uuid
import os
import time
import threading

MQ_HOST = 'aw-sdx-monitor.renci.org'

class RpcProducer(object):
    def __init__(self, timeout):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST))

        self.channel = self.connection.channel()
        self.timeout = timeout
        self.exchange_name = ''

        t1 = threading.Thread(target=self.keep_live, args=())
        t1.start()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(queue=self.callback_queue,
                            on_message_callback=self.on_response,
                            auto_ack=True)


    def keep_live(self):
        while True:
            time.sleep(30)
            msg = "[MQ]: Sending Heart Beat"
            # self.connection.process_data_events()
            self.call(msg)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        # if not self.connection or self.connection.is_closed:
        #     # print("Reopening connection...")
        #     self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_HOST))
        #     self.channel = self.connection.channel()
        #     # print("Connection reopened.")
        #     # channel.exchange_declare(exchange=self.exchange_name)

        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(exchange='',
                                    routing_key='rpc_queue',
                                    properties=pika.BasicProperties(
                                        reply_to=self.callback_queue,
                                        correlation_id=self.corr_id,
                                    ),
                                    body=str(body))
                            
        timer = 0
        while self.response is None:
            time.sleep(1)
            timer += 1
            if timer == self.timeout:
                return "No response from MQ receiver"
            self.connection.process_data_events()

        # self.channel.close()
        return self.response

if __name__ == "__main__":
    rpc = RpcProducer()
    body = "test body"
    print("Published Message: {}".format(body))
    response = rpc.call(body)
    print(" [.] Got response: " + str(response))