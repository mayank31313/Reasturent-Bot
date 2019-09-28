## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye


## Generated Story 6592995140769689933
* greet{"PERSON": "Amit"}
    - slot{"PERSON": "Amit"}
    - utter_greet
    - utter_get_order
* inform{"food": "Biryani"}
    - slot{"food": "Biryani"}
    - utter_options
* order_food{"food": "Biryani"}
    - slot{"food": "Biryani"}
    - action_order_food

## Generated Story -4445509362779047923
* greet{"PERSON": "Amit"}
    - slot{"PERSON": "Amit"}
    - utter_greet
    - utter_get_order
* inform{"food": "Biryani"}
    - slot{"food": "Biryani"}
    - utter_options
* book_seat
    - action_book_seat

## interactive_story_1
* greet{"PERSON": "Mayank"}
    - slot{"PERSON": "Mayank"}
    - utter_greet
    - utter_get_order
* order_food{"food": "Deserts"}
    - slot{"food": "Deserts"}
    - utter_options
* order_food
    - action_order_food
    - form{"name": "action_order_food"}
    - slot{"food": "Deserts"}
    - form{"name": null}
    - slot{"requested_slot": null}
