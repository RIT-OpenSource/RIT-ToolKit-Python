from json import loads, dumps
from os.path import exists, abspath
from os import mkdir

class Counter():
    def __init__(self, file_path = './data/counter/list.json'):
        self.file_path = file_path
        if not exists('./data'): mkdir('data')
        if not exists('./data/counter'): mkdir('./data/counter')
        if not exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as ListFile:
                ListFile.write(dumps(
                    [
                        {
                            'name': '\u8fdc\u53e4\u6b8b\u9ab8\u6316\u6398\u91cf',
                            'value': 0
                        }
                    ]
                ))
    #
    def getall(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as ListFile:
                return loads(ListFile.read())
        except:
            return {}
    #
    def get(self, name):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as ListFile:
                List = loads(ListFile.read())
        except:
            raise FileNotFoundError(f'Missing Data File: {abspath(self.file_path)} is not exists.')
        for counter in List:
            if counter['name'] == name:
                return counter['value']
        return None
    #
    def set(self, name, value):
        with open(self.file_path, 'r', encoding='utf-8') as ListFile:
            List = loads(ListFile.read())
        for counter in List:
            if counter['name'] == name:
                counter['value'] = value
                break
        with open(self.file_path, 'w', encoding='utf-8') as ListFile:
            ListFile.write(dumps(List))
    #
    def join(self, name, value):
        with open(self.file_path, 'r', encoding='utf-8') as ListFile:
            List = loads(ListFile.read())
        List.append({
            'name': name,
            'value': value
        })
        with open(self.file_path, 'w', encoding='utf-8') as ListFile:
            ListFile.write(dumps(List))
    #
    def remove(self, name):
        with open(self.file_path, 'r', encoding='utf-8') as ListFile:
            List = loads(ListFile.read())
        updated_list = [counter for counter in List if counter['name'] != name]
        with open(self.file_path, 'w', encoding='utf-8') as ListFile:
            ListFile.write(dumps(updated_list))