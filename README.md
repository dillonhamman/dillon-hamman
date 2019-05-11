# dillon-hamman
# Record Sorter
## Usage 
This project is a straight forward 
implementation of a record sorter. It is provided in Python 3.7.

```json
{
"data": "File holding a list of records."
}
```
### List all people in record 

**Definition**

`GET /records`

**Response**

- `200 OK` 
```json
[
    {
      "last name": "Hamman",
      "first name": "Dillon",
      "gender": "Male",
      "color": "Purple",
      "date of birth": "4/23/1998"
    }
]
```

### Adding a new person to the record

**Definition**

`POST /records`

**Arguments**

-`"last name": a string` a persons last name
-`"first name": a string` a persons first name
-`"gender": a string` a persons gender 
-`"color": a string` a persons favorite color
-`"dob": a string` a persons date of birth 

If a record contains a person that already exist, the existing person is overwritten.

**Response**

-`201 Created` on success
```json
{
    "last name": "Wayne",
    "first name": "Bruce",
    "gender": "Male",
    "color": "black",
    "dob": "12/30/1975"
}
```

## Lookup record by gender

`GET /records/gender`

## Lookup record by age

`GET /records/age`

## Lookup record by last name

`GET /records/lastname`
