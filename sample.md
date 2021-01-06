# Title
## Subtitle
### Heading 3
#### Fetch resource
- **GET /route**
	- Success Codes
		- 200 OK
			- json[key[string], another_key(status_code), status_msg(status_message)]
#### Create/update another resourse
- **POST /another/route**
	- **Request Body (WIP)**
		- JSON
	- Success Codes
		- 201 CREATED
			- json[path[string], timestamp[int]<extra note here>]
#### Delete a resource
- **DELETE /wildcard/route/***
	- Success Codes
		- 200 OK
#### Update a resource
- **PATCH /yet/another/route**
- **PUT /a/route**
	- **Url Parameters (WIP)**
		- ['?url=parameters&go=here']
#### Everything!!!
- **POST /route/one**
- **PUT /route/two**
	- **Url Parameters (WIP)**
		- ['?auth=TOKEN&page=1', '?auth=TOKEN&method=post']
	- **Request Body (WIP)**
		- JSON: json[param1[string], param2[int], param3[json[param4[string], param5[int]]]]
		- JSON
	- Success Codes
		- 201 Created
			- json
		- 200 OK
			- json
