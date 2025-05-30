# Assinment2test
Single Responsibility Principle (SRP)
Each function in my program is dedicated to a specific task. For example, the function that validates approvals is distinct from the one that displays information. This separation ensures that each component has a clear focus.

Open/Closed Principle
The code is designed to accommodate new features without modifying existing ones. For instance, I can add new approval rules by creating new functions, which keeps the existing logic intact and enhances maintainability.

Keep It Simple, Stupid (KISS)
I prioritize simplicity by writing concise and straightforward functions. For example, checks for whether a total is below a certain threshold are implemented using clear if statements, avoiding unnecessary complexity.

Composition Over Inheritance
Although I don't use classes, I apply this principle by breaking the program into small, reusable components. Instead of creating large blocks of logic, I develop modular functions that can be utilized in various parts of the application.

Separation of Concerns
Each script or function serves a specific purpose, such as managing approvals, displaying information, processing input, or performing calculations. This clear separation makes the code easier to understand, debug, and modify, as changes in one area do not impact others.

Don’t Repeat Yourself (DRY)
I eliminated redundant logic by creating shared functions. For instance, there is a single function responsible for printing requisition details, so any changes to the print format are made in one place, ensuring consistency.

You Aren’t Gonna Need It (YAGNI)
The code includes only the features necessary for its current functionality. I avoided adding superfluous functions or variables, keeping the program focused and efficient.

Avoid Premature Optimization
I ensured the program functions correctly before making any performance improvements. Once I confirmed its functionality, I then worked on enhancing the code's structure and readability for better maintainability.

Refactoring and Clean Code
After completing the initial version, I revisited the code to improve its organization. I removed unnecessary lines, chose descriptive names for variables and functions, and reorganized sections to enhance clarity and maintain a clean layout.
