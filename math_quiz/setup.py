from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Name of the package
    version="0.1",
    packages=find_packages(),  # Automatically find packages in the project directory
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Command to run `math_quiz` from the terminal
        ],
    },
    install_requires=[],  # List of dependencies (if any)
    description="A simple command-line math quiz game.",
    long_description=open("README.md").read(),  # This reads your README file as a long description
    long_description_content_type="text/markdown",  # Ensures Markdown is parsed correctly
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_math_quiz_repo",  # GitHub repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify Python version compatibility
)
