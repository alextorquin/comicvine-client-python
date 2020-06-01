# Response

Object representing a response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | An integer indicating the result of the request. Acceptable values are:   - 1:OK   - 100:Invalid API Key   - 101:Object Not Found   - 102:Error in URL Format   - 103:&#39;jsonp&#39; format requires a &#39;json_callback&#39; argument   - 104:Filter Error   - 105:Subscriber only video is for subscribers only  | [optional] 
**error** | **str** | A text string representing the status_code | [optional] 
**number_of_total_results** | **int** | The number of total results matching the filter conditions specified | [optional] 
**number_of_page_results** | **int** | The number of results on this page | [optional] 
**results** | [**AnyOfvolumeissuepersonobjectarray**](AnyOfvolumeissuepersonobjectarray.md) | Zero or more items that match the filters specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


