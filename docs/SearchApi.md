# comicvine_client.SearchApi

All URIs are relative to *https://comicvine.gamespot.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search to ComicVine database


# **search**
> EntitiesResponse search(format=format, query=query, field_list=field_list, limit=limit, offset=offset, resources=resources)

Search to ComicVine database

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
    api_instance = comicvine_client.SearchApi(api_client)
    format = 'xml' # str | The data format of the response takes either xml, json, or jsonp. (optional) (default to 'xml')
query = 'Yoko Tsuno' # str | The search string. (optional)
field_list = 'id,birth,description' # str | List of field names to include in the response. Use this if you want to reduce the size of the response payload. This filter can accept multiple arguments, each delimited with a \",\" (optional)
limit = 100 # int | The number of results to display per page. This value defaults to 100 and can not exceed this number. (optional) (default to 100)
offset = 200 # int | Return results starting with the object at the offset specified. (optional)
resources = 'character,volume' # str | List of resources to filter results. This filter can accept multiple arguments, each delimited with a \",\". Available options are:   character   concept   origin   object   location   issue   story_arc   volume   publisher   person   team   video  (optional)

    try:
        # Search to ComicVine database
        api_response = api_instance.search(format=format, query=query, field_list=field_list, limit=limit, offset=offset, resources=resources)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The data format of the response takes either xml, json, or jsonp. | [optional] [default to &#39;xml&#39;]
 **query** | **str**| The search string. | [optional] 
 **field_list** | **str**| List of field names to include in the response. Use this if you want to reduce the size of the response payload. This filter can accept multiple arguments, each delimited with a \&quot;,\&quot; | [optional] 
 **limit** | **int**| The number of results to display per page. This value defaults to 100 and can not exceed this number. | [optional] [default to 100]
 **offset** | **int**| Return results starting with the object at the offset specified. | [optional] 
 **resources** | **str**| List of resources to filter results. This filter can accept multiple arguments, each delimited with a \&quot;,\&quot;. Available options are:   character   concept   origin   object   location   issue   story_arc   volume   publisher   person   team   video  | [optional] 

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

