number: int = 5
text: str = 'Hello'
decimal: float = 2.5
active: bool = True

names: list = ['Bod', 'Dane', 'Sane']
coordinate: tuple = (12, 22)
unique: set = {12, 1331, 1221}
data: dict = {'name': "bob", 'age': 19}


def cal(string, a, b, c, d):
    print(string[a:b] + string[c:d])
text: str = 'Hello'

cal(text, 1, 2, 1, 4)

def cal(string, a, b, c, d):
    print(string[a:b] + string[c:d])
text = "ABCDE"
cal(text, 1, 2, 1, 4)