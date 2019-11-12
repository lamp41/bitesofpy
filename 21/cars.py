import re

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}
grep = 'CO'
search_trail_list = []
for model in cars:
    for car in cars[model]:
        if re.search(grep, car, re.IGNORECASE):
            search_trail_list.append(car)
print(search_trail_list)

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    Jeep_list = cars["Jeep"]
    return ", ".join(Jeep_list)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    list_of_first = []
    for model in cars:
        list_of_first.append(cars[model][0])
    return list_of_first


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    search_trail_list = []
    for model in cars:
        for car in cars[model]:
            if re.search(grep, car, re.IGNORECASE):
                search_trail_list.append(car)
    search_trail_list.sort()
    return search_trail_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for model in cars:
        cars[model].sort()
    return cars
