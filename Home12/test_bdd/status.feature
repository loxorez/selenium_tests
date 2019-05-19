Feature: Status feature
  Description: Feature description placed here

  Scenario Outline: Create short text status
    Given initial amount os statuses
    Given logged user
    When I add status with <text>
    Then a new status block appears
    Then this status block has <text> and author

    Examples:
    | text                                             |
    | EHdrZowjuixmtt3T8UZ8O0haBFQ6uRUMiMooMtSnF        |
    | ываывпывпЫАФПФЫП                                 |
    | 1234567890                                       |
    | ^#Fz>wq3{JXQ:$&&d]18_T[}h>3s+(Vsic!@on0ew!G#LGlP |


  Scenario Outline: Create long text status
    Given initial amount os statuses
    Given logged user
    When I add status with <text>
    Then a new status block appears
    Then i click button to show whole status
    Then this status block has <text> and author

    Examples:
    | text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | eDzvqREYbKsWmAdLrJGdGa9hTlsmqIrAk2VvNQBFaWvI6EMcw7JEikSXaezEHdrZowjuixmtt3T8UZ8O0haBFQ6uRUMiMooMtSnFJftMhZxY8uAJ3rhoTPbgON8S56tOWVZ1roy3TpQk9fGesBoaqI4l0c9tNHRtyh5ld93PMvwZ7FmyBuLP0uhxZfDwL4K6DbR96KxWsv9eFUjm74BslUu9amDymoUqS6JmQy0wGFgRJYszfrAqMcjv8ifVaQN8AgN3OSzndX5RSP7AOYWEmPId0ki0eLqlYK2lHLr5foAgeY0dxYMjju3gzlZGN49071uIOXli3mfKIOnEde3uSt67wnc9CWFCbAG3VWzE1HSOghr3ZUZxVHtagPC209PqNHHxvugix9IwuAMh0EhzrL2oY5emNLTiKDUeA920qyfH14hHwBf4Pd1QBckuGaR8EakFxmc8qf57p4JfBSllQ6iHYKY1UnTOkMK234TTv0dJCWSvI5VzEmsCNpVPP2P6myvD4HomjaS3wtzeYytKvdFwT8EOFG01WaIOijNlrVuZ08ML0Cr8NztfUiDRL9HQIrTz5uTPmfPn0y5yL1u9IN7HtBXTa6uJPmibckth6mjykkKazOyEtB1SWBaTJ6kTvRNRMcygBcxxptFHU7N9Js3Lm9qlcz5n283Fn7wuNe1ULfOmRJXKIQ5CrTydVGe43PGz9FEXXxTbp |
    | vlGgCiCYaGBK75SD42zbTTGy6Dl5eXqS3Gm3Y8Zm0ILXdFa1gRRmCMew978sxVSIC1wgRMyXZXXW6xCypzUgPNIYZ3pCS2uqk00DtBkAPNKZFPn1ES8BencC7b762dx3wt87ls13QIkXvmCVDSnGbNYQYgQs1VG0FD88Dvhv5tb6hROwsSofOyG3k0HL4Q02IAAVKErYg3MGEV1zVZWzRGgfmKnbNAgWruyoX6Wl5NlE9hFY0gp0WiDZnXfhTA0FHYpGO5F8EUFOekI8M0XRqjzttJhcazyO4mGY28RygL7GVyaTqtWvOo94uHlVq3WrN7dri4Mbtf3wp4jzveXXtV5Yz0k84YWegZNFIiEZg4dCPVPV1xv0LHuxKqiLWVPP2j7QLdRxeQRZsaQE0TAcATGcoNE2NrTE2Mxi1X6ZNTJsWJflxv9Znf0uAUigTpEL4TlZmWBbiPeQ5EqVapxinskQPAslIjWVO6yQHQnqGhi5wNQzUgwm21uMyy03AZF5y90dUSvxhwIplRbLQ84ieRC0BGnfNjYVgZssTrTY31BbohR9OXgGP7sFCuAm8zsYntnrmagiZojnxgMnQxYvgN1nqwl17t2L8lc5rMmbRsebyKoDGYwvhWb5Ut7jTMPqsNMvbDVeq                                                                     |


  Scenario Outline: Create empty status
    Given logged user
    When status input field is empty and contain <placeholder_text>
    When i submit empty status
    Then inform message box appears with <results_box_message>

    Examples:
    | placeholder_text  | results_box_message           |
    | What’s happening? | PLEASE FILL THE FORM PROPERLY |


  Scenario Outline: Delete status
    Given logged user
    Given initial amount os statuses
    When I add status with <text>
    Then a new status block appears
    Then i delete created status, initial amount of statuses the same as after delete

    Examples:
    | text                                                                                                                       |
    | YA^#Fz>wq3{JXQ:$&&d]18_T[}h>3s+(Vsic!@on0ew!G#LGlP',N^y'!EdYuV'Z_8RW"z(F+.:XK)E'n}bB1Dn>C>~30]Y}9mxttjM"R'>=$;WVdTW        |
    | wKN!,!U,9`^$j^>Mh}2C0K#t^Ux?RQp$zZaeGgpon~!VajEl>Jo)}W7AXbqV]Io1q!Lwd:~G%H}vlY_\eop7,-N#RH24[DW}h!rpxq==J-DuhXrZ2RHE}t-P&e |


  Scenario Outline: Like counter
    Given logged user
    Given create new status
    Given initial likes value
    When user click like button
    Then likes values increased
    Then like string has user likes message

    Examples:


  Scenario Outline: Inside status counter
    Given logged user
    Given create new status
    Given initial status inside comments value
    When user add inside comments in status
    Then inside status comments value has increased

    Examples:



