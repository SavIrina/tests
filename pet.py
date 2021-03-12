import requests
import unittest
newpet = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 145,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "sammy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
findpet = requests.post('https://petstore.swagger.io/v2/pet/145', json={
  "id": 145,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "sammy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
updatepet = requests.post('https://petstore.swagger.io/v2/pet/145', json={
  "code": 200,
  "type": "unknown",
  "message": "145"
})
petwhithupdate = requests.post('https://petstore.swagger.io/v2/pet/145', json={
  "id": 145,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "LittleDog",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "updateDoggy"
})
deletemydoggy = requests.post('https://petstore.swagger.io/v2/pet/145', json={
  "code": 200,
  "type": "unknown",
  "message": "145"
})

