Feature: Avatar feature
  Description: Feature description placed here

  Scenario Outline: Change avatar
    Given logged user
    When user select avatar in change avatar modal
    Then inform message box appears with <results_box_message>

    Examples:
    | results_box_message     |
    | AVATAR HAS BEEN CHANGED |
