# Напишите классы сериализации контейнеров с данными Python в json, bin файлы. Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface.

import abc
import json
import pickle

file_name = 'data'

class SerializationInterface (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def serialize(self, data):
        pass

    @abc.abstractmethod
    def deserialize(self, data):
        pass

class JsonSerialization(SerializationInterface):
    def serialize(self, data):
        with open(file_name + '.json', 'w') as f:
            json.dump(data, f)

    def deserialize(self, data):
        with open(file_name + '.json', 'r') as f:
           return json.load(f)

class BinSerialization(SerializationInterface):
    def serialize(self, data):
        with open(file_name + '.bin', 'wb') as f:
            pickle.dump(data, f)
        
    def deserialize(self, data):
        with open(file_name + '.bin', 'rb') as f:
           return pickle.load(f)

if __name__ == '__main__':
    data = {'name': 'Test', 'email': 'test@gmail.com'}
    data_json=JsonSerialization()
    data_bin = BinSerialization()
    data_json.serialize(data)
    data_bin.serialize(data)

    print(data_json.deserialize(data))
    print(data_bin.deserialize(data))
