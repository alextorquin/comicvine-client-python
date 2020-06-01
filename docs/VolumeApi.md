# comicvine_client.VolumeApi

All URIs are relative to *https://comicvine.gamespot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_volume**](VolumeApi.md#get_volume) | **GET** /volume/{id} | Get a particular volume


# **get_volume**
> InlineResponse200 get_volume(id, format=format, field_list=field_list)

Get a particular volume

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import comicvine_client
from comicvine_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://comicvine.gamespot.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = comicvine_client.Configuration(
    host = "https://comicvine.gamespot.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = comicvine_client.Configuration(
    host = "https://comicvine.gamespot.com/api",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with comicvine_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = comicvine_client.VolumeApi(api_client)
    id = '4050-87668' # str | Unique ID of the entity.
format = 'xml' # str | The data format of the response takes either xml, json, or jsonp. (optional) (default to 'xml')
field_list = 'id,birth,description' # str | List of field names to include in the response. Use this if you want to reduce the size of the response payload. This filter can accept multiple arguments, each delimited with a \",\" (optional)

    try:
        # Get a particular volume
        api_response = api_instance.get_volume(id, format=format, field_list=field_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VolumeApi->get_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the entity. | 
 **format** | **str**| The data format of the response takes either xml, json, or jsonp. | [optional] [default to &#39;xml&#39;]
 **field_list** | **str**| List of field names to include in the response. Use this if you want to reduce the size of the response payload. This filter can accept multiple arguments, each delimited with a \&quot;,\&quot; | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the volume |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

