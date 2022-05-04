input = {'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 
        'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}
		
'''
output:
				Transmitted rate is 1000.00 and Received rate is 9000.00 on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group01
				Transmitted rate is 1000.00 and Received rate is 9000.00 on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group02
'''

print("Transmitted rate is", input['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Tx Frame Rate'],
     "and Received rate is", input['stream_group01']['stream_group01-EndpointSet-1 - Flow Group 0001']['Rx Frame Rate'], 
     "on stream_group01-EndpointSet-1 - Flow Group 0001 of stream_group01")


print("Transmitted rate is", input['stream_group02']['stream_group02-EndpointSet-1 - Flow Group 0001']['Tx Frame Rate'],
     "and Received rate is", input['stream_group02']['stream_group02-EndpointSet-1 - Flow Group 0001']['Rx Frame Rate'], 
     "on stream_group02-EndpointSet-1 - Flow Group 0001 of stream_group02")
