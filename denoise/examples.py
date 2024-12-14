history = [
    {
        "role": "system",
        "content": """You are an assistant who needs to do your job according to the needs of the conversation"""
    },
    {
        "role": "user",
        "content": """While it is typically not recommended to catch Errors as they indicate serious problems, if we were to do so, it could look something like: try { CharsetEncoder ce = Charset.defaultCharset().newEncoder(); char[] chars = new char[]{'t', 'e', 's', 't'}; ce.encode(CharBuffer.wrap(chars)); } catch (CoderMalfunctionError cme) { // handle the error } \n\n Extract and format the code in Context, if not code is found, please respond with 'None'"""
    },
    {
        "role": "assistant",
        "content": """try { 
        CharsetEncoder ce = Charset.defaultCharset().newEncoder(); 
        char[] chars = new char[]{'t', 'e', 's', 't'}; 
        ce.encode(CharBuffer.wrap(chars)); 
    } 
    catch (CoderMalfunctionError cme) { 
        // handle the error 
    }"""
    },
    {
        "role": "user",
        "content": """"    Here is an example code snippet that will cause an AssertionError: 


    public class Main {
        public static void main(String[] args) {
            int value = 15;
            assert(value < 10) : 'The value should be less than 10';
        }
    }

    In this example, the assertion will fail because value is not less than 10, causing an AssertionError to be thrown. \n\n , if not code is found, please respond with 'None'"""
    },
    {
        "role": "assistant",
        "content": """    public class Main {
        public static void main(String[] args) {
            int value = 15;
            assert(value < 10) : 'The value should be less than 10';
        }
    }"""
    },
    {
        "role": "user",
        "content": """Unfortunately, it is not straightforward to provide a sample Java code snippet that causes an AnnotationFormatError as this error is mostly caused by JVM internals when reading from a .class file."""
    },
    {
        "role": "assistant",
        "content": "None"
    }
]