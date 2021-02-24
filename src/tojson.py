import json
class ToJson():
    def listToJson(self,lst,tablename):
        tablename = tablename.split(',')
        list_json = dict(zip(tablename, lst))
        str_json = json.dumps(list_json, ensure_ascii=False)  # json转为string
        return str_json