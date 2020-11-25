import requests


#get information from user - what they want to query
#get information from the form, pass to view in context_dictionary
#therefore all this code should be in a view


user_request = ''
#if they want all the modes of transport do the following query
if user_request == "mode":
    #something like this url will be used - depends where we host the api
    modes_response = requests.get("http://aws.amazon.com/open-transport/mode")
    #if the status code says the request went ok
    if modes_response.status_code==200:
        #the json returned by the query can be translated to a python list of dictionaries
        #each dictionary has a key 'short-desc' which is mapped to a string detailing the mode of transport
        mode_list_of_dict = modes_response.json()
        modes = [dictionary['short-desc'] for dictionary in mode_list_of_dict]

elif user_request == "operator":
    #get this operator_param from the form, will be a string 
    operator_param = ''
    #get the operator we want to lookup
    operators_response = requests.get("http://aws.amazon.com/open-transport/operator", params=operator_param)
    if operators_response.status_code==200:
        #get the json returned
        #
        pass





