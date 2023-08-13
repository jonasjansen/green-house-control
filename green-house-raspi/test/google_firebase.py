from api.firebase import firebase
import json

test = firebase.get_document("override", "override_heating")

# firebase.test()
print(json.dumps(firebase.get_document("override", "override_light")))
print(json.dumps(firebase.get_document("override", "override_heating")))
print(json.dumps(firebase.get_document("environment", "oYyOKbApgDnkoI5dhbv6"), default=str))
test_object = {
    "humidity": "90",
    "temperature": "21",
    "moisture": "1.90",
    "light_state": "on",
    "heating_state": "off",
    "image_path": "light.jpg",
    "timestamp": "2023-03-02 11:00:00.703000+00:00"
}
# self.add_document("environment", test_object)
override_heating = firebase.get_document("override", "override_heating")
override_heating["counter"] = 2
firebase.update_document("override", "override_heating", override_heating)
