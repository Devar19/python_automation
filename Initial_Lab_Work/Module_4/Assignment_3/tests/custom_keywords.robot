*** Settings ***
Library    ../libraries/math_library.py
Library    BuiltIn


*** Test Cases ***
Calculate Sum Using Custom Python Keyword

    ${result}=    Calculate Sum    10    20

    Log    Calculated result: ${result}

    Should Be Equal As Numbers
    ...    ${result}
    ...    30


String Manipulation Using Custom Python Keyword

    ${text}=    Set Variable    Robot Framework Automation

    ${upper}=    Convert To Upper
    ...    ${text}

    ${lower}=    Convert To Lower
    ...    ${text}

    Log    Original: ${text}
    Log    Uppercase: ${upper}
    Log    Lowercase: ${lower}

    Should Be Equal
    ...    ${upper}
    ...    ROBOT FRAMEWORK AUTOMATION

    Should Be Equal
    ...    ${lower}
    ...    robot framework automation