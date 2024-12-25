examples = [
    {
        "role": "system",
        "content": """You are an assistant who needs to do your job according to the needs of the conversation"""
    }, 
    {
        "role": "user",
        "content": """
        ***context***
        "name": "AssertionError",
                    "children": [],
                    "info": {
                        "definition": "An AssertionError is a subclass of the Error class in Java. It is thrown to indicate that an assertion (a statement that must be true for the program to work correctly) has failed.",
                        "reasons": "Assertions are used as a debugging tool to test for conditions that the programmer believes must be true at a certain point in a program. If the condition is not met, the AssertionError is thrown. This typically indicates a bug in the program, because it means that the programmer's assumption about the behavior of the program was incorrect. In production code, assertions are typically disabled, so assertion errors can also indicate that the code is running in an environment where the programmer did not expect it to run.",
                        "dangerous_operations": "These are not truly 'dangerous' operations, since they are intended for use in debugging, not in production code. However, a common mistake is to have code with side effects in an assertion. Since assertions can be disabled, this code may not run in production, leading to subtle bugs. It is therefore best to avoid any code that modifies the program state in an assertion.",
                        "sample_code": "```java\npublic class Main {\n    public static void main(String[] args) {\n        int value = 15;\n        assert(value < 10) : 'The value should be less than 10';\n    }\n}\n```",
                        "handle_code": "None",
                        "handling_logic": "Use assertions to set conditions in the code and catch AssertionError to handle failed assumptions, reporting failure."
                    },
                    "scenario": "execute a unit test or perform a code assertion through assert statement",
                    "property": "and the evaluated condition does not hold true, resulting in an AssertionError"
                },
        ***question***
        complete the None place in Context
    """
    }, {
        "role": "assistant",
        "content": "public class Main {\n    public static void main(String[] args) {\n        try {\n            int value = 15;\n            assert(value < 10) : 'The value should be less than 10';\n        } catch (AssertionError e) {\n            e.printStackTrace();\n            /* handle the error here */\n        }\n    }\n}"
    }
]