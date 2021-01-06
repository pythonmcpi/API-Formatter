# API-Formatter
Converts an API documentation from a custom format to markdown.

## Custom Format
'#' is a comment
'##' is a '#' in markdown, '###' is '##', '####' is '###', so you can have Heading 1-3.

Full Syntax of a line
```
METHOD /route [?url=parameters\[&opt=ional\]] [if METHOD==POST then request body as json (see below)] [ | <repeat the previous syntax> -> <HTTP code on success> <HTTP code's name on success> [response as json] [ ^ <HTTP code on success> <HTTP code's name on success> [response as json] ["<reason>"]] [ | <HTTP code on error> <HTTP code's name on error> [response as json] ["<reason>"] [ | <repeat the previous error syntax> ]
```
Example
```
GET /route/to/resource | GET /alternative/route -> 200 OK json
```
Example with basically every option
```
POST /route/one ?auth=TOKEN&page=1 json[param1[string], param2[int], param3[json[param4[string], param5[int]]]] | PUT /rute/two ?auth=TOKEN&method=post {"data": DATA_GOES_HERE}-> 201 Created json ^ 2001 OK json | 403 Forbidden "No token/bad token provided" | 500 Internal Server Error json[error[string], error_code[int]]
```

### Custom JSON Format
Direct Json
```
{...}
```
JSON placeholder
```
json
```
Full format (whitespaced for clarity, '#' means a comment)
```
json[ # Required
	KEY_NAME_WITHOUT_QUOTES[TYPE], # The '[TYPE]' part is optional, TYPE can be string, int, or json (TYPE json follows this same format)
	ANOTHERKEY[TYPE]=VALUE <SOME COMMENT>, # '=VALUE' is optional, '[TYPE]' is optional if =VALUE is not provided
	# In the last time, '<SOME COMMENT>' is optional
]
```

### Converted Markdown Format
> Names based on custom format

**METHOD /route?name=parameters&opt=ional** 
**METHOD /route2?name=parameter**
	**Url Paramters**
		- (ROUTE) name=parameters REQUIRED|OPTIONAL
	**Request Body (JSON)**
	**Success Codes**
		- NUMBER DESCRIPTION
			- Response (JSON)
			- REASON
		...
	**Error Codes**
		- NUMBER DESCRIPTION
			- Response (JSON)
			- REASON
		...
...
#### Converted Markdown Format Json
> Indentation will be prepended to each line
- \* (JSON)
	- "KEY"
		- TYPE
		- VALUE (Could be nested json)
	...
