## happy path
* greet
  - utter_greet
* affirm
  - utter_happy
*say_name{"name": "vamsy"}
  - slot{"name": "vamsy"}
  - utter_name

## sad path 1
* greet
  - utter_greet
* deny
  - utter_name_help
* say_name{"name": "vamsy"}
  - slot{"name": "vamsy"}
  - utter_name

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## intrested
* intrested
  - utter_intrested

## out of scope other
* out_of_scope
  - utter_out_of_scope

## telljoke
* telljoke
  - utter_telljoke


## handle_insult
* handle_insult
  - utter_insult
   
## Main
* Main
  - utter_menu

## Machine_Learning
* Machine_Learning
  - utter_ML

## Python
* Python
  - utter_python

## products_available
* products_available
  - utter_products_available

## chatbot_dsw
* chatbot_dsw
  - utter_chatbot_dsw

## facerec_dsw
* facerec_dsw
  - utter_facerec_dsw

## kyc_ocr
* kyc_ocr
  - utter_kyc_ocr

## smart_form_dsw
* smart_form_dsw
  - utter_smart_form_dsw

## aadhar_masking_dsw
* aadhar_masking_dsw
  - utter_aadhar_masking_dsw

## Trainings_available
* Trainings_available
  - utter_Trainings_available

## business_intelligence_dsw
* business_intelligence_dsw
  - utter_business_intelligence_dsw

## ai_dsw
* ai_dsw
  - utter_ai_dsw

## vm_ware_dsw
* vm_ware_dsw
  - utter_vm_ware_dsw

## Services
* services_available
    - utter_services_available

## data_science_dsw
* data_science_dsw
  - utter_data_science_dsw

## software_development_dsw
* software_development_dsw
  - utter_software_development_dsw

## Robotic Process Automation
* Robotic_Process_Automation_dsw
  - utter_rpa_dsw

## intern DSW
* intern_dsw
  - utter_intern_dsw

## laugh
* laugh
  - utter_joke_another
* affirm
  - utter_telljoke

## laugh2
* laugh
  - utter_joke_another
* deny
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* say_name{"name": "lakshmi"}
    - slot{"name": "lakshmi"}
    - utter_name
* products_available
    - utter_products_available
* smart_form_dsw
    - utter_smart_form_dsw
* intrested
    - utter_intrested
    - Data_Form
    - form{"name": "Data_Form"}
    - slot{"requested_slot": "email"}
* say_email{"email": "lakshmi44@gmail.com"}
    - Data_Form
    - form{"name": "Data_Form"}
    - slot{"name": "lakshmi"}
    - slot{"email": "lakshmi44@gmail.com"}
    - slot{"requested_slot": "phone"}
* enter_phone_number{"phone": "9849021164"}
    - form: Data_Form
    - slot{"phone": "9849021164"}
    - form{"name": null}
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* say_name{"name": "parinay"}
    - slot{"name": "parinay"}
    - utter_name
* Trainings_available
    - utter_Trainings_available
* ai_dsw
    - utter_ai_dsw
* intrested
    - utter_intrested
    - Data_Form
    - form{"name": "Data_Form"}
    - slot{"requested_slot": "email"}
* say_email
    - Data_Form
    - form{"name": "Data_Form"}
    - slot{"name": "parinay"}
    - slot{"email": "parinay@yahoo.com"}
    - slot{"requested_slot": "phone"}
* form: enter_phone_number
    - form: Data_Form
    - slot{"phone": "8881456735"}
    - form{"name": null}
* goodbye
  - utter_goodbye