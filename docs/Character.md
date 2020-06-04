# Character

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for the entity. | 
**name** | **str** | Name for the entity | [optional] 
**aliases** | **str** | List of aliases the entity is known by. A \\n (newline) seperates each alias. | [optional] 
**api_detail_url** | **str** | URL pointing to the entity detail resource. | [optional] 
**description** | **str** | Description of the entity. | [optional] 
**deck** | **str** | Brief summary of the Entity. | [optional] 
**site_detail_url** | **str** | URL pointing to the concept on Giant Bomb. | [optional] 
**date_added** | **str** | Date the entity was added to Comic Vine. | [optional] 
**date_last_updated** | **str** | Date the entity was last updated on Comic Vine. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**birth** | **str** | A date, if one exists, that the person was born on. Not an origin date. | [optional] 
**count_of_issue_appearances** | **int** | Number of issues this person appears in. | [optional] 
**gender** | **int** | Gender of the person. Available options are: Male (1), Female (2), Other (3) | [optional] 
**story_arc_credits** | **list[object]** | List of story arcs this person appears in. | [optional] 
**volume_credits** | [**list[Volume]**](Volume.md) |  | [optional] 
**issue_credits** | [**list[Issue]**](Issue.md) |  | [optional] 
**character_enemies** | [**list[Character]**](Character.md) |  | [optional] 
**character_friends** | [**list[Character]**](Character.md) |  | [optional] 
**creators** | [**list[Person]**](Person.md) |  | [optional] 
**first_appeared_in_issue** | [**Issue**](Issue.md) |  | [optional] 
**issues_died_in** | [**list[Issue]**](Issue.md) |  | [optional] 
**movies** | **list[object]** | Movies the character was in. | [optional] 
**origin** | **object** | The origin of the character. Human, Alien, Robot ...etc | [optional] 
**powers** | **object** | List of super powers a character has. | [optional] 
**publisher** | **object** | The primary publisher a character is attached to. | [optional] 
**real_name** | **str** | Real name of the character. | [optional] 
**team_enemies** | **list[object]** | List of teams that are enemies of this character. | [optional] 
**team_friends** | **list[object]** | List of teams that are friends with this character. | [optional] 
**teams** | **list[object]** | List of teams this character is a member of. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


