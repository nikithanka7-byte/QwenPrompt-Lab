def build_prompt(technique, task):

    if technique == "Zero-shot":

        return f"""
Answer the following task directly and accurately.

Task:
{task}
""".strip()


    elif technique == "One-shot":

        return f"""
Use the example below to understand the expected answer style.

Example:

Task: Explain Python.

Answer:
Python is a high-level programming language used to develop
applications, automate tasks, analyze data, and build AI systems.

Now answer this task:

Task:
{task}
""".strip()


    elif technique == "Few-shot":

        return f"""
Study the examples below and follow their answer style.

Example 1:

Task: What is AI?

Answer:
Artificial Intelligence is technology that enables computers
to perform tasks that normally require human intelligence.


Example 2:

Task: What is Machine Learning?

Answer:
Machine Learning is a branch of AI where computers learn
patterns from data and use them to make predictions or decisions.


Example 3:

Task: What is NLP?

Answer:
Natural Language Processing enables computers to understand,
process, and generate human language.


Now answer the following task:

Task:
{task}
""".strip()


    elif technique == "CoT":

        return f"""
Solve the following task carefully.

Follow these steps:

1. Understand the task.
2. Identify the important information.
3. Apply the appropriate method.
4. Verify the result.
5. Provide the final answer.

Do not reveal private or hidden chain-of-thought.
Provide only a concise explanation of the important steps.

Task:
{task}
""".strip()


    elif technique == "Manual CoT":

        return f"""
Solve the following task using this structured format.

Step 1 - Understand:
Explain what the task is asking.

Step 2 - Identify:
Identify the important information.

Step 3 - Apply:
Explain the appropriate method or approach.

Step 4 - Verify:
Check whether the answer is reasonable.

Step 5 - Final Answer:
Provide the final answer clearly.

Do not reveal private or hidden chain-of-thought.

Task:
{task}
""".strip()


    elif technique == "ToT":

        return f"""
Solve the following task by considering multiple approaches.

Approach A:
Suggest one possible solution and briefly evaluate it.

Approach B:
Suggest another possible solution and briefly evaluate it.

Approach C:
Suggest another solution if useful.

Comparison:
Compare the possible approaches.

Selection:
Choose the most suitable approach.

Final Answer:
Provide the final answer with a concise explanation.

Do not reveal private or hidden chain-of-thought.

Task:
{task}
""".strip()


    else:

        raise ValueError(
            f"Unknown prompting technique: {technique}"
        )