# SPDX-FileCopyrightText: 2019 Max Taggart
#
# SPDX-License-Identifier: MIT

from columnar import columnar
from click import style


headers = ['Id', 'DestinationEntityId', 'DataMartId', 'Name', 'Classification', 'Description', 'Status', 'SourceConnectionId', 'GroupingColumn', 'GroupingFormat', 'ContentId', 'BindingType', 'GrainName', 'LoadTypeCode', 'AttributeValues@odata.context', 'UserDefinedSQL', 'IncrementalColumnName', 'SourceDatabaseName', 'SourceSchemaName', 'SourceTableAlias', 'Script', 'ExecutionEnvironmentId', 'ColumnSeparatorName', 'FilePattern', 'FirstRowAsHeaders', 'RetainNulls', 'RowDelimiter', 'CodePage', 'FilePatternType', 'TextQualifier', 'NonPersistedSQL', 'IsProtected', 'ResultDataFrameName']
data = [[175, 177, 10, 'mag_pythong', 'Generic', None, 'Active', 13, None, None, '94f53103-ef6f-4052-aa50-2abc85ec1578', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(175)/AttributeValues', '-', '-', '-', '-', '-', "print('hello world!')\n# Add additional Python here\nprint('done!')", '1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [259, 260, 13, 'pythonTest2Binding', 'Generic', None, 'Active', 18, None, None, '7a67136a-2135-44a5-a96a-f742c115a3ca', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(259)/AttributeValues', '-', '-', '-', '-', '-', "print('hello world!')\n# Add additional Python here\nprint('done!')", '1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1356, 260, 13, 'TestQueryRewriters', 'Generic', None, 'Active', 18, None, None, '32006127-ac82-4363-851b-9b42f4965127', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1356)/AttributeValues', '-', '-', '-', '-', '-', "print('hello world!')\r\n# Add additional Python here\r\nprint(vars())\r\nprint('done!')", '2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1361, 1368, 1021, 'PythonPluginTestBinding', 'Generic', None, 'Active', 1027, None, None, '356a162f-8958-408a-a9d5-a775a82bb5f0', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1361)/AttributeValues', '-', '-', '-', '-', '-', "\r\nbinding_output = NLPSAM_Test_AdventureWorks2012Person.assign(name=lambda x: x.FirstNameTest, age=lambda x: x.BusinessEntityIDTest, weight=lambda x: x.BusinessEntityIDTest * 2)[['age', 'name', 'weight']]\r\n", '2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1366, 1375, 1024, 'IncrementalSAMBinding', 'Generic', None, 'Active', 1030, None, None, '3deb7679-1b41-4f12-b965-d89586e677c8', 'Python', None, 'Incremental', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1366)/AttributeValues', '-', '-', '-', '-', '-', '\r\nbinding_output = NLPSAM_PluginTest_IncrementalSM\r\nprint(binding_output)\r\n', '2', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1368, 1376, 1025, 'PythonStreamingTestBinding', 'Generic', None, 'Active', 1031, None, None, '7753d5c0-13c0-4e45-bfa8-f7e5aa260fa4', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1368)/AttributeValues', '-', '-', '-', '-', '-', '\r\nimport pandas as pd\r\n\r\n@binding.group_task("BusinessEntityIDTest")\r\ndef task(input_frame):\r\n    return pd.DataFrame({\r\n\t\t"FirstNM" : input_frame.FirstNameTest,\r\n\t\t"LastNM" : input_frame.LastNameTest.str.lower()\r\n\t})\r\n', '4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1369, 1377, 1026, 'PythonMultisourceTestBinding', 'Generic', None, 'Active', 1032, None, None, 'd578aef7-dab9-4fdc-a1a0-fffae798ee3d', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1369)/AttributeValues', '-', '-', '-', '-', '-', '\r\nimport pandas as pd\r\n\r\n@binding.multisource()\r\ndef task(input_dict):\r\n\tprint(f"Input Dict:{input_dict}")\r\n\treturn pd.DataFrame({"MagicNumber" : input_dict["NLPSAM_Test_AdventureWorks2012Person"].FirstNameTest.str.len() + input_dict["NLPSAM_PluginTest_PythonStreamingTestDestination"].LastNM.str.len()})\r\n', '4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], [1374, 1378, 1030, 'MetadataServicePythonBinding', 'Generic', None, 'Active', 1035, None, None, '19a22200-3224-4b21-870f-8cc0a8d0591f', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1374)/AttributeValues', '-', '-', '-', '-', '-', "print('hello')", '1', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'Temp'], [1377, 1381, 1032, 'MetadataServicePythonBinding', 'Generic', None, 'Active', 1037, None, None, 'd0551d80-7ddd-4962-aaad-ca407daa7fc1', 'Python', None, 'Full', 'https://nlpmag.hqcatalyst.local/MetadataService/v1/$metadata#SourceBindings(1377)/AttributeValues', '-', '-', '-', '-', '-', '@binding.multisource()\ndef task(source_dict):\n    source = source_dict[\'NLPSAM_Test_AdventureWorks2012Person\']\n    return source[[\'FirstNameTest\', \'LastNameTest\']].rename(index=str, columns={\n        \'FirstNameTest\' : "FirstNameNM",\n        \'LastNameTest\' : "LastNameNM"\n        })', '4', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'Temp']]

table = columnar(data, headers)
print(table)