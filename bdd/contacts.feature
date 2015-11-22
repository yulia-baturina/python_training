Scenario Outline: add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  |firstname|lastname|email|
  |name1|lastname1|email1|
  |name2|lastname2|email2|

Scenario: delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario: update a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given I provide new <firstname>, <lastname> and <email>
  When I edit the contact in the list
  Then the updated contact list is equal to the old list with the updated contact

  Examples:
  |firstname|lastname|email|
  |nameup1|lastnameup1|emailup1|
  |nameup2|lastnameup2|emailup2|