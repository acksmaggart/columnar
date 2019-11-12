from columnar import columnar

headers = ["User", "Message", "Zip"]
data = [
    ['Yiying Lu', 'Fried Dumplings!!!! Yum! 😍😍😍', 47130],
    ['Jennifer Lee', 'Facebook banned the 🍑, can you believe it?', 97153],
    ['Premier12', '本日のヒーロー🦸周東選手✨　#周東佑京　#侍ジャパン #プレミア12 #AUSP12 #Premier12', 549726]
]
table = columnar(data, headers)
print(table)
