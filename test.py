from sql import quizDB

DB2 = quizDB()


question = [{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"for (var i = 0; i < 3; i++) {\n  setTimeout(() => console.log(i), 1);\n}\nfor (let i = 0; i < 3; i++) {\n  setTimeout(() => console.log(i), 1);\n}",
    "option":["A: 0 1 2 and 0 1 2","0 1 2 and 3 3 3","3 3 3 and 0 1 2","undefined and ReferenceError"],
    "answer":2,
    "type":"js",
    "explanation":"Because of the event queue in JavaScript, the setTimeout callback function is called after the loop has been executed. Since the variable i in the first loop was declared using the var keyword, this value was global. During the loop, we incremented the value of i by 1 each time, using the unary operator ++. By the time the setTimeout callback function was invoked, i was equal to 3 in the first example.In the second loop, the variable i was declared using the let keyword: variables declared with the let (and const) keyword are block-scoped (a block is anything between { }). During each iteration, i will have a new value, and each value is scoped inside the loop."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
{
    "question":"What''s the output?",
    "code":"   function sayHi() {\n        console.log(name);\n        console.log(age);\n        var name = ''Lydia'';\n        let age = 21;\n    }\n    sayHi();",
    "option":["Lydia and undefined","Lydia and ReferenceError","ReferenceError and 21","undefined and ReferenceError"],
    "answer":3,
    "type":"js",
    "explanation":"Within the function, we first declare the name variable with the var keyword. This means that the variable gets hoisted (memory space is set up during the creation phase) with the default value of undefined, until we actually get to the line where we define the variable. We haven''t defined the variable yet on the line where we try to log the name variable, so it still holds the value of undefined.Variables with the let keyword (and const) are hoisted, but unlike var, don''t get initialized. They are not accessible before the line we declare (initialize) them. This is called the ''temporal dead zone''. When we try to access the variables before they are declared, JavaScript throws a ReferenceError."
},
]



a = DB2.addQuestion(question[1])
b = DB2.getQuestion(2)
print(b)