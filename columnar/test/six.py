from columnar import columnar

headers = ['name', 'id', 'host', 'notes']

data = [
    ['busybox', 'c3c37d5d-38d2-409f-8d02-600fd9d51239', 'linuxnode-1-292735', 'Test server.'],
    ['alpine-python', '6bb77855-0fda-45a9-b553-e19e1a795f1e', 'linuxnode-2-249253', 'The one that runs python.'],
    ['redis', 'afb648ba-ac97-4fb2-8953-9a5b5f39663e', 'linuxnode-3-3416918', 'For queues and stuff.'],
    ['app-server', 'b866cd0f-bf80-40c7-84e3-c40891ec68f9', 'linuxnode-4-295918', 'A popular destination.'],
    ['nginx', '76fea0f0-aa53-4911-b7e4-fae28c2e469b', 'linuxnode-5-292735', 'Traffic Cop'],
]

table = columnar(data, headers, no_borders=True)
print(table)