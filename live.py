"""
This is the Live Photos module supporting all the ReST actions
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%dT%H:%M:%S"))


# Data to serve with our API
LIVE_PHOTOS = {
    "Storage::Photos::Asset::OXZsVTFlaEhSNjBFc1doaWVxM0xGdz09": {
		"Identifier": "Storage::Photos::Asset::OXZsVTFlaEhSNjBFc1doaWVxM0xGdz09",
		"IsLivePhoto": True,
		"Mime": "image/jpeg",
		"Timestamp": "2017-05-26T14:16:51",
		"TimestampKind": "Utc"
    },
    "Storage::Photos::Asset::NUd0V2llYVpiekpTK0lOOUF2YndYZz09": {
		"Identifier": "Storage::Photos::Asset::NUd0V2llYVpiekpTK0lOOUF2YndYZz09",
		"IsLivePhoto": True,
		"Mime": "image/jpeg",
		"Timestamp": "2017-05-26T14:15:11",
		"TimestampKind": "Utc"
    },
    "Storage::Photos::Asset::ZWhOdEVOWEgxaWJJU2JLRzhHSW1Qdz09": {
		"Identifier": "Storage::Photos::Asset::ZWhOdEVOWEgxaWJJU2JLRzhHSW1Qdz09",
		"IsLivePhoto": True,
		"Mime": "image/jpeg",
		"Timestamp": "2017-04-07T14:57:34",
		"TimestampKind": "Utc"
    },
}

def upload_photo(upfile):
	return "Got this:" + upfile

def read_all():
    """
    This function responds to a request for /photos/live
    with the complete lists of Live Photos

    :return:        json string of Live Photos
    """
    return list(LIVE_PHOTOS.values())


# def read_one(lname):
#     """
#     This function responds to a request for /api/people/{lname}
#     with one matching person from people
# 
#     :param lname:   last name of person to find
#     :return:        person matching last name
#     """
#     # Does the person exist in people?
#     if lname in PEOPLE:
#         person = PEOPLE.get(lname)
# 
#     # otherwise, nope, not found
#     else:
#         abort(
#             404, "Person with last name {lname} not found".format(lname=lname)
#         )
# 
#     return person
# 
# 
# def create(person):
#     """
#     This function creates a new person in the people structure
#     based on the passed in person data
# 
#     :param person:  person to create in people structure
#     :return:        201 on success, 406 on person exists
#     """
#     lname = person.get("lname", None)
#     fname = person.get("fname", None)
# 
#     # Does the person exist already?
#     if lname not in PEOPLE and lname is not None:
#         PEOPLE[lname] = {
#             "lname": lname,
#             "fname": fname,
#             "timestamp": get_timestamp(),
#         }
#         return make_response(
#             "{lname} successfully created".format(lname=lname), 201
#         )
# 
#     # Otherwise, they exist, that's an error
#     else:
#         abort(
#             406,
#             "Peron with last name {lname} already exists".format(lname=lname),
#         )
# 
# 
# def update(lname, person):
#     """
#     This function updates an existing person in the people structure
# 
#     :param lname:   last name of person to update in the people structure
#     :param person:  person to update
#     :return:        updated person structure
#     """
#     # Does the person exist in people?
#     if lname in PEOPLE:
#         PEOPLE[lname]["fname"] = person.get("fname")
#         PEOPLE[lname]["timestamp"] = get_timestamp()
# 
#         return PEOPLE[lname]
# 
#     # otherwise, nope, that's an error
#     else:
#         abort(
#             404, "Person with last name {lname} not found".format(lname=lname)
#         )
# 
# 
# def delete(lname):
#     """
#     This function deletes a person from the people structure
# 
#     :param lname:   last name of person to delete
#     :return:        200 on successful delete, 404 if not found
#     """
#     # Does the person to delete exist?
#     if lname in PEOPLE:
#         del PEOPLE[lname]
#         return make_response(
#             "{lname} successfully deleted".format(lname=lname), 200
#         )
# 
#     # Otherwise, nope, person to delete not found
#     else:
#         abort(
#             404, "Person with last name {lname} not found".format(lname=lname)
#         )
