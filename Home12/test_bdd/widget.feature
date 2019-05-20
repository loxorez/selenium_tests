Feature: Widget feature
  Description: Widget feature description placed here

  Scenario Outline: Change welcome widget settings
    Given logged user
    Given widget settings page
    When user add <new_content_message>
    When user add <new_title_message>
    Then enable title and save settings
    Then widget has <new_content_message> and <new_title_message>

    Examples:
      | new_content_message                 | new_title_message       |
      | 952Wpwx48UZ8O0haBFQ6uRUMiMooMtSnF   | d]18_T[}h>3s+(Vsic!@on0 |
      | Q:$&&d]18_T[}h>3s+(Vsiыва1234567890 | T3ST WeLcOmE T1TlE @#$  |
      | Some user welcome message           | Welcome box title       |